from django.forms import ModelForm
from.models import Room,User,Enquiry
from django.contrib.auth.forms import UserCreationForm

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class RoomForm (ModelForm):
    class Meta:
        model = Room
        fields='__all__'
        exclude=['host','participants']

class UserForm (ModelForm):
    class Meta:
        model = User
        fields = ['avatar','name','username','email']

class EnquiryForm (ModelForm):
    class Meta:
        model = Enquiry
        fields = ['name','email','body']