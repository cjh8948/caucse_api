#-*-coding:utf-8-*-
from apiprj.api1_app.models import Member
from apiprj.oauth_app.utils import check_mysql_password 
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class AuthBackend:
    "mysql password system 으로 사용자 인증할 수 있도록 Backend 작성"

    def authenticate(self, username=None, password=None):
        "username, password가 유효하면 User 반환, 그 외의 경우 None 반환"
        # usename 에 해당하는 member(legacy db object) 검색
        try:
            member = Member.objects.get(id=username)
        except ObjectDoesNotExist:
            return None
        
        # password가 유효하면 django user 반환
        if check_mysql_password(password, member.password):
            try:
                user = User.objects.get(username=username)
                if user.password != member.password:
                    user.password = member.password
                    user.save()
            except ObjectDoesNotExist:
                # 해당 member가 django user에 등록되어있지 않은 경우, 새로 등록
                user = User(username=username, password=member.password)
                user.save()
            return user
        return None
    
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except ObjectDoesNotExist:
            return None
