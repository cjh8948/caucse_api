#-*- coding:utf-8 -*-
from django.forms import ModelForm
from apiprj.oauth_app.models import Consumer

class ConsumerForm(ModelForm):
    
    class Meta:
        model = Consumer
        fields = ('name', 'description')
