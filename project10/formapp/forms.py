
from django import forms

class Register(forms.Form):
    name=forms.CharField(max_length=20)
    uname=forms.CharField(max_length=20)
    password=forms.CharField(max_length=15,widget=forms.PasswordInput)

    def clean_name(self):
        name=self.cleaned_data['name']
        if name.isalpha():
            return name
        else:
            raise forms.ValidationError(message="name should be alphabet only")
        
    def clean_uname(self):
        uname=self.cleaned_data['uname']
        if uname[0].isalpha() and uname.isalnum():
            return uname
        else:
            raise forms.ValidationError(message="username should be start alphabet and use alphabet and digits")
    def clean_password(self):
        password=self.cleaned_data['password']
        ap,dg,sp=0,0,0
        for ch in password:
            if ch.isalpha():
                ap=ap+1
            elif ch.isdigit():
                dg=dg+1
            else:
                sp=sp+1
        if ap>=4 and dg>=2 and sp>=1:
            return password
        raise forms.ValidationError(message="you should be enter 4+ alphabets 2+ digits 1+ special character")