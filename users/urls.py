
from django.conf.urls import url, include
from django.urls import path
from .views import (
    doctor_view,
    patient_view,
    patient_detail,
)
from . import views

urlpatterns = [
    # path('', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^main/$', views.main, name='main'),
    url(r'^login/$', views.login_user, name='login'),
    url(r'^registration/$', views.register_user, name='signup'),
    # path('patient/<int:pk>/',
    #       patient_detail.as_view(),
    #       name='patient_detail_urlpattern'),
    path('doctor/',
         doctor_view.as_view(),
         name='doctor_view_url'),

    path('patient/',
         patient_view.as_view(),
         name='patient_view_url'),

    path('patient/<int:pk>',
         patient_detail.as_view(),
         name='patient_detail_url'),

    path('', include('appointment.urls')),
# url(r'^patient/(?P<pk>\d+)/view/$', patient_view.as_view(), name='patient_view_url'),
]
