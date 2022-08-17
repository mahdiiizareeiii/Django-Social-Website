from dataclasses import fields
from socket import fromshare
from xml.etree.ElementTree import Comment
from django import forms
from .models import Post


class PostCreateUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("body",)


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("body"),
        widgets = {
            "body": forms.Textarea(attrs={"class":"form-control"})
        }


class CommentReplyForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("body",)