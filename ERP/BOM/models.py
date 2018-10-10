from django.db import models

class Setor(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
	    return self.name

class Empregado(models.Model):
    nome = models.CharField(max_length=30)
    id_setor = models.ForeignKey(Setor, on_delete=models.CASCADE)
    usuario = models.CharField(max_length=8)
    senha = models.CharField(max_length=8)

    def __str__(self):
        return self.nome
    
class Fornecedor(models.Model):
    nameforn = models.CharField(max_length=30)
    cnpj = models.CharField(max_length=14)

    def __str__(self):
        return self.nameforn

class Matp(models.Model):
    namemp = models.CharField(max_length=30)
    id_fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)

    def __str__(self):
        return self.namemp

class Produto(models.Model):
    namep = models.CharField(max_length=30)
    matps = models.ManyToManyField(Matp)

    def __str__(self):
        return self.namep