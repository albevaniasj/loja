
function confirmarExclusao(entidade, id) {
    const confirmar = confirm(`Tem certeza que deseja excluir este ${entidade}?`);
    if (confirmar) {
        window.location.href = `/${entidade}s/${id}/deletar/`;
    }
}


function editarCliente(id) {
    window.location.href = `/clientes/${id}/editar/`;
}


function editarFornecedor(id) {
    window.location.href = `/fornecedores/${id}/editar/`;
}


function editarPedido(id) {
    window.location.href = `/pedidos/${id}/editar/`;
}


function editarPagamento(id) {
    window.location.href = `/pagamentos/${id}/editar/`;
}


document.getElementById('pedido-form')?.addEventListener('submit', function(event) {
    const cliente = document.querySelector('#id_cliente').value;
    const produtos = document.querySelector('#id_produtos').value;
    const valorTotal = document.querySelector('#id_valor_total').value;
    if (!cliente || !produtos || valorTotal <= 0) {
        alert('Por favor, preencha os campos corretamente.');
        event.preventDefault();
    }
});


document.getElementById('pagamento-form')?.addEventListener('submit', function(event) {
    const valorPago = document.querySelector('#id_valor_pago').value;
    const pedido = document.querySelector('#id_pedido').value;
    if (valorPago <= 0 || !pedido) {
        alert('Por favor, preencha os campos corretamente.');
        event.preventDefault();
    }
});


function editarProduto(id) {
    window.location.href = `/produtos/${id}/editar/`;
}


function editarCategoria(id) {
    window.location.href = `/categorias/${id}/editar/`;
}


document.getElementById('cliente-form')?.addEventListener('submit', function(event) {
    const nomeCliente = document.querySelector('#id_nome').value;
    const endereco = document.querySelector('#id_endereco').value;
    if (!nomeCliente || !endereco) {
        alert('Por favor, preencha os campos corretamente.');
        event.preventDefault();
    }
});


document.getElementById('fornecedor-form')?.addEventListener('submit', function(event) {
    const nomeFornecedor = document.querySelector('#id_nome').value;
    const cnpj = document.querySelector('#id_cnpj').value;
    if (!nomeFornecedor || !cnpj) {
        alert('Por favor, preencha os campos corretamente.');
        event.preventDefault();
    }
});


document.querySelector('#confirmar-exclusao-categoria')?.addEventListener('click', function(event) {
    if (!confirm('Tem certeza que deseja excluir esta categoria?')) {
        event.preventDefault();
    }
});


document.querySelector('#confirmar-exclusao-produto')?.addEventListener('click', function(event) {
    if (!confirm('Tem certeza que deseja excluir este produto?')) {
        event.preventDefault();
    }
});


document.querySelector('#confirmar-exclusao-cliente')?.addEventListener('click', function(event) {
    if (!confirm('Tem certeza que deseja excluir este cliente?')) {
        event.preventDefault();
    }
});


document.querySelector('#confirmar-exclusao-fornecedor')?.addEventListener('click', function(event) {
    if (!confirm('Tem certeza que deseja excluir este fornecedor?')) {
        event.preventDefault();
    }
});


document.querySelector('#confirmar-exclusao-pedido')?.addEventListener('click', function(event) {
    if (!confirm('Tem certeza que deseja excluir este pedido?')) {
        event.preventDefault();
    }
});


document.querySelector('#confirmar-exclusao-pagamento')?.addEventListener('click', function(event) {
    if (!confirm('Tem certeza que deseja excluir este pagamento?')) {
        event.preventDefault();
    }
});
