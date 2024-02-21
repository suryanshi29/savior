from django.contrib import admin
from django.template.context_processors import static
from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path,include
from .import settings
from django.conf.urls.static import static
urlpatterns = [

    path('test',views.test,name="test"),
    path('display',views.display,name="display"),
    path('delete/<int:id>',views.delete,name="delete"),
    path('update/<int:id>',views.update,name="update"),

    path('update/updaterecord/<int:id>', views.updaterecord, name="updaterecord"),

    path('login',views.login,name="login"),
    path('',views.home,name="home"),
    path('home.html',views.home, name="home"),
    path('hospital',views.hospital,name="hospital"),
    path('emergencyfrom',views.emergencyfrom,name="emergencyfrom"),
    path('hospage',views.hospage,name="hospage"),
    path('patient',views.patient,name="patient"),
    path('hospital_list',views.hospital_list,name="hospital_list"),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

