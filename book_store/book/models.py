from django.db import models
from django.urls import reverse




class Category(models.Model):
    title = models.CharField(max_length=150)


    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'



class Subcategory(models.Model):
    category = models.ForeignKey(Category, related_name='categorylangs', on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'


class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)
    subcategory = models.ManyToManyField
    title = models.CharField(max_length=10000)
    slug = models.SlugField(unique=True)
    price = models.FloatField()
    description = models.TextField()
    аuthor = models.CharField(max_length=10000, blank=True)
    number_pages = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='image')
    create_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('book', kwargs={"pk": self.pk})


    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Images(models.Model):
    product = models.ForeignKey(Book,on_delete=models.CASCADE)
    title = models.CharField(max_length=50,blank=True)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title


class Rating(models.Model):
    post = models.ForeignKey(Book, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)


    def __str__(self):
        return str(self.pk)