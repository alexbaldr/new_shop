from django.db import models
# from django.contrib.auth import get_user_model
from django.utils.text import slugify
from authorization.models import User
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# User = get_user_model()


class Publishers(models.Model):
    name = models.CharField(max_length=50)
    info = models.TextField(blank=True)

    class Meta:
        verbose_name = "Издательство"
        verbose_name_plural = "Издательства"

    def __str__(self):
        return '{}'.format(self.name)

class Genres(models.Model):
    name = models.CharField(max_length=20,)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    def __str__(self):
        return '{}'.format(self.name)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Genres, self).save(*args, **kwargs)
    
class Authors(models.Model):

    name = models.CharField(max_length=100)
    country =models.CharField(max_length=50)
    bio = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to='images', blank=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return '{}'.format(self.name)


class Books(models.Model):
    name = models.CharField(max_length=100)
    author = models.ManyToManyField(Authors, related_name='authors',)
    genre = models.ManyToManyField(Genres, related_name='genres',)
    info = models.TextField(max_length=1000, blank=True)
    publisher = models.ForeignKey(Publishers, related_name='publisher', on_delete=models.SET_DEFAULT, default=1)
    # price = models.DecimalField(default=0)
    likes = GenericRelation('Like')

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = 'Книги'
    
    def __str__(self):
        return self.name

    @property
    def total_likes(self):
        return self.likes.count()

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    comment = models.ForeignKey('Comments', on_delete=models.CASCADE, blank=True, null=True)
    book = models.ForeignKey(Books, on_delete=models.CASCADE, blank=True, null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id  = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = "Лайк"
        verbose_name_plural = 'Лайки'


class Comments(models.Model):
    book =  models.ForeignKey(Books, on_delete=models.CASCADE,  related_name='comments_book')
    user = models.ForeignKey(User, related_name='comment', on_delete=models.SET_DEFAULT, default=1)
    text = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    likes = GenericRelation(Like)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = 'Коментарии'

    def __str__(self):
        return '{}: {}'.format(self.user, self.text)

    @property
    def total_likes(self):
        return self.likes.count()
