from django.db import models

# Create your models here.
class Food(models.Model):
    foodId=models.AutoField(primary_key=True)
    foodName=models.CharField(max_length=30)
    foodType=models.CharField(max_length=30)
    foodCategory=models.CharField(max_length=30)
    foodPrice=models.FloatField(max_length=30)
    class Meta:                                                       
        db_table='food501'

class Customer(models.Model):
    custName=models.CharField(max_length=30)
    custEmail=models.CharField(primary_key=True,max_length=30)
    custPassword=models.CharField(max_length=10)
    custContact=models.CharField(max_length=10)
    custAddress=models.CharField(max_length=30)
    class Meta:
        db_table='customer501'

class Admin(models.Model):
    adminName=models.CharField(primary_key=True,max_length=10)
    adminPassword=models.CharField(max_length=10)
    class Meta:
        db_table='admin501'

class Cart(models.Model):
    cartId=models.AutoField(primary_key=True)
    custEmail=models.CharField(max_length=30)
    foodId=models.CharField(max_length=10)
    foodName=models.CharField(max_length=30)
    foodPrice=models.FloatField()
    foodQuantity=models.CharField(max_length=10)
    totalPrice=models.FloatField()
    class Meta:
        db_table='cart501'

class Orders(models.Model):
    orderId=models.AutoField(primary_key=True)
    custEmail=models.CharField(max_length=30)
    orderDate=models.CharField(max_length=30)
    totalBill=models.FloatField()
    class Meta:
        db_table='order501'