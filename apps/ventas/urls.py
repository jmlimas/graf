from django.conf.urls import url
from . import views 

urlpatterns = [
	url(r'^dona/$',views.DonaView.as_view(),name='gra_dona'),
	url(r'^area/$',views.AreaView.as_view(), name='gra_area'),
	url(r'^bar/$',views.BarView.as_view(), name='bar_area'),
	url(r'^datos/$', views.DatosdonaListView.as_view(),name='datos_dona') ,   
]
