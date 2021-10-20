from django import forms
from comment.models import Comment



class CommentForm(forms.ModelForm):
    user = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control1', 'style': 'width:1000px; margin-left: 50px;'}), required=True)
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'textarea', 'style': 'width:1000px; margin-left: 50px;'}), required=True)


    class Meta:
        model = Comment
        fields = ('user', 'body')


