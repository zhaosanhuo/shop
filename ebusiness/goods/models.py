from django.db import models

# Create your models here.
#用户
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.username


#商品
class Goods(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    picture = models.FileField(upload_to='./upload/')
    desc = models.TextField()

    def __str__(self):
        return self.name


#收货地址
class Address(models.Model):
    user = models.ForeignKey(User, on_delete=False)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return self.address


#总订单
class Orders(models.Model):
    address = models.ForeignKey(Address, on_delete=False)
    create_time = models.DateTimeField(auto_now=True)
    status = models.BooleanField()

    def __str__(self):
        return self.create_time


#单个订单
class Orede(models.Model):
    order = models.ForeignKey(Orders, on_delete=False)
    user = models.ForeignKey(User, on_delete=False)
    goods = models.ForeignKey(Goods, on_delete=False)
    count = models.IntegerField()
