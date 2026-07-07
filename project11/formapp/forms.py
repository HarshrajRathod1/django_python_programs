from django import forms

class RegisterForm(forms.Form):
    name=forms.CharField(max_length=20)
    uname=forms.CharField(max_length=20)
    password=forms.CharField(max_length=15,widget=forms.PasswordInput)
    reenterpassword=password=forms.CharField(max_length=15,widget=forms.PasswordInput)

    def clean(self):
        cleaned_data=super().clean()
        name=cleaned_data['name']
        password=cleaned_data['password']
        reenterpassword=cleaned_data['reenterpassword']

        if not name.isalpha():
            raise forms.ValidationError(message="name must be alphabet only")
        
        if not password==reenterpassword:
            raise forms.ValidationError(message="please enter both password is same")
        
        return cleaned_data

