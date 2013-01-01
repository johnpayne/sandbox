# -*- coding: utf-8 -*-
### required - do no delete
def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires
def index():
    form=SQLFORM.factory(
        Field('your_email',requires=IS_EMAIL()),
        Field('question',requires=IS_NOT_EMPTY()))
    if form.process().accepted:
        if mail.send(to='admin@example.com',
                  subject='from %s' % form.vars.your_email,
                  message = form.vars.question):
            response.flash = 'Thank you'
            response.js = "jQuery('#%s').hide()" % request.cid
        else:
            form.errors.your_email = "Unable to send the email"
    return dict(form=form, message=T("Start your search below:"))

    #return dict()

def error():
    return dict()

def results():
    if form.errors:
        response.flash = 'form has errors'
    elif request.vars.homeOwnership:
        query = db.marketplace6.id>request.vars.priorLoansStart&db.marketplace6
        db.thing.name.contains('m')&(db.thing.id==1)

                               
        grid=SQLFORM.grid(query)
    return locals()
    
