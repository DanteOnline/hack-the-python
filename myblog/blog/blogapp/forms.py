from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    name = forms.CharField(label='Название',
                           widget=forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form-control'}))

    class Meta:
        model = Post
        exclude = ('user',)
