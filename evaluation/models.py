from turtle import title
from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.title} from {self.year}'


class ZipCode(models.Model):
    d_codigo = models.CharField(max_length=200)
    d_asenta = models.CharField(max_length=200)
    d_tipo_asenta = models.CharField(max_length=200)
    D_mnpio = models.CharField(max_length=200)
    d_estado = models.CharField(max_length=200)
    d_ciudad = models.CharField(max_length=200)
    d_CP = models.CharField(max_length=200)
    c_estado = models.CharField(max_length=200)
    c_oficina = models.CharField(max_length=200)
    c_CP = models.CharField(null=True, blank=True, max_length=200)
    c_tipo_asenta = models.CharField(max_length=200)
    c_mnpio = models.CharField(max_length=200)
    id_asenta_cpcons = models.CharField(max_length=200)
    d_zona = models.CharField(max_length=200)
    c_cve_ciudad = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f'{self.d_estado} => {self.D_mnpio} => {self.d_asenta} => {self.d_codigo}'
