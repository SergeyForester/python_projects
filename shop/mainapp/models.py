from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Категория товаров")

    def __str__(self):
        return self.name


class Sort(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Сорт продуктов")

    def __str__(self):
        return self.name


class Species(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name="Порода дерева")

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    price = models.DecimalField(verbose_name="Цена", decimal_places=2, max_digits=5)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория товара")
    sort = models.ForeignKey(Sort, on_delete=models.CASCADE, verbose_name="Сорт", null=True, blank=True)
    species = models.ForeignKey(Species, on_delete=models.CASCADE, verbose_name="Порода дерева")
    length = models.DecimalField(verbose_name="Длина", decimal_places=2, max_digits=3)
    quantity = models.PositiveIntegerField(verbose_name="Количество")
    rating = models.PositiveIntegerField(verbose_name="Рейтинг продукта", default=0)
    date = models.DateField(auto_now=True)
    photo = models.ImageField(verbose_name="Фото продукта")

    def __str__(self):
        return self.name


class Order(models.Model):
    PENDING = 'В процессе'
    COMPLETED = 'Завершен'

    CARD = 'Карта'
    PICKUP = 'Самовывоз'


    user = models.CharField(max_length=200)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default=PENDING)
    delivery_type = models.CharField(max_length=20, default=PICKUP)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    item = models.ForeignKey(Product, on_delete=models.CASCADE)

