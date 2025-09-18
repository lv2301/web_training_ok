from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify



class Page(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)  # nuevo campo
    content = RichTextField(verbose_name="Contenido")
    image = models.ImageField(upload_to='pages_images/', blank=True, null=True)
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    price = models.DecimalField("Precio", max_digits=8, decimal_places=2, null=True, blank=True)
    mostrar_precio = models.BooleanField("¿Mostrar precio públicamente?", default=False)


    class Meta:
        verbose_name = "página"
        verbose_name_plural = "páginas"
        ordering = ['order', 'title']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Page, self).save(*args, **kwargs)

    def __str__(self):
        return self.title