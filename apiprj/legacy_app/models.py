from django.db import models
from abstract_models import (AbstractBoardShortPassword,
                             AbstractBoardLongPassword, AbstractPhotoBoard,
                             AbstractMemo1, AbstractMemo2,
                             AbstractComment1, AbstractComment2)

class BoardAlumni(AbstractBoardLongPassword):
    class Meta:
        db_table = u'board_alumni'

class BoardAnonymous(AbstractBoardLongPassword):
    class Meta:
        db_table = u'board_anonymous'

class BoardFreeboard(AbstractBoardLongPassword):
    class Meta:
        db_table = u'board_freeboard'        
        
class BoardAllaplus(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_allaplus'
        
class BoardAlumni00(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_alumni00'

class BoardAlumni01(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_alumni01'

class BoardAlumni02(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_alumni02'

class BoardAlumni03(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_alumni03'

class BoardAlumni04(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_alumni04'

class BoardAlumni05(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_alumni05'

class BoardAlumni06(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_alumni06'

class BoardAlumni07(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_alumni07'

class BoardAlumni08(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_alumni08'

class BoardAlumni09(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_alumni09'

class BoardAlumni10(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_alumni10'

class BoardAlumni72(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_alumni72'

class BoardAlumni73(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_alumni73'

class BoardAlumni74(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_alumni74'

class BoardAlumni75(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_alumni75'

class BoardAlumni76(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_alumni76'

class BoardAlumni77(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_alumni77'

class BoardAlumni78(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_alumni78'

class BoardAlumni79(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_alumni79'

class BoardAlumni80(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_alumni80'

class BoardAlumni81(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_alumni81'

class BoardAlumni82(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_alumni82'

class BoardAlumni83(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_alumni83'

class BoardAlumni84(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_alumni84'

class BoardAlumni85(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_alumni85'

class BoardAlumni86(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_alumni86'

class BoardAlumni87(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_alumni87'

class BoardAlumni88(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_alumni88'

class BoardAlumni89(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_alumni89'

class BoardAlumni90(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_alumni90'

class BoardAlumni91(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_alumni91'

class BoardAlumni92(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_alumni92'

class BoardAlumni93(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_alumni93'

class BoardAlumni94(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_alumni94'

class BoardAlumni95(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_alumni95'

class BoardAlumni96(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_alumni96'

class BoardAlumni97(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_alumni97'

class BoardAlumni98(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_alumni98'

class BoardAlumni99(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_alumni99'

class BoardAlumniMemory(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_alumni_memory'

class BoardAlumninews(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_alumninews'

class BoardAlumninews1(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_alumninews1'

class BoardBoardTour(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_board_tour'

class BoardBug(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_bug'

class BoardCafeAppellation(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_cafe_appellation'

class BoardCafeAppellation2(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_cafe_appellation2'

class BoardCafeAppellation3(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_cafe_appellation3'

class BoardCafeBoard3(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_cafe_board3'

class BoardCafeChuri(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_cafe_churi'

class BoardCafeCuti(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_cafe_cuti'

class BoardCafeForum(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_cafe_forum'

class BoardCafeGirlStudent(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_cafe_girl_student'

class BoardCafeGutter(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_cafe_gutter'

class BoardCafeGutter2(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_cafe_gutter2'

class BoardCafeHandtruth(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_cafe_handtruth'

class BoardCafeHandtruth2(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_cafe_handtruth2'

class BoardCafeHeukseoker(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_cafe_heukseoker'

class BoardCafeHeukseoker2(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_cafe_heukseoker2'

class BoardCafeHomesteal(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_cafe_homesteal'

class BoardCafeIris(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_cafe_iris'

class BoardCafeItSecurity(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_cafe_it_security'

class BoardCafeJokbal(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_cafe_jokbal'

class BoardCafeJstorm(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_cafe_jstorm'

class BoardCafeMountainLove(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_cafe_mountain_love'

class BoardCafeNote(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_cafe_note'

class BoardCafeNote2(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_cafe_note2'

class BoardCafePresent(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_cafe_present'

class BoardCafeSecurelab(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_cafe_securelab'

class BoardCafeSecurelab2(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_cafe_securelab2'

class BoardCafeSnsd(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_cafe_snsd'

class BoardCafeSteamers(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_cafe_steamers'

class BoardCafeSteamers2(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_cafe_steamers2'

class BoardCafeSteamers3(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_cafe_steamers3'

class BoardCafeTspin(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_cafe_tspin'

class BoardCafeWow(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_cafe_wow'

class BoardCaucsesa(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_caucsesa'

class BoardCgraph(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_cgraph'

class BoardClubAbroad(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_club_abroad'

class BoardClubBaseball(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_club_baseball'

class BoardClubBrenntano(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_club_brenntano'

class BoardClubCamera(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_club_camera'

class BoardClubComball(AbstractBoardShortPassword):
    class Meta:
        db_table = u'board_club_comball'

class BoardClubCurseware(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_club_curseware'

class BoardClubCurseware2(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_club_curseware2'

class BoardClubDevils(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_club_devils'

class BoardClubEcs(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_club_ecs'

class BoardClubFootlove(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_club_footlove'

class BoardClubFr(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_club_fr'

class BoardClubFreesoul(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_club_freesoul'

class BoardClubGame(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_club_game'

class BoardClubMaim(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_club_maim'

class BoardClubMios(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_club_mios'

class BoardClubMiosSub1(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_club_mios_sub1'

class BoardClubNetory(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_club_netory'

class BoardClubOomg(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_club_oomg'

class BoardClubQuestion(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_club_question'

class BoardClubShift(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_club_shift'

class BoardClubSoesl(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_club_soesl'

class BoardClubSsoa(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_club_ssoa'

class BoardClubStaff(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_club_staff'

class BoardClubSullen(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_club_sullen'

class BoardClubSylph(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_club_sylph'

class BoardClubTrash(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_club_trash'

class BoardClubWithweve(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_club_withweve'

class BoardClubZp(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_club_zp'

class BoardCounsel(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_counsel'

class BoardCsebiz(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_csebiz'

class BoardCsebizLecture(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_csebiz_lecture'

class BoardCsesa(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_csesa'

class BoardCsesaSub1(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_csesa_sub1'

class BoardCsesaSub2(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_csesa_sub2'

class BoardCsesac(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_csesac'

class BoardDcgallers(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_dcgallers'

class BoardDiscuss(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_discuss'

class BoardDoc(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_doc'

class BoardDogsix(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_dogsix'

class BoardDongneHidden(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_dongne_hidden'

class BoardDongneteam(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_dongneteam'

class BoardDongneteamtest(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_dongneteamtest'

class BoardDumb(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_dumb'

class BoardEnter(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_enter'

class BoardEtc(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_etc'

class BoardEvent(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_event'

class BoardExtreamsport(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_extreamsport'

class BoardFacse(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_facse'

class BoardFacse2(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_facse2'

class BoardFishgrow(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_fishgrow'

class BoardGamemoney(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_gamemoney'

class BoardGujja(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_gujja'

class BoardHelp(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_help'

class BoardHex(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_hex'

class BoardHexSub1(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_hex_sub1'

class BoardItnews(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_itnews'

class BoardJhonson(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_jhonson'

class BoardLecture(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_lecture'

class BoardLost(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_lost'

class BoardMarlboro(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_marlboro'

class BoardMarlboro2(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_marlboro2'

class BoardMemResearch(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_mem_research'

class BoardMenssmells(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_menssmells'

class BoardNba(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_nba'

class BoardNotice(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_notice'

class BoardPaperNeo(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_paper_neo'

class BoardPaperPop(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_paper_pop'

class BoardParkcue(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_parkcue'

class BoardParkcueSub1(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_parkcue_sub1'

class BoardPartAd(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_part_ad'

class BoardPartCulture(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_part_culture'

class BoardPartEveryday(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_part_everyday'

class BoardPartJungtong(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_part_jungtong'

class BoardPartNeo(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_part_neo'

class BoardPartPlan(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_part_plan'

class BoardPartPlanRecords(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_part_plan_records'

class BoardPartSocial(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_part_social'

class BoardPcmanage(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_pcmanage'

class BoardPhoto(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_photo'

class BoardPhoto2(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_photo2'

class BoardPoll(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_poll'

class BoardPray(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_pray'

class BoardQna(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_qna'

class BoardRecruit(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_recruit'

class BoardReload(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_reload'

class BoardRevolution(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_revolution'

class BoardSketch(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_sketch'

class BoardSyf(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_syf'

class BoardTemp(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_temp'

class BoardTest(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_test'

class BoardTest1(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_test1'

class BoardTestPaper(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_test_paper'

class BoardToeic850(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_toeic850'

class BoardToto(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_toto'

class BoardTrashNovel(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_trash_novel'

class BoardTwistedlife(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_twistedlife'

class BoardVeryrealtrue(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_veryrealtrue'

class BoardVolunteers(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_volunteers'

class BoardWebzineTheme(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_webzine_theme'

class BoardWithweveData(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_withweve_data'

class BoardWithweveFree(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'board_withweve_free'

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

class CommentAllaplus(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_allaplus'

class CommentAlumni(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_alumni'

class CommentAlumni00(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_alumni00'

class CommentAlumni01(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_alumni01'

class CommentAlumni02(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_alumni02'

class CommentAlumni03(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_alumni03'

class CommentAlumni04(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_alumni04'

class CommentAlumni05(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_alumni05'

class CommentAlumni06(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_alumni06'

class CommentAlumni07(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_alumni07'

class CommentAlumni08(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_alumni08'

class CommentAlumni09(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_alumni09'

class CommentAlumni10(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_alumni10'

class CommentAlumni72(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_alumni72'

class CommentAlumni73(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_alumni73'

class CommentAlumni74(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_alumni74'

class CommentAlumni75(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_alumni75'

class CommentAlumni76(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_alumni76'

class CommentAlumni77(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_alumni77'

class CommentAlumni78(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_alumni78'

class CommentAlumni79(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_alumni79'

class CommentAlumni80(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_alumni80'

class CommentAlumni81(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_alumni81'

class CommentAlumni82(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_alumni82'

class CommentAlumni83(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_alumni83'

class CommentAlumni84(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_alumni84'

class CommentAlumni85(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_alumni85'

class CommentAlumni86(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_alumni86'

class CommentAlumni87(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_alumni87'

class CommentAlumni88(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_alumni88'

class CommentAlumni89(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_alumni89'

class CommentAlumni90(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_alumni90'

class CommentAlumni91(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_alumni91'

class CommentAlumni92(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_alumni92'

class CommentAlumni93(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_alumni93'

class CommentAlumni94(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_alumni94'

class CommentAlumni95(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_alumni95'

class CommentAlumni96(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_alumni96'

class CommentAlumni97(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_alumni97'

class CommentAlumni98(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_alumni98'

class CommentAlumni99(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_alumni99'

class CommentAlumniMemory(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_alumni_memory'

class CommentAlumninews(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_alumninews'

class CommentAlumninews1(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_alumninews1'

class CommentAnonymous(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_anonymous'

class CommentBoardTour(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_board_tour'

class CommentBug(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_bug'

class CommentCafeAppellation(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_cafe_appellation'

class CommentCafeAppellation2(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_cafe_appellation2'

class CommentCafeAppellation3(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_cafe_appellation3'

class CommentCafeBoard3(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_cafe_board3'

class CommentCafeChuri(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_cafe_churi'

class CommentCafeCuti(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_cafe_cuti'

class CommentCafeForum(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_cafe_forum'

class CommentCafeGirlStudent(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_cafe_girl_student'

class CommentCafeGutter(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_cafe_gutter'

class CommentCafeGutter2(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_cafe_gutter2'

class CommentCafeHandtruth(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_cafe_handtruth'

class CommentCafeHandtruth2(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_cafe_handtruth2'

class CommentCafeHeukseoker(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_cafe_heukseoker'

class CommentCafeHeukseoker2(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_cafe_heukseoker2'

class CommentCafeHomesteal(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_cafe_homesteal'

class CommentCafeIris(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_cafe_iris'

class CommentCafeItSecurity(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_cafe_it_security'

class CommentCafeJokbal(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_cafe_jokbal'

class CommentCafeJstorm(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_cafe_jstorm'

class CommentCafeMountainLove(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_cafe_mountain_love'

class CommentCafeNote(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_cafe_note'

class CommentCafeNote2(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_cafe_note2'

class CommentCafePresent(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_cafe_present'

class CommentCafeSecurelab(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_cafe_securelab'

class CommentCafeSecurelab2(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_cafe_securelab2'

class CommentCafeSnsd(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_cafe_snsd'

class CommentCafeSteamers(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_cafe_steamers'

class CommentCafeSteamers2(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_cafe_steamers2'

class CommentCafeSteamers3(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_cafe_steamers3'

class CommentCafeTspin(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_cafe_tspin'

class CommentCafeWow(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_cafe_wow'

class CommentCaucsesa(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_caucsesa'

class CommentCgraph(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_cgraph'

class CommentClubAbroad(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_club_abroad'

class CommentClubBaseball(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_club_baseball'

class CommentClubBrenntano(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_club_brenntano'

class CommentClubCamera(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_club_camera'

class CommentClubComball(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_club_comball'

class CommentClubCurseware(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_club_curseware'

class CommentClubCurseware2(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_club_curseware2'

class CommentClubDevils(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_club_devils'

class CommentClubEcs(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_club_ecs'

class CommentClubFootlove(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_club_footlove'

class CommentClubFr(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_club_fr'

class CommentClubFreesoul(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_club_freesoul'

class CommentClubGame(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_club_game'

class CommentClubMaim(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_club_maim'

class CommentClubMios(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_club_mios'

class CommentClubMiosSub1(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_club_mios_sub1'

class CommentClubNetory(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_club_netory'

class CommentClubOomg(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_club_oomg'

class CommentClubQuestion(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_club_question'

class CommentClubShift(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_club_shift'

class CommentClubSoesl(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_club_soesl'

class CommentClubSsoa(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_club_ssoa'

class CommentClubStaff(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_club_staff'

class CommentClubSullen(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_club_sullen'

class CommentClubSylph(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_club_sylph'

class CommentClubTrash(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_club_trash'

class CommentClubWithweve(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_club_withweve'

class CommentClubZp(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_club_zp'

class CommentCounsel(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_counsel'

class CommentCsebiz(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_csebiz'

class CommentCsebizLecture(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_csebiz_lecture'

class CommentCsesa(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_csesa'

class CommentCsesaSub1(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_csesa_sub1'

class CommentCsesaSub2(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_csesa_sub2'

class CommentCsesac(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_csesac'

class CommentDcgallers(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_dcgallers'

class CommentDiscuss(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_discuss'

class CommentDoc(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_doc'

class CommentDogsix(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_dogsix'

class CommentDongneHidden(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_dongne_hidden'

class CommentDongneteam(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_dongneteam'

class CommentDongneteamtest(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_dongneteamtest'

class CommentDumb(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_dumb'

class CommentEnter(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_enter'

class CommentEtc(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_etc'

class CommentEvent(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_event'

class CommentExtreamsport(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_extreamsport'

class CommentFacse(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_facse'

class CommentFacse2(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_facse2'

class CommentFishgrow(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_fishgrow'

class CommentFreeboard(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_freeboard'

class CommentGamemoney(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_gamemoney'

class CommentGujja(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_gujja'

class CommentHelp(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_help'

class CommentHex(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_hex'

class CommentHexSub1(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_hex_sub1'

class CommentItnews(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_itnews'

class CommentJhonson(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_jhonson'

class CommentLecture(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_lecture'

class CommentLost(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_lost'

class CommentMalboro2(AbstractComment2):
    class Meta:
        db_table = u'comment_malboro2'

class CommentMarlboro(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_marlboro'

class CommentMarlboro2(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_marlboro2'

class CommentMemResearch(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_mem_research'

class CommentMenssmells(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_menssmells'

class CommentNba(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_nba'

class CommentNotice(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_notice'

class CommentPaperNeo(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_paper_neo'

class CommentPaperPop(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_paper_pop'

class CommentParkcue(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_parkcue'

class CommentParkcueSub1(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_parkcue_sub1'

class CommentPartAd(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_part_ad'

class CommentPartCulture(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_part_culture'

class CommentPartEveryday(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_part_everyday'

class CommentPartJungtong(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_part_jungtong'

class CommentPartNeo(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_part_neo'

class CommentPartPlan(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_part_plan'

class CommentPartPlanRecords(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_part_plan_records'

class CommentPartSocial(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_part_social'

class CommentPcmanage(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_pcmanage'

class CommentPhoto(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_photo'

class CommentPhoto2(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_photo2'

class CommentPoll(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_poll'

class CommentPray(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_pray'

class CommentQna(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_qna'

class CommentRecruit(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_recruit'

class CommentReload(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_reload'

class CommentRevolution(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_revolution'

class CommentSketch(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_sketch'

class CommentSyf(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_syf'

class CommentTemp(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_temp'

class CommentTest(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_test'

class CommentTest1(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_test1'

class CommentTestPaper(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_test_paper'

class CommentToeic850(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_toeic850'

class CommentToto(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_toto'

class CommentTrashNovel(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_trash_novel'

class CommentTwistedlife(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_twistedlife'

class CommentVeryrealtrue(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_veryrealtrue'

class CommentVolunteers(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_volunteers'

class CommentWebzineTheme(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_webzine_theme'

class CommentWithweveData(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_withweve_data'

class CommentWithweveFree(AbstractComment1):
# AbstractComment1
    class Meta:
        db_table = u'comment_withweve_free'

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

class MemoAllaplus(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_allaplus'

class MemoAlumni00(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_alumni00'

class MemoAlumni01(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_alumni01'

class MemoAlumni02(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_alumni02'

class MemoAlumni03(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_alumni03'

class MemoAlumni04(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_alumni04'

class MemoAlumni05(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_alumni05'

class MemoAlumni06(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_alumni06'

class MemoAlumni07(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_alumni07'

class MemoAlumni08(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_alumni08'

class MemoAlumni09(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_alumni09'

class MemoAlumni10(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_alumni10'

class MemoAlumni72(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_alumni72'

class MemoAlumni73(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_alumni73'

class MemoAlumni74(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_alumni74'

class MemoAlumni75(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_alumni75'

class MemoAlumni76(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_alumni76'

class MemoAlumni77(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_alumni77'

class MemoAlumni78(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_alumni78'

class MemoAlumni79(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_alumni79'

class MemoAlumni80(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_alumni80'

class MemoAlumni81(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_alumni81'

class MemoAlumni82(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_alumni82'

class MemoAlumni83(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_alumni83'

class MemoAlumni84(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_alumni84'

class MemoAlumni85(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_alumni85'

class MemoAlumni86(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_alumni86'

class MemoAlumni87(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_alumni87'

class MemoAlumni88(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_alumni88'

class MemoAlumni89(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_alumni89'

class MemoAlumni90(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_alumni90'

class MemoAlumni91(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_alumni91'

class MemoAlumni92(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_alumni92'

class MemoAlumni93(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_alumni93'

class MemoAlumni94(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_alumni94'

class MemoAlumni95(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_alumni95'

class MemoAlumni96(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_alumni96'

class MemoAlumni97(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_alumni97'

class MemoAlumni98(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_alumni98'

class MemoAlumni99(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_alumni99'

class MemoCafeAppellation(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_cafe_appellation'

class MemoCafeChuri(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_cafe_churi'

class MemoCafeCuti(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_cafe_cuti'

class MemoCafeForum(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_cafe_forum'

class MemoCafeGirlStudent(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_cafe_girl_student'

class MemoCafeGutter(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_cafe_gutter'

class MemoCafeHandtruth(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_cafe_handtruth'

class MemoCafeHeukseoker(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_cafe_heukseoker'

class MemoCafeHomesteal(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_cafe_homesteal'

class MemoCafeIris(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_cafe_iris'

class MemoCafeItSecurity(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_cafe_it_security'

class MemoCafeJokbal(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_cafe_jokbal'

class MemoCafeJstorm(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_cafe_jstorm'

class MemoCafeMountainLove(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_cafe_mountain_love'

class MemoCafeNote(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_cafe_note'

class MemoCafePresent(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_cafe_present'

class MemoCafeSecurelab(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_cafe_securelab'

class MemoCafeSnsd(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_cafe_snsd'

class MemoCafeSteamers(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_cafe_steamers'

class MemoCafeTspin(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_cafe_tspin'

class MemoCafeWow(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_cafe_wow'

class MemoCgraph(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_cgraph'

class MemoClubAbroad(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_club_abroad'

class MemoClubBrenntano(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_club_brenntano'

class MemoClubCurseware(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_club_curseware'

class MemoClubDumb(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_club_dumb'

class MemoClubEcs(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_club_ecs'

class MemoClubFootlove(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_club_footlove'

class MemoClubFr(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_club_fr'

class MemoClubMios(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_club_mios'

class MemoClubWithweve(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_club_withweve'

class MemoCsebiz(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_csebiz'

class MemoCsesa(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_csesa'

class MemoCsesac(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_csesac'

class MemoDcgallers(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_dcgallers'

class MemoDogsix(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_dogsix'

class MemoDongneteam(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_dongneteam'

class MemoEtc(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_etc'

class MemoExtreamsport(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_extreamsport'

class MemoFacse(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_facse'

class MemoFishgrow(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_fishgrow'

class MemoGamemoney(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_gamemoney'

class MemoGraduation(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_graduation'

class MemoGujja(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_gujja'

class MemoHex(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_hex'

class MemoInfo02(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_info_02'

class MemoInfoMemory(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_info_memory'

class MemoInfoMisc(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_info_misc'

class MemoJhonson(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_jhonson'

class MemoKcPhotoDc(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_kc_photo_dc'

class MemoKcPhotoFc(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_kc_photo_fc'

class MemoKichongPhoto(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_kichong_photo'

class MemoMarket(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_market'

class MemoMarlboro(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_marlboro'

class MemoMemResearch(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_mem_research'

class MemoMemory(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_memory'

class MemoMenssmells(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_menssmells'

class MemoNba(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_nba'

class MemoOekaki(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_oekaki'

class MemoParkcue(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_parkcue'

class MemoPartAd(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_part_ad'

class MemoPartCulture(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_part_culture'

class MemoPartJungtong(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_part_jungtong'

class MemoPartNeo(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_part_neo'

class MemoPartPlan(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_part_plan'

class MemoPartSocial(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_part_social'

class MemoPhoto(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_photo'

class MemoPhoto2(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_photo2'

class MemoPray(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_pray'

class MemoReload(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_reload'

class MemoRevolution(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_revolution'

class MemoSketch(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_sketch'

class MemoStudyBook(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_study_book'

class MemoSyf(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_syf'

class MemoTrash(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_trash'

class MemoTwistedlife(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_twistedlife'

class MemoUnited(AbstractMemo2):
    class Meta:
        db_table = u'memo_united'

class MemoVeryrealtrue(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_veryrealtrue'

class MemoVolunteers(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_volunteers'

class MemoWebzineBook(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_webzine_book'

class MemoWebzinePeople(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_webzine_people'

class MemoWebzinePhoto(AbstractMemo1):
# AbstractMemo1
    class Meta:
        db_table = u'memo_webzine_photo'

class MemoWebzineculture(AbstractMemo1):
# AbstractMemo1
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
    id = models.AutoField(primary_key=True)
    word = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'nospam'

class PhotoAllaplus(models.Model):
# AbstractPhotoBoard
    class Meta:
        db_table = u'photo_allaplus'

class PhotoAlumni00(AbstractMemo1):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'photo_alumni00'

class PhotoAlumni01(AbstractMemo1):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'photo_alumni01'

class PhotoAlumni02(AbstractMemo1):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'photo_alumni02'

class PhotoAlumni03(AbstractMemo1):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'photo_alumni03'

class PhotoAlumni04(AbstractMemo1):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'photo_alumni04'

class PhotoAlumni05(AbstractPhotoBoard):
# AbstractPhotoBoard
    class Meta:
        db_table = u'photo_alumni05'

class PhotoAlumni06(AbstractPhotoBoard):
# AbstractPhotoBoard
    class Meta:
        db_table = u'photo_alumni06'

class PhotoAlumni07(AbstractPhotoBoard):
# AbstractPhotoBoard
    class Meta:
        db_table = u'photo_alumni07'

class PhotoAlumni08(AbstractPhotoBoard):
# AbstractPhotoBoard
    class Meta:
        db_table = u'photo_alumni08'

class PhotoAlumni09(AbstractPhotoBoard):
# AbstractPhotoBoard
    class Meta:
        db_table = u'photo_alumni09'

class PhotoAlumni10(AbstractPhotoBoard):
# AbstractPhotoBoard
    class Meta:
        db_table = u'photo_alumni10'

class PhotoAlumni72(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'photo_alumni72'

class PhotoAlumni73(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'photo_alumni73'

class PhotoAlumni74(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'photo_alumni74'

class PhotoAlumni75(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'photo_alumni75'

class PhotoAlumni76(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'photo_alumni76'

class PhotoAlumni77(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'photo_alumni77'

class PhotoAlumni78(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'photo_alumni78'

class PhotoAlumni79(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'photo_alumni79'

class PhotoAlumni80(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'photo_alumni80'

class PhotoAlumni81(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'photo_alumni81'

class PhotoAlumni82(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'photo_alumni82'

class PhotoAlumni83(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'photo_alumni83'

class PhotoAlumni84(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'photo_alumni84'

class PhotoAlumni85(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'photo_alumni85'

class PhotoAlumni86(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'photo_alumni86'

class PhotoAlumni87(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'photo_alumni87'

class PhotoAlumni88(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'photo_alumni88'

class PhotoAlumni89(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'photo_alumni89'

class PhotoAlumni90(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'photo_alumni90'

class PhotoAlumni91(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'photo_alumni91'

class PhotoAlumni92(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'photo_alumni92'

class PhotoAlumni93(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'photo_alumni93'

class PhotoAlumni94(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'photo_alumni94'

class PhotoAlumni95(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'photo_alumni95'

class PhotoAlumni96(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'photo_alumni96'

class PhotoAlumni97(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'photo_alumni97'

class PhotoAlumni98(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'photo_alumni98'

class PhotoAlumni99(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'photo_alumni99'

class PhotoCafeAppellation(AbstractPhotoBoard):
# AbstractPhotoBoard
    class Meta:
        db_table = u'photo_cafe_appellation'

class PhotoCafeChuri(AbstractPhotoBoard):
# AbstractPhotoBoard
    class Meta:
        db_table = u'photo_cafe_churi'

class PhotoCafeCuti(AbstractPhotoBoard):
# AbstractPhotoBoard
    class Meta:
        db_table = u'photo_cafe_cuti'

class PhotoCafeForum(AbstractPhotoBoard):
# AbstractPhotoBoard
    class Meta:
        db_table = u'photo_cafe_forum'

class PhotoCafeGirlStudent(AbstractPhotoBoard):
# AbstractPhotoBoard
    class Meta:
        db_table = u'photo_cafe_girl_student'

class PhotoCafeGutter(AbstractPhotoBoard):
# AbstractPhotoBoard
    class Meta:
        db_table = u'photo_cafe_gutter'

class PhotoCafeHandtruth(AbstractPhotoBoard):
# AbstractPhotoBoard
    class Meta:
        db_table = u'photo_cafe_handtruth'

class PhotoCafeHeukseoker(AbstractPhotoBoard):
# AbstractPhotoBoard
    class Meta:
        db_table = u'photo_cafe_heukseoker'

class PhotoCafeHomesteal(AbstractPhotoBoard):
# AbstractPhotoBoard
    class Meta:
        db_table = u'photo_cafe_homesteal'

class PhotoCafeIris(AbstractPhotoBoard):
# AbstractPhotoBoard
    class Meta:
        db_table = u'photo_cafe_iris'

class PhotoCafeItSecurity(AbstractPhotoBoard):
# AbstractPhotoBoard
    class Meta:
        db_table = u'photo_cafe_it_security'

class PhotoCafeJokbal(AbstractPhotoBoard):
# AbstractPhotoBoard
    class Meta:
        db_table = u'photo_cafe_jokbal'

class PhotoCafeJstorm(AbstractPhotoBoard):
# AbstractPhotoBoard
    class Meta:
        db_table = u'photo_cafe_jstorm'

class PhotoCafeMountainLove(AbstractPhotoBoard):
# AbstractPhotoBoard
    class Meta:
        db_table = u'photo_cafe_mountain_love'

class PhotoCafeNote(AbstractPhotoBoard):
# AbstractPhotoBoard
    class Meta:
        db_table = u'photo_cafe_note'

class PhotoCafePresent(AbstractPhotoBoard):
# AbstractPhotoBoard
    class Meta:
        db_table = u'photo_cafe_present'

class PhotoCafeSecurelab(AbstractPhotoBoard):
# AbstractPhotoBoard
    class Meta:
        db_table = u'photo_cafe_securelab'

class PhotoCafeSnsd(AbstractPhotoBoard):
# AbstractPhotoBoard
    class Meta:
        db_table = u'photo_cafe_snsd'

class PhotoCafeSteamers(AbstractPhotoBoard):
# AbstractPhotoBoard
    class Meta:
        db_table = u'photo_cafe_steamers'

class PhotoCafeTspin(AbstractPhotoBoard):
# AbstractPhotoBoard
    class Meta:
        db_table = u'photo_cafe_tspin'

class PhotoCafeWow(AbstractPhotoBoard):
# AbstractPhotoBoard
    class Meta:
        db_table = u'photo_cafe_wow'

class PhotoCgraph(AbstractPhotoBoard):
# AbstractPhotoBoard
    class Meta:
        db_table = u'photo_cgraph'

class PhotoClubAbroad(AbstractPhotoBoard):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'photo_club_abroad'

class PhotoClubBrenntano(AbstractPhotoBoard):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'photo_club_brenntano'

class PhotoClubCurseware(AbstractPhotoBoard):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'photo_club_curseware'

class PhotoClubDumb(AbstractPhotoBoard):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'photo_club_dumb'

class PhotoClubEcs(AbstractPhotoBoard):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'photo_club_ecs'

class PhotoClubFootlove(AbstractPhotoBoard):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'photo_club_footlove'

class PhotoClubFr(AbstractPhotoBoard):
# AbstractPhotoBoard
    class Meta:
        db_table = u'photo_club_fr'

class PhotoClubMios(AbstractPhotoBoard):
# AbstractPhotoBoard
    class Meta:
        db_table = u'photo_club_mios'

class PhotoClubWithweve(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'photo_club_withweve'

class PhotoCsebiz(AbstractPhotoBoard):
# AbstractPhotoBoard
    class Meta:
        db_table = u'photo_csebiz'

class PhotoCsesa(AbstractPhotoBoard):
# AbstractPhotoBoard
    class Meta:
        db_table = u'photo_csesa'

class PhotoCsesac(AbstractPhotoBoard):
# AbstractPhotoBoard
    class Meta:
        db_table = u'photo_csesac'

class PhotoDcgallers(AbstractPhotoBoard):
# AbstractPhotoBoard
    class Meta:
        db_table = u'photo_dcgallers'

class PhotoDogsix(AbstractPhotoBoard):
# AbstractPhotoBoard
    class Meta:
        db_table = u'photo_dogsix'

class PhotoDongneteam(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'photo_dongneteam'

class PhotoEtc(AbstractPhotoBoard):
# AbstractPhotoBoard
    class Meta:
        db_table = u'photo_etc'

class PhotoExtreamsport(AbstractPhotoBoard):
# AbstractPhotoBoard
    class Meta:
        db_table = u'photo_extreamsport'

class PhotoFacse(AbstractPhotoBoard):
# AbstractPhotoBoard
    class Meta:
        db_table = u'photo_facse'

class PhotoFishgrow(AbstractPhotoBoard):
# AbstractPhotoBoard
    class Meta:
        db_table = u'photo_fishgrow'

class PhotoGamemoney(AbstractPhotoBoard):
# AbstractPhotoBoard
    class Meta:
        db_table = u'photo_gamemoney'

class PhotoGraduation(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'photo_graduation'

class PhotoGujja(AbstractPhotoBoard):
# AbstractPhotoBoard
    class Meta:
        db_table = u'photo_gujja'

class PhotoHex(AbstractPhotoBoard):
# AbstractPhotoBoard
    class Meta:
        db_table = u'photo_hex'

class PhotoInfo02(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'photo_info_02'

class PhotoInfoMemory(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'photo_info_memory'

class PhotoInfoMisc(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'photo_info_misc'

class PhotoJhonson(AbstractPhotoBoard):
# AbstractPhotoBoard
    class Meta:
        db_table = u'photo_jhonson'

class PhotoKcPhotoDc(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'photo_kc_photo_dc'

class PhotoKcPhotoFc(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'photo_kc_photo_fc'

class PhotoKichongPhoto(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'photo_kichong_photo'

class PhotoMarket(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'photo_market'

class PhotoMarlboro(AbstractPhotoBoard):
# AbstractPhotoBoard
    class Meta:
        db_table = u'photo_marlboro'

class PhotoMemResearch(AbstractPhotoBoard):
# AbstractPhotoBoard
    class Meta:
        db_table = u'photo_mem_research'

class PhotoMemory(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'photo_memory'

class PhotoMenssmells(AbstractPhotoBoard):
# AbstractPhotoBoard
    class Meta:
        db_table = u'photo_menssmells'

class PhotoNba(AbstractPhotoBoard):
# AbstractPhotoBoard
    class Meta:
        db_table = u'photo_nba'

class PhotoOekaki(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'photo_oekaki'

class PhotoParkcue(AbstractPhotoBoard):
# AbstractPhotoBoard
    class Meta:
        db_table = u'photo_parkcue'

class PhotoPartAd(AbstractBoardShortPassword):
    class Meta:
        db_table = u'photo_part_ad'

class PhotoPartCulture(AbstractPhotoBoard):
# AbstractPhotoBoard
    class Meta:
        db_table = u'photo_part_culture'

class PhotoPartJungtong(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'photo_part_jungtong'

class PhotoPartNeo(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'photo_part_neo'

class PhotoPartPlan(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'photo_part_plan'

class PhotoPartSocial(AbstractPhotoBoard):
# AbstractPhotoBoard
    class Meta:
        db_table = u'photo_part_social'

class PhotoPhoto(AbstractPhotoBoard):
# AbstractPhotoBoard
    class Meta:
        db_table = u'photo_photo'

class PhotoPhoto2(AbstractPhotoBoard):
# AbstractPhotoBoard
    class Meta:
        db_table = u'photo_photo2'

class PhotoPray(AbstractPhotoBoard):
# AbstractPhotoBoard
    class Meta:
        db_table = u'photo_pray'

class PhotoReload(AbstractPhotoBoard):
# AbstractPhotoBoard
    class Meta:
        db_table = u'photo_reload'

class PhotoRevolution(AbstractPhotoBoard):
# AbstractPhotoBoard
    class Meta:
        db_table = u'photo_revolution'

class PhotoSketch(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'photo_sketch'

class PhotoStudyBook(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'photo_study_book'

class PhotoSyf(AbstractPhotoBoard):
# AbstractPhotoBoard
    class Meta:
        db_table = u'photo_syf'

class PhotoTrash(AbstractPhotoBoard):
# AbstractPhotoBoard
    class Meta:
        db_table = u'photo_trash'

class PhotoTwistedlife(AbstractPhotoBoard):
# AbstractPhotoBoard
    class Meta:
        db_table = u'photo_twistedlife'

class PhotoUnited(models.Model):
    id = models.AutoField(primary_key=True)
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

class PhotoVeryrealtrue(AbstractPhotoBoard):
# AbstractPhotoBoard
    class Meta:
        db_table = u'photo_veryrealtrue'

class PhotoVolunteers(AbstractPhotoBoard):
# AbstractPhotoBoard
    class Meta:
        db_table = u'photo_volunteers'

class PhotoWebzineBook(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'photo_webzine_book'

class PhotoWebzinePeople(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'photo_webzine_people'

class PhotoWebzinePhoto(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
    class Meta:
        db_table = u'photo_webzine_photo'

class PhotoWebzineculture(AbstractBoardShortPassword):
    #AbstractBoardShortPassword
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
    class Meta:
        db_table = u'photoinfo'

class PollData(models.Model):
    id = models.AutoField(primary_key=True)
    poll_id = models.IntegerField()
    data_id = models.IntegerField()
    content = models.CharField(max_length=180)
    class Meta:
        db_table = u'poll_data'

class PollMain(models.Model):
    id = models.AutoField(primary_key=True)
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
    id = models.AutoField(primary_key=True)
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

#class Zipcode(models.Model):
#    zipcode = models.CharField(max_length=21, db_column='ZIPCODE', blank=True) # Field name made lowercase.
#    sido = models.CharField(max_length=12, db_column='SIDO', blank=True) # Field name made lowercase.
#    gugun = models.CharField(max_length=39, db_column='GUGUN', blank=True) # Field name made lowercase.
#    dong = models.CharField(max_length=129, db_column='DONG', blank=True) # Field name made lowercase.
#    bunji = models.CharField(max_length=51, db_column='BUNJI', blank=True) # Field name made lowercase.
#    class Meta:
#        db_table = u'zipcode'





