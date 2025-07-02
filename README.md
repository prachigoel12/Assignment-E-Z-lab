🔐 Secure File Sharing System with Role-Based Access (Ops & Client)

Implemented a secure file-sharing web system using Django REST Framework.

✔ Features:
- Two types of users: Ops (can upload files), Client (can download)
- Ops can upload only pptx, docx, xlsx files
- Client users can:
  • Sign up and receive encrypted verification link via email
  • Verify email before login
  • View list of uploaded files
  • Download file via secure one-time encrypted URL

✔ Tech Used:
- Python + Django + DRF
- JWT Authentication
- Fernet Encryption for secure download links
- SQLite (can be swapped with PostgreSQL/MySQL)
- Email backend: Django console (easy debug)

✔ Security:
- Role-based permissions
- File type validation
- Link-only download access (client only)

Commit includes:
- API views for login, signup, upload, email verify, list & download
- Utility for Fernet encryption of file links
- URL routing and role-safe access

Secure File Sharing System(Django)
A role-based secure file-sharing backend API built with Django REST Framework. Supports Ops Users and Client Users with secure upload/download functionality.
👤 User Roles
✅ Ops User
Login

Upload .pptx, .docx, .xlsx files only

✅ Client User
Sign up and receive encrypted email verification link

Verify account to activate

Login

View list of uploaded files

Download via secure encrypted URL (only accessible by client)

⚙️ Tech Stack
Python, Django, DRF

JWT Authentication

Fernet (for secure URL generation)

SQLite / PostgreSQL

Django console email backend

🔐 Security Highlights
Role-based access control

File type validation (only office formats allowed)

Encrypted one-time download links (for verified clients only)

Email verification before login

Setup Instructions-
git clone https://github.com/yourusername/secure-file-sharing.git
cd secure-file-sharing
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver


Folder Structure-

secure_file_sharing/
├── core/
│   ├── views.py
│   ├── models.py
│   ├── serializers.py
│   └── urls.py
├── users/
│   └── (custom user logic, roles)
├── media/
│   └── uploaded_files/
├── secure_file_sharing/
│   └── settings.py
├── templates/ (if using HTML emails)
├── .env.example
├── requirements.txt
├── Dockerfile (optional)
├── README.md
├── manage.py


