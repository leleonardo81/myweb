from . import models
from django import forms

class CreateCommentForm(forms.ModelForm):
    
    comment = forms.CharField(widget=forms.Textarea(attrs={
            "class" : "fields",
            "required" : True,
            "placeholder":"Your Message",
             }))
    
    class Meta:
           model = models.Comment
           fields = ["comment"]

class CreateReplyForm(forms.Form):
    replies = forms.CharField(widget=forms.Textarea(attrs={
            "class" : "fields",
            "required" : True,
            "placeholder":"Reply here",
             }))
    class Meta:
           model = models.Comment