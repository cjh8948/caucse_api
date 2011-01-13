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
    password = models.CharField(max_length=123, blank=True)   # need to syncdb
    file_name = models.CharField(max_length=300, blank=True)  # need to syncdb
    class Meta:
        abstract = True        
   
class AbstractComment(models.Model):        
    id = models.AutoField(primary_key=True)
    idx = models.IntegerField()
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)  
    user_id = models.CharField(max_length=90)
    name = models.CharField(max_length=225) # need to syncdb
    password = models.CharField(max_length=144, blank=True) # need to syncdb
    class Meta:
        abstract = True        
   
class AbstractMemo(models.Model):            
    id = models.AutoField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)        
    reg_date = models.DateTimeField(null=True, blank=True) # need to syncdb
    #password = models.CharField(max_length=48, null=True, blank=True) # need to syncdb
    class Meta:
        abstract = True
        