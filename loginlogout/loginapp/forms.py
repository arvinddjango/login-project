from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from loginapp.models import Profile


STATE_CHOICES=(('d','Delhi'),('k','Kolkata'),('c','Chennai'),('p','Punjab'))
GENDER_CHOICES=(('m','Male'),('f','Female'))

class UserRegisterForm(UserCreationForm):
    username=forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username'}))
    email= forms.EmailField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Email'}))
    password1=forms.CharField(label='',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'}))
    password2=forms.CharField(label='',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password'}))

    class Meta:
        model=User
        fields=['username','email','password1','password2']

class UserUpdateForm(forms.ModelForm):
    username=forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username'}))
    email= forms.EmailField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Email'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    image=forms.ImageField()
    #image=forms.ImageField(label='Image file input',widget=forms.FileInput(attrs={'class':'form-control-file'}))
    fname=forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Name'}))
    adsress=forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Address'}))
    city=forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter City'}))
    postalcode=forms.IntegerField(label='',widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Postalcode'}))
    mobile=forms.IntegerField(label='',widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Mobile No'}))
    dob=forms.DateField(label='',widget=forms.widgets.DateInput(format="%Y-%m-%d", attrs={'class':'form-control'}))
    state=forms.ChoiceField(label='',choices=STATE_CHOICES,widget=forms.Select(attrs={'class':'form-control'}))
    gender=forms.ChoiceField(label='',choices=GENDER_CHOICES,widget=forms.RadioSelect(attrs={'class':'form-control'}))
    terms=forms.BooleanField(label='Check me out',widget=forms.CheckboxInput(attrs={'class':'form-check-input'}))

    class Meta:
        model = Profile
        fields = ['image','fname','adsress','city','postalcode','mobile','dob','state','gender','terms']
