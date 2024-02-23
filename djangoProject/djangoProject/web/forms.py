from django import forms

from djangoProject.profiles.models import Profile


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'age')

        widgets = {
            "username": forms.TextInput(attrs={"placeholder": "Username", },),
            "email": forms.EmailInput(attrs={"placeholder": "Email", },),
            "age": forms.NumberInput(attrs={"placeholder": "Age", },),
        }