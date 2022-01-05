from django import forms

from authapp.forms import UserRegisterForm, UserProfilerForm
from authapp.models import User

class UserAdminRegisterForm(UserRegisterForm):
    image = forms.ImageField(widget=forms.FileInput(),required=False)

    class Meta:
        model = User;
        fields = ('username','email','image','first_name','last_name','password1','password2','age')

    def __init__(self,*args,**kwargs):
        super(UserAdminRegisterForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form'
            field.widget.attrs['class'] = 'form-control py-4'
        self.fields['image'].widget.attrs['class'] = 'custom-file-input'

class UserAdminProfilerForm(UserProfilerForm):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control py-4','readonly':False}))
    username = forms.Field(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'readonly': False}))

    # class Meta:
    #     model = User
    #     fields = ('username','email','image','first_name','last_name','password1','password2','age')

    # def __init__(self,*args,**kwargs):
    #     super(UserAdminProfilerForm, self).__init__(*args, **kwargs)
    #
    #     for field_name, field in self.fields.items():
    #         field.widget.attrs['class'] = 'form'
    #         field.widget.attrs['class'] = 'form-control py-4'
    #     self.fields['image'].widget.attrs['class'] = 'custom-file-input'