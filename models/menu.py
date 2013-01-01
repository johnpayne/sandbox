response.title = settings.title
response.subtitle = settings.subtitle
response.meta.author = '%(author)s <%(author_email)s>' % settings
response.meta.keywords = settings.keywords
response.meta.description = settings.description
response.menu = [
(T('Index'),URL('default','index')==URL(),URL('default','index'),[]),
(T('Test'),URL('default','test')==URL(),URL('default','test'),[]),
(T('Search'),URL('search','index')==URL(),URL('search','index'),[]),
]
