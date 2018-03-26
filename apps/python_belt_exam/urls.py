from django.conf.urls import url
from . import views           # From the current directoy, import views.py
urlpatterns = [
    url(r'^/?$', views.index), # Any request should be handled by the views.py's index method
    url(r'^sign_up', views.sign_up),
    url(r'^sign_in', views.sign_in),
    url(r'^dashboard', views.dash),
    url(r'^wish_items/(?P<id>\d+)/?$', views.add),
    url(r'^wish_items/create/?$', views.create),
    url(r'^create', views.submit),
    url(r'^steal/(?P<id>\d+)/?$', views.steal),
    url(r'^remove/(?P<id>\d+)/?$', views.remove),

    # url(r'^books/?$', views.books),
    # url(r'^books/add/?$', views.add),
    # url(r'^books/add/submit/?$', views.submit_review),
    # url(r'^books/add/review/?$', views.add_review),
    # url(r'^books/(?P<id>\d+)/?$', views.specific),
    url(r'^logout', views.logout),
    # url(r'^delete/(?P<id>\d+)$', views.delete),
	# url(r'^users/(?P<id>\d+)$', views.user_profile),
    # url(r'^new', views.add),
    # url(r'^submit_add', views.submit_add),
    # url(r'^(?P<id>\d+)/?$', views.show), # question mark means the question mark may or may not be there
    # url(r'^(?P<id>\d+)/?/edit$', views.edit),
    # url(r'^(?P<id>\d+)/submit_edit/?$', views.submit_edit),
    # url(r'^(?P<id>\d+)/submit_delete/?$', views.submit_delete),
    # url(r'^result', views.result),
    # url(r'^new$', views.reset), #r'^(?P<id>\d+)$
]
