from django import forms
from blog.models import Post


class MemberStoryForm(forms.ModelForm):
    """
    A form for creating and editing member stories.
    """
    class Meta:
        model = Post
        fields = ["featured_image", "title", "content", "excerpt"]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'excerpt': forms.Textarea(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }
