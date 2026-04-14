from django.db import models

class Artigo(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE)
    texto = models.TextField()

    def __str__(self):
        return self.texto
        


