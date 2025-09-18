from django.db import models
from django.contrib.auth.models import User

class CuotaMensual(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cuotas')
    fecha_inicio = models.DateField()
    fecha_vencimiento = models.DateField()
    monto = models.DecimalField(max_digits=8, decimal_places=2)
    pagado = models.BooleanField(default=False)

    class Meta:
        verbose_name = "cuota mensual"
        verbose_name_plural = "cuotas mensuales"
        ordering = ['-fecha_inicio']

    def __str__(self):
        return f"Cuota de {self.user.username} ({self.fecha_inicio.strftime('%m/%Y')})"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client_profile')
    full_name = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    bio = models.TextField(blank=True)
    link = models.URLField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    is_client = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username