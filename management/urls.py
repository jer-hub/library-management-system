from django.urls import path
from management.views import BookManagementView, DepartmentManagementView, UserManagementView

app_name = "management"

urlpatterns = [
   path("books/", BookManagementView.as_view(), name="book_management"),
   path("books/form_book_view/", BookManagementView.form_book_view, name="form_book_view"),
   path("books/book_list/", BookManagementView.back_to_book_list, name="book_list"),
   path("books/delete_book/", BookManagementView.delete_book, name="delete_book"),
]

urlpatterns += [
   path("departments/", DepartmentManagementView.as_view(), name="department_management"),
   path("departments/form_department_view/", DepartmentManagementView.form_department_view, name="form_department_view"),
   path("departments/department_list/", DepartmentManagementView.back_to_department_list, name="department_list"),
   path("departments/delete_department/", DepartmentManagementView.delete_department, name="delete_department"),
]

urlpatterns += [
   path("users/", UserManagementView.as_view(), name="user_management"),
   path("users/form_user_view/", UserManagementView.form_user_view, name="form_user_view"),
   path("users/user_list/", UserManagementView.back_to_user_list, name="user_list"),
   path("users/delete_user/", UserManagementView.delete_user, name="delete_user"),

]