from turtle import title
from typing import Any
from django.views.generic import TemplateView
from management.models import Book, Department
from management.views import paginated_context
from project.forms import FilterForm, SearchForm

class BookListView(TemplateView):
    template_name = "project/home.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        model = Book.objects.all().order_by("title")
        context["searchform"] = SearchForm()
        context["filterform"] = FilterForm()
        if self.request.GET.get("search") and self.request.GET.get("dept_select"):
            context['query'] = self.request.GET.get("search")
            context["dept_select"] = self.request.GET.get("dept_select")
            department = Department.objects.get(pk=self.request.GET.get("dept_select"))
            model = Book.objects.filter(department=department, title__contains=self.request.GET.get("search"))
        elif self.request.GET.get("search"):
            context['query'] = self.request.GET.get("search")
            model = Book.objects.filter(title__contains=self.request.GET.get("search"))
        elif self.request.GET.get("dept_select"):
            context["dept_select"] = self.request.GET.get("dept_select")
            department = Department.objects.get(pk=self.request.GET.get("dept_select"))
            model = Book.objects.filter(department=department)
        page_number = self.request.GET.get("page")
        context['books'] = paginated_context(model, 25, page_number, "books", "title")['books']
        return context
        