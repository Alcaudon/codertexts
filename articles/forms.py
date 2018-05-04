from django.forms import Textarea, ModelForm

from articles.models import Comment


class NewCommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {
            'text': ''
        }
        widgets = {"text": Textarea(attrs={'class': 'full-width', 'placeholder': 'Deja tu comentario'})}