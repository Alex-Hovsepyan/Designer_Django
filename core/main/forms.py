from django import forms
from .models import HomeContactPost, ContactPost

class ContactModelForm(forms.ModelForm):

    class Meta:

        model = HomeContactPost
        fields = ['user_name', 'user_surname', 'user_email', 'user_subject', 'user_message']

class ContactModelForm2(forms.ModelForm):

    class Meta:

        model = ContactPost
        fields = ['user_name', 'user_surname', 'user_email', 'user_subject', 'user_message']