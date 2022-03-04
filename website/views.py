from calendar import c
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["username"] = "佐藤"
        return ctxt

#aboutページ用のview
class AboutView(TemplateView):
    template_name = "about.html"