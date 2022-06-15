import uuid

from django.db import models
from django.urls import reverse


class Books(models.Model):
    title_russian = models.CharField(max_length=150, help_text='Введите название на русском языке')
    title_foreign = models.CharField(max_length=150, help_text='Введите название на иностранном языке',
                                     null=True, blank=True)

    description = models.TextField(max_length=1000, help_text='Введите описание книги')
    genre = models.ManyToManyField('Genre')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    cost_daily = models.DecimalField(max_digits=8, decimal_places=2)
    amount_ex = models.IntegerField()
    author = models.ManyToManyField('Author')
    date_registration = models.DateTimeField()
    number_of_pages = models.IntegerField()
    year_of_publication = models.DateField()
    pubdate = models.DateTimeField()
    image = models.ManyToManyField('ImageBook')

    def __str__(self):
        return self.title_russian

    def get_absolute_url(self):
        return reverse('books-detail', args=[str(self.id)])

    class Meta:
        ordering = ["title_russian", "-pubdate"]
        verbose_name_plural = 'Книги'


class Author(models.Model):
    surname = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    second_name = models.CharField(max_length=150, null=True, blank=True)
    image = models.ManyToManyField('ImageAuthor')

#    @property
    def __str__(self):
        return self.surname

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    class Meta:
        ordering = ["surname"]
        verbose_name_plural = 'Авторы'


class Customers(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(unique=True)
    date_of_birthday = models.DateField(null=True, blank=True)
    ages = models.IntegerField()

    option = (
        ('Male', 'Man'),
        ('Female', 'Woman'),
    )
    sex = models.CharField(max_length=7, choices=option, default='Male')
    number_of_passport = models.CharField(max_length=9, unique=True)
    place = models.CharField(max_length=30)

#    def __str__(self):
#        return self.name

    class Meta:
         verbose_name_plural = 'Пользователи'


class Genre(models.Model):
    name = models.CharField(max_length=50, help_text='Введите', unique=True)

    def __str__(self):
        return self.name
    class Meta:
         verbose_name_plural = 'Жанры'


class ImageAuthor(models.Model):
    title = models.CharField(max_length=20, unique=True)
    image = models.ImageField()

    def __str__(self):
        return self.title


    class Meta:
         verbose_name_plural = 'Изображения авторов'


class ImageBook(models.Model):
    title = models.CharField(max_length=20, unique=True)
    image = models.ImageField()


    def __str__(self):
        return self.title


    class Meta:
         verbose_name_plural = 'Изображения книг'


class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    book = models.ForeignKey(Books, on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = [
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    ]
    status = models.CharField(max_length=10, choices=LOAN_STATUS, blank=True, default='m')

    class Meta:
        ordering = ["due_back"]
        verbose_name_plural = 'Экземпляры книг'

    def __str__(self):
        return '%s (%s)' % (self.id, self.book.title_russian)
