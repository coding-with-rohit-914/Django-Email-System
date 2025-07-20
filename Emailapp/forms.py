from django import forms

class EmailForm(forms.Form):
    to_email = forms.EmailField(label="To")
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    attachment = forms.FileField(required=False, label="Attach File")
