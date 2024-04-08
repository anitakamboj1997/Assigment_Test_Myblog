from django import forms
from .models import Comment, Post

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['user_name', 'email', 'comment']
        widgets = {
            'user_name': forms.TextInput(attrs={'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email'}),
            'comment': forms.Textarea(attrs={'placeholder': 'Your Comment'}),
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)  # Get the user from kwargs
        super(PostForm, self).__init__(*args, **kwargs)
