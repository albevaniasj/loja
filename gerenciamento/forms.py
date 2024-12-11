from django import forms
from .models import Categoria, Produto, Cliente, Fornecedor, Pedido, Pagamento


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'estoque', 'categoria']


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'telefone']


class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['nome', 'email', 'telefone']


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'produtos', 'quantidade', 'status']


class PagamentoForm(forms.ModelForm):
    class Meta:
        model = Pagamento
        fields = ['cliente', 'pedido', 'data_pagamento', 'valor_pago']  