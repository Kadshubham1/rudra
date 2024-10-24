from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['first_name', 'email', 'phone', 'gender', 'date', 'department', 'comments']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control py-3 border-primary bg-transparent text-white', 'placeholder': 'Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control py-3 border-primary bg-transparent text-white', 'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control py-3 border-primary bg-transparent', 'placeholder': 'Phone'}),
            'gender': forms.Select(attrs={'class': 'form-select py-3 border-primary bg-transparent'}),
            'date': forms.DateInput(attrs={'class': 'form-control py-3 border-primary bg-transparent', 'type': 'date'}),
            'department': forms.Select(attrs={'class': 'form-select py-3 border-primary bg-transparent'}),
            'comments': forms.Textarea(attrs={'class': 'form-control border-primary bg-transparent text-white', 'rows': 5, 'placeholder': 'Write Comments'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add default empty option for gender
        self.fields['gender'].choices = [('', 'Select your gender')] + list(self.fields['gender'].choices)[1:]
        # Add default empty option for department
        self.fields['department'].choices = [('', 'Select department')] + list(self.fields['department'].choices)[1:]