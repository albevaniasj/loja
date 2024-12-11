from django.urls import path
from . import views

urlpatterns = [
    
    path('categorias/', views.categoria_list, name='categoria_list'),
    path('categoria/create/', views.categoria_create, name='categoria_create'),
    path('categoria/edit/<int:id>/', views.categoria_edit, name='categoria_edit'),
    path('categoria/confirm_delete/<int:id>/', views.categoria_delete, name='categoria_confirm_delete'),  

    
    path('produtos/', views.produto_list, name='produto_list'),
    path('produto/create/', views.produto_create, name='produto_create'),
    path('produto/edit/<int:id>/', views.produto_edit, name='produto_edit'),
    path('produto/confirm_delete/<int:id>/', views.produto_delete, name='produto_confirm_delete'),  

  
  
    path('clientes/', views.cliente_list, name='cliente_list'),
    path('cliente/create/', views.cliente_create, name='cliente_create'),
    path('cliente/edit/<int:id>/', views.cliente_edit, name='cliente_edit'),
    path('cliente/confirm_delete/<int:id>/', views.cliente_delete, name='cliente_confirm_delete'),  


    path('fornecedores/', views.fornecedor_list, name='fornecedor_list'),
    path('fornecedor/create/', views.fornecedor_create, name='fornecedor_create'),
    path('fornecedor/edit/<int:id>/', views.fornecedor_edit, name='fornecedor_edit'),
    path('fornecedor/confirm_delete/<int:id>/', views.fornecedor_delete, name='fornecedor_confirm_delete'),  


    path('pedidos/', views.pedido_list, name='pedido_list'),
    path('pedido/create/', views.pedido_create, name='pedido_create'),
    path('pedido/edit/<int:id>/', views.pedido_edit, name='pedido_edit'),
    path('pedido/confirm_delete/<int:id>/', views.pedido_delete, name='pedido_confirm_delete'),  

    
    path('pagamentos/', views.pagamento_list, name='pagamento_list'),
    path('pagamento/create/', views.pagamento_create, name='pagamento_create'),
    path('pagamento/edit/<int:id>/', views.pagamento_edit, name='pagamento_edit'),
    path('pagamento/confirm_delete/<int:id>/', views.pagamento_delete, name='pagamento_confirm_delete'),  
]
