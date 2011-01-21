#! -*- coding: utf8 -*- 
from django.core import urlresolvers
from django.contrib.admindocs import utils
from django.contrib.admindocs.views import (get_root_path, 
                                            missing_docutils_page,
                                            extract_views_from_urlpatterns,
                                            simplify_regex)
from django.http import Http404
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.utils.importlib import import_module
from django.utils.translation import ugettext as _
import urls as api1_urls
import apiprj.oauth_app.urls as oauth_urls

def view_index(request):
    if not utils.docutils_is_available:
        return missing_docutils_page(request)

    view_dict = {}
    view_functions = extract_views_from_urlpatterns(api1_urls.urlpatterns) + \
                     extract_views_from_urlpatterns(oauth_urls.urlpatterns)

    for (func, regex) in view_functions:
        view = {'name': getattr(func, '__name__', func.__class__.__name__),
                'module': func.__module__,
                'url': simplify_regex(regex)}
        if view['name'] in ['authorize', 'access_token', 'request_token']:
            view['url'] = "/oauth%s"%view['url']
        view['group'] = view['url'].split('/')[1]

        if view_dict.has_key(view['group']):
            view_dict[view['group']].append(view)
        else:
            view_dict[view['group']] = [view]
    
    return render_to_response('doc/view_index.tpl', {
        'root_path': get_root_path(),
        'view_dict': view_dict
    }, context_instance=RequestContext(request))
    
def view_detail(request, view):
    if not utils.docutils_is_available:
        return missing_docutils_page(request)

    mod, func = urlresolvers.get_mod_func(view)
    try:
        view_func = getattr(import_module(mod), func)
    except (ImportError, AttributeError):
        raise Http404
    title, body, metadata = utils.parse_docstring(view_func.__doc__)
    if title:
        title = utils.parse_rst(title, 'view', _('view:') + view)
    if body:
        body = utils.parse_rst(body, 'view', _('view:') + view)
    for key in metadata:
        metadata[key] = utils.parse_rst(metadata[key], 'model', _('view:') + view)
    
    name = view.split('.')[-1].replace('_','/')
    return render_to_response('doc/view_detail.tpl', {
        'root_path': get_root_path(),
        'name': name,
        'summary': title,
        'body': body,
        'meta': metadata,
    }, context_instance=RequestContext(request))