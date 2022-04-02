from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views import View

from analytics.models import ClickEvent

from .forms import SubmitUrlForm
from .models import KirrURL
# Create your views here.

class HomeView(View):
	def get(self, request, *args, **kwargs):
		the_form = SubmitUrlForm()
		context = {
			"title": "Kirr.co",
			"form": the_form,
		}
		return render(request, "shortener/home.html", context)

	def post(self, request, *args, **kwargs):
		form = SubmitUrlForm(request.POST)
		context = {"form": form,
				   "title": "Kirr.co"}
		template = "shortener/home.html"
		if form.is_valid():
			print(form.cleaned_data)
			new_url = form.cleaned_data.get("url")
			if "https://" not in new_url and "http://" not in new_url:
				new_url = "https://" + new_url
			obj, created = KirrURL.objects.get_or_create(url=new_url)
			context = {
				"object": obj,
				"created": created,
			}
			if created:
				template = "shortener/success.html"	
			else:
				template = "shortener/already-exists.html"
		return render(request, template, context)

class URLRedirectView(View):
	def get(self, request, shortcode=None, *args, **kwargs):
		print(shortcode)
		qs = KirrURL.objects.filter(shortcode__iexact=shortcode)
		print(qs)
		if qs.count() != 1 and not qs.exists():
			raise Http404
		obj = qs.first()
		print(ClickEvent.objects.create_event(obj))
		print(obj.url)

		return HttpResponseRedirect(obj.url)

