from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Membership
from django.contrib.auth.models import User


# Create your forms here.

class NewUserForm(UserCreationForm):
	age = forms.IntegerField(required=False)

	class Meta:
		model = User, Membership
		fields = ("full_name", "email", "password1", "password2", 
	             "phone_number", "age", "voice_type", )
	
    # def __init__(self, *args, **kwargs):
    #     """
    #     Add placeholders and classes, remove auto-generated
    #     labels and set autofocus on first field
    #     """
    #     super().__init__(*args, **kwargs)
    #     placeholders = {
    #         'full_name': 'Full Name',
    #         'email': 'Email Address',
    #         'phone_number': 'Phone Number',
    #         'voice_type': 'Voice type',
    #     }

    #     self.fields['full_name'].widget.attrs['autofocus'] = True
    #     for field in self.fields:
    #         if self.fields[field].required:
    #             placeholder = f'{placeholders[field]} *'
    #         else:
    #             placeholder = placeholders[field]
    #         self.fields[field].widget.attrs['placeholder'] = placeholder
    #         self.fields[field].widget.attrs['class'] = 'stripe-style-input'
    #         self.fields[field].label = False

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user