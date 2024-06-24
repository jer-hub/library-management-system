from typing import Any
from django.http import HttpResponse
from django.urls import reverse
from customuserauth.mixins import RedirectUnauthenticatedUsersMixin
from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView
from .models import Book, Department
from .forms import BookForm, DepartmentForm
from customuserauth.forms import RegisterForm
from django.core.paginator import Paginator
from render_block import render_block_to_string
from django.contrib.auth import get_user_model

# Create your views here.

User = get_user_model()

class BookManagementView(RedirectUnauthenticatedUsersMixin, TemplateView):
    template_name = "management/book_management.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        model = Book.objects.all()
        page_number = self.request.GET.get('page')
        return paginated_context(model, 25, page_number, "books","title")

    @classmethod
    def form_book_view(self, request):
        context = {}
        context["bookform"] = BookForm()
        context["button_name"] = "Add Book"
        context["button_css"] = "btn btn-success"
        instance = None
        if request.method == "GET":
            if request.GET['book_id']:
                instance = Book.objects.get(id=request.GET['book_id'])
                context['book_id'] = instance.id
                context["bookform"] = BookForm(instance=instance)
                context["button_name"] = "Update Book"
                context["button_css"] = "btn btn-info"

        if request.method == "POST":
            if request.POST['book_id']:
                instance = Book.objects.get(id=request.POST['book_id'])
            form = BookForm(request.POST, instance=instance)
            if form.is_valid:
                form.save()
            return redirect("management:book_management")
        return render(request, 'management/_partials/add_book_view.html', context)
    
    @classmethod
    def back_to_book_list(self, request):
        model = Book.objects.all().order_by('title')
        page_number = request.GET.get('page')
        context = paginated_context(model, 25, page_number, "books","title")
        return render(request, 'management/_partials/list_of_books.html', context)
    
    @classmethod
    def delete_book(self, request):
        checkedboxes = request.POST.getlist("box")
        Book.objects.filter(id__in=checkedboxes).delete()
        model = Book.objects.all().order_by('title')        
        page_number = request.GET.get('page')
        context = paginated_context(model, 25, page_number, "books","title")
        return render(request, 'management/_partials/list_of_books.html', context)

class DepartmentManagementView(RedirectUnauthenticatedUsersMixin, TemplateView):
    template_name = "management/dept_management.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        model = Department.objects.all()
        page_number = self.request.GET.get('page')
        return paginated_context(model, 25, page_number, "departments","name")

    @classmethod
    def form_department_view(self, request):
        context = {}
        context["departmentform"] = DepartmentForm()
        context["button_name"] = "Add Department"
        context["button_css"] = "btn btn-success"
        instance = None
        if request.method == "GET":
            if request.GET['department_id']:
                instance = Department.objects.get(id=request.GET['department_id'])
                context['department_id'] = instance.id
                context["departmentform"] = DepartmentForm(instance=instance)
                context["button_name"] = "Update"
                context["button_css"] = "btn btn-info"

        if request.method == "POST":
            if request.POST['department_id']:
                instance = Department.objects.get(id=request.POST['department_id'])
            form = DepartmentForm(request.POST, instance=instance)
            if form.is_valid:
                form.save()
            return redirect("management:department_management")
        return render(request, 'management/_partials/add_department_view.html', context)
    
    @classmethod
    def back_to_department_list(self, request):
        model = Department.objects.all().order_by('name')
        page_number = request.GET.get('page')
        context = paginated_context(model, 25, page_number, "departments","name")
        return render(request, 'management/_partials/list_of_departments.html', context)
    
    @classmethod
    def delete_department(self, request):
        checkedboxes = request.POST.getlist("box")
        Department.objects.filter(id__in=checkedboxes).delete()
        model = Department.objects.all().order_by('name')        
        page_number = request.GET.get('page')
        context = paginated_context(model, 25, page_number, "departments","name")
        return render(request, 'management/_partials/list_of_departments.html', context)
    
class UserManagementView(RedirectUnauthenticatedUsersMixin, TemplateView):
    template_name = "management/user_management.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        model = User.objects.all()
        page_number = self.request.GET.get('page')
        return paginated_context(model, 25, page_number, "users","email")

    @classmethod
    def form_user_view(self, request):
        context = {}
        context["userform"] = RegisterForm()
        context["button_name"] = "Add User"
        context["button_css"] = "btn btn-success"
        instance = None
        if request.method == "GET":
            if request.GET['user_id']:
                instance = User.objects.get(id=request.GET['user_id'])
                context['user_id'] = instance.id
                context["userform"] = RegisterForm(instance=instance)
                context["button_name"] = "Update"
                context["button_css"] = "btn btn-info"

        if request.method == "POST":
            if request.POST['user_id']:
                instance = User.objects.get(id=request.POST['user_id'])
            form = RegisterForm(request.POST, instance=instance)
            context["userform"] = form
            if form.is_valid():
                form.save()
                response = HttpResponse()
                response['HX-Redirect'] = reverse('management:user_management')
                return response
            else:
                context["userform_errors"] = form.errors
            
        return render(request, 'management/_partials/add_user_view.html', context)
    
    @classmethod
    def back_to_user_list(self, request):
        model = User.objects.all().order_by('email')
        page_number = request.GET.get('page')
        context = paginated_context(model, 25, page_number, "users","email")
        return render(request, 'management/_partials/list_of_users.html', context)
    
    @classmethod
    def delete_user(self, request):
        checkedboxes = request.POST.getlist("box")
        User.objects.filter(id__in=checkedboxes).delete()
        model = User.objects.all().order_by('email')        
        page_number = request.GET.get('page')
        context = paginated_context(model, 25, page_number, "users","email")
        return render(request, 'management/_partials/list_of_users.html', context)

def paginated_context(model, page,page_number, context_name, order_by):
        context = {}
        obj = model.order_by(order_by)
        paginator = Paginator(obj, page)
        context[context_name] = paginator.get_page(page_number)
        return context