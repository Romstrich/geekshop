import json
from mainapp.models import Product, Product_Category
from django.core.management.base import BaseCommand



def load_from_json(file_name):
    with open(file_name,mode='r',encoding='utf-8') as infile:
        return json.load(infile)

class Command(BaseCommand):
    def handle(self,*args,**options):
        categories=load_from_json('mainapp/fixtures/Categories.json')

        Product_Category.objects.all().delete()
        for category in categories:
            cat=category.get('fields')
            cat['id']=category.get('pk')
            new_category = Product_Category(**cat)
            new_category.save()

        products=load_from_json('mainapp/fixtures/Product.json')
        Product.objects.all().delete()
        for product in products:
            prod=product.get('fields')
            category=prod.get('category')
            _category=Product_Category.objects.get(id=category)
            prod['category']=_category
            new_category=Product(**prod)
            new_category.save()