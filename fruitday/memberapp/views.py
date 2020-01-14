from django.shortcuts import render,get_object_or_404
from .models import *
from django.db import DatabaseError
import logging
import random
# Create your views here.

def index(request):
    try:
        good_fruit_type = get_object_or_404(GoodsType,title="水果")
        fruit_goods = random.sample(list(good_fruit_type.goods_set.all()),2)
    except DatabaseError as e:
        logging.warning(e)


    types = GoodsType.objects.all()
    goods = Goods.objects.all()


    ac=[]
    typess = GoodsType.objects.all()
    for type in typess:
        b={}
        b['type'] = type.title
        good_type = get_object_or_404(GoodsType, title=type.title)
        f_goods = random.sample(list(good_type.goods_set.all()), 2)
        b['goods'] = f_goods
        ac.append(b)
    return render(request,'memberapp/index.html',{'good_list':locals()})


def detail_one(request):
    good_id = request.GET.get('goodid')[0]
    try:
        goodone = Goods.objects.filter(id=good_id)
    except DatabaseError as e:
        logging.warning(e)
    return render(request,'memberapp/detail.html',{'goodone':goodone[0]})




