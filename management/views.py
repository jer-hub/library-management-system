from typing import Any, Dict
from django.http import HttpResponse
from django.urls import reverse
from customuserauth.mixins import Is_AdministratorMixin, RedirectUnauthenticatedUsersMixin
from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView
from .models import Book, Department
from .forms import BookForm, DepartmentForm
from customuserauth.forms import RegisterForm, UpdateUserForm
from django.core.paginator import Paginator
from django.contrib.auth import get_user_model
from render_block import render_block_to_string
from django_htmx.http import HttpResponseLocation
from django.db.models import Q
# Create your views here.

User = get_user_model()


class BookManagementView(Is_AdministratorMixin, TemplateView):
    template_name = "management/book_management.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        search = self.request.GET.get("search_book")
        page_number = self.request.GET.get("page")
        if search:
            books = Book.objects.filter(title__icontains=search)
        else:
            books = Book.objects.all()
        paginated_books = paginated_context(books, 25, page_number, "books", "title")
        context.update(paginated_books)
        context["search_book"] = search

        return context

    @classmethod
    def search_book_list(self, request):
        context = {}
        search = request.GET.get("search_book")
        model = Book.objects.all()
        if search:
            context["search_book"]=search
            model = Book.objects.filter(title__contains=search)
        page_number = request.GET.get("page_number")
        context = paginated_context(model, 25, page_number, "books", "title")
        html = render_block_to_string(
            "management/book_management.html", "books", context
        )
        return HttpResponse(html)

    @classmethod
    def form_book_view(self, request):
        context = {}
        context["bookform"] = BookForm()
        context["button_name"] = "Add Book"
        context["button_css"] = "btn btn-success"
        instance = None
        if request.method == "GET":
            if request.GET["book_id"]:
                instance = Book.objects.get(id=request.GET["book_id"])
                context["book_id"] = instance.id
                context["bookform"] = BookForm(instance=instance)
                context["button_name"] = "Update Book"
                context["button_css"] = "btn btn-info"

        if request.method == "POST":
            if request.POST["book_id"]:
                instance = Book.objects.get(id=request.POST["book_id"])
            form = BookForm(request.POST, instance=instance)
            if form.is_valid:
                form.save()
                return redirect(request.META.get("HTTP_REFERER", "/"))
        return render(request, "management/_partials/add_book_view.html", context)

    @classmethod
    def delete_book(self, request):
        checkedboxes = request.POST.getlist("box")
        Book.objects.filter(id__in=checkedboxes).delete()
        model = Book.objects.all().order_by("title")
        page_number = request.GET.get("page")
        context = paginated_context(model, 25, page_number, "books", "title")
        return render(request, "management/_partials/list_of_books.html", context)


class DepartmentManagementView(Is_AdministratorMixin, TemplateView):
    template_name = "management/dept_management.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        model = Department.objects.all()
        page_number = self.request.GET.get("page")
        return paginated_context(model, 25, page_number, "departments", "name")

    @classmethod
    def form_department_view(self, request):
        context = {}
        context["departmentform"] = DepartmentForm()
        context["button_name"] = "Add Department"
        context["button_css"] = "btn btn-success"
        instance = None
        if request.method == "GET":
            if request.GET["department_id"]:
                instance = Department.objects.get(id=request.GET["department_id"])
                context["department_id"] = instance.id
                context["departmentform"] = DepartmentForm(instance=instance)
                context["button_name"] = "Update"
                context["button_css"] = "btn btn-info"

        if request.method == "POST":
            if request.POST["department_id"]:
                instance = Department.objects.get(id=request.POST["department_id"])
            form = DepartmentForm(request.POST, instance=instance)
            if form.is_valid:
                form.save()
                return redirect(request.META.get("HTTP_REFERER", "/"))
        return render(request, "management/_partials/add_department_view.html", context)

    @classmethod
    def delete_department(self, request):
        checkedboxes = request.POST.getlist("box")
        Department.objects.filter(id__in=checkedboxes).delete()
        model = Department.objects.all().order_by("name")
        page_number = request.GET.get("page")
        context = paginated_context(model, 25, page_number, "departments", "name")
        return render(request, "management/_partials/list_of_departments.html", context)


class UserManagementView(Is_AdministratorMixin, TemplateView):
    template_name = "management/user_management.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        search = self.request.GET.get("search_user")
        page_number = self.request.GET.get("page")
        if search:
            users = User.objects.filter(Q(first_name__contains=search) | Q(last_name__contains=search))
        else:
            users = User.objects.all()
        paginated_users = paginated_context(users, 25, page_number, "users", "id")
        context.update(paginated_users)
        return context

    @classmethod
    def form_user_view(self, request):
        context = {}
        context["userform"] = RegisterForm()
        context["button_name"] = "Add User"
        context["button_css"] = "btn btn-success"
        instance = None
        if request.method == "GET":
            if request.GET["user_id"]:
                instance = User.objects.get(id=request.GET["user_id"])
                context["user_id"] = instance.id
                context["userform"] = UpdateUserForm(instance=instance)
                context["button_name"] = "Update"
                context["button_css"] = "btn btn-info"

        if request.method == "POST":
            if request.POST["user_id"]:
                instance = User.objects.get(id=request.POST["user_id"])
                form = UpdateUserForm(request.POST, instance=instance)
            else:
                form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                response = HttpResponseLocation(request.META.get("HTTP_REFERER", "/"))
                return response
            else:
                context["userform"] = form
                context["button_name"] = "Update"
                context["button_css"] = "btn btn-info"
                html = render_block_to_string(
                    "management/_partials/add_user_view.html", "userform", context
                )
                return HttpResponse(html)

        return render(request, "management/_partials/add_user_view.html", context)

    @classmethod
    def delete_user(self, request):
        context = {}
        checkedboxes = request.POST.getlist("box")
        User.objects.filter(id__in=checkedboxes).delete()
        page_number = request.GET.get("page")
        users = User.objects.all()
        paginated_users = paginated_context(users, 25, page_number, "users", "id")
        context.update(paginated_users)
        return render(request, "management/_partials/list_of_users.html", context)


def paginated_context(queryset, per_page, page_number, context_name, order_by):
    paginator = Paginator(queryset.order_by(order_by), per_page)
    page_obj = paginator.get_page(page_number)
    return {context_name: page_obj}


def back_page(request):
    return redirect(request.META.get("HTTP_REFERER", "/"))
