from django import forms

from .models import Category, Page


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

    name = forms.CharField(max_length=Category.name_max_length, help_text='Please enter category name')
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)


class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        exclude = ('category',)

    title = forms.CharField(max_length=Category.name_max_length, help_text='Please enter title of the page')
    url = forms.URLField(max_length=128, help_text='Please enter URL of the page')
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
