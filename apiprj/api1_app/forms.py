#-*- coding:utf-8 -*-
from django import forms

class AddConsumerForm(forms.Form):
    name = forms.CharField(label=u'이름', max_length=255, min_length=5)
    description = forms.CharField(label='설명', max_length=255, min_length=5)
    type = forms.ChoiceField(label='형태',choices=(('B', 'Browser'), 
                                                   ('C', 'Client')))
