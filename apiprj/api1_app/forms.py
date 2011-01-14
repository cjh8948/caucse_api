#-*- coding:utf-8 -*-
from apiprj.oauth_app.models import Consumer
from django.forms import ModelForm

class ConsumerForm(ModelForm):
    
    class Meta:
        model = Consumer
        fields = ('name', 'description')
