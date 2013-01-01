# -*- coding: utf-8 -*-
### required - do no delete
def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires
def index():
    return dict(message=T("index view"))

def error():
    return dict()

def test():
    if request.vars.visitor_name:
        session.visitor_name = request.vars.visitor_name
        redirect(URL('test2'))
    return dict()

def test2():
    grid=SQLFORM.grid(db.marketplace6, user_signature=False)
    return locals()
