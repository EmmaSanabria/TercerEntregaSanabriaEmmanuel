from django import forms

class UserForm(forms.Form):
    user = forms.CharField()
    password = forms.CharField()

class PostForm(forms.Form):
    user_posting = forms.CharField()
    post = forms.CharField()

class GroupForm(forms.Form):
     name_group= forms.CharField()
     description = forms.CharField()