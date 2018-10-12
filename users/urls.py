
from django.conf.urls import url, include
from django.urls import path
from .views import (
    DoctorView,
    PatientView,
    PatientDetail,
)
from . import views

urlpatterns = [
    url(r'^login/$', views.login_user, name='login'),
    url(r'^signup/$', views.register_user, name='signup'),

    path('doctor/',
         DoctorView.as_view(),
         name='doctor_view_url'),

    path('patient/',
         PatientView.as_view(),
         name='patient_view_url'),

    path('patient/<int:pk>',
         PatientDetail.as_view(),
         name='patient_detail_url'),

    path('', include('appointment.urls')),
]
