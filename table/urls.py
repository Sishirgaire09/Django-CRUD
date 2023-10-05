from django.urls import path ,include 
from . import views

urlpatterns = [
    path("<int:id>/", views.table_form , name = 'table-form'), #get anf post req. for update operation
    path("", views.table_form , name = 'table-form'), #get anf post req. for insert operation 
    path("product_list/", views.product_list , name = 'table-list'), #fet req to retrieve and display all records
    path("table_delete/<int:id>/", views.table_delete , name = 'table-delete'),

]