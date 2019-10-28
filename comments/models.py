from django.db import models
from djstore.models import Product,Topproduct
from django.utils.translation import gettext_lazy as _

# Create your models here.


class CommentPost(models.Model):
    user = models.CharField(_('User'),max_length=20)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='comments',null=True,blank=True)
    topproduct = models.ForeignKey(Topproduct,on_delete=models.CASCADE,related_name='comments',null=True,blank=True)
    comment=models.CharField(_('Comment'),max_length=255)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user

    class Meta:
        ordering=['-date']


