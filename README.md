# Django-Email-System
Django Email Sender with Attachments

A Django-based application for sending emails with file attachments (documents, images, videos, etc.) via SMTP.

📌 Features
✔ Send Emails with SMTP (Gmail, Outlook, or custom servers)
✔ Attach Files (PDF, DOCX, images, videos, etc.)
✔ HTML & Plain Text email templates
✔ File Validation (size, type, and security checks)
✔ Responsive UI with Bootstrap 5
✔ Environment Variables for secure SMTP credentials

🛠 Technologies Used
Backend: Django 4.2+

Frontend: HTML5, CSS3, Bootstrap 5

Email Service: SMTP (Gmail.)

File Handling: Django’s FileField & Pillow (for images)

Security: Environment variables (python-decouple or django-environ)

⚙ Installation & Setup
Prerequisites
Python 3.8+

Django 4.2+

An SMTP service (Gmail, SendGrid, etc.)

Configure SMTP in settings.py(change in this file)

python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # e.g., Gmail
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'  # add your email
EMAIL_HOST_PASSWORD = 'your-app-password'  # add your password

Run migrations & start the server

bash
python manage.py migrate
python manage.py runserver
Access the app
Open http://127.0.0.1:8000 in your browser.

🔒 Security Best Practices
✅ Never hardcode SMTP credentials – Use .env files with python-decouple.
✅ Restrict file uploads – Validate file types & scan for malware.
✅ Use App Passwords (Gmail) instead of your real password.
✅ Enable 2FA on your email account for extra security.

📧 How to Use?
Fill in the email form (subject, recipient, message).

Attach files (supports multiple files).

Send! (Check spam folder if email doesn’t arrive).

📜 License
MIT License – Free for personal and commercial use.

📬 Contact
For issues/suggestions, open a GitHub Issue or contact:
📧 xyz84208@gmail.com

🚨 Important Notes
⚠ Test in Development First! Avoid accidentally spamming users.
