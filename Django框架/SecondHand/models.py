# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Comments(models.Model):
    product = models.OneToOneField('Productname', models.DO_NOTHING, db_column='Product_id', primary_key=True)  # Field name made lowercase.
    product_comments = models.CharField(db_column='Product_comments', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'comments'


class Favorite(models.Model):
    user = models.OneToOneField('User', models.DO_NOTHING, primary_key=True)
    product = models.ForeignKey('Productname', models.DO_NOTHING, db_column='Product_id')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'favorite'
        unique_together = (('user', 'product'),)


class Order(models.Model):
    user = models.OneToOneField('User', models.DO_NOTHING, primary_key=True)
    product = models.ForeignKey('Productname', models.DO_NOTHING, db_column='Product_id')  # Field name made lowercase.
    order_status = models.CharField(db_column='Order_status', max_length=10)  # Field name made lowercase.
    order_operation = models.CharField(db_column='Order_operation', max_length=100, blank=True, null=True)  # Field name made lowercase.
    product_number = models.CharField(max_length=10, blank=True, null=True)
    trading_hour = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'order'
        unique_together = (('user', 'product'),)


class ProductRecord(models.Model):
    user = models.OneToOneField('User', models.DO_NOTHING, primary_key=True)
    product = models.ForeignKey('Productname', models.DO_NOTHING, db_column='Product_id')  # Field name made lowercase.
    headline = models.CharField(max_length=100)
    product_category = models.IntegerField()
    product_discription = models.CharField(max_length=100, blank=True, null=True)
    picture = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'product_record'
        unique_together = (('user', 'product'),)


class Productname(models.Model):
    product_id = models.IntegerField(db_column='Product_id', primary_key=True)  # Field name made lowercase.
    product_name = models.CharField(db_column='Product_name', max_length=15)  # Field name made lowercase.
    user = models.ForeignKey('User', models.DO_NOTHING)
    amount = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'productname'
        unique_together = (('product_id', 'user'),)


class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=20)
    user_city = models.CharField(max_length=40, blank=True, null=True)
    user_gender = models.CharField(max_length=10, blank=True, null=True)
    user_signature = models.CharField(max_length=50, blank=True, null=True)
    icon = models.CharField(db_column='Icon', max_length=100, blank=True, null=True)  # Field name made lowercase.
    phone_number = models.CharField(max_length=11)
    email = models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = 'user'
