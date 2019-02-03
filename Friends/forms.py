from . import models
from django import forms

class FriendForm(forms.ModelForm):
        name = forms.CharField(widget=forms.TextInput(attrs={
                "class" : "friendfields",
                "required" : True,
                "placeholder":"Your Name",
                }))
        gender = forms.ChoiceField(choices=(('Male',"Male"),('Female', "Female")))
        birthplace = forms.CharField(widget=forms.TextInput(attrs={
                "class" : "friendfields",
                "required" : True,
                "placeholder":"Birth Place",
                }))
        birthday = forms.DateField(widget=forms.SelectDateWidget(attrs={
                "class" : "datefield",
                "required" : True,
                }, years=[2019-i for i in range(100)]))
        line = forms.CharField(widget=forms.TextInput(attrs={
                "class" : "friendfields",
                "required" : True,
                "placeholder":"ID LINE",
                }))
        desc = forms.CharField(widget=forms.Textarea(attrs={
                "class" : "bigfields",
                "required" : True,
                "placeholder":"Describe Yourself",
                }))

        class Meta:
                model = models.Friend
                fields = ["name", "gender", "birthplace", "birthday", "line", "desc"]