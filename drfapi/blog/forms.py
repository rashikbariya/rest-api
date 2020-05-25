from django import forms
from .models import Posts

class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = [
            'owner',
            'content',
            'image',
        ]

    #validation
    def clean_content(self, *args, **kwargs):
        content = self.cleaned_data.get('content')
        if len(content) > 300:
            raise forms.ValidationError("content is too long")
        return content

    def clean(self, *args, **kwargs):
        data = self.cleaned_data
        content = data.get('content', None)
        if content == "":
            content = None
        image = data.get("image", None)
        if content is None and image is None:
            raise forms.ValidationError('Content or image is required')
        return super().clean(*args, **kwargs)