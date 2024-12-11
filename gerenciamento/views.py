from django.shortcuts import render, redirect, get_object_or_404
from .models import Categoria, Produto, Cliente, Fornecedor, Pedido, Pagamento
from .forms import CategoriaForm, ProdutoForm, ClienteForm, FornecedorForm, PedidoForm, PagamentoForm
from django.shortcuts import render

def base(request):
    return render(request, 'gerenciamento/base.html')


def categoria_list(request):
    categorias = Categoria.objects.all()
    return render(request, 'gerenciamento/categoria_list.html', {'categorias': categorias})

def categoria_create(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categoria_list')
    else:
        form = CategoriaForm()
    return render(request, 'gerenciamento/categoria_form.html', {'form': form})

def categoria_edit(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('categoria_list')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'gerenciamento/categoria_form.html', {'form': form})

def categoria_delete(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    categoria.delete()
    return redirect('categoria_list')



def produto_list(request):
    produtos = Produto.objects.all()
    return render(request, 'gerenciamento/produto_list.html', {'produtos': produtos})

def produto_create(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produto_list')
    else:
        form = ProdutoForm()
    return render(request, 'gerenciamento/produto_form.html', {'form': form})

def produto_edit(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('produto_list')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'gerenciamento/produto_form.html', {'form': form})

def produto_delete(request, id):
    produto = get_object_or_404(Produto, id=id)
    produto.delete()
    return redirect('produto_list')



def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'gerenciamento/cliente_list.html', {'clientes': clientes})

def cliente_create(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm()
    return render(request, 'gerenciamento/cliente_form.html', {'form': form})

def cliente_edit(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'gerenciamento/cliente_form.html', {'form': form})

def cliente_delete(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    cliente.delete()
    return redirect('cliente_list')



def fornecedor_list(request):
    fornecedores = Fornecedor.objects.all()
    return render(request, 'gerenciamento/fornecedor_list.html', {'fornecedores': fornecedores})

def fornecedor_create(request):
    if request.method == 'POST':
        form = FornecedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fornecedor_list')
    else:
        form = FornecedorForm()
    return render(request, 'gerenciamento/fornecedor_form.html', {'form': form})

def fornecedor_edit(request, id):
    fornecedor = get_object_or_404(Fornecedor, id=id)
    if request.method == 'POST':
        form = FornecedorForm(request.POST, instance=fornecedor)
        if form.is_valid():
            form.save()
            return redirect('fornecedor_list')
    else:
        form = FornecedorForm(instance=fornecedor)
    return render(request, 'gerenciamento/fornecedor_form.html', {'form': form})

def fornecedor_delete(request, id):
    fornecedor = get_object_or_404(Fornecedor, id=id)
    fornecedor.delete()
    return redirect('fornecedor_list')



def pedido_list(request):
    pedidos = Pedido.objects.all()  
    if request.method == 'POST':  
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pedido_list')  
    else:
        form = PedidoForm()  
    
    return render(request, 'gerenciamento/pedido_form.html', {'form': form, 'pedidos': pedidos})

def pedido_create(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pedido_list')  
    else:
        form = PedidoForm()
    return render(request, 'gerenciamento/pedido_form.html', {'form': form})

def pedido_edit(request, id):
    pedido = get_object_or_404(Pedido, id=id)
    if request.method == 'POST':
        form = PedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            return redirect('pedido_list')
    else:
        form = PedidoForm(instance=pedido)
    return render(request, 'gerenciamento/pedido_form.html', {'form': form})

def pedido_delete(request, id):
    pedido = get_object_or_404(Pedido, id=id)
    pedido.delete()
    return redirect('pedido_list')



def pagamento_list(request):
    pagamentos = Pagamento.objects.all()
    return render(request, 'gerenciamento/pagamento_list.html', {'pagamentos': pagamentos})

def pagamento_create(request):
    if request.method == 'POST':
        form = PagamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pagamento_list')
    else:
        form = PagamentoForm()
    return render(request, 'gerenciamento/pagamento_form.html', {'form': form})

def pagamento_edit(request, id):
    pagamento = get_object_or_404(Pagamento, id=id)
    if request.method == 'POST':
        form = PagamentoForm(request.POST, instance=pagamento)
        if form.is_valid():
            form.save()
            return redirect('pagamento_list')
    else:
        form = PagamentoForm(instance=pagamento)
    return render(request, 'gerenciamento/pagamento_form.html', {'form': form})

def pagamento_delete(request, id):
    pagamento = get_object_or_404(Pagamento, id=id)
    pagamento.delete()
    return redirect('pagamento_list')
