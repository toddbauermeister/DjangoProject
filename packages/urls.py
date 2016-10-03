from django.conf.urls import url
from . import views

app_name = 'packages'

urlpatterns = [


    url(r'^$', views.index, name='index'),

    url(r'^login_user/$', views.login_user, name='login_user'),

    url(r'^logout_user/$', views.logout_user, name='logout_user'),

    url(r'^(?P<package_id>[0-9]+)/$', views.extra, name='extra'),

    url(r'^create_package/$', views.create_package, name='create_package'),

    url(r'^update_package_status/', views.update_package_status, name='update_package_status'),

    url(r'^track_packages/', views.track_packages, name='track_packages'),

    url(r'^(?P<package_id>[0-9]+)/delete_package', views.delete_package, name='delete_package'),









]