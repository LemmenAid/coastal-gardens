from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """
    Form for creating and editing comments.

    This form is based on the `Comment` model and includes a single field:
    - `body`: Text field for the content of the comment.

    By using this form, users can submit comments that are validated and
    saved as `Comment` model instances.
    """
    class Meta:
        model = Comment
        fields = ('body',)
