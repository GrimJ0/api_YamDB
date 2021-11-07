from django.contrib.auth.models import AbstractUser, BaseUserManager

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """

        user = self.model(
            email=email,
            **kwargs
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **kwargs):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            is_staff=True,
            is_superuser=True,
            **kwargs
        )
        user.set_password(password)
        user.save()
        return user



class User(AbstractUser):
    """Расширение модели пользователя."""
    ROLE_CHOICES = (
        ('user', 'user'),
        ('moderator', 'moderator'),
        ('admin', 'admin'),
    )

    username = models.CharField(max_length=200, unique=True)
    bio = models.TextField(max_length=200, blank=True)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = MyUserManager()



class Category(models.Model):
    """Список категорий."""
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    """Жанры произведений."""
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField(verbose_name="Год выпуска", null=True, blank=True)
    description = models.TextField()
    rating = models.IntegerField(null=True, blank=True)
    genre = models.ManyToManyField(Genre)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)


class Review(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    score = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True)
    title = models.ForeignKey(Title, on_delete=models.CASCADE, related_name='reviews')


class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True)

    def __str__(self):
        return self.text
