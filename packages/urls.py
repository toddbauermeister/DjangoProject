from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    url(r'^index/', views.index, name='index'),

    url(r'^$', views.login_user, name='login'),

    url(r'^login_user/$', views.login_user, name='login_user'),

    url(r'^logout/$', views.logout_user, name='logout_user'),

    url(r'^(?P<package_id>[0-9]+)/$', views.extra, name='extra'),

    url(r'^create_package/', views.create_package, name='create_package'),

    url(r'^(?P<package_id>[0-9]+)/cancel_package/(?P<student_id>[0-9]+)/$', views.cancel_package, name='cancel_package'),

    url(r'^update_package_status/', views.update_package_status, name='update_package_status'),

    url(r'^track_packages/', views.track_packages, name='track_packages'),
]