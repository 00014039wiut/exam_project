from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'


class Product(models.Model):
    class RatingChoices(models.IntegerChoices):
        zero = 0
        one = 1
        two = 2
        three = 3
        four = 4
        five = 5

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    discount = models.IntegerField()
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RatingChoices.choices, default=RatingChoices.zero.value)

    @property
    def discounted_price(self):
        return self.price * (1 - (self.discount / 100))

    def __str__(self):
        return self.name


class Order(models.Model):
    name = models.CharField(max_length=100)

    phone_number = models.CharField(max_length=20)
    quantity = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    is_appropriate = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
