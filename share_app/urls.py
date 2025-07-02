from django.urls import path
from .views import (
    RegisterClient, VerifyEmail, UploadFile,
    ListFiles, GetDownloadLink, DownloadFile
)

urlpatterns = [
    path('client/signup', RegisterClient.as_view()),
    path('verify/<str:token>', VerifyEmail.as_view()),
    path('ops/upload', UploadFile.as_view()),
    path('client/files', ListFiles.as_view()),
    path('download-file/<int:file_id>', GetDownloadLink.as_view()),
    path('download/<str:enc_id>', DownloadFile.as_view()),
]
