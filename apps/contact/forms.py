from django import forms 
from apps.home.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact 
        fields = ('name', 'phone', 'email')
        widgets = {
            'name' : forms.TextInput(attrs={'class': "form-control"}),
            'phone' : forms.TextInput(attrs={'class': "form-control"}),
            'email' : forms.EmailInput(attrs={'class': "form-control"}) 
        }