from django.db import models

# Create your models here.
class GoodsType(models.Model):
    title = models.CharField('分类名称',max_length=30,null=False)
    desc = models.CharField('描述',max_length=200,default='商品描述')
    isdelete = models.BooleanField('删除',default=False)

    def __str__(self):
        return self.title


class Goods(models.Model):
    title = models.CharField('商品名称',max_length=30,null=False)
    price = models.DecimalField('商品价格',max_digits=8,decimal_places=2)
    desc = models.CharField('描述',max_length=200)
    unit = models.CharField('单位',max_length=30)
    picture = models.ImageField('商品图片',upload_to='static/images/goods',default='normal.png')
    detail = models.CharField('商品详情',max_length=1000,default='商品详情')
    isdelete = models.BooleanField('删除',default=False)
    type = models.ForeignKey(GoodsType,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    #下面两个函数的作用都是为了跳转到相应的url
    def get_absolute_url(self):
        if self.type.title == '水果' or self.type.title == '玩具':
            return '/memberapp/detail/?goodid={}/'.format(self.id)
        elif self.type.title == '肉类':
            return  u'不爱吃'

    def get_adcart_url(self):
        return '/cartinfo/addcart/?gcount=1&goodid={}'.format(self.id)
