from django.conf import settings
from django.conf.urls import url

from users.views import RetrieveUser, UpdateUser
from . import views

url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

urlpatterns = [
    url(r'^register/$', views.register, name="register"),
    url(r'^users/$', views.users, name="users"),
    url(r'^token-auth/$', views.token_auth, name="token_auth"),
    url(r'^get/$', RetrieveUser.as_view(), name="retrieve"),
    url(r'^update/$', UpdateUser.as_view(), name="update"),
]
