from django.urls import path
from management.views import BookManagementView, DepartmentManagementView, UserManagementView, back_page

app_name = "management"

urlpatterns = [
   path("books/", BookManagementView.as_view(), name="book_management"),
   path("books/form_book_view/", BookManagementView.form_book_view, name="form_book_view"),
   path("books/delete_book/", BookManagementView.delete_book, name="delete_book"),
]

urlpatterns += [
   path("departments/", DepartmentManagementView.as_view(), name="department_management"),
   path("departments/form_department_view/", DepartmentManagementView.form_department_view, name="form_department_view"),
   path("departments/delete_department/", DepartmentManagementView.delete_department, name="delete_department"),
]

urlpatterns += [
   path("users/", UserManagementView.as_view(), name="user_management"),
   path("users/form_user_view/", UserManagementView.form_user_view, name="form_user_view"),
   path("users/delete_user/", UserManagementView.delete_user, name="delete_user"),

]

urlpatterns += [
    path("back/", back_page, name="back_page")
]