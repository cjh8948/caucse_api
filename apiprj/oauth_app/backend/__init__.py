from apiprj.api1_app.models import Member
from apiprj.oauth_app.utils import check_mysql_password 
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class AuthBackend:
    def authenticate(self, username=None, password=None):
        member = Member.objects.get(id=username)
        if check_mysql_password(password, member.password):
            try:
                user = User.objects.get(username=username)
                if user.password != member.password:
                    user.password = member.password
                    user.save()
            except ObjectDoesNotExist:
                user = User(username=username, password=member.password)
                user.save()
            return user
        return None
    
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except ObjectDoesNotExist:
            return None
