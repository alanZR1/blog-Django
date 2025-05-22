from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        flieds = ['titulo', 'contenido']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control'}),
        }
        