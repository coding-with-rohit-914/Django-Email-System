from django.shortcuts import render
from django.core.mail import EmailMessage
from .forms import EmailForm
from django.conf import settings

def send_email_view(request):
    message_sent = False
    if request.method == 'POST':
        form = EmailForm(request.POST, request.FILES)
        if form.is_valid():
            to = form.cleaned_data['to_email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            attachment = request.FILES.get('attachment')
            email = EmailMessage(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [to]
            )
            if attachment:
                email.attach(attachment.name, attachment.read(), attachment.content_type)
            email.send()
            message_sent = True
            form = EmailForm()
    else:
        form = EmailForm()
    return render(request, 'send_email.html', {'form': form, 'message_sent': message_sent})