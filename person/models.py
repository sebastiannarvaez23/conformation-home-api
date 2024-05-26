from django.db import models

# Create your models here.
class TypeIdentification(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="id")
    name_short = models.CharField(max_length=2, verbose_name="Nombre Corto")
    name_long = models.CharField(max_length=100, verbose_name="Nombre Largo")

class Person(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="id")
    is_head_household = models.BooleanField(verbose_name="Es cabeza de hogar")
    first_name = models.CharField(max_length=200, verbose_name="Primer Nombre")
    second_name = models.CharField(max_length=200, verbose_name="Segundo Nombre", blank=True, null=True)
    first_last_name = models.CharField(max_length=200, verbose_name="Primer Apellido")
    second_last_name = models.CharField(max_length=200, verbose_name="Segundo Apellido", blank=True, null=True)
    date_birth = models.DateField(verbose_name="Fecha de Nacimiento")
    num_identification = models.CharField(max_length=200, unique=True, verbose_name="Número Identificación")
    type_identification = models.ForeignKey(TypeIdentification, on_delete=models.DO_NOTHING, verbose_name="Tipo Identificación")