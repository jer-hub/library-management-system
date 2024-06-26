from turtle import title
from typing import Any
from django.views.generic import TemplateView
from management.models import Book
from management.views import paginated_context

class BookListView(TemplateView):
    template_name = "project/home.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        model = Book.objects.all().order_by("title")
        if self.request.GET.get("search_book"):
            context["query"] = self.request.GET.get("search_book")
            model = Book.objects.filter(title__contains = self.request.GET.get("search_book"))
        page_number = self.request.GET.get("page")
        context = paginated_context(model, 25, page_number, "books", "title")
        return context
        