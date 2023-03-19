from django import forms

from .models import Post, Contact


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'url', 'description', 'image']
        # fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-2', 'placeholder': 'Enter title'},),
            'url': forms.URLInput(attrs={'class': 'form-control my-2', 'placeholder': 'Enter related link'},),
            'description': forms.Textarea(attrs={'class': 'form-control my-2', 'placeholder': 'Please describe'},),
            'img': forms.ClearableFileInput(attrs={'class': 'form-control my-2', 'type': 'file'},),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        # fields = '__all__'
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control my-2', 'placeholder': 'Enter name'},),
            'email': forms.EmailInput(attrs={'class': 'form-control my-2', 'placeholder': 'Enter email'},),
            'subject': forms.TextInput(attrs={'class': 'form-control my-2', 'placeholder': 'Enter subject'},),
            'message': forms.Textarea(attrs={'class': 'form-control my-2', 'placeholder': 'Enter message', },),
        }
