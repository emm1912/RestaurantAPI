from django.urls import path
from . import views

urlpatterns = [
    path('tables/', views.tables_list),
    path('tables/<int:id>', views.tables_item),

    
]