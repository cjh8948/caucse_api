#-*- coding:utf-8 -*-
"동네API exceptions"

NotImplementedYet = NotImplementedError

class RequiredParameterDoesNotExist(Exception):
    "필수 입력 파라미터가 없는 경우" 
    pass

class DatabaseTableDoesNotExist(Exception):
    "존재하지 않는 django model을 eval 하려는 경우"
    pass

class PermissionDenied(Exception):
    "권한이 없는 작업을 시도하는 경우"
    pass

class AuthError(Exception):
    "인증 과정에서의 에러"
    pass

