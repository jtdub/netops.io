from django.http import HttpResponse
from django.template import loader


def index(request):
    """Render Home Page."""
    template = loader.get_template("home/base.html")
    context = {}
    return HttpResponse(template.render(context, request))
