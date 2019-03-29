from django import forms

class CommentsForm(forms.Form):
    content_text = forms.CharField(max_length=50)
