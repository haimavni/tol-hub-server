# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------
import os

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    s = request.env.http_host
    subdomain = ''
    if '//' in s:
        s = s.split('//')[-1]
    if ':' in s:
        domain, port = s.split(':')
    else:
        domain, port = s, ''
    host = '.'.join(domain.split('.')[-2:])
    if port:
        host += ':' + port
    lst = domain.split('.')
    domain = lst[0]
    if domain in ('gbstories', 'tol'):
        idx = 0
        app = 'gbs'
    else:
        idx = 1
        app = domain
        
    subdomain = ''.join(lst[idx:-2])
    if subdomain == 'dev':
        app += '__dev'
    elif subdomain == 'test':
        app += '__test'
    elif app == 'gbs':
        app += '__www'

    fname = 'applications/{app}/static/aurelia/index-{app}.html'.format(app=app)
    idx = 'index-{app}'.format(app=app) if os.path.isfile(fname) else 'index'
    redirect("http://{host}/{app}/static/aurelia/{idx}.html".format(host=host, app=app, idx=idx))
    
def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


