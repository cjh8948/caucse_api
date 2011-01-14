#-*-coding:utf-8-*-
"""
legacy의 board_*, comment_*, memo_* 테이블을 추상화. 
django 의 Abstract Model기능을 이용해 구현.
"""
from django.db import models
  
class AbstractBoard(models.Model):
    id = models.AutoField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    ip = models.IPAddressField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72, blank=True)
    notice_deadline = models.DateField(null=True, blank=True)
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
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
    reg_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return ",".join((str(self.id), self.content, self.name))
