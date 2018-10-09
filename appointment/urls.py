from django.conf.urls import url
from django.urls import path
from .views import (
    patient_detail,
    doctor_detail,
    patient_view,
)
from . import views


urlpatterns = [
    # path('', views.post_list, name='post_list'),
    # path('post/', views.post_list, name='post_list'),
    # path('/<int:pk>', views.post_detail, name='post_detail'),
    # make an appointment with doctor

    url(r'^patient/(?P<pk>\d+)/appointment/$', views.make_appointment, name='make_appointment_url'),
    url(r'^patient/(?P<pk>\d+)/view/$', patient_view.as_view(), name='patient_view_url'),
    path('patient/<int:pk>/',
         patient_detail.as_view(),
         name='patient_detail_urlpattern'),

    url(r'^doctor/(?P<pk>\d+)/prescription/$', views.make_prescription, name='make_prescription_url'),
    url(r'^doctor/(?P<doc_pk>\d+)/prescription/(?P<pat_pk>\d+)/$', views.prescribe, name='prescribe_url'),
    path('doctor/<int:pk>/',
         doctor_detail.as_view(),
         name='doctor_detail_urlpattern'),
    # # find the current dosage
    # path('patient/<int:pk>', views.patient_prescription, name='make_appointment'),# how to find comment for post
    # path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    # url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    # url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    # url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    # url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    # url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    # url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
]