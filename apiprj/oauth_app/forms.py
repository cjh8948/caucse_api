#-*-coding:utf8-*-
from django import forms

refresh_help_txt = u"""\
consumer secret이 공개되지 않도록 주의하세요.<br/>
만일 secret이 공개된 경우 본 항목을 체크해서 key와 secret을 재발급 받으세요.
"""

class ConsumerCreateForm(forms.Form):
    name = forms.CharField(max_length=100, min_length=2, 
                           label=u'애플리케이션 이름',
                           help_text=u'애플리케이션 이름 <br/>(ex: 동네M, i동네)')
    description = forms.CharField(min_length=10, widget=forms.Textarea,
                                  label=u'설명',
                                  help_text=u'애플리케이션에 대한 간단한 설명<br/> (ex: 동네-facebook 연동 서비스)')
    
class ConsumerEditForm(ConsumerCreateForm):
    refresh_key = forms.BooleanField(required=False,
                                     label=u'key, secret 재생성', 
                                     help_text=refresh_help_txt)