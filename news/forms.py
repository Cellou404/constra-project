from django.forms import widgets
from .models import Comment
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column


class CommentForm2(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'content',)

        widgets = {
            "name": forms.TextInput(
                attrs={
                    'class': 'form-group col-md-6 mb-0',
                    'placeholder': 'Full name. Ex: John Doe'
                }
            ),
            "email": forms.TextInput(
                attrs={
                    'class': 'form-group col-md-6 mb-0',
                    'placeholder': 'Email. Ex:johndoe123@gmail.com'
                }
            ),
            "content": forms.Textarea(
                attrs={
                    'class': 'form-group',
                    'placeholder': 'Your comment...', 
                    'rows': 5
                }
            ),
            
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'content')

    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Full name. Ex: John Doe'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email. Ex:johndoe123@gmail.com'}))
    content = forms.CharField(
        label='comment',
        widget=forms.Textarea(attrs={'placeholder': 'Your comment...', 'rows': 5})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False 
        self.helper.layout = Layout(
            'content',
            Row(
                Column('name', css_class='form-group col-md-6 mb-0'),
                Column('email', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            
            Submit('submit', 'Submit')
        )
