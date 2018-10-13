from django.db import models

# Create your models here.
class Cliente(models.Model):
	rut = models.CharField(max_Length=10)
	nombre = models.CharField(max_Length=30)
	apellido = models.CharField(max_Length=30)
	fechaNacimiento = models.DataField()
	op=(('M','Masculino'),('F','Femenino'))
	Sexo = models.CharField(max_Length=1, choices=op,default='M')

	def nombreCompleto(self):
		cadena = "{0} {1}"
		return cadena.format(self.nombre,self.apellido)

	def __str__(self):
		return self.nombreCompleto()


class Cupon(models.Model):
	codigo = models.PositiveSmallIntegerField()
	nombre = models.CharField(max_Length=15)
	estado = models.BooleanField(default=True)

	def __str__(self):
		return "{0} {1}".format(self.codigo, self.nombre)


class AsignacionCupones(models.Model):
	cliente = models.ForeignKey(Cliente, null = False, blank = False, on_delete=models.CASCADE)
	cupon = models.ForeignKey(Cupon, null = False, blank = False, on_delete=models.CASCADE)
    fechaAsignacion = models.DateTimeField(auto_now_add = True)

    def __str__(self):
    	cadena = "{0} => {1}"
    	return cadena.format(self.Cliente, self.Cupon.nombre)