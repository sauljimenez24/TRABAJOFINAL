from django.db import models

# Create your models here.
class AlumnoT(models.Model):
    apaterno=models.CharField(max_length=50,verbose_name="Apellido Paterno")
    amaterno=models.CharField(max_length=50,verbose_name="Apellido Materno")
    nombre=models.CharField(max_length=50,verbose_name="nombre")
    fecha_nacimiento=models.DateField(verbose_name='fecha de nacimiento', null=False,blank=False)
    fecha_ingreso=models.DateField(verbose_name='Fecha de ingreso', null=False,blank=False)

class Frase(models.Model):
    comentario=models.TextField(verbose_name='comentrio', max_length=400)
    Alumno_fk=models.ForeignKey(AlumnoT, on_delete=models.CASCADE)
    
class Meta:
    db_table="Alumnos"
    verbose_name="Alumno"
    verbose_name_plural="Alumnos"

def _str_(self)-> str:
    return self.nombre

class Frase(models.Model):
    comentario=models.TextField(verbose_name='comentario', max_length=400)
    Alumno_fk=models.ForeignKey(AlumnoT, on_delete=models.CASCADE)

class Meta:
    verbose_name="frase"
    verbose_name_plural="frases"