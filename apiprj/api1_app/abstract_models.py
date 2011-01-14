#-*-coding:utf-8-*-
"""
abstract_models package
~~~~~~~~~~~~~~~~~~~~~~~

legacy의 board_*, comment_*, memo_* 테이블을 추상화. 
django 의 Abstract Model기능을 이용해 구현.
"""
from django.db import models
  
class AbstractBoard(models.Model):
    id = models.AutoField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    # TODO: Impact to legacy, normalize Database scheme
    # file_name, password 의 길이가 일정하지 않음.
    password = models.CharField(max_length=123, blank=True)
    file_name = models.CharField(max_length=300, blank=True)

    class Meta:
        abstract = True
        
    def __unicode__(self):
        return ",".join((str(self.id), self.title, self.name))        
   
class AbstractComment(models.Model):        
    id = models.AutoField(primary_key=True)
    idx = models.IntegerField()
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)  
    user_id = models.CharField(max_length=90)
    # TODO: Impact to legacy, normalize Database scheme 
    # name, password field 의 길이가 일정하지 않음.
    name = models.CharField(max_length=225) 
    password = models.CharField(max_length=144, blank=True) 

    class Meta:
        abstract = True  
              
    def __unicode__(self):
        return ",".join((str(self.id), self.content, self.name))
         
class AbstractMemo(models.Model):            
    id = models.AutoField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    # TODO: Impact to legacy, normalize Database scheme 
    # reg_date field 가 일부는 DateField, 일부는 DateTimeField임. 
    # password field 의 유무 여부가 테이블에 따라 다름. 
    reg_date = models.DateTimeField(null=True, blank=True) 
    #password = models.CharField(max_length=48, null=True, blank=True) 

    class Meta:
        abstract = True

    def __unicode__(self):
        return ",".join((str(self.id), self.content, self.name))