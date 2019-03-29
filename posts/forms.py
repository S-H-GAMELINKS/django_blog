from django import from .forms import 

class CommentsForm(forms.Form):
    content_text = forms.CharField(max_length=50)
    