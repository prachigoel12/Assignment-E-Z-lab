from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import User, SharedFile
from .serializers import RegisterSerializer, FileSerializer
from .utils import encrypt, decrypt
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.conf import settings

class RegisterClient(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = encrypt(user.email)
            url = f"http://localhost:8000/verify/{token}"
            send_mail("Verify your email", f"Click: {url}",
                      settings.EMAIL_HOST_USER, [user.email])
            return Response({"verify_url": url})
        return Response(serializer.errors)

class VerifyEmail(APIView):
    def get(self, request, token):
        try:
            email = decrypt(token)
            user = User.objects.get(email=email)
            user.email_verified = True
            user.save()
            return Response({"message": "Email verified"})
        except:
            return Response({"error": "Invalid token"})

class UploadFile(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        if not request.user.is_ops:
            return Response({"error": "Only Ops user can upload"})
        file = request.FILES.get('file')
        if not file.name.endswith(('.docx', '.pptx', '.xlsx')):
            return Response({"error": "Invalid file type"})
        SharedFile.objects.create(uploaded_by=request.user, file=file)
        return Response({"message": "File uploaded"})

class ListFiles(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        files = SharedFile.objects.all()
        serializer = FileSerializer(files, many=True)
        return Response(serializer.data)

class GetDownloadLink(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, file_id):
        if not request.user.is_client:
            return Response({"error": "Only client can download"})
        file = get_object_or_404(SharedFile, id=file_id)
        enc = encrypt(str(file.id))
        return Response({
            "download-link": f"http://localhost:8000/download/{enc}",
            "message": "success"
        })

class DownloadFile(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, enc_id):
        try:
            file_id = decrypt(enc_id)
            file = get_object_or_404(SharedFile, id=file_id)
            if not request.user.is_client:
                return Response({"error": "Unauthorized"})
            return Response({"file_url": file.file.url})
        except:
            return Response({"error": "Invalid or expired link"})
