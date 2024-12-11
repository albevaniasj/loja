from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField(null=True, blank=True)  
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)  

    def __str__(self):
        return self.nome

class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)  
    telefone = models.CharField(max_length=15, blank=True, null=True)  

    def __str__(self):
        return self.nome

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    produtos = models.ManyToManyField(Produto)
    quantidade = models.PositiveIntegerField()  
    status = models.CharField(max_length=50)  

    def __str__(self):
        return f"Pedido {self.id} - {self.cliente.nome}"

class Pagamento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    data_pagamento = models.DateTimeField()
    valor_pago = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Pagamento para Pedido {self.pedido.id}"
