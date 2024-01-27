from django.db import models

class User(models.Model):
    surname = models.CharField(max_length = 100)
    name = models.CharField(max_length = 100)
    patronymic = models.CharField(max_length = 100)
    email = models.EmailField(max_length=254)
    telephone = models.CharField(max_length = 20)
    country = models.CharField(max_length = 100)
    region = models.CharField(max_length = 100)
    destrict = models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)
    street = models.CharField(max_length = 100)
    home = models.CharField(max_length = 100)
    liter = models.CharField(max_length = 3)
    flat = models.CharField(max_length = 4)
    create_at = models.DateField(auto_now_add = True)

    def __str__(self):
        return f'Фамилия: {self.surname}\nИмя: {self.name}\nОтчество: {self.patronymic}\nEmail: {self.email}\nДата регистрации: {self.create_at}'

class Product(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.DecimalField(max_digits = 8, decimal_places=0)
    create_at = models.DateField(auto_now_add = True)

    def __str__(self):
        return f'Наименование: {self.name}\nОписание: {self.description}\nЦена: {self.price}\nКоличество: {self.quantity}\nДата создания: {self.create_at}'

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)
    count_product = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'Сумма: {self.total_price}\nДата создания: {self.date_ordered}'

