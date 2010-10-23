# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class BoardAllaplus(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_allaplus'

class BoardAlumni(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=123, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_alumni'

class BoardAlumni00(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_alumni00'

class BoardAlumni01(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_alumni01'

class BoardAlumni02(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_alumni02'

class BoardAlumni03(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_alumni03'

class BoardAlumni04(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_alumni04'

class BoardAlumni05(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_alumni05'

class BoardAlumni06(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_alumni06'

class BoardAlumni07(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_alumni07'

class BoardAlumni08(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_alumni08'

class BoardAlumni09(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_alumni09'

class BoardAlumni10(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_alumni10'

class BoardAlumni72(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_alumni72'

class BoardAlumni73(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_alumni73'

class BoardAlumni74(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_alumni74'

class BoardAlumni75(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_alumni75'

class BoardAlumni76(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_alumni76'

class BoardAlumni77(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_alumni77'

class BoardAlumni78(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_alumni78'

class BoardAlumni79(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_alumni79'

class BoardAlumni80(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_alumni80'

class BoardAlumni81(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_alumni81'

class BoardAlumni82(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_alumni82'

class BoardAlumni83(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_alumni83'

class BoardAlumni84(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_alumni84'

class BoardAlumni85(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_alumni85'

class BoardAlumni86(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_alumni86'

class BoardAlumni87(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_alumni87'

class BoardAlumni88(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_alumni88'

class BoardAlumni89(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_alumni89'

class BoardAlumni90(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_alumni90'

class BoardAlumni91(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_alumni91'

class BoardAlumni92(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_alumni92'

class BoardAlumni93(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_alumni93'

class BoardAlumni94(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_alumni94'

class BoardAlumni95(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_alumni95'

class BoardAlumni96(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_alumni96'

class BoardAlumni97(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_alumni97'

class BoardAlumni98(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_alumni98'

class BoardAlumni99(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_alumni99'

class BoardAlumniMemory(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_alumni_memory'

class BoardAlumninews(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_alumninews'

class BoardAlumninews1(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_alumninews1'

class BoardAnonymous(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=123, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_anonymous'

class BoardBoardTour(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_board_tour'

class BoardBug(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_bug'

class BoardCafeChuri(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_cafe_churi'

class BoardCafeCuti(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_cafe_cuti'

class BoardCafeForum(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_cafe_forum'

class BoardCafeGirlStudent(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_cafe_girl_student'

class BoardCafeGutter(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_cafe_gutter'

class BoardCafeGutter2(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_cafe_gutter2'

class BoardCafeHandtruth(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_cafe_handtruth'

class BoardCafeHandtruth2(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_cafe_handtruth2'

class BoardCafeHeukseoker(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_cafe_heukseoker'

class BoardCafeHeukseoker2(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_cafe_heukseoker2'

class BoardCafeIris(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_cafe_iris'

class BoardCafeItSecurity(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_cafe_it_security'

class BoardCafeJstorm(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_cafe_jstorm'

class BoardCafeMountainLove(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_cafe_mountain_love'

class BoardCafeNote(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_cafe_note'

class BoardCafeNote2(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_cafe_note2'

class BoardCafeSecurelab(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_cafe_securelab'

class BoardCafeSecurelab2(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_cafe_securelab2'

class BoardCafeSnsd(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_cafe_snsd'

class BoardCafeTspin(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_cafe_tspin'

class BoardCafeWow(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_cafe_wow'

class BoardCaucsesa(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_caucsesa'

class BoardCgraph(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_cgraph'

class BoardClubAbroad(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_club_abroad'

class BoardClubBaseball(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_club_baseball'

class BoardClubBrenntano(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_club_brenntano'

class BoardClubCamera(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_club_camera'

class BoardClubComball(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_club_comball'

class BoardClubCurseware(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_club_curseware'

class BoardClubCurseware2(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_club_curseware2'

class BoardClubDevils(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_club_devils'

class BoardClubEcs(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_club_ecs'

class BoardClubFootlove(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_club_footlove'

class BoardClubFr(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_club_fr'

class BoardClubFreesoul(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_club_freesoul'

class BoardClubGame(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_club_game'

class BoardClubMaim(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_club_maim'

class BoardClubMios(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_club_mios'

class BoardClubMiosSub1(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_club_mios_sub1'

class BoardClubNetory(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_club_netory'

class BoardClubOomg(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_club_oomg'

class BoardClubQuestion(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_club_question'

class BoardClubShift(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_club_shift'

class BoardClubSoesl(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_club_soesl'

class BoardClubSsoa(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_club_ssoa'

class BoardClubStaff(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_club_staff'

class BoardClubSullen(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_club_sullen'

class BoardClubSylph(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_club_sylph'

class BoardClubTrash(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_club_trash'

class BoardClubWithweve(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_club_withweve'

class BoardClubZp(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_club_zp'

class BoardCounsel(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_counsel'

class BoardCsebiz(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_csebiz'

class BoardCsebizLecture(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_csebiz_lecture'

class BoardCsesa(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_csesa'

class BoardCsesaSub1(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_csesa_sub1'

class BoardCsesaSub2(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_csesa_sub2'

class BoardCsesac(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_csesac'

class BoardDcgallers(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_dcgallers'

class BoardDiscuss(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_discuss'

class BoardDoc(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_doc'

class BoardDogsix(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_dogsix'

class BoardDongneHidden(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_dongne_hidden'

class BoardDongneteam(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_dongneteam'

class BoardDongneteamtest(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_dongneteamtest'

class BoardDumb(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_dumb'

class BoardEnter(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_enter'

class BoardEvent(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_event'

class BoardExtreamsport(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_extreamsport'

class BoardFacse(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_facse'

class BoardFacse2(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_facse2'

class BoardFreeboard(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=123, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_freeboard'

class BoardGamemoney(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_gamemoney'

class BoardGujja(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_gujja'

class BoardHelp(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_help'

class BoardHex(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_hex'

class BoardHexSub1(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_hex_sub1'

class BoardItnews(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_itnews'

class BoardJhonson(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_jhonson'

class BoardLecture(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_lecture'

class BoardLost(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_lost'

class BoardMarlboro(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_marlboro'

class BoardMarlboro2(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_marlboro2'

class BoardMemResearch(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_mem_research'

class BoardNba(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_nba'

class BoardNotice(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_notice'

class BoardPaperNeo(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_paper_neo'

class BoardPaperPop(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_paper_pop'

class BoardParkcue(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_parkcue'

class BoardParkcueSub1(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_parkcue_sub1'

class BoardPartAd(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_part_ad'

class BoardPartCulture(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_part_culture'

class BoardPartEveryday(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_part_everyday'

class BoardPartJungtong(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_part_jungtong'

class BoardPartNeo(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_part_neo'

class BoardPartPlan(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_part_plan'

class BoardPartPlanRecords(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_part_plan_records'

class BoardPartSocial(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_part_social'

class BoardPcmanage(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_pcmanage'

class BoardPhoto(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_photo'

class BoardPhoto2(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_photo2'

class BoardPoll(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_poll'

class BoardPray(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_pray'

class BoardQna(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_qna'

class BoardRecruit(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_recruit'

class BoardReload(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_reload'

class BoardSketch(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_sketch'

class BoardTemp(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_temp'

class BoardTest(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_test'

class BoardTest1(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_test1'

class BoardTestPaper(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_test_paper'

class BoardToeic850(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_toeic850'

class BoardToto(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_toto'

class BoardTrashNovel(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_trash_novel'

class BoardTwistedlife(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_twistedlife'

class BoardVolunteers(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_volunteers'

class BoardWebzineTheme(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_webzine_theme'

class BoardWithweveData(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'board_withweve_data'

class Boardinfo(models.Model):
    no = models.IntegerField(primary_key=True)
    tablename = models.CharField(max_length=75)
    title = models.CharField(max_length=300)
    admin_id = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    belongto = models.CharField(max_length=90, blank=True)
    skin = models.CharField(max_length=60, blank=True)
    header = models.CharField(max_length=240, blank=True)
    tail = models.CharField(max_length=240, blank=True)
    line_number = models.IntegerField()
    permission = models.BigIntegerField()
    use_category = models.IntegerField()
    category = models.TextField(blank=True)
    use_notice = models.IntegerField(null=True, blank=True)
    use_fileupload = models.IntegerField(null=True, blank=True)
    max_filesize = models.BigIntegerField(null=True, blank=True)
    use_filtering = models.IntegerField(null=True, blank=True)
    filter = models.TextField(blank=True)
    count = models.IntegerField(null=True, blank=True)
    random = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return ", ".join([self.title, self.tablename])

    class Meta:
        db_table = u'boardinfo'

class CafeCalendarAdmin(models.Model):
    no = models.IntegerField(primary_key=True)
    width = models.TextField(blank=True)
    height = models.TextField(blank=True)
    class Meta:
        db_table = u'cafe_calendar_admin'

class CafeInfo(models.Model):
    no = models.IntegerField(primary_key=True)
    cafe_name = models.CharField(max_length=90)
    cafe_nick = models.CharField(max_length=150)
    adminid = models.CharField(max_length=30)
    is_hidden = models.IntegerField()
    member_list = models.TextField(blank=True)
    board_list = models.TextField()
    photo_board_list = models.TextField()
    front_photo = models.CharField(max_length=180, blank=True)
    front_text = models.TextField(blank=True)
    section = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return ", ".join([self.cafe_name, self.cafe_nick])

    class Meta:
        db_table = u'cafe_info'

class Calendar(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateTimeField()
    n_insert = models.IntegerField()
    content = models.CharField(max_length=600)
    writer_id = models.CharField(max_length=60, blank=True)
    writer_name = models.CharField(max_length=60, blank=True)
    type = models.CharField(max_length=60, blank=True)
    type_open = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'calendar'

class CalendarAdmin(models.Model):
    no = models.IntegerField(primary_key=True)
    width = models.TextField(blank=True)
    height = models.TextField(blank=True)
    class Meta:
        db_table = u'calendar_admin'

class ClubInfo(models.Model):
    no = models.IntegerField(primary_key=True)
    club_name = models.CharField(max_length=75)
    club_nick = models.CharField(max_length=120)
    board_table_name = models.CharField(max_length=150)
    homepage = models.CharField(max_length=120, blank=True)
    section = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return ", ".join([self.club_name, self.club_nick])

    class Meta:
        db_table = u'club_info'

class CommentAllaplus(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_allaplus'

class CommentAlumni(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_alumni'

class CommentAlumni00(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_alumni00'

class CommentAlumni01(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_alumni01'

class CommentAlumni02(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_alumni02'

class CommentAlumni03(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_alumni03'

class CommentAlumni04(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_alumni04'

class CommentAlumni05(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_alumni05'

class CommentAlumni06(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_alumni06'

class CommentAlumni07(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_alumni07'

class CommentAlumni08(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_alumni08'

class CommentAlumni09(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_alumni09'

class CommentAlumni10(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_alumni10'

class CommentAlumni72(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_alumni72'

class CommentAlumni73(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_alumni73'

class CommentAlumni74(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_alumni74'

class CommentAlumni75(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_alumni75'

class CommentAlumni76(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_alumni76'

class CommentAlumni77(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_alumni77'

class CommentAlumni78(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_alumni78'

class CommentAlumni79(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_alumni79'

class CommentAlumni80(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_alumni80'

class CommentAlumni81(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_alumni81'

class CommentAlumni82(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_alumni82'

class CommentAlumni83(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_alumni83'

class CommentAlumni84(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_alumni84'

class CommentAlumni85(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_alumni85'

class CommentAlumni86(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_alumni86'

class CommentAlumni87(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_alumni87'

class CommentAlumni88(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_alumni88'

class CommentAlumni89(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_alumni89'

class CommentAlumni90(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_alumni90'

class CommentAlumni91(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_alumni91'

class CommentAlumni92(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_alumni92'

class CommentAlumni93(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_alumni93'

class CommentAlumni94(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_alumni94'

class CommentAlumni95(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_alumni95'

class CommentAlumni96(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_alumni96'

class CommentAlumni97(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_alumni97'

class CommentAlumni98(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_alumni98'

class CommentAlumni99(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_alumni99'

class CommentAlumniMemory(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_alumni_memory'

class CommentAlumninews(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_alumninews'

class CommentAlumninews1(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_alumninews1'

class CommentAnonymous(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_anonymous'

class CommentBoardTour(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_board_tour'

class CommentBug(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_bug'

class CommentCafeChuri(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_cafe_churi'

class CommentCafeCuti(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_cafe_cuti'

class CommentCafeForum(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_cafe_forum'

class CommentCafeGirlStudent(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_cafe_girl_student'

class CommentCafeGutter(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_cafe_gutter'

class CommentCafeGutter2(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_cafe_gutter2'

class CommentCafeHandtruth(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_cafe_handtruth'

class CommentCafeHandtruth2(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_cafe_handtruth2'

class CommentCafeHeukseoker(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_cafe_heukseoker'

class CommentCafeHeukseoker2(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_cafe_heukseoker2'

class CommentCafeIris(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_cafe_iris'

class CommentCafeItSecurity(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_cafe_it_security'

class CommentCafeJstorm(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_cafe_jstorm'

class CommentCafeMountainLove(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_cafe_mountain_love'

class CommentCafeNote(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_cafe_note'

class CommentCafeNote2(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_cafe_note2'

class CommentCafeSecurelab(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_cafe_securelab'

class CommentCafeSecurelab2(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_cafe_securelab2'

class CommentCafeSnsd(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_cafe_snsd'

class CommentCafeTspin(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_cafe_tspin'

class CommentCafeWow(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_cafe_wow'

class CommentCaucsesa(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_caucsesa'

class CommentCgraph(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_cgraph'

class CommentClubAbroad(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_club_abroad'

class CommentClubBaseball(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_club_baseball'

class CommentClubBrenntano(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_club_brenntano'

class CommentClubCamera(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_club_camera'

class CommentClubComball(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_club_comball'

class CommentClubCurseware(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_club_curseware'

class CommentClubCurseware2(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_club_curseware2'

class CommentClubDevils(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_club_devils'

class CommentClubEcs(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_club_ecs'

class CommentClubFootlove(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_club_footlove'

class CommentClubFr(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_club_fr'

class CommentClubFreesoul(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_club_freesoul'

class CommentClubGame(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_club_game'

class CommentClubMaim(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_club_maim'

class CommentClubMios(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_club_mios'

class CommentClubMiosSub1(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_club_mios_sub1'

class CommentClubNetory(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_club_netory'

class CommentClubOomg(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_club_oomg'

class CommentClubQuestion(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_club_question'

class CommentClubShift(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_club_shift'

class CommentClubSoesl(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_club_soesl'

class CommentClubSsoa(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_club_ssoa'

class CommentClubStaff(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_club_staff'

class CommentClubSullen(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_club_sullen'

class CommentClubSylph(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_club_sylph'

class CommentClubTrash(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_club_trash'

class CommentClubWithweve(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_club_withweve'

class CommentClubZp(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_club_zp'

class CommentCounsel(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_counsel'

class CommentCsebiz(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_csebiz'

class CommentCsebizLecture(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_csebiz_lecture'

class CommentCsesa(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_csesa'

class CommentCsesaSub1(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_csesa_sub1'

class CommentCsesaSub2(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_csesa_sub2'

class CommentCsesac(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_csesac'

class CommentDcgallers(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_dcgallers'

class CommentDiscuss(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_discuss'

class CommentDoc(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_doc'

class CommentDogsix(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_dogsix'

class CommentDongneHidden(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_dongne_hidden'

class CommentDongneteam(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_dongneteam'

class CommentDongneteamtest(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_dongneteamtest'

class CommentDumb(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_dumb'

class CommentEnter(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_enter'

class CommentEvent(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_event'

class CommentExtreamsport(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_extreamsport'

class CommentFacse(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_facse'

class CommentFacse2(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_facse2'

class CommentFreeboard(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_freeboard'

class CommentGamemoney(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_gamemoney'

class CommentGujja(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_gujja'

class CommentHelp(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_help'

class CommentHex(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_hex'

class CommentHexSub1(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_hex_sub1'

class CommentItnews(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_itnews'

class CommentJhonson(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_jhonson'

class CommentLecture(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_lecture'

class CommentLost(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_lost'

class CommentMalboro2(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_malboro2'

class CommentMarlboro(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_marlboro'

class CommentMemResearch(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_mem_research'

class CommentNba(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_nba'

class CommentNotice(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_notice'

class CommentPaperNeo(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_paper_neo'

class CommentPaperPop(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_paper_pop'

class CommentParkcue(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_parkcue'

class CommentParkcueSub1(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_parkcue_sub1'

class CommentPartAd(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_part_ad'

class CommentPartCulture(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_part_culture'

class CommentPartEveryday(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_part_everyday'

class CommentPartJungtong(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_part_jungtong'

class CommentPartNeo(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_part_neo'

class CommentPartPlan(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_part_plan'

class CommentPartPlanRecords(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_part_plan_records'

class CommentPartSocial(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_part_social'

class CommentPcmanage(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_pcmanage'

class CommentPhoto(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_photo'

class CommentPhoto2(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_photo2'

class CommentPoll(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_poll'

class CommentPray(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_pray'

class CommentQna(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_qna'

class CommentRecruit(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_recruit'

class CommentReload(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_reload'

class CommentSketch(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_sketch'

class CommentTemp(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_temp'

class CommentTest(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_test'

class CommentTest1(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_test1'

class CommentTestPaper(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_test_paper'

class CommentToeic850(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_toeic850'

class CommentToto(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_toto'

class CommentTrashNovel(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_trash_novel'

class CommentTwistedlife(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_twistedlife'

class CommentVolunteers(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_volunteers'

class CommentWebzineTheme(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_webzine_theme'

class CommentWithweveData(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    class Meta:
        db_table = u'comment_withweve_data'

class Favorite(models.Model):
    no = models.IntegerField(primary_key=True)
    user_id = models.CharField(max_length=30, blank=True)
    tablename = models.CharField(max_length=60, blank=True)
    priority = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'favorite'

class LoginStatistics(models.Model):
    number = models.IntegerField(primary_key=True)
    id_number = models.IntegerField(null=True, blank=True)
    login_time = models.DateTimeField(null=True, blank=True)
    name = models.CharField(max_length=75)
    id = models.CharField(max_length=30)
    department = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'login_statistics'

class MemResearch(models.Model):
    no = models.IntegerField(primary_key=True)
    id = models.CharField(max_length=30, blank=True)
    picture = models.CharField(max_length=180, blank=True)
    class Meta:
        db_table = u'mem_research'

class Member(models.Model):
    number = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=75)
    student_id = models.BigIntegerField()
    level = models.IntegerField()
    id = models.CharField(max_length=30)
    password = models.CharField(max_length=123, blank=True)
    department = models.IntegerField(null=True, blank=True)
    email = models.TextField(blank=True)
    homepage = models.TextField(blank=True)
    birthday = models.DateField(null=True, blank=True)
    sun_moon = models.IntegerField(null=True, blank=True)
    home_addr_1 = models.TextField(blank=True)
    home_addr_2 = models.TextField(blank=True)
    home_zipcode = models.CharField(max_length=30, blank=True)
    home_phone = models.CharField(max_length=60, blank=True)
    job_addr_1 = models.TextField(blank=True)
    job_addr_2 = models.TextField(blank=True)
    job_zipcode = models.CharField(max_length=30, blank=True)
    job_phone = models.CharField(max_length=60, blank=True)
    cell_phone = models.CharField(max_length=60, blank=True)
    job_series = models.IntegerField(null=True, blank=True)
    messenger = models.TextField(blank=True)
    introduce = models.TextField(blank=True)
    open_close = models.IntegerField(null=True, blank=True)
    regdate = models.IntegerField(null=True, blank=True)
    id_number = models.IntegerField(null=True, blank=True)
    update_info = models.IntegerField()
    hint = models.IntegerField(null=True, blank=True)
    answer = models.CharField(max_length=120, blank=True)
    cafe_name = models.TextField(blank=True)
    session = models.IntegerField(null=True, blank=True)
    memo = models.TextField(blank=True)
    favorite = models.IntegerField(null=True, blank=True)
    flag = models.IntegerField(null=True, blank=True)
    society_number = models.CharField(max_length=39, blank=True)

    def __unicode__(self):
        return ", ".join([self.name, self.id, str(self.student_id)])

    class Meta:
        db_table = u'member'

class MemberTest(models.Model):
    number = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=75)
    student_id = models.BigIntegerField()
    level = models.IntegerField()
    id = models.CharField(max_length=30)
    password = models.CharField(max_length=48)
    department = models.IntegerField(null=True, blank=True)
    email = models.TextField(blank=True)
    homepage = models.TextField(blank=True)
    birthday = models.DateField(null=True, blank=True)
    sun_moon = models.IntegerField(null=True, blank=True)
    home_addr_1 = models.TextField(blank=True)
    home_addr_2 = models.TextField(blank=True)
    home_zipcode = models.CharField(max_length=30, blank=True)
    home_phone = models.CharField(max_length=60, blank=True)
    job_addr_1 = models.TextField(blank=True)
    job_addr_2 = models.TextField(blank=True)
    job_zipcode = models.CharField(max_length=30, blank=True)
    job_phone = models.CharField(max_length=60, blank=True)
    cell_phone = models.CharField(max_length=60, blank=True)
    job_series = models.IntegerField(null=True, blank=True)
    messenger = models.TextField(blank=True)
    introduce = models.TextField(blank=True)
    open_close = models.IntegerField(null=True, blank=True)
    regdate = models.IntegerField(null=True, blank=True)
    id_number = models.IntegerField(null=True, blank=True)
    update_info = models.IntegerField(null=True, blank=True)
    hint = models.IntegerField(null=True, blank=True)
    answer = models.CharField(max_length=120, blank=True)
    cafe_name = models.TextField(blank=True)
    session = models.IntegerField(null=True, blank=True)
    memo = models.TextField(blank=True)
    class Meta:
        db_table = u'member_test'

class MemoAllaplus(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_allaplus'

class MemoAlumni00(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_alumni00'

class MemoAlumni01(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_alumni01'

class MemoAlumni02(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_alumni02'

class MemoAlumni03(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_alumni03'

class MemoAlumni04(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_alumni04'

class MemoAlumni05(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_alumni05'

class MemoAlumni06(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_alumni06'

class MemoAlumni07(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_alumni07'

class MemoAlumni08(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_alumni08'

class MemoAlumni09(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_alumni09'

class MemoAlumni10(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_alumni10'

class MemoAlumni72(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_alumni72'

class MemoAlumni73(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_alumni73'

class MemoAlumni74(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_alumni74'

class MemoAlumni75(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_alumni75'

class MemoAlumni76(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_alumni76'

class MemoAlumni77(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_alumni77'

class MemoAlumni78(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_alumni78'

class MemoAlumni79(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_alumni79'

class MemoAlumni80(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_alumni80'

class MemoAlumni81(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_alumni81'

class MemoAlumni82(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_alumni82'

class MemoAlumni83(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_alumni83'

class MemoAlumni84(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_alumni84'

class MemoAlumni85(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_alumni85'

class MemoAlumni86(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_alumni86'

class MemoAlumni87(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_alumni87'

class MemoAlumni88(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_alumni88'

class MemoAlumni89(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_alumni89'

class MemoAlumni90(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_alumni90'

class MemoAlumni91(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_alumni91'

class MemoAlumni92(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_alumni92'

class MemoAlumni93(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_alumni93'

class MemoAlumni94(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_alumni94'

class MemoAlumni95(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_alumni95'

class MemoAlumni96(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_alumni96'

class MemoAlumni97(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_alumni97'

class MemoAlumni98(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_alumni98'

class MemoAlumni99(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_alumni99'

class MemoCafeChuri(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_cafe_churi'

class MemoCafeCuti(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_cafe_cuti'

class MemoCafeForum(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_cafe_forum'

class MemoCafeGirlStudent(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_cafe_girl_student'

class MemoCafeGutter(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_cafe_gutter'

class MemoCafeHandtruth(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_cafe_handtruth'

class MemoCafeHeukseoker(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_cafe_heukseoker'

class MemoCafeIris(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_cafe_iris'

class MemoCafeItSecurity(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_cafe_it_security'

class MemoCafeJstorm(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_cafe_jstorm'

class MemoCafeMountainLove(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_cafe_mountain_love'

class MemoCafeNote(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_cafe_note'

class MemoCafeSecurelab(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_cafe_securelab'

class MemoCafeSnsd(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_cafe_snsd'

class MemoCafeTspin(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_cafe_tspin'

class MemoCafeWow(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_cafe_wow'

class MemoCgraph(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_cgraph'

class MemoClubAbroad(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_club_abroad'

class MemoClubBrenntano(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_club_brenntano'

class MemoClubCurseware(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_club_curseware'

class MemoClubDumb(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_club_dumb'

class MemoClubEcs(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_club_ecs'

class MemoClubFootlove(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_club_footlove'

class MemoClubFr(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_club_fr'

class MemoClubMios(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_club_mios'

class MemoClubWithweve(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_club_withweve'

class MemoCsebiz(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_csebiz'

class MemoCsesa(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_csesa'

class MemoCsesac(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_csesac'

class MemoDcgallers(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_dcgallers'

class MemoDogsix(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_dogsix'

class MemoDongneteam(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_dongneteam'

class MemoExtreamsport(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_extreamsport'

class MemoFacse(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_facse'

class MemoGamemoney(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_gamemoney'

class MemoGraduation(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_graduation'

class MemoGujja(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_gujja'

class MemoHex(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_hex'

class MemoInfo02(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_info_02'

class MemoInfoMemory(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_info_memory'

class MemoInfoMisc(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_info_misc'

class MemoJhonson(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_jhonson'

class MemoKcPhotoDc(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_kc_photo_dc'

class MemoKcPhotoFc(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_kc_photo_fc'

class MemoKichongPhoto(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_kichong_photo'

class MemoMarket(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_market'

class MemoMarlboro(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_marlboro'

class MemoMemResearch(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_mem_research'

class MemoMemory(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_memory'

class MemoNba(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_nba'

class MemoOekaki(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_oekaki'

class MemoParkcue(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_parkcue'

class MemoPartAd(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_part_ad'

class MemoPartCulture(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_part_culture'

class MemoPartJungtong(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_part_jungtong'

class MemoPartNeo(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_part_neo'

class MemoPartPlan(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_part_plan'

class MemoPartSocial(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_part_social'

class MemoPhoto(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_photo'

class MemoPhoto2(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_photo2'

class MemoPray(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_pray'

class MemoReload(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_reload'

class MemoSketch(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_sketch'

class MemoStudyBook(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_study_book'

class MemoTrash(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_trash'

class MemoTwistedlife(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_twistedlife'

class MemoUnited(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_united'

class MemoVolunteers(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_volunteers'

class MemoWebzineBook(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_webzine_book'

class MemoWebzinePeople(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_webzine_people'

class MemoWebzinePhoto(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_webzine_photo'

class MemoWebzineculture(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=48, blank=True)
    reg_date = models.DateField(null=True, blank=True)
    content = models.TextField(blank=True)
    headnum = models.IntegerField(null=True, blank=True)
    depth = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'memo_webzineculture'

class Message(models.Model):
    msg_no = models.IntegerField(primary_key=True)
    receive_id = models.CharField(max_length=30, blank=True)
    send_id = models.CharField(max_length=30, blank=True)
    m_title = models.CharField(max_length=765)
    m_content = models.TextField(blank=True)
    t_sent = models.IntegerField(null=True, blank=True)
    t_received = models.IntegerField(null=True, blank=True)
    confirm = models.IntegerField()
    deletion = models.IntegerField()
    class Meta:
        db_table = u'message'

class Nospam(models.Model):
    id = models.IntegerField(primary_key=True)
    word = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'nospam'

class PhotoAllaplus(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=135, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_allaplus'

class PhotoAlumni00(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_alumni00'

class PhotoAlumni01(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_alumni01'

class PhotoAlumni02(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_alumni02'

class PhotoAlumni03(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_alumni03'

class PhotoAlumni04(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_alumni04'

class PhotoAlumni05(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=135, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_alumni05'

class PhotoAlumni06(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=135, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_alumni06'

class PhotoAlumni07(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=135, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_alumni07'

class PhotoAlumni08(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=135, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_alumni08'

class PhotoAlumni09(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=135, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_alumni09'

class PhotoAlumni10(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=135, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_alumni10'

class PhotoAlumni72(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_alumni72'

class PhotoAlumni73(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_alumni73'

class PhotoAlumni74(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_alumni74'

class PhotoAlumni75(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_alumni75'

class PhotoAlumni76(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_alumni76'

class PhotoAlumni77(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_alumni77'

class PhotoAlumni78(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_alumni78'

class PhotoAlumni79(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_alumni79'

class PhotoAlumni80(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_alumni80'

class PhotoAlumni81(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_alumni81'

class PhotoAlumni82(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_alumni82'

class PhotoAlumni83(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_alumni83'

class PhotoAlumni84(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_alumni84'

class PhotoAlumni85(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_alumni85'

class PhotoAlumni86(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_alumni86'

class PhotoAlumni87(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_alumni87'

class PhotoAlumni88(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_alumni88'

class PhotoAlumni89(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_alumni89'

class PhotoAlumni90(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_alumni90'

class PhotoAlumni91(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_alumni91'

class PhotoAlumni92(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_alumni92'

class PhotoAlumni93(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_alumni93'

class PhotoAlumni94(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_alumni94'

class PhotoAlumni95(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_alumni95'

class PhotoAlumni96(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_alumni96'

class PhotoAlumni97(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_alumni97'

class PhotoAlumni98(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_alumni98'

class PhotoAlumni99(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_alumni99'

class PhotoCafeChuri(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=135, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_cafe_churi'

class PhotoCafeCuti(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=135, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_cafe_cuti'

class PhotoCafeForum(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=135, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_cafe_forum'

class PhotoCafeGirlStudent(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=135, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_cafe_girl_student'

class PhotoCafeGutter(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=135, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_cafe_gutter'

class PhotoCafeHandtruth(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=135, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_cafe_handtruth'

class PhotoCafeHeukseoker(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=135, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_cafe_heukseoker'

class PhotoCafeIris(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=135, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_cafe_iris'

class PhotoCafeItSecurity(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=135, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_cafe_it_security'

class PhotoCafeJstorm(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=135, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_cafe_jstorm'

class PhotoCafeMountainLove(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=135, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_cafe_mountain_love'

class PhotoCafeNote(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=135, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_cafe_note'

class PhotoCafeSecurelab(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=135, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_cafe_securelab'

class PhotoCafeSnsd(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=135, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_cafe_snsd'

class PhotoCafeTspin(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=135, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_cafe_tspin'

class PhotoCafeWow(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=135, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_cafe_wow'

class PhotoCgraph(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=135, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_cgraph'

class PhotoClubAbroad(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_club_abroad'

class PhotoClubBrenntano(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_club_brenntano'

class PhotoClubCurseware(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_club_curseware'

class PhotoClubDumb(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_club_dumb'

class PhotoClubEcs(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_club_ecs'

class PhotoClubFootlove(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_club_footlove'

class PhotoClubFr(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=135, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_club_fr'

class PhotoClubMios(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=135, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_club_mios'

class PhotoClubWithweve(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_club_withweve'

class PhotoCsebiz(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=135, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_csebiz'

class PhotoCsesa(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=135, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_csesa'

class PhotoCsesac(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=135, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_csesac'

class PhotoDcgallers(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=135, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_dcgallers'

class PhotoDogsix(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=135, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_dogsix'

class PhotoDongneteam(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_dongneteam'

class PhotoExtreamsport(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=135, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_extreamsport'

class PhotoFacse(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=135, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_facse'

class PhotoGamemoney(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=135, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_gamemoney'

class PhotoGraduation(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_graduation'

class PhotoGujja(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=135, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_gujja'

class PhotoHex(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=135, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_hex'

class PhotoInfo02(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_info_02'

class PhotoInfoMemory(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_info_memory'

class PhotoInfoMisc(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_info_misc'

class PhotoJhonson(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=135, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_jhonson'

class PhotoKcPhotoDc(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_kc_photo_dc'

class PhotoKcPhotoFc(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_kc_photo_fc'

class PhotoKichongPhoto(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_kichong_photo'

class PhotoMarket(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_market'

class PhotoMarlboro(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=135, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_marlboro'

class PhotoMemResearch(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=135, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_mem_research'

class PhotoMemory(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_memory'

class PhotoNba(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=135, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_nba'

class PhotoOekaki(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_oekaki'

class PhotoParkcue(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=135, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_parkcue'

class PhotoPartAd(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_part_ad'

class PhotoPartCulture(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=135, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_part_culture'

class PhotoPartJungtong(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_part_jungtong'

class PhotoPartNeo(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_part_neo'

class PhotoPartPlan(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_part_plan'

class PhotoPartSocial(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=135, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_part_social'

class PhotoPhoto(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=135, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_photo'

class PhotoPhoto2(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=135, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_photo2'

class PhotoPray(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=135, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_pray'

class PhotoReload(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=135, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_reload'

class PhotoSketch(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_sketch'

class PhotoStudyBook(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_study_book'

class PhotoTrash(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=135, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_trash'

class PhotoTwistedlife(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=135, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_twistedlife'

class PhotoUnited(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=60)
    ip = models.CharField(max_length=51, blank=True)
    title = models.CharField(max_length=300)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=180, blank=True)
    count = models.IntegerField(null=True, blank=True)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_united'

class PhotoVolunteers(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=135, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_volunteers'

class PhotoWebzineBook(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_webzine_book'

class PhotoWebzinePeople(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_webzine_people'

class PhotoWebzinePhoto(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_webzine_photo'

class PhotoWebzineculture(models.Model):
    id = models.IntegerField(primary_key=True)
    idx = models.IntegerField()
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=75)
    password = models.CharField(max_length=48, blank=True)
    ip = models.CharField(max_length=51, blank=True)
    email = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=72)
    notice_deadline = models.DateField()
    title = models.CharField(max_length=300)
    count = models.IntegerField(null=True, blank=True)
    reg_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(blank=True)
    file_name = models.CharField(max_length=300, blank=True)
    thread = models.CharField(max_length=765)
    comment = models.IntegerField()
    class Meta:
        db_table = u'photo_webzineculture'

class Photoinfo(models.Model):
    no = models.IntegerField(primary_key=True)
    tablename = models.CharField(max_length=75)
    title = models.CharField(max_length=300)
    admin_id = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    belongto = models.CharField(max_length=90, blank=True)
    skin = models.CharField(max_length=60, blank=True)
    header = models.CharField(max_length=240, blank=True)
    tail = models.CharField(max_length=240, blank=True)
    line_number = models.IntegerField()
    permission = models.BigIntegerField()
    use_category = models.IntegerField()
    category = models.TextField(blank=True)
    use_notice = models.IntegerField(null=True, blank=True)
    use_fileupload = models.IntegerField(null=True, blank=True)
    max_filesize = models.BigIntegerField(null=True, blank=True)
    use_filtering = models.IntegerField(null=True, blank=True)
    filter = models.TextField(blank=True)
    count = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return ", ".join([self.title, self.tablename])

    class Meta:
        db_table = u'photoinfo'

class PollData(models.Model):
    id = models.IntegerField(primary_key=True)
    poll_id = models.IntegerField()
    data_id = models.IntegerField()
    content = models.CharField(max_length=180)
    class Meta:
        db_table = u'poll_data'

class PollMain(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=180)
    content = models.TextField()
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    target = models.CharField(max_length=180)
    progress = models.CharField(max_length=3)
    retry = models.CharField(max_length=3)
    retry_num = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'poll_main'

class PollResult(models.Model):
    id = models.IntegerField(primary_key=True)
    poll_id = models.IntegerField()
    data_id = models.IntegerField()
    user_id = models.CharField(max_length=60)
    select_time = models.DateTimeField(null=True, blank=True)
    ip = models.CharField(max_length=45, blank=True)
    class Meta:
        db_table = u'poll_result'

class PopupNotice(models.Model):
    num = models.IntegerField(primary_key=True)
    msg = models.TextField(blank=True)
    class Meta:
        db_table = u'popup_notice'

class RssAdmin(models.Model):
    no = models.IntegerField(primary_key=True)
    address1 = models.TextField(blank=True)
    address2 = models.TextField(blank=True)
    maxnum = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'rss_admin'

class RssContent(models.Model):
    no = models.IntegerField(primary_key=True)
    address = models.TextField(blank=True)
    maxnum = models.IntegerField(null=True, blank=True)
    useornot = models.IntegerField(null=True, blank=True)
    description = models.TextField(blank=True)
    frequency = models.IntegerField()
    class Meta:
        db_table = u'rss_content'

class RssPersonal(models.Model):
    number = models.IntegerField(primary_key=True)
    user_id = models.CharField(max_length=30, blank=True)
    rss_add = models.TextField(blank=True)
    callorder = models.IntegerField(null=True, blank=True)
    callnum = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'rss_personal'

class Zipcode(models.Model):
    zipcode = models.CharField(max_length=21, db_column='ZIPCODE', blank=True) # Field name made lowercase.
    sido = models.CharField(max_length=12, db_column='SIDO', blank=True) # Field name made lowercase.
    gugun = models.CharField(max_length=39, db_column='GUGUN', blank=True) # Field name made lowercase.
    dong = models.CharField(max_length=129, db_column='DONG', blank=True) # Field name made lowercase.
    bunji = models.CharField(max_length=51, db_column='BUNJI', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'zipcode'

