from django.http import HttpResponse
from functools import wraps
import json

def api_exception(view_func):
    def handle_exception(request, *arg, **keywords):
        try:
            return view_func(request, *arg, **keywords)
        except Exception as e:
            return HttpResponse(json.dumps({'status': 'error',
                                            'type': str(type(e)),
                                            'message': str(e)}))
    
    return wraps(view_func)(handle_exception)

