# -*-coding:utf-8-*-
"""
`django-admin.py inspectdb` 커맨드를 통해 legacy 분석 후 자동 생성된 모델을
기반으로 `django-admin.py gen_models` 커맨드로 자동생성한 Board*, Comment*, 
Memo* 모델이 포함하였음. 

* gen_models 커맨드는 boardinfo, photoinfo 테이블에 저장된 tablename을 기반으로
모델을 자동생성함. boardinfo에 등록되지 않은 테이블은 자동생성되지 않음.
"""
from django.db import models
from abstract_models import AbstractBoard, AbstractMemo, AbstractComment

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

# auto generated for board board_allaplus
class BoardAllaplus(AbstractBoard):
    class Meta:
        db_table = u'board_allaplus'
class CommentAllaplus(AbstractComment):
    class Meta:
        db_table = u'comment_allaplus'

# auto generated for board board_alumni
class BoardAlumni(AbstractBoard):
    class Meta:
        db_table = u'board_alumni'
class CommentAlumni(AbstractComment):
    class Meta:
        db_table = u'comment_alumni'

# auto generated for board board_alumni00
class BoardAlumni00(AbstractBoard):
    class Meta:
        db_table = u'board_alumni00'
class CommentAlumni00(AbstractComment):
    class Meta:
        db_table = u'comment_alumni00'

# auto generated for board board_alumni01
class BoardAlumni01(AbstractBoard):
    class Meta:
        db_table = u'board_alumni01'
class CommentAlumni01(AbstractComment):
    class Meta:
        db_table = u'comment_alumni01'

# auto generated for board board_alumni02
class BoardAlumni02(AbstractBoard):
    class Meta:
        db_table = u'board_alumni02'
class CommentAlumni02(AbstractComment):
    class Meta:
        db_table = u'comment_alumni02'

# auto generated for board board_alumni03
class BoardAlumni03(AbstractBoard):
    class Meta:
        db_table = u'board_alumni03'
class CommentAlumni03(AbstractComment):
    class Meta:
        db_table = u'comment_alumni03'

# auto generated for board board_alumni04
class BoardAlumni04(AbstractBoard):
    class Meta:
        db_table = u'board_alumni04'
class CommentAlumni04(AbstractComment):
    class Meta:
        db_table = u'comment_alumni04'

# auto generated for board board_alumni05
class BoardAlumni05(AbstractBoard):
    class Meta:
        db_table = u'board_alumni05'
class CommentAlumni05(AbstractComment):
    class Meta:
        db_table = u'comment_alumni05'

# auto generated for board board_alumni06
class BoardAlumni06(AbstractBoard):
    class Meta:
        db_table = u'board_alumni06'
class CommentAlumni06(AbstractComment):
    class Meta:
        db_table = u'comment_alumni06'

# auto generated for board board_alumni07
class BoardAlumni07(AbstractBoard):
    class Meta:
        db_table = u'board_alumni07'
class CommentAlumni07(AbstractComment):
    class Meta:
        db_table = u'comment_alumni07'

# auto generated for board board_alumni08
class BoardAlumni08(AbstractBoard):
    class Meta:
        db_table = u'board_alumni08'
class CommentAlumni08(AbstractComment):
    class Meta:
        db_table = u'comment_alumni08'

# auto generated for board board_alumni09
class BoardAlumni09(AbstractBoard):
    class Meta:
        db_table = u'board_alumni09'
class CommentAlumni09(AbstractComment):
    class Meta:
        db_table = u'comment_alumni09'

# auto generated for board board_alumni10
class BoardAlumni10(AbstractBoard):
    class Meta:
        db_table = u'board_alumni10'
class CommentAlumni10(AbstractComment):
    class Meta:
        db_table = u'comment_alumni10'

# auto generated for board board_alumni72
class BoardAlumni72(AbstractBoard):
    class Meta:
        db_table = u'board_alumni72'
class CommentAlumni72(AbstractComment):
    class Meta:
        db_table = u'comment_alumni72'

# auto generated for board board_alumni73
class BoardAlumni73(AbstractBoard):
    class Meta:
        db_table = u'board_alumni73'
class CommentAlumni73(AbstractComment):
    class Meta:
        db_table = u'comment_alumni73'

# auto generated for board board_alumni74
class BoardAlumni74(AbstractBoard):
    class Meta:
        db_table = u'board_alumni74'
class CommentAlumni74(AbstractComment):
    class Meta:
        db_table = u'comment_alumni74'

# auto generated for board board_alumni75
class BoardAlumni75(AbstractBoard):
    class Meta:
        db_table = u'board_alumni75'
class CommentAlumni75(AbstractComment):
    class Meta:
        db_table = u'comment_alumni75'

# auto generated for board board_alumni76
class BoardAlumni76(AbstractBoard):
    class Meta:
        db_table = u'board_alumni76'
class CommentAlumni76(AbstractComment):
    class Meta:
        db_table = u'comment_alumni76'

# auto generated for board board_alumni77
class BoardAlumni77(AbstractBoard):
    class Meta:
        db_table = u'board_alumni77'
class CommentAlumni77(AbstractComment):
    class Meta:
        db_table = u'comment_alumni77'

# auto generated for board board_alumni78
class BoardAlumni78(AbstractBoard):
    class Meta:
        db_table = u'board_alumni78'
class CommentAlumni78(AbstractComment):
    class Meta:
        db_table = u'comment_alumni78'

# auto generated for board board_alumni79
class BoardAlumni79(AbstractBoard):
    class Meta:
        db_table = u'board_alumni79'
class CommentAlumni79(AbstractComment):
    class Meta:
        db_table = u'comment_alumni79'

# auto generated for board board_alumni80
class BoardAlumni80(AbstractBoard):
    class Meta:
        db_table = u'board_alumni80'
class CommentAlumni80(AbstractComment):
    class Meta:
        db_table = u'comment_alumni80'

# auto generated for board board_alumni81
class BoardAlumni81(AbstractBoard):
    class Meta:
        db_table = u'board_alumni81'
class CommentAlumni81(AbstractComment):
    class Meta:
        db_table = u'comment_alumni81'

# auto generated for board board_alumni82
class BoardAlumni82(AbstractBoard):
    class Meta:
        db_table = u'board_alumni82'
class CommentAlumni82(AbstractComment):
    class Meta:
        db_table = u'comment_alumni82'

# auto generated for board board_alumni83
class BoardAlumni83(AbstractBoard):
    class Meta:
        db_table = u'board_alumni83'
class CommentAlumni83(AbstractComment):
    class Meta:
        db_table = u'comment_alumni83'

# auto generated for board board_alumni84
class BoardAlumni84(AbstractBoard):
    class Meta:
        db_table = u'board_alumni84'
class CommentAlumni84(AbstractComment):
    class Meta:
        db_table = u'comment_alumni84'

# auto generated for board board_alumni85
class BoardAlumni85(AbstractBoard):
    class Meta:
        db_table = u'board_alumni85'
class CommentAlumni85(AbstractComment):
    class Meta:
        db_table = u'comment_alumni85'

# auto generated for board board_alumni86
class BoardAlumni86(AbstractBoard):
    class Meta:
        db_table = u'board_alumni86'
class CommentAlumni86(AbstractComment):
    class Meta:
        db_table = u'comment_alumni86'

# auto generated for board board_alumni87
class BoardAlumni87(AbstractBoard):
    class Meta:
        db_table = u'board_alumni87'
class CommentAlumni87(AbstractComment):
    class Meta:
        db_table = u'comment_alumni87'

# auto generated for board board_alumni88
class BoardAlumni88(AbstractBoard):
    class Meta:
        db_table = u'board_alumni88'
class CommentAlumni88(AbstractComment):
    class Meta:
        db_table = u'comment_alumni88'

# auto generated for board board_alumni89
class BoardAlumni89(AbstractBoard):
    class Meta:
        db_table = u'board_alumni89'
class CommentAlumni89(AbstractComment):
    class Meta:
        db_table = u'comment_alumni89'

# auto generated for board board_alumni90
class BoardAlumni90(AbstractBoard):
    class Meta:
        db_table = u'board_alumni90'
class CommentAlumni90(AbstractComment):
    class Meta:
        db_table = u'comment_alumni90'

# auto generated for board board_alumni91
class BoardAlumni91(AbstractBoard):
    class Meta:
        db_table = u'board_alumni91'
class CommentAlumni91(AbstractComment):
    class Meta:
        db_table = u'comment_alumni91'

# auto generated for board board_alumni92
class BoardAlumni92(AbstractBoard):
    class Meta:
        db_table = u'board_alumni92'
class CommentAlumni92(AbstractComment):
    class Meta:
        db_table = u'comment_alumni92'

# auto generated for board board_alumni93
class BoardAlumni93(AbstractBoard):
    class Meta:
        db_table = u'board_alumni93'
class CommentAlumni93(AbstractComment):
    class Meta:
        db_table = u'comment_alumni93'

# auto generated for board board_alumni94
class BoardAlumni94(AbstractBoard):
    class Meta:
        db_table = u'board_alumni94'
class CommentAlumni94(AbstractComment):
    class Meta:
        db_table = u'comment_alumni94'

# auto generated for board board_alumni95
class BoardAlumni95(AbstractBoard):
    class Meta:
        db_table = u'board_alumni95'
class CommentAlumni95(AbstractComment):
    class Meta:
        db_table = u'comment_alumni95'

# auto generated for board board_alumni96
class BoardAlumni96(AbstractBoard):
    class Meta:
        db_table = u'board_alumni96'
class CommentAlumni96(AbstractComment):
    class Meta:
        db_table = u'comment_alumni96'

# auto generated for board board_alumni97
class BoardAlumni97(AbstractBoard):
    class Meta:
        db_table = u'board_alumni97'
class CommentAlumni97(AbstractComment):
    class Meta:
        db_table = u'comment_alumni97'

# auto generated for board board_alumni98
class BoardAlumni98(AbstractBoard):
    class Meta:
        db_table = u'board_alumni98'
class CommentAlumni98(AbstractComment):
    class Meta:
        db_table = u'comment_alumni98'

# auto generated for board board_alumni99
class BoardAlumni99(AbstractBoard):
    class Meta:
        db_table = u'board_alumni99'
class CommentAlumni99(AbstractComment):
    class Meta:
        db_table = u'comment_alumni99'

# auto generated for board board_alumninews
class BoardAlumninews(AbstractBoard):
    class Meta:
        db_table = u'board_alumninews'
class CommentAlumninews(AbstractComment):
    class Meta:
        db_table = u'comment_alumninews'

# auto generated for board board_alumninews1
class BoardAlumninews1(AbstractBoard):
    class Meta:
        db_table = u'board_alumninews1'
class CommentAlumninews1(AbstractComment):
    class Meta:
        db_table = u'comment_alumninews1'

# auto generated for board board_alumni_memory
class BoardAlumniMemory(AbstractBoard):
    class Meta:
        db_table = u'board_alumni_memory'
class CommentAlumniMemory(AbstractComment):
    class Meta:
        db_table = u'comment_alumni_memory'

# auto generated for board board_anonymous
class BoardAnonymous(AbstractBoard):
    class Meta:
        db_table = u'board_anonymous'
class CommentAnonymous(AbstractComment):
    class Meta:
        db_table = u'comment_anonymous'

# auto generated for board board_board_tour
class BoardBoardTour(AbstractBoard):
    class Meta:
        db_table = u'board_board_tour'
class CommentBoardTour(AbstractComment):
    class Meta:
        db_table = u'comment_board_tour'

# auto generated for board board_bug
class BoardBug(AbstractBoard):
    class Meta:
        db_table = u'board_bug'
class CommentBug(AbstractComment):
    class Meta:
        db_table = u'comment_bug'

# auto generated for board board_cafe_appellation
class BoardCafeAppellation(AbstractBoard):
    class Meta:
        db_table = u'board_cafe_appellation'
class CommentCafeAppellation(AbstractComment):
    class Meta:
        db_table = u'comment_cafe_appellation'

# auto generated for board board_cafe_appellation2
class BoardCafeAppellation2(AbstractBoard):
    class Meta:
        db_table = u'board_cafe_appellation2'
class CommentCafeAppellation2(AbstractComment):
    class Meta:
        db_table = u'comment_cafe_appellation2'

# auto generated for board board_cafe_appellation3
class BoardCafeAppellation3(AbstractBoard):
    class Meta:
        db_table = u'board_cafe_appellation3'
class CommentCafeAppellation3(AbstractComment):
    class Meta:
        db_table = u'comment_cafe_appellation3'

# auto generated for board board_cafe_board3
class BoardCafeBoard3(AbstractBoard):
    class Meta:
        db_table = u'board_cafe_board3'
class CommentCafeBoard3(AbstractComment):
    class Meta:
        db_table = u'comment_cafe_board3'

# auto generated for board board_cafe_churi
class BoardCafeChuri(AbstractBoard):
    class Meta:
        db_table = u'board_cafe_churi'
class CommentCafeChuri(AbstractComment):
    class Meta:
        db_table = u'comment_cafe_churi'

# auto generated for board board_cafe_cuti
class BoardCafeCuti(AbstractBoard):
    class Meta:
        db_table = u'board_cafe_cuti'
class CommentCafeCuti(AbstractComment):
    class Meta:
        db_table = u'comment_cafe_cuti'

# auto generated for board board_cafe_forum
class BoardCafeForum(AbstractBoard):
    class Meta:
        db_table = u'board_cafe_forum'
class CommentCafeForum(AbstractComment):
    class Meta:
        db_table = u'comment_cafe_forum'

# auto generated for board board_cafe_girl_student
class BoardCafeGirlStudent(AbstractBoard):
    class Meta:
        db_table = u'board_cafe_girl_student'
class CommentCafeGirlStudent(AbstractComment):
    class Meta:
        db_table = u'comment_cafe_girl_student'

# auto generated for board board_cafe_gutter
class BoardCafeGutter(AbstractBoard):
    class Meta:
        db_table = u'board_cafe_gutter'
class CommentCafeGutter(AbstractComment):
    class Meta:
        db_table = u'comment_cafe_gutter'

# auto generated for board board_cafe_gutter2
class BoardCafeGutter2(AbstractBoard):
    class Meta:
        db_table = u'board_cafe_gutter2'
class CommentCafeGutter2(AbstractComment):
    class Meta:
        db_table = u'comment_cafe_gutter2'

# auto generated for board board_cafe_handtruth
class BoardCafeHandtruth(AbstractBoard):
    class Meta:
        db_table = u'board_cafe_handtruth'
class CommentCafeHandtruth(AbstractComment):
    class Meta:
        db_table = u'comment_cafe_handtruth'

# auto generated for board board_cafe_handtruth2
class BoardCafeHandtruth2(AbstractBoard):
    class Meta:
        db_table = u'board_cafe_handtruth2'
class CommentCafeHandtruth2(AbstractComment):
    class Meta:
        db_table = u'comment_cafe_handtruth2'

# auto generated for board board_cafe_heukseoker
class BoardCafeHeukseoker(AbstractBoard):
    class Meta:
        db_table = u'board_cafe_heukseoker'
class CommentCafeHeukseoker(AbstractComment):
    class Meta:
        db_table = u'comment_cafe_heukseoker'

# auto generated for board board_cafe_heukseoker2
class BoardCafeHeukseoker2(AbstractBoard):
    class Meta:
        db_table = u'board_cafe_heukseoker2'
class CommentCafeHeukseoker2(AbstractComment):
    class Meta:
        db_table = u'comment_cafe_heukseoker2'

# auto generated for board board_cafe_homesteal
class BoardCafeHomesteal(AbstractBoard):
    class Meta:
        db_table = u'board_cafe_homesteal'
class CommentCafeHomesteal(AbstractComment):
    class Meta:
        db_table = u'comment_cafe_homesteal'

# auto generated for board board_cafe_iris
class BoardCafeIris(AbstractBoard):
    class Meta:
        db_table = u'board_cafe_iris'
class CommentCafeIris(AbstractComment):
    class Meta:
        db_table = u'comment_cafe_iris'

# auto generated for board board_cafe_it_security
class BoardCafeItSecurity(AbstractBoard):
    class Meta:
        db_table = u'board_cafe_it_security'
class CommentCafeItSecurity(AbstractComment):
    class Meta:
        db_table = u'comment_cafe_it_security'

# auto generated for board board_cafe_jokbal
class BoardCafeJokbal(AbstractBoard):
    class Meta:
        db_table = u'board_cafe_jokbal'
class CommentCafeJokbal(AbstractComment):
    class Meta:
        db_table = u'comment_cafe_jokbal'

# auto generated for board board_cafe_jstorm
class BoardCafeJstorm(AbstractBoard):
    class Meta:
        db_table = u'board_cafe_jstorm'
class CommentCafeJstorm(AbstractComment):
    class Meta:
        db_table = u'comment_cafe_jstorm'

# auto generated for board board_cafe_mountain_love
class BoardCafeMountainLove(AbstractBoard):
    class Meta:
        db_table = u'board_cafe_mountain_love'
class CommentCafeMountainLove(AbstractComment):
    class Meta:
        db_table = u'comment_cafe_mountain_love'

# auto generated for board board_cafe_note
class BoardCafeNote(AbstractBoard):
    class Meta:
        db_table = u'board_cafe_note'
class CommentCafeNote(AbstractComment):
    class Meta:
        db_table = u'comment_cafe_note'

# auto generated for board board_cafe_note2
class BoardCafeNote2(AbstractBoard):
    class Meta:
        db_table = u'board_cafe_note2'
class CommentCafeNote2(AbstractComment):
    class Meta:
        db_table = u'comment_cafe_note2'

# auto generated for board board_cafe_present
class BoardCafePresent(AbstractBoard):
    class Meta:
        db_table = u'board_cafe_present'
class CommentCafePresent(AbstractComment):
    class Meta:
        db_table = u'comment_cafe_present'

# auto generated for board board_cafe_securelab
class BoardCafeSecurelab(AbstractBoard):
    class Meta:
        db_table = u'board_cafe_securelab'
class CommentCafeSecurelab(AbstractComment):
    class Meta:
        db_table = u'comment_cafe_securelab'

# auto generated for board board_cafe_securelab2
class BoardCafeSecurelab2(AbstractBoard):
    class Meta:
        db_table = u'board_cafe_securelab2'
class CommentCafeSecurelab2(AbstractComment):
    class Meta:
        db_table = u'comment_cafe_securelab2'

# auto generated for board board_cafe_snsd
class BoardCafeSnsd(AbstractBoard):
    class Meta:
        db_table = u'board_cafe_snsd'
class CommentCafeSnsd(AbstractComment):
    class Meta:
        db_table = u'comment_cafe_snsd'

# auto generated for board board_cafe_steamers
class BoardCafeSteamers(AbstractBoard):
    class Meta:
        db_table = u'board_cafe_steamers'
class CommentCafeSteamers(AbstractComment):
    class Meta:
        db_table = u'comment_cafe_steamers'

# auto generated for board board_cafe_steamers2
class BoardCafeSteamers2(AbstractBoard):
    class Meta:
        db_table = u'board_cafe_steamers2'
class CommentCafeSteamers2(AbstractComment):
    class Meta:
        db_table = u'comment_cafe_steamers2'

# auto generated for board board_cafe_steamers3
class BoardCafeSteamers3(AbstractBoard):
    class Meta:
        db_table = u'board_cafe_steamers3'
class CommentCafeSteamers3(AbstractComment):
    class Meta:
        db_table = u'comment_cafe_steamers3'

# auto generated for board board_cafe_tspin
class BoardCafeTspin(AbstractBoard):
    class Meta:
        db_table = u'board_cafe_tspin'
class CommentCafeTspin(AbstractComment):
    class Meta:
        db_table = u'comment_cafe_tspin'

# auto generated for board board_cafe_wow
class BoardCafeWow(AbstractBoard):
    class Meta:
        db_table = u'board_cafe_wow'
class CommentCafeWow(AbstractComment):
    class Meta:
        db_table = u'comment_cafe_wow'

# auto generated for board board_caucsesa
class BoardCaucsesa(AbstractBoard):
    class Meta:
        db_table = u'board_caucsesa'
class CommentCaucsesa(AbstractComment):
    class Meta:
        db_table = u'comment_caucsesa'

# auto generated for board board_cgraph
class BoardCgraph(AbstractBoard):
    class Meta:
        db_table = u'board_cgraph'
class CommentCgraph(AbstractComment):
    class Meta:
        db_table = u'comment_cgraph'

# auto generated for board board_club_abroad
class BoardClubAbroad(AbstractBoard):
    class Meta:
        db_table = u'board_club_abroad'
class CommentClubAbroad(AbstractComment):
    class Meta:
        db_table = u'comment_club_abroad'

# auto generated for board board_club_baseball
class BoardClubBaseball(AbstractBoard):
    class Meta:
        db_table = u'board_club_baseball'
class CommentClubBaseball(AbstractComment):
    class Meta:
        db_table = u'comment_club_baseball'

# auto generated for board board_club_brenntano
class BoardClubBrenntano(AbstractBoard):
    class Meta:
        db_table = u'board_club_brenntano'
class CommentClubBrenntano(AbstractComment):
    class Meta:
        db_table = u'comment_club_brenntano'

# auto generated for board board_club_camera
class BoardClubCamera(AbstractBoard):
    class Meta:
        db_table = u'board_club_camera'
class CommentClubCamera(AbstractComment):
    class Meta:
        db_table = u'comment_club_camera'

# auto generated for board board_club_comball
class BoardClubComball(AbstractBoard):
    class Meta:
        db_table = u'board_club_comball'
class CommentClubComball(AbstractComment):
    class Meta:
        db_table = u'comment_club_comball'

# auto generated for board board_club_curseware
class BoardClubCurseware(AbstractBoard):
    class Meta:
        db_table = u'board_club_curseware'
class CommentClubCurseware(AbstractComment):
    class Meta:
        db_table = u'comment_club_curseware'

# auto generated for board board_club_curseware2
class BoardClubCurseware2(AbstractBoard):
    class Meta:
        db_table = u'board_club_curseware2'
class CommentClubCurseware2(AbstractComment):
    class Meta:
        db_table = u'comment_club_curseware2'

# auto generated for board board_club_devils
class BoardClubDevils(AbstractBoard):
    class Meta:
        db_table = u'board_club_devils'
class CommentClubDevils(AbstractComment):
    class Meta:
        db_table = u'comment_club_devils'

# auto generated for board board_club_ecs
class BoardClubEcs(AbstractBoard):
    class Meta:
        db_table = u'board_club_ecs'
class CommentClubEcs(AbstractComment):
    class Meta:
        db_table = u'comment_club_ecs'

# auto generated for board board_club_footlove
class BoardClubFootlove(AbstractBoard):
    class Meta:
        db_table = u'board_club_footlove'
class CommentClubFootlove(AbstractComment):
    class Meta:
        db_table = u'comment_club_footlove'

# auto generated for board board_club_fr
class BoardClubFr(AbstractBoard):
    class Meta:
        db_table = u'board_club_fr'
class CommentClubFr(AbstractComment):
    class Meta:
        db_table = u'comment_club_fr'

# auto generated for board board_club_freesoul
class BoardClubFreesoul(AbstractBoard):
    class Meta:
        db_table = u'board_club_freesoul'
class CommentClubFreesoul(AbstractComment):
    class Meta:
        db_table = u'comment_club_freesoul'

# auto generated for board board_club_game
class BoardClubGame(AbstractBoard):
    class Meta:
        db_table = u'board_club_game'
class CommentClubGame(AbstractComment):
    class Meta:
        db_table = u'comment_club_game'

# auto generated for board board_club_maim
class BoardClubMaim(AbstractBoard):
    class Meta:
        db_table = u'board_club_maim'
class CommentClubMaim(AbstractComment):
    class Meta:
        db_table = u'comment_club_maim'

# auto generated for board board_club_mios
class BoardClubMios(AbstractBoard):
    class Meta:
        db_table = u'board_club_mios'
class CommentClubMios(AbstractComment):
    class Meta:
        db_table = u'comment_club_mios'

# auto generated for board board_club_mios_sub1
class BoardClubMiosSub1(AbstractBoard):
    class Meta:
        db_table = u'board_club_mios_sub1'
class CommentClubMiosSub1(AbstractComment):
    class Meta:
        db_table = u'comment_club_mios_sub1'

# auto generated for board board_club_netory
class BoardClubNetory(AbstractBoard):
    class Meta:
        db_table = u'board_club_netory'
class CommentClubNetory(AbstractComment):
    class Meta:
        db_table = u'comment_club_netory'

# auto generated for board board_club_oomg
class BoardClubOomg(AbstractBoard):
    class Meta:
        db_table = u'board_club_oomg'
class CommentClubOomg(AbstractComment):
    class Meta:
        db_table = u'comment_club_oomg'

# auto generated for board board_club_question
class BoardClubQuestion(AbstractBoard):
    class Meta:
        db_table = u'board_club_question'
class CommentClubQuestion(AbstractComment):
    class Meta:
        db_table = u'comment_club_question'

# auto generated for board board_club_shift
class BoardClubShift(AbstractBoard):
    class Meta:
        db_table = u'board_club_shift'
class CommentClubShift(AbstractComment):
    class Meta:
        db_table = u'comment_club_shift'

# auto generated for board board_club_soesl
class BoardClubSoesl(AbstractBoard):
    class Meta:
        db_table = u'board_club_soesl'
class CommentClubSoesl(AbstractComment):
    class Meta:
        db_table = u'comment_club_soesl'

# auto generated for board board_club_ssoa
class BoardClubSsoa(AbstractBoard):
    class Meta:
        db_table = u'board_club_ssoa'
class CommentClubSsoa(AbstractComment):
    class Meta:
        db_table = u'comment_club_ssoa'

# auto generated for board board_club_staff
class BoardClubStaff(AbstractBoard):
    class Meta:
        db_table = u'board_club_staff'
class CommentClubStaff(AbstractComment):
    class Meta:
        db_table = u'comment_club_staff'

# auto generated for board board_club_sullen
class BoardClubSullen(AbstractBoard):
    class Meta:
        db_table = u'board_club_sullen'
class CommentClubSullen(AbstractComment):
    class Meta:
        db_table = u'comment_club_sullen'

# auto generated for board board_club_sylph
class BoardClubSylph(AbstractBoard):
    class Meta:
        db_table = u'board_club_sylph'
class CommentClubSylph(AbstractComment):
    class Meta:
        db_table = u'comment_club_sylph'

# auto generated for board board_club_trash
class BoardClubTrash(AbstractBoard):
    class Meta:
        db_table = u'board_club_trash'
class CommentClubTrash(AbstractComment):
    class Meta:
        db_table = u'comment_club_trash'

# auto generated for board board_club_withweve
class BoardClubWithweve(AbstractBoard):
    class Meta:
        db_table = u'board_club_withweve'
class CommentClubWithweve(AbstractComment):
    class Meta:
        db_table = u'comment_club_withweve'

# auto generated for board board_club_zp
class BoardClubZp(AbstractBoard):
    class Meta:
        db_table = u'board_club_zp'
class CommentClubZp(AbstractComment):
    class Meta:
        db_table = u'comment_club_zp'

# auto generated for board board_counsel
class BoardCounsel(AbstractBoard):
    class Meta:
        db_table = u'board_counsel'
class CommentCounsel(AbstractComment):
    class Meta:
        db_table = u'comment_counsel'

# auto generated for board board_csebiz
class BoardCsebiz(AbstractBoard):
    class Meta:
        db_table = u'board_csebiz'
class CommentCsebiz(AbstractComment):
    class Meta:
        db_table = u'comment_csebiz'

# auto generated for board board_csebiz_lecture
class BoardCsebizLecture(AbstractBoard):
    class Meta:
        db_table = u'board_csebiz_lecture'
class CommentCsebizLecture(AbstractComment):
    class Meta:
        db_table = u'comment_csebiz_lecture'

# auto generated for board board_csesa
class BoardCsesa(AbstractBoard):
    class Meta:
        db_table = u'board_csesa'
class CommentCsesa(AbstractComment):
    class Meta:
        db_table = u'comment_csesa'

# auto generated for board board_csesac
class BoardCsesac(AbstractBoard):
    class Meta:
        db_table = u'board_csesac'
class CommentCsesac(AbstractComment):
    class Meta:
        db_table = u'comment_csesac'

# auto generated for board board_csesa_sub1
class BoardCsesaSub1(AbstractBoard):
    class Meta:
        db_table = u'board_csesa_sub1'
class CommentCsesaSub1(AbstractComment):
    class Meta:
        db_table = u'comment_csesa_sub1'

# auto generated for board board_csesa_sub2
class BoardCsesaSub2(AbstractBoard):
    class Meta:
        db_table = u'board_csesa_sub2'
class CommentCsesaSub2(AbstractComment):
    class Meta:
        db_table = u'comment_csesa_sub2'

# auto generated for board board_dcgallers
class BoardDcgallers(AbstractBoard):
    class Meta:
        db_table = u'board_dcgallers'
class CommentDcgallers(AbstractComment):
    class Meta:
        db_table = u'comment_dcgallers'

# auto generated for board board_discuss
class BoardDiscuss(AbstractBoard):
    class Meta:
        db_table = u'board_discuss'
class CommentDiscuss(AbstractComment):
    class Meta:
        db_table = u'comment_discuss'

# auto generated for board board_doc
class BoardDoc(AbstractBoard):
    class Meta:
        db_table = u'board_doc'
class CommentDoc(AbstractComment):
    class Meta:
        db_table = u'comment_doc'

# auto generated for board board_dogsix
class BoardDogsix(AbstractBoard):
    class Meta:
        db_table = u'board_dogsix'
class CommentDogsix(AbstractComment):
    class Meta:
        db_table = u'comment_dogsix'

# auto generated for board board_dongneteam
class BoardDongneteam(AbstractBoard):
    class Meta:
        db_table = u'board_dongneteam'
class CommentDongneteam(AbstractComment):
    class Meta:
        db_table = u'comment_dongneteam'

# auto generated for board board_dongneteamtest
class BoardDongneteamtest(AbstractBoard):
    class Meta:
        db_table = u'board_dongneteamtest'
class CommentDongneteamtest(AbstractComment):
    class Meta:
        db_table = u'comment_dongneteamtest'

# auto generated for board board_dongne_hidden
class BoardDongneHidden(AbstractBoard):
    class Meta:
        db_table = u'board_dongne_hidden'
class CommentDongneHidden(AbstractComment):
    class Meta:
        db_table = u'comment_dongne_hidden'

# auto generated for board board_dumb
class BoardDumb(AbstractBoard):
    class Meta:
        db_table = u'board_dumb'
class CommentDumb(AbstractComment):
    class Meta:
        db_table = u'comment_dumb'

# auto generated for board board_enter
class BoardEnter(AbstractBoard):
    class Meta:
        db_table = u'board_enter'
class CommentEnter(AbstractComment):
    class Meta:
        db_table = u'comment_enter'

# auto generated for board board_etc
class BoardEtc(AbstractBoard):
    class Meta:
        db_table = u'board_etc'
class CommentEtc(AbstractComment):
    class Meta:
        db_table = u'comment_etc'

# auto generated for board board_event
class BoardEvent(AbstractBoard):
    class Meta:
        db_table = u'board_event'
class CommentEvent(AbstractComment):
    class Meta:
        db_table = u'comment_event'

# auto generated for board board_extreamsport
class BoardExtreamsport(AbstractBoard):
    class Meta:
        db_table = u'board_extreamsport'
class CommentExtreamsport(AbstractComment):
    class Meta:
        db_table = u'comment_extreamsport'

# auto generated for board board_facse
class BoardFacse(AbstractBoard):
    class Meta:
        db_table = u'board_facse'
class CommentFacse(AbstractComment):
    class Meta:
        db_table = u'comment_facse'

# auto generated for board board_facse2
class BoardFacse2(AbstractBoard):
    class Meta:
        db_table = u'board_facse2'
class CommentFacse2(AbstractComment):
    class Meta:
        db_table = u'comment_facse2'

# auto generated for board board_fishgrow
class BoardFishgrow(AbstractBoard):
    class Meta:
        db_table = u'board_fishgrow'
class CommentFishgrow(AbstractComment):
    class Meta:
        db_table = u'comment_fishgrow'

# auto generated for board board_freeboard
class BoardFreeboard(AbstractBoard):
    class Meta:
        db_table = u'board_freeboard'
class CommentFreeboard(AbstractComment):
    class Meta:
        db_table = u'comment_freeboard'

# auto generated for board board_gamemoney
class BoardGamemoney(AbstractBoard):
    class Meta:
        db_table = u'board_gamemoney'
class CommentGamemoney(AbstractComment):
    class Meta:
        db_table = u'comment_gamemoney'

# auto generated for board board_gujja
class BoardGujja(AbstractBoard):
    class Meta:
        db_table = u'board_gujja'
class CommentGujja(AbstractComment):
    class Meta:
        db_table = u'comment_gujja'

# auto generated for board board_help
class BoardHelp(AbstractBoard):
    class Meta:
        db_table = u'board_help'
class CommentHelp(AbstractComment):
    class Meta:
        db_table = u'comment_help'

# auto generated for board board_hex
class BoardHex(AbstractBoard):
    class Meta:
        db_table = u'board_hex'
class CommentHex(AbstractComment):
    class Meta:
        db_table = u'comment_hex'

# auto generated for board board_hex_sub1
class BoardHexSub1(AbstractBoard):
    class Meta:
        db_table = u'board_hex_sub1'
class CommentHexSub1(AbstractComment):
    class Meta:
        db_table = u'comment_hex_sub1'

# auto generated for board board_itnews
class BoardItnews(AbstractBoard):
    class Meta:
        db_table = u'board_itnews'
class CommentItnews(AbstractComment):
    class Meta:
        db_table = u'comment_itnews'

# auto generated for board board_jhonson
class BoardJhonson(AbstractBoard):
    class Meta:
        db_table = u'board_jhonson'
class CommentJhonson(AbstractComment):
    class Meta:
        db_table = u'comment_jhonson'

# auto generated for board board_lecture
class BoardLecture(AbstractBoard):
    class Meta:
        db_table = u'board_lecture'
class CommentLecture(AbstractComment):
    class Meta:
        db_table = u'comment_lecture'

# auto generated for board board_lost
class BoardLost(AbstractBoard):
    class Meta:
        db_table = u'board_lost'
class CommentLost(AbstractComment):
    class Meta:
        db_table = u'comment_lost'

# auto generated for board board_marlboro
class BoardMarlboro(AbstractBoard):
    class Meta:
        db_table = u'board_marlboro'
class CommentMarlboro(AbstractComment):
    class Meta:
        db_table = u'comment_marlboro'

# auto generated for board board_marlboro2
class BoardMarlboro2(AbstractBoard):
    class Meta:
        db_table = u'board_marlboro2'
class CommentMarlboro2(AbstractComment):
    class Meta:
        db_table = u'comment_marlboro2'

# auto generated for board board_mem_research
class BoardMemResearch(AbstractBoard):
    class Meta:
        db_table = u'board_mem_research'
class CommentMemResearch(AbstractComment):
    class Meta:
        db_table = u'comment_mem_research'

# auto generated for board board_menssmells
class BoardMenssmells(AbstractBoard):
    class Meta:
        db_table = u'board_menssmells'
class CommentMenssmells(AbstractComment):
    class Meta:
        db_table = u'comment_menssmells'

# auto generated for board board_nba
class BoardNba(AbstractBoard):
    class Meta:
        db_table = u'board_nba'
class CommentNba(AbstractComment):
    class Meta:
        db_table = u'comment_nba'

# auto generated for board board_notice
class BoardNotice(AbstractBoard):
    class Meta:
        db_table = u'board_notice'
class CommentNotice(AbstractComment):
    class Meta:
        db_table = u'comment_notice'

# auto generated for board board_paper_neo
class BoardPaperNeo(AbstractBoard):
    class Meta:
        db_table = u'board_paper_neo'
class CommentPaperNeo(AbstractComment):
    class Meta:
        db_table = u'comment_paper_neo'

# auto generated for board board_paper_pop
class BoardPaperPop(AbstractBoard):
    class Meta:
        db_table = u'board_paper_pop'
class CommentPaperPop(AbstractComment):
    class Meta:
        db_table = u'comment_paper_pop'

# auto generated for board board_parkcue
class BoardParkcue(AbstractBoard):
    class Meta:
        db_table = u'board_parkcue'
class CommentParkcue(AbstractComment):
    class Meta:
        db_table = u'comment_parkcue'

# auto generated for board board_parkcue_sub1
class BoardParkcueSub1(AbstractBoard):
    class Meta:
        db_table = u'board_parkcue_sub1'
class CommentParkcueSub1(AbstractComment):
    class Meta:
        db_table = u'comment_parkcue_sub1'

# auto generated for board board_part_ad
class BoardPartAd(AbstractBoard):
    class Meta:
        db_table = u'board_part_ad'
class CommentPartAd(AbstractComment):
    class Meta:
        db_table = u'comment_part_ad'

# auto generated for board board_part_culture
class BoardPartCulture(AbstractBoard):
    class Meta:
        db_table = u'board_part_culture'
class CommentPartCulture(AbstractComment):
    class Meta:
        db_table = u'comment_part_culture'

# auto generated for board board_part_everyday
class BoardPartEveryday(AbstractBoard):
    class Meta:
        db_table = u'board_part_everyday'
class CommentPartEveryday(AbstractComment):
    class Meta:
        db_table = u'comment_part_everyday'

# auto generated for board board_part_jungtong
class BoardPartJungtong(AbstractBoard):
    class Meta:
        db_table = u'board_part_jungtong'
class CommentPartJungtong(AbstractComment):
    class Meta:
        db_table = u'comment_part_jungtong'

# auto generated for board board_part_neo
class BoardPartNeo(AbstractBoard):
    class Meta:
        db_table = u'board_part_neo'
class CommentPartNeo(AbstractComment):
    class Meta:
        db_table = u'comment_part_neo'

# auto generated for board board_part_plan
class BoardPartPlan(AbstractBoard):
    class Meta:
        db_table = u'board_part_plan'
class CommentPartPlan(AbstractComment):
    class Meta:
        db_table = u'comment_part_plan'

# auto generated for board board_part_plan_records
class BoardPartPlanRecords(AbstractBoard):
    class Meta:
        db_table = u'board_part_plan_records'
class CommentPartPlanRecords(AbstractComment):
    class Meta:
        db_table = u'comment_part_plan_records'

# auto generated for board board_part_social
class BoardPartSocial(AbstractBoard):
    class Meta:
        db_table = u'board_part_social'
class CommentPartSocial(AbstractComment):
    class Meta:
        db_table = u'comment_part_social'

# auto generated for board board_pcmanage
class BoardPcmanage(AbstractBoard):
    class Meta:
        db_table = u'board_pcmanage'
class CommentPcmanage(AbstractComment):
    class Meta:
        db_table = u'comment_pcmanage'

# auto generated for board board_photo
class BoardPhoto(AbstractBoard):
    class Meta:
        db_table = u'board_photo'
class CommentPhoto(AbstractComment):
    class Meta:
        db_table = u'comment_photo'

# auto generated for board board_photo2
class BoardPhoto2(AbstractBoard):
    class Meta:
        db_table = u'board_photo2'
class CommentPhoto2(AbstractComment):
    class Meta:
        db_table = u'comment_photo2'

# auto generated for board board_poll
class BoardPoll(AbstractBoard):
    class Meta:
        db_table = u'board_poll'
class CommentPoll(AbstractComment):
    class Meta:
        db_table = u'comment_poll'

# auto generated for board board_pray
class BoardPray(AbstractBoard):
    class Meta:
        db_table = u'board_pray'
class CommentPray(AbstractComment):
    class Meta:
        db_table = u'comment_pray'

# auto generated for board board_qna
class BoardQna(AbstractBoard):
    class Meta:
        db_table = u'board_qna'
class CommentQna(AbstractComment):
    class Meta:
        db_table = u'comment_qna'

# auto generated for board board_recruit
class BoardRecruit(AbstractBoard):
    class Meta:
        db_table = u'board_recruit'
class CommentRecruit(AbstractComment):
    class Meta:
        db_table = u'comment_recruit'

# auto generated for board board_reload
class BoardReload(AbstractBoard):
    class Meta:
        db_table = u'board_reload'
class CommentReload(AbstractComment):
    class Meta:
        db_table = u'comment_reload'

# auto generated for board board_revolution
class BoardRevolution(AbstractBoard):
    class Meta:
        db_table = u'board_revolution'
class CommentRevolution(AbstractComment):
    class Meta:
        db_table = u'comment_revolution'

# auto generated for board board_sketch
class BoardSketch(AbstractBoard):
    class Meta:
        db_table = u'board_sketch'
class CommentSketch(AbstractComment):
    class Meta:
        db_table = u'comment_sketch'

# auto generated for board board_syf
class BoardSyf(AbstractBoard):
    class Meta:
        db_table = u'board_syf'
class CommentSyf(AbstractComment):
    class Meta:
        db_table = u'comment_syf'

# auto generated for board board_temp
class BoardTemp(AbstractBoard):
    class Meta:
        db_table = u'board_temp'
class CommentTemp(AbstractComment):
    class Meta:
        db_table = u'comment_temp'

# auto generated for board board_test
class BoardTest(AbstractBoard):
    class Meta:
        db_table = u'board_test'
class CommentTest(AbstractComment):
    class Meta:
        db_table = u'comment_test'

# auto generated for board board_test1
class BoardTest1(AbstractBoard):
    class Meta:
        db_table = u'board_test1'
class CommentTest1(AbstractComment):
    class Meta:
        db_table = u'comment_test1'

# auto generated for board board_test_paper
class BoardTestPaper(AbstractBoard):
    class Meta:
        db_table = u'board_test_paper'
class CommentTestPaper(AbstractComment):
    class Meta:
        db_table = u'comment_test_paper'

# auto generated for board board_toeic850
class BoardToeic850(AbstractBoard):
    class Meta:
        db_table = u'board_toeic850'
class CommentToeic850(AbstractComment):
    class Meta:
        db_table = u'comment_toeic850'

# auto generated for board board_toto
class BoardToto(AbstractBoard):
    class Meta:
        db_table = u'board_toto'
class CommentToto(AbstractComment):
    class Meta:
        db_table = u'comment_toto'

# auto generated for board board_trash_novel
class BoardTrashNovel(AbstractBoard):
    class Meta:
        db_table = u'board_trash_novel'
class CommentTrashNovel(AbstractComment):
    class Meta:
        db_table = u'comment_trash_novel'

# auto generated for board board_twistedlife
class BoardTwistedlife(AbstractBoard):
    class Meta:
        db_table = u'board_twistedlife'
class CommentTwistedlife(AbstractComment):
    class Meta:
        db_table = u'comment_twistedlife'

# auto generated for board board_veryrealtrue
class BoardVeryrealtrue(AbstractBoard):
    class Meta:
        db_table = u'board_veryrealtrue'
class CommentVeryrealtrue(AbstractComment):
    class Meta:
        db_table = u'comment_veryrealtrue'

# auto generated for board board_volunteers
class BoardVolunteers(AbstractBoard):
    class Meta:
        db_table = u'board_volunteers'
class CommentVolunteers(AbstractComment):
    class Meta:
        db_table = u'comment_volunteers'

# auto generated for board board_webzine_theme
class BoardWebzineTheme(AbstractBoard):
    class Meta:
        db_table = u'board_webzine_theme'
class CommentWebzineTheme(AbstractComment):
    class Meta:
        db_table = u'comment_webzine_theme'

# auto generated for board board_withweve_data
class BoardWithweveData(AbstractBoard):
    class Meta:
        db_table = u'board_withweve_data'
class CommentWithweveData(AbstractComment):
    class Meta:
        db_table = u'comment_withweve_data'

# auto generated for board board_withweve_free
class BoardWithweveFree(AbstractBoard):
    class Meta:
        db_table = u'board_withweve_free'
class CommentWithweveFree(AbstractComment):
    class Meta:
        db_table = u'comment_withweve_free'

# auto generated for board photo_allaplus
class PhotoAllaplus(AbstractBoard):
    class Meta:
        db_table = u'photo_allaplus'
class MemoAllaplus(AbstractMemo):
    class Meta:
        db_table = u'memo_allaplus'

# auto generated for board photo_alumni00
class PhotoAlumni00(AbstractBoard):
    class Meta:
        db_table = u'photo_alumni00'
class MemoAlumni00(AbstractMemo):
    class Meta:
        db_table = u'memo_alumni00'

# auto generated for board photo_alumni01
class PhotoAlumni01(AbstractBoard):
    class Meta:
        db_table = u'photo_alumni01'
class MemoAlumni01(AbstractMemo):
    class Meta:
        db_table = u'memo_alumni01'

# auto generated for board photo_alumni02
class PhotoAlumni02(AbstractBoard):
    class Meta:
        db_table = u'photo_alumni02'
class MemoAlumni02(AbstractMemo):
    class Meta:
        db_table = u'memo_alumni02'

# auto generated for board photo_alumni03
class PhotoAlumni03(AbstractBoard):
    class Meta:
        db_table = u'photo_alumni03'
class MemoAlumni03(AbstractMemo):
    class Meta:
        db_table = u'memo_alumni03'

# auto generated for board photo_alumni04
class PhotoAlumni04(AbstractBoard):
    class Meta:
        db_table = u'photo_alumni04'
class MemoAlumni04(AbstractMemo):
    class Meta:
        db_table = u'memo_alumni04'

# auto generated for board photo_alumni05
class PhotoAlumni05(AbstractBoard):
    class Meta:
        db_table = u'photo_alumni05'
class MemoAlumni05(AbstractMemo):
    class Meta:
        db_table = u'memo_alumni05'

# auto generated for board photo_alumni06
class PhotoAlumni06(AbstractBoard):
    class Meta:
        db_table = u'photo_alumni06'
class MemoAlumni06(AbstractMemo):
    class Meta:
        db_table = u'memo_alumni06'

# auto generated for board photo_alumni07
class PhotoAlumni07(AbstractBoard):
    class Meta:
        db_table = u'photo_alumni07'
class MemoAlumni07(AbstractMemo):
    class Meta:
        db_table = u'memo_alumni07'

# auto generated for board photo_alumni08
class PhotoAlumni08(AbstractBoard):
    class Meta:
        db_table = u'photo_alumni08'
class MemoAlumni08(AbstractMemo):
    class Meta:
        db_table = u'memo_alumni08'

# auto generated for board photo_alumni09
class PhotoAlumni09(AbstractBoard):
    class Meta:
        db_table = u'photo_alumni09'
class MemoAlumni09(AbstractMemo):
    class Meta:
        db_table = u'memo_alumni09'

# auto generated for board photo_alumni10
class PhotoAlumni10(AbstractBoard):
    class Meta:
        db_table = u'photo_alumni10'
class MemoAlumni10(AbstractMemo):
    class Meta:
        db_table = u'memo_alumni10'

# auto generated for board photo_alumni72
class PhotoAlumni72(AbstractBoard):
    class Meta:
        db_table = u'photo_alumni72'
class MemoAlumni72(AbstractMemo):
    class Meta:
        db_table = u'memo_alumni72'

# auto generated for board photo_alumni73
class PhotoAlumni73(AbstractBoard):
    class Meta:
        db_table = u'photo_alumni73'
class MemoAlumni73(AbstractMemo):
    class Meta:
        db_table = u'memo_alumni73'

# auto generated for board photo_alumni74
class PhotoAlumni74(AbstractBoard):
    class Meta:
        db_table = u'photo_alumni74'
class MemoAlumni74(AbstractMemo):
    class Meta:
        db_table = u'memo_alumni74'

# auto generated for board photo_alumni75
class PhotoAlumni75(AbstractBoard):
    class Meta:
        db_table = u'photo_alumni75'
class MemoAlumni75(AbstractMemo):
    class Meta:
        db_table = u'memo_alumni75'

# auto generated for board photo_alumni76
class PhotoAlumni76(AbstractBoard):
    class Meta:
        db_table = u'photo_alumni76'
class MemoAlumni76(AbstractMemo):
    class Meta:
        db_table = u'memo_alumni76'

# auto generated for board photo_alumni77
class PhotoAlumni77(AbstractBoard):
    class Meta:
        db_table = u'photo_alumni77'
class MemoAlumni77(AbstractMemo):
    class Meta:
        db_table = u'memo_alumni77'

# auto generated for board photo_alumni78
class PhotoAlumni78(AbstractBoard):
    class Meta:
        db_table = u'photo_alumni78'
class MemoAlumni78(AbstractMemo):
    class Meta:
        db_table = u'memo_alumni78'

# auto generated for board photo_alumni79
class PhotoAlumni79(AbstractBoard):
    class Meta:
        db_table = u'photo_alumni79'
class MemoAlumni79(AbstractMemo):
    class Meta:
        db_table = u'memo_alumni79'

# auto generated for board photo_alumni80
class PhotoAlumni80(AbstractBoard):
    class Meta:
        db_table = u'photo_alumni80'
class MemoAlumni80(AbstractMemo):
    class Meta:
        db_table = u'memo_alumni80'

# auto generated for board photo_alumni81
class PhotoAlumni81(AbstractBoard):
    class Meta:
        db_table = u'photo_alumni81'
class MemoAlumni81(AbstractMemo):
    class Meta:
        db_table = u'memo_alumni81'

# auto generated for board photo_alumni82
class PhotoAlumni82(AbstractBoard):
    class Meta:
        db_table = u'photo_alumni82'
class MemoAlumni82(AbstractMemo):
    class Meta:
        db_table = u'memo_alumni82'

# auto generated for board photo_alumni83
class PhotoAlumni83(AbstractBoard):
    class Meta:
        db_table = u'photo_alumni83'
class MemoAlumni83(AbstractMemo):
    class Meta:
        db_table = u'memo_alumni83'

# auto generated for board photo_alumni84
class PhotoAlumni84(AbstractBoard):
    class Meta:
        db_table = u'photo_alumni84'
class MemoAlumni84(AbstractMemo):
    class Meta:
        db_table = u'memo_alumni84'

# auto generated for board photo_alumni85
class PhotoAlumni85(AbstractBoard):
    class Meta:
        db_table = u'photo_alumni85'
class MemoAlumni85(AbstractMemo):
    class Meta:
        db_table = u'memo_alumni85'

# auto generated for board photo_alumni86
class PhotoAlumni86(AbstractBoard):
    class Meta:
        db_table = u'photo_alumni86'
class MemoAlumni86(AbstractMemo):
    class Meta:
        db_table = u'memo_alumni86'

# auto generated for board photo_alumni87
class PhotoAlumni87(AbstractBoard):
    class Meta:
        db_table = u'photo_alumni87'
class MemoAlumni87(AbstractMemo):
    class Meta:
        db_table = u'memo_alumni87'

# auto generated for board photo_alumni88
class PhotoAlumni88(AbstractBoard):
    class Meta:
        db_table = u'photo_alumni88'
class MemoAlumni88(AbstractMemo):
    class Meta:
        db_table = u'memo_alumni88'

# auto generated for board photo_alumni89
class PhotoAlumni89(AbstractBoard):
    class Meta:
        db_table = u'photo_alumni89'
class MemoAlumni89(AbstractMemo):
    class Meta:
        db_table = u'memo_alumni89'

# auto generated for board photo_alumni90
class PhotoAlumni90(AbstractBoard):
    class Meta:
        db_table = u'photo_alumni90'
class MemoAlumni90(AbstractMemo):
    class Meta:
        db_table = u'memo_alumni90'

# auto generated for board photo_alumni91
class PhotoAlumni91(AbstractBoard):
    class Meta:
        db_table = u'photo_alumni91'
class MemoAlumni91(AbstractMemo):
    class Meta:
        db_table = u'memo_alumni91'

# auto generated for board photo_alumni92
class PhotoAlumni92(AbstractBoard):
    class Meta:
        db_table = u'photo_alumni92'
class MemoAlumni92(AbstractMemo):
    class Meta:
        db_table = u'memo_alumni92'

# auto generated for board photo_alumni93
class PhotoAlumni93(AbstractBoard):
    class Meta:
        db_table = u'photo_alumni93'
class MemoAlumni93(AbstractMemo):
    class Meta:
        db_table = u'memo_alumni93'

# auto generated for board photo_alumni94
class PhotoAlumni94(AbstractBoard):
    class Meta:
        db_table = u'photo_alumni94'
class MemoAlumni94(AbstractMemo):
    class Meta:
        db_table = u'memo_alumni94'

# auto generated for board photo_alumni95
class PhotoAlumni95(AbstractBoard):
    class Meta:
        db_table = u'photo_alumni95'
class MemoAlumni95(AbstractMemo):
    class Meta:
        db_table = u'memo_alumni95'

# auto generated for board photo_alumni96
class PhotoAlumni96(AbstractBoard):
    class Meta:
        db_table = u'photo_alumni96'
class MemoAlumni96(AbstractMemo):
    class Meta:
        db_table = u'memo_alumni96'

# auto generated for board photo_alumni97
class PhotoAlumni97(AbstractBoard):
    class Meta:
        db_table = u'photo_alumni97'
class MemoAlumni97(AbstractMemo):
    class Meta:
        db_table = u'memo_alumni97'

# auto generated for board photo_alumni98
class PhotoAlumni98(AbstractBoard):
    class Meta:
        db_table = u'photo_alumni98'
class MemoAlumni98(AbstractMemo):
    class Meta:
        db_table = u'memo_alumni98'

# auto generated for board photo_alumni99
class PhotoAlumni99(AbstractBoard):
    class Meta:
        db_table = u'photo_alumni99'
class MemoAlumni99(AbstractMemo):
    class Meta:
        db_table = u'memo_alumni99'

# auto generated for board photo_cafe_appellation
class PhotoCafeAppellation(AbstractBoard):
    class Meta:
        db_table = u'photo_cafe_appellation'
class MemoCafeAppellation(AbstractMemo):
    class Meta:
        db_table = u'memo_cafe_appellation'

# auto generated for board photo_cafe_churi
class PhotoCafeChuri(AbstractBoard):
    class Meta:
        db_table = u'photo_cafe_churi'
class MemoCafeChuri(AbstractMemo):
    class Meta:
        db_table = u'memo_cafe_churi'

# auto generated for board photo_cafe_cuti
class PhotoCafeCuti(AbstractBoard):
    class Meta:
        db_table = u'photo_cafe_cuti'
class MemoCafeCuti(AbstractMemo):
    class Meta:
        db_table = u'memo_cafe_cuti'

# auto generated for board photo_cafe_forum
class PhotoCafeForum(AbstractBoard):
    class Meta:
        db_table = u'photo_cafe_forum'
class MemoCafeForum(AbstractMemo):
    class Meta:
        db_table = u'memo_cafe_forum'

# auto generated for board photo_cafe_girl_student
class PhotoCafeGirlStudent(AbstractBoard):
    class Meta:
        db_table = u'photo_cafe_girl_student'
class MemoCafeGirlStudent(AbstractMemo):
    class Meta:
        db_table = u'memo_cafe_girl_student'

# auto generated for board photo_cafe_gutter
class PhotoCafeGutter(AbstractBoard):
    class Meta:
        db_table = u'photo_cafe_gutter'
class MemoCafeGutter(AbstractMemo):
    class Meta:
        db_table = u'memo_cafe_gutter'

# auto generated for board photo_cafe_handtruth
class PhotoCafeHandtruth(AbstractBoard):
    class Meta:
        db_table = u'photo_cafe_handtruth'
class MemoCafeHandtruth(AbstractMemo):
    class Meta:
        db_table = u'memo_cafe_handtruth'

# auto generated for board photo_cafe_heukseoker
class PhotoCafeHeukseoker(AbstractBoard):
    class Meta:
        db_table = u'photo_cafe_heukseoker'
class MemoCafeHeukseoker(AbstractMemo):
    class Meta:
        db_table = u'memo_cafe_heukseoker'

# auto generated for board photo_cafe_homesteal
class PhotoCafeHomesteal(AbstractBoard):
    class Meta:
        db_table = u'photo_cafe_homesteal'
class MemoCafeHomesteal(AbstractMemo):
    class Meta:
        db_table = u'memo_cafe_homesteal'

# auto generated for board photo_cafe_iris
class PhotoCafeIris(AbstractBoard):
    class Meta:
        db_table = u'photo_cafe_iris'
class MemoCafeIris(AbstractMemo):
    class Meta:
        db_table = u'memo_cafe_iris'

# auto generated for board photo_cafe_it_security
class PhotoCafeItSecurity(AbstractBoard):
    class Meta:
        db_table = u'photo_cafe_it_security'
class MemoCafeItSecurity(AbstractMemo):
    class Meta:
        db_table = u'memo_cafe_it_security'

# auto generated for board photo_cafe_jokbal
class PhotoCafeJokbal(AbstractBoard):
    class Meta:
        db_table = u'photo_cafe_jokbal'
class MemoCafeJokbal(AbstractMemo):
    class Meta:
        db_table = u'memo_cafe_jokbal'

# auto generated for board photo_cafe_jstorm
class PhotoCafeJstorm(AbstractBoard):
    class Meta:
        db_table = u'photo_cafe_jstorm'
class MemoCafeJstorm(AbstractMemo):
    class Meta:
        db_table = u'memo_cafe_jstorm'

# auto generated for board photo_cafe_mountain_love
class PhotoCafeMountainLove(AbstractBoard):
    class Meta:
        db_table = u'photo_cafe_mountain_love'
class MemoCafeMountainLove(AbstractMemo):
    class Meta:
        db_table = u'memo_cafe_mountain_love'

# auto generated for board photo_cafe_note
class PhotoCafeNote(AbstractBoard):
    class Meta:
        db_table = u'photo_cafe_note'
class MemoCafeNote(AbstractMemo):
    class Meta:
        db_table = u'memo_cafe_note'

# auto generated for board photo_cafe_present
class PhotoCafePresent(AbstractBoard):
    class Meta:
        db_table = u'photo_cafe_present'
class MemoCafePresent(AbstractMemo):
    class Meta:
        db_table = u'memo_cafe_present'

# auto generated for board photo_cafe_securelab
class PhotoCafeSecurelab(AbstractBoard):
    class Meta:
        db_table = u'photo_cafe_securelab'
class MemoCafeSecurelab(AbstractMemo):
    class Meta:
        db_table = u'memo_cafe_securelab'

# auto generated for board photo_cafe_snsd
class PhotoCafeSnsd(AbstractBoard):
    class Meta:
        db_table = u'photo_cafe_snsd'
class MemoCafeSnsd(AbstractMemo):
    class Meta:
        db_table = u'memo_cafe_snsd'

# auto generated for board photo_cafe_steamers
class PhotoCafeSteamers(AbstractBoard):
    class Meta:
        db_table = u'photo_cafe_steamers'
class MemoCafeSteamers(AbstractMemo):
    class Meta:
        db_table = u'memo_cafe_steamers'

# auto generated for board photo_cafe_tspin
class PhotoCafeTspin(AbstractBoard):
    class Meta:
        db_table = u'photo_cafe_tspin'
class MemoCafeTspin(AbstractMemo):
    class Meta:
        db_table = u'memo_cafe_tspin'

# auto generated for board photo_cafe_wow
class PhotoCafeWow(AbstractBoard):
    class Meta:
        db_table = u'photo_cafe_wow'
class MemoCafeWow(AbstractMemo):
    class Meta:
        db_table = u'memo_cafe_wow'

# auto generated for board photo_cgraph
class PhotoCgraph(AbstractBoard):
    class Meta:
        db_table = u'photo_cgraph'
class MemoCgraph(AbstractMemo):
    class Meta:
        db_table = u'memo_cgraph'

# auto generated for board photo_club_abroad
class PhotoClubAbroad(AbstractBoard):
    class Meta:
        db_table = u'photo_club_abroad'
class MemoClubAbroad(AbstractMemo):
    class Meta:
        db_table = u'memo_club_abroad'

# auto generated for board photo_club_brenntano
class PhotoClubBrenntano(AbstractBoard):
    class Meta:
        db_table = u'photo_club_brenntano'
class MemoClubBrenntano(AbstractMemo):
    class Meta:
        db_table = u'memo_club_brenntano'

# auto generated for board photo_club_curseware
class PhotoClubCurseware(AbstractBoard):
    class Meta:
        db_table = u'photo_club_curseware'
class MemoClubCurseware(AbstractMemo):
    class Meta:
        db_table = u'memo_club_curseware'

# auto generated for board photo_club_dumb
class PhotoClubDumb(AbstractBoard):
    class Meta:
        db_table = u'photo_club_dumb'
class MemoClubDumb(AbstractMemo):
    class Meta:
        db_table = u'memo_club_dumb'

# auto generated for board photo_club_ecs
class PhotoClubEcs(AbstractBoard):
    class Meta:
        db_table = u'photo_club_ecs'
class MemoClubEcs(AbstractMemo):
    class Meta:
        db_table = u'memo_club_ecs'

# auto generated for board photo_club_footlove
class PhotoClubFootlove(AbstractBoard):
    class Meta:
        db_table = u'photo_club_footlove'
class MemoClubFootlove(AbstractMemo):
    class Meta:
        db_table = u'memo_club_footlove'

# auto generated for board photo_club_fr
class PhotoClubFr(AbstractBoard):
    class Meta:
        db_table = u'photo_club_fr'
class MemoClubFr(AbstractMemo):
    class Meta:
        db_table = u'memo_club_fr'

# auto generated for board photo_club_mios
class PhotoClubMios(AbstractBoard):
    class Meta:
        db_table = u'photo_club_mios'
class MemoClubMios(AbstractMemo):
    class Meta:
        db_table = u'memo_club_mios'

# auto generated for board photo_club_withweve
class PhotoClubWithweve(AbstractBoard):
    class Meta:
        db_table = u'photo_club_withweve'
class MemoClubWithweve(AbstractMemo):
    class Meta:
        db_table = u'memo_club_withweve'

# auto generated for board photo_csebiz
class PhotoCsebiz(AbstractBoard):
    class Meta:
        db_table = u'photo_csebiz'
class MemoCsebiz(AbstractMemo):
    class Meta:
        db_table = u'memo_csebiz'

# auto generated for board photo_csesa
class PhotoCsesa(AbstractBoard):
    class Meta:
        db_table = u'photo_csesa'
class MemoCsesa(AbstractMemo):
    class Meta:
        db_table = u'memo_csesa'

# auto generated for board photo_csesac
class PhotoCsesac(AbstractBoard):
    class Meta:
        db_table = u'photo_csesac'
class MemoCsesac(AbstractMemo):
    class Meta:
        db_table = u'memo_csesac'

# auto generated for board photo_dcgallers
class PhotoDcgallers(AbstractBoard):
    class Meta:
        db_table = u'photo_dcgallers'
class MemoDcgallers(AbstractMemo):
    class Meta:
        db_table = u'memo_dcgallers'

# auto generated for board photo_dogsix
class PhotoDogsix(AbstractBoard):
    class Meta:
        db_table = u'photo_dogsix'
class MemoDogsix(AbstractMemo):
    class Meta:
        db_table = u'memo_dogsix'

# auto generated for board photo_dongneteam
class PhotoDongneteam(AbstractBoard):
    class Meta:
        db_table = u'photo_dongneteam'
class MemoDongneteam(AbstractMemo):
    class Meta:
        db_table = u'memo_dongneteam'

# auto generated for board photo_etc
class PhotoEtc(AbstractBoard):
    class Meta:
        db_table = u'photo_etc'
class MemoEtc(AbstractMemo):
    class Meta:
        db_table = u'memo_etc'

# auto generated for board photo_extreamsport
class PhotoExtreamsport(AbstractBoard):
    class Meta:
        db_table = u'photo_extreamsport'
class MemoExtreamsport(AbstractMemo):
    class Meta:
        db_table = u'memo_extreamsport'

# auto generated for board photo_facse
class PhotoFacse(AbstractBoard):
    class Meta:
        db_table = u'photo_facse'
class MemoFacse(AbstractMemo):
    class Meta:
        db_table = u'memo_facse'

# auto generated for board photo_fishgrow
class PhotoFishgrow(AbstractBoard):
    class Meta:
        db_table = u'photo_fishgrow'
class MemoFishgrow(AbstractMemo):
    class Meta:
        db_table = u'memo_fishgrow'

# auto generated for board photo_gamemoney
class PhotoGamemoney(AbstractBoard):
    class Meta:
        db_table = u'photo_gamemoney'
class MemoGamemoney(AbstractMemo):
    class Meta:
        db_table = u'memo_gamemoney'

# auto generated for board photo_graduation
class PhotoGraduation(AbstractBoard):
    class Meta:
        db_table = u'photo_graduation'
class MemoGraduation(AbstractMemo):
    class Meta:
        db_table = u'memo_graduation'

# auto generated for board photo_gujja
class PhotoGujja(AbstractBoard):
    class Meta:
        db_table = u'photo_gujja'
class MemoGujja(AbstractMemo):
    class Meta:
        db_table = u'memo_gujja'

# auto generated for board photo_hex
class PhotoHex(AbstractBoard):
    class Meta:
        db_table = u'photo_hex'
class MemoHex(AbstractMemo):
    class Meta:
        db_table = u'memo_hex'

# auto generated for board photo_info_02
class PhotoInfo02(AbstractBoard):
    class Meta:
        db_table = u'photo_info_02'
class MemoInfo02(AbstractMemo):
    class Meta:
        db_table = u'memo_info_02'

# auto generated for board photo_info_memory
class PhotoInfoMemory(AbstractBoard):
    class Meta:
        db_table = u'photo_info_memory'
class MemoInfoMemory(AbstractMemo):
    class Meta:
        db_table = u'memo_info_memory'

# auto generated for board photo_info_misc
class PhotoInfoMisc(AbstractBoard):
    class Meta:
        db_table = u'photo_info_misc'
class MemoInfoMisc(AbstractMemo):
    class Meta:
        db_table = u'memo_info_misc'

# auto generated for board photo_jhonson
class PhotoJhonson(AbstractBoard):
    class Meta:
        db_table = u'photo_jhonson'
class MemoJhonson(AbstractMemo):
    class Meta:
        db_table = u'memo_jhonson'

# auto generated for board photo_kc_photo_dc
class PhotoKcPhotoDc(AbstractBoard):
    class Meta:
        db_table = u'photo_kc_photo_dc'
class MemoKcPhotoDc(AbstractMemo):
    class Meta:
        db_table = u'memo_kc_photo_dc'

# auto generated for board photo_kc_photo_fc
class PhotoKcPhotoFc(AbstractBoard):
    class Meta:
        db_table = u'photo_kc_photo_fc'
class MemoKcPhotoFc(AbstractMemo):
    class Meta:
        db_table = u'memo_kc_photo_fc'

# auto generated for board photo_kichong_photo
class PhotoKichongPhoto(AbstractBoard):
    class Meta:
        db_table = u'photo_kichong_photo'
class MemoKichongPhoto(AbstractMemo):
    class Meta:
        db_table = u'memo_kichong_photo'

# auto generated for board photo_market
class PhotoMarket(AbstractBoard):
    class Meta:
        db_table = u'photo_market'
class MemoMarket(AbstractMemo):
    class Meta:
        db_table = u'memo_market'

# auto generated for board photo_marlboro
class PhotoMarlboro(AbstractBoard):
    class Meta:
        db_table = u'photo_marlboro'
class MemoMarlboro(AbstractMemo):
    class Meta:
        db_table = u'memo_marlboro'

# auto generated for board photo_memory
class PhotoMemory(AbstractBoard):
    class Meta:
        db_table = u'photo_memory'
class MemoMemory(AbstractMemo):
    class Meta:
        db_table = u'memo_memory'

# auto generated for board photo_mem_research
class PhotoMemResearch(AbstractBoard):
    class Meta:
        db_table = u'photo_mem_research'
class MemoMemResearch(AbstractMemo):
    class Meta:
        db_table = u'memo_mem_research'

# auto generated for board photo_menssmells
class PhotoMenssmells(AbstractBoard):
    class Meta:
        db_table = u'photo_menssmells'
class MemoMenssmells(AbstractMemo):
    class Meta:
        db_table = u'memo_menssmells'

# auto generated for board photo_nba
class PhotoNba(AbstractBoard):
    class Meta:
        db_table = u'photo_nba'
class MemoNba(AbstractMemo):
    class Meta:
        db_table = u'memo_nba'

# auto generated for board photo_oekaki
class PhotoOekaki(AbstractBoard):
    class Meta:
        db_table = u'photo_oekaki'
class MemoOekaki(AbstractMemo):
    class Meta:
        db_table = u'memo_oekaki'

# auto generated for board photo_parkcue
class PhotoParkcue(AbstractBoard):
    class Meta:
        db_table = u'photo_parkcue'
class MemoParkcue(AbstractMemo):
    class Meta:
        db_table = u'memo_parkcue'

# auto generated for board photo_part_ad
class PhotoPartAd(AbstractBoard):
    class Meta:
        db_table = u'photo_part_ad'
class MemoPartAd(AbstractMemo):
    class Meta:
        db_table = u'memo_part_ad'

# auto generated for board photo_part_culture
class PhotoPartCulture(AbstractBoard):
    class Meta:
        db_table = u'photo_part_culture'
class MemoPartCulture(AbstractMemo):
    class Meta:
        db_table = u'memo_part_culture'

# auto generated for board photo_part_jungtong
class PhotoPartJungtong(AbstractBoard):
    class Meta:
        db_table = u'photo_part_jungtong'
class MemoPartJungtong(AbstractMemo):
    class Meta:
        db_table = u'memo_part_jungtong'

# auto generated for board photo_part_neo
class PhotoPartNeo(AbstractBoard):
    class Meta:
        db_table = u'photo_part_neo'
class MemoPartNeo(AbstractMemo):
    class Meta:
        db_table = u'memo_part_neo'

# auto generated for board photo_part_plan
class PhotoPartPlan(AbstractBoard):
    class Meta:
        db_table = u'photo_part_plan'
class MemoPartPlan(AbstractMemo):
    class Meta:
        db_table = u'memo_part_plan'

# auto generated for board photo_part_social
class PhotoPartSocial(AbstractBoard):
    class Meta:
        db_table = u'photo_part_social'
class MemoPartSocial(AbstractMemo):
    class Meta:
        db_table = u'memo_part_social'

# auto generated for board photo_photo
class PhotoPhoto(AbstractBoard):
    class Meta:
        db_table = u'photo_photo'
class MemoPhoto(AbstractMemo):
    class Meta:
        db_table = u'memo_photo'

# auto generated for board photo_photo2
class PhotoPhoto2(AbstractBoard):
    class Meta:
        db_table = u'photo_photo2'
class MemoPhoto2(AbstractMemo):
    class Meta:
        db_table = u'memo_photo2'

# auto generated for board photo_pray
class PhotoPray(AbstractBoard):
    class Meta:
        db_table = u'photo_pray'
class MemoPray(AbstractMemo):
    class Meta:
        db_table = u'memo_pray'

# auto generated for board photo_reload
class PhotoReload(AbstractBoard):
    class Meta:
        db_table = u'photo_reload'
class MemoReload(AbstractMemo):
    class Meta:
        db_table = u'memo_reload'

# auto generated for board photo_revolution
class PhotoRevolution(AbstractBoard):
    class Meta:
        db_table = u'photo_revolution'
class MemoRevolution(AbstractMemo):
    class Meta:
        db_table = u'memo_revolution'

# auto generated for board photo_sketch
class PhotoSketch(AbstractBoard):
    class Meta:
        db_table = u'photo_sketch'
class MemoSketch(AbstractMemo):
    class Meta:
        db_table = u'memo_sketch'

# auto generated for board photo_study_book
class PhotoStudyBook(AbstractBoard):
    class Meta:
        db_table = u'photo_study_book'
class MemoStudyBook(AbstractMemo):
    class Meta:
        db_table = u'memo_study_book'

# auto generated for board photo_syf
class PhotoSyf(AbstractBoard):
    class Meta:
        db_table = u'photo_syf'
class MemoSyf(AbstractMemo):
    class Meta:
        db_table = u'memo_syf'

# auto generated for board photo_trash
class PhotoTrash(AbstractBoard):
    class Meta:
        db_table = u'photo_trash'
class MemoTrash(AbstractMemo):
    class Meta:
        db_table = u'memo_trash'

# auto generated for board photo_twistedlife
class PhotoTwistedlife(AbstractBoard):
    class Meta:
        db_table = u'photo_twistedlife'
class MemoTwistedlife(AbstractMemo):
    class Meta:
        db_table = u'memo_twistedlife'

# auto generated for board photo_veryrealtrue
class PhotoVeryrealtrue(AbstractBoard):
    class Meta:
        db_table = u'photo_veryrealtrue'
class MemoVeryrealtrue(AbstractMemo):
    class Meta:
        db_table = u'memo_veryrealtrue'

# auto generated for board photo_volunteers
class PhotoVolunteers(AbstractBoard):
    class Meta:
        db_table = u'photo_volunteers'
class MemoVolunteers(AbstractMemo):
    class Meta:
        db_table = u'memo_volunteers'

# auto generated for board photo_webzineculture
class PhotoWebzineculture(AbstractBoard):
    class Meta:
        db_table = u'photo_webzineculture'
class MemoWebzineculture(AbstractMemo):
    class Meta:
        db_table = u'memo_webzineculture'

# auto generated for board photo_webzine_book
class PhotoWebzineBook(AbstractBoard):
    class Meta:
        db_table = u'photo_webzine_book'
class MemoWebzineBook(AbstractMemo):
    class Meta:
        db_table = u'memo_webzine_book'

# auto generated for board photo_webzine_people
class PhotoWebzinePeople(AbstractBoard):
    class Meta:
        db_table = u'photo_webzine_people'
class MemoWebzinePeople(AbstractMemo):
    class Meta:
        db_table = u'memo_webzine_people'

# auto generated for board photo_webzine_photo
class PhotoWebzinePhoto(AbstractBoard):
    class Meta:
        db_table = u'photo_webzine_photo'
class MemoWebzinePhoto(AbstractMemo):
    class Meta:
        db_table = u'memo_webzine_photo'
