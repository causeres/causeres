from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self):
        ctxt=super().get_context_data()
        ctxt["username"]="春風"
        return ctxt

class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self):
        ctxt=super().get_context_data()
        ctxt["num"]=1000
        ctxt["mylist"]=[
            "test1",
            "test2",
            "test3",
            "test4",
            "test5"
        ]
        return ctxt

# Create your views here.
