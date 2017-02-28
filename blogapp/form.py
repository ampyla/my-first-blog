from django import forms
from .models import Post
from .models import Comments

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('comments_text',)