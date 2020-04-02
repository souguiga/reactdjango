# #!/usr/bin/env python3

# # initialize django
# import os
# os.environ['DJANGO_SETTINGS_MODULE'] = 'arcticapi.settings'
# import django
# django.setup()

# # regular imports
# from api.models import Category

# # main script
# def main():
#     for cat in Category.objects.all():
#         print(cat.id, cat.title)


# # bootstrap
# if __name__ == '__main__':
#     main()



#!/usr/bin/env python3

# initialize django
import json

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'arcticapi.settings'
import django
django.setup()

# regular imports
from api.models import Category, Product

# main script
def main():



    # prod = Product.objects.get(id="749868")
    # prod.filename = "packing_peanuts"
    # prod.save()
    

    # with open('products.json') as json_file:
    #     data = json.load(json_file)
    
    # products = data['products']
    # for prod in products:
    #     dbprod = Product()
    #     dbprod.id = prod['id']
    #     dbcat = Category()
    #     dbcat = Category.objects.get(title=prod['category'])
    #     dbprod.category = dbcat
    #     dbprod.name = prod['name']
    #     dbprod.description = prod['description']
    #     dbprod.filename = prod['filename']
    #     dbprod.price = prod['price']        
    #     dbprod.save
    #     Product.objects.create(id=dbprod.id, category=dbprod.category, name=dbprod.name, description=dbprod.description, filename=dbprod.filename, price=dbprod.price)
    #     print(Product.objects.all())

    #Category.objects.get(title='TestStuff').delete()



# bootstrap
if __name__ == '__main__':
    main()
