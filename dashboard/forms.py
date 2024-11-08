from django import forms
from blog.models import Post

class MemberStoryForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["featured_image", "title", "content", "excerpt"]
