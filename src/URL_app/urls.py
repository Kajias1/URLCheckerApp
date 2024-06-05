from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("update", views.check_all),
    path("delete_url/<int:id>", views.delete_url_record, name="delete_url"),
    path("check_url/<int:id>", views.check_url_record, name="check_url"),
]