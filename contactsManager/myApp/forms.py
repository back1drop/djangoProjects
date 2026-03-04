from .models import Contact
from django import forms

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields=['name','phone','email']

    def clean_phone(self):
        phone=self.cleaned_data.get('phone')
        phone=phone.replace(" ","")
        if phone.startswith("+"):
            if not phone[1:].isdigit():
                raise forms.ValidationError("Phone number must contain only digits after '+' sign.")
        else:
            if not phone.isdigit():
                raise forms.ValidationError("Phone number must contain only digits.")
        if len(phone)<10:
            raise forms.ValidationError("Phone number must be at least 10 digits long.")
        return phone
    
    def clean(self):
        cleaned_data=super().clean()
        phone=cleaned_data.get("phone")
        email=cleaned_data.get("email")

        if not phone and not email:
            raise forms.ValidationError("You must provide at least a phone number or an email.")
        if phone and Contact.objects.filter(phone=phone).exists():
            raise forms.ValidationError("A contact with this phone number already exists.")
        return cleaned_data
