from django import forms

class ConsumerCreateForm(forms.Form):
    name = forms.CharField(max_length=100, min_length=2)
    description = forms.CharField(min_length=10, widget=forms.Textarea)