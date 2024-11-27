from django.urls import path
from . import views
from .views import ExpenditureCreateView
urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('task-list/', views.taskList, name="task-list"),
    path('matrix-list/', views.matrixList, name="matrix-list"),
    path('customer-list/', views.customerList, name="customer-list"),
    #path('customer-list/', views.matrixList, name="matrix-list"),
    path('task-detail/<str:pk>/', views.taskDetail, name="task-Detail"),
    path('task-update/<str:pk>/', views.taskUpdate, name="task-update"),
    path('task-create/', views.taskCreate, name="task-Create"),
    path('matrix-create/', views.martixCreate, name="matrix-Create"),
    path('customer-create/', views.customerCreate, name="cusromer-Create"),
    path('expenditures/', ExpenditureCreateView.as_view(), name='expenditure-create'),

    path('task-delete/', views.taskDelete, name="task-delete"),

  ]