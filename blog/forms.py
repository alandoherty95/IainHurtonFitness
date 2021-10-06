from django import forms
from .models import BlogPost
from .widgets import CustomClearableFileInput


# Form for adding blog posts
class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        """
        Adds placeholders and classes, removes auto-generated
        labels, sets autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'Title',
            'body': 'Body',
            'image': 'Image',
        }

        self.fields['title'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'input-shadow'
            self.fields[field].label = False
