from django.http import HttpResponseRedirect
from django.conf import settings

DEFAULT_PATH = getattr(settings, "DEFAULT_REDIRECT_URL", "http://www.kirr.co")

def wildcard_redirect(request, path=None):
	new_url = DEFAULT_PATH
	if path is not None:
		new_url = DEFAULT_PATH + "/" + path
	return HttpResponseRedirect(new_url)