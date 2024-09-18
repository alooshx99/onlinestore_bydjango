from django.urls import path
from .views import CategoryListCreate, CategoryRetrieveUpdateDestroy, ProductListCreate, ProductRetrieveUpdateDestroy, TransactionListCreate, TransactionRetrieveUpdateDestroy
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('categories/', CategoryListCreate.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroy.as_view(), name='category-retrieve-update-destroy'),

    path('products/', ProductListCreate.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroy.as_view(), name='product-retrieve-update-destroy'),

    path('transactions/', TransactionListCreate.as_view(), name='transaction-list-create'),
    path('transactions/<int:pk>/', TransactionRetrieveUpdateDestroy.as_view(), name='transaction-retrieve-update-destroy'),

    path('auth/login/', obtain_auth_token, name='api_token_auth')
]