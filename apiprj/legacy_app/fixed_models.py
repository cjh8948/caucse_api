from django.db import models

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
    class Meta:
        db_table = u'cafe_info'

class Calendar(models.Model):
    id = models.AutoField(primary_key=True)
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
    class Meta:
        db_table = u'club_info'

class Favorite(models.Model):
    no = models.IntegerField(primary_key=True)
    user_id = models.CharField(max_length=30, blank=True)
    tablename = models.CharField(max_length=60, blank=True)
    priority = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'favorite'

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
    class Meta:
        db_table = u'member'
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
    id = models.AutoField(primary_key=True)
    word = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'nospam'


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
    class Meta:
        db_table = u'photoinfo'

class PopupNotice(models.Model):
    num = models.IntegerField(primary_key=True)
    msg = models.TextField(blank=True)
    class Meta:
        db_table = u'popup_notice'





