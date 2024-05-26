from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class BlogType(models.Model):
    name = models.CharField(_("Название типа"), max_length=50)

    def __str__(self):
        return self.name
    
    
class Blog(models.Model):

    title = models.CharField(_("Название"), max_length=50)
    cover = models.ImageField(_("Обложка"), upload_to='blog_covers/')
    type = models.ForeignKey(BlogType, verbose_name=_("Тип блога"), on_delete=models.CASCADE)
    subtitle = models.CharField(_("Заголовок"), max_length=512)
    first_description = models.TextField(_("Первое описание"))
    image = models.ImageField(_("Картинка"), upload_to='blog_content-images/')
    second_description = models.TextField(_("Второе описание"))
    
    
    class Meta:
        verbose_name = _("Blog")
        verbose_name_plural = _("Blogs")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Blog_detail", kwargs={"pk": self.pk})
    
    

class Group(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='group_images/')
    articles = models.ManyToManyField('Blog', related_name='groups', blank=True)
    tests = models.ManyToManyField('testsapp.Test', related_name='groups', blank=True)

    def __str__(self):
        return self.name