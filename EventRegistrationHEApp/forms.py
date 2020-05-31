from django import forms

from EventRegistrationHEApp.models import ErRegisteredUsers

class RegisterForm(forms.ModelForm):
    class Meta():
        model = ErRegisteredUsers
        fields = ['full_name', 'mobile', 'email', 'id_cards', 'registration_type', 'no_of_tickets']
