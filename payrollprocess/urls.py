from django.urls import path

from . import views


urlpatterns = [
    #path('',views.index, name= 'index'),
    path('', views.IndexView.as_view(),name = 'index'),
    path('addemployee',views.addemployee, name= 'addemployee'),
    path('editemployee',views.editemployee, name= 'editemployee'),
    path('deleteemployee',views.deleteemployee, name= 'deleteemployee'),
    path('downloadreport',views.downloadreport, name= 'downloadreport'),

    path('addemployeeform',views.AddEmployeeForm.as_view(), name= 'addemployeeform'),
]