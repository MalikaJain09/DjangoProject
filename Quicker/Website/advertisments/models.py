from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=150)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class UserAdd(models.Model):
    user_name = models.CharField(max_length=200, primary_key=True, default='Unknown')
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    Phone = models.CharField(max_length=200)


class Category(models.Model):
    category_name = models.CharField(max_length=200, primary_key=True, default='Other Category')


class sub_category(models.Model):
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category_name = models.CharField(max_length=200, primary_key=True, default='Others')


class RegisterAdd(models.Model):
    owner = models.ForeignKey(UserAdd , on_delete=models.CASCADE, null=True, related_name='owner' , default='Unknown')
    category_of_product = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_of_product', null=True , default='Other Category')
    sub_category_of_product = models.ForeignKey(sub_category, on_delete=models.CASCADE , related_name='category_of_product', null=True , default='Others')
    add_Title= models.CharField(max_length=200, default='None')
    product_name = models.CharField(max_length=200, default='Product Name Missing')
    condition= models.CharField(max_length=200, default='Not Mentioned')
    brand_Type= models.CharField(max_length=200, default='Not Mentioned')
    model_of_product= models.CharField(max_length=200, default='Not Mentioned')
    price_of_product = models.FloatField(null=False , default='Not on Sale')
    add_description= models.CharField(max_length=200, default='Not Mentioned')
    upload_photos = models.ImageField(upload_to='images/' , default='No Images')
    active_status = models.BooleanField(default=True)
    time_of_post = models.DateField(default='')


class Products(RegisterAdd):
    add_id = models.IntegerField(primary_key=True, default=00)


class Review(models.Model):
    review_of_add = models.ForeignKey(Products, on_delete=models.CASCADE)
    name_of_customer = models.CharField(max_length=200, default='Identity Not mentioned')
    reviews_of_add = models.CharField(max_length=500, default='None')
    time_of_review = models.DateField(default='')
