from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms

class EditProfileForm(UserChangeForm):
    password = forms.CharField(label='', widget=forms.TextInput(attrs={'type':'hidden'}))

    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name', 'email','password',)
        

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label='',widget=forms.TextInput(attrs={'class':'validate',  'placeholder': 'Email Address'}))
    first_name = forms.CharField(max_length=100, label='', widget=forms.TextInput(attrs={'class':'validate', 'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=100, label='', widget=forms.TextInput(attrs={'class':'validate',  'placeholder': 'Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)

    def __init__(self, *args, **kwargs):
        
        super(SignUpForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].label = ''
        self.fields['username'].widget.attrs['class'] = 'validate'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].help_text = '<span class="text-helper grey-text text-darken-2">Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only</span>'

        
        self.fields['password1'].label = ''
        self.fields['password1'].widget.attrs['class'] = 'validate'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].help_text = '<span class="text-helper grey-text text-darken-2">Your password can’t be too similar to your other personal information.<br>Your password must contain at least 8 characters.<br>Your password can’t be a commonly used password.<br>Your password can’t be entirely numeric.</span>'

        
        
        self.fields['password2'].label = ''
        self.fields['password2'].widget.attrs['class'] = 'validate'
        self.fields['password2'].widget.attrs['placeholder'] = 'Re-confirm Password'
        self.fields['password2'].help_text = '<span class="text-helper grey-text text-darken-2">Enter the same password as before, for verification.</span>'


