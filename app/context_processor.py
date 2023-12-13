from app.models import *
from django.db.models import Min, Max

def default(request):
    categories = Category.objects.all()
    brands = Brand.objects.all()
    min_max_price = Product.objects.aggregate(Min("price"), Max("price"))
    
    return ({
        'categories':categories,
        'brands':brands,
        'min_max_price':min_max_price,
    })