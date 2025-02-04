from django import forms

from server.models import Category, Source


class CategoryForm(forms.ModelForm):
    class Meta(object):
        model = Category
        fields = '__all__'


class SourceForm(forms.ModelForm):
    class Meta(object):
        model = Source
        fields = '__all__'
