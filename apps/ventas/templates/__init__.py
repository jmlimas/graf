from django.views.generic import TemplateView,ListView
from .models import Inventario 
from django.db.models import Count


class AreaView(TemplateView):
	template_name = 'area.html'

class DonaView(TemplateView):
	template_name ='dona.html'

class BarView(TemplateView):
	template_name ='bar.html'


class DatosdonaListView(TemplateView):
	template_name = 'ventas/datos_dona.html'	

	def get_context_data(self, **kwargs):
		context = super(DatosdonaListView, self).get_context_data(**kwargs)
		context['dato'] = Inventario.objects.all().values('categoria').annotate(total=Count('categoria')).order_by('total')
		print context['dato'] 
		return context
