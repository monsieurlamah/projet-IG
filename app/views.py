from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from app.models import *
from app.form import ProductReviewForm
from django.db.models import Avg
from taggit.models import Tag
from django.template.loader import render_to_string


def index(request):
    products = Product.objects.filter(product_status="publier", featured=True).order_by("-id")
    categories = Category.objects.all()
    context = {
        'products':products,
        'categories':categories,
    }
    return render(request, 'app/index.html', context)

def product_list_view(request):
    products = Product.objects.filter(product_status="publier", featured=True).order_by("-id")
    categories = Category.objects.all()
    brands = Brand.objects.all()
    
    context = {
        'products':products,
        'categories':categories,
        'brands':brands,
    }
    return render(request, 'app/product-list.html', context)

def category_list_view(request):
    categories = Category.objects.all()
    context = {
        'categories':categories
    }
    return render(request, 'app/category-list.html', context)


def category_product_list(request, cid):
    category = Category.objects.get(cid=cid)
    products = Product.objects.filter(product_status="publier", featured=True, category=category)
    categories = Category.objects.all()
    brands = Brand.objects.all()
    
    context={
        'products':products,
        'categories':categories,
        'brands':brands,
        'category':category
    }
    return render(request, 'app/category-product.html', context)

def product_detail_view(request, pid):
    product = Product.objects.get(pid=pid)
    related_product = Product.objects.filter(category=product.category, product_status="publier", featured=True).exclude(pid=pid)
    product_featured = Product.objects.filter(product_status="publier", featured=True).order_by("-id")
    p_images = product.p_images.all()
    review_form = ProductReviewForm()    
    # Getting all reviews related to a product
    reviews = ProductReview.objects.filter(product=product).order_by("-date")
    
    # Getting average review
    average_rating = ProductReview.objects.filter(product=product).aggregate(rating=Avg('rating'))
    
    make_review = True
    if request.user.is_authenticated:
        user_review_count = ProductReview.objects.filter(user=request.user, product=product).count()
        if user_review_count > 0:
            make_review = False
            
    context = {
        'product':product,
        'p_images':p_images,
        'reviews':reviews,
        'average_rating':average_rating,
        'product_featured':product_featured,
        'related_product':related_product,
        'review_form':review_form,
        'make_review':make_review,
       
    }
    return render(request, 'app/product-detail.html', context)


def tag_list(request, tag_slug=None):
    products = Product.objects.filter(product_status="publier").order_by("-id")
    brands = Brand.objects.all()

    
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        products = products.filter(tags__in=[tag])
    context = {
        'products':products,
        'tag':tag,
        'brands':brands,
    }
    return render(request, 'app/tag.html', context)

def ajax_add_review(request, pid):
    product = Product.objects.get(pid=pid)
    user = request.user
    
    review = ProductReview.objects.create(
        user=user,
        product=product,
        review=request.POST['review'],
        rating=request.POST['rating'],
    )
    
    context = {
        'user': user.username,
        'review':request.POST['review'],
        'rating':request.POST['rating'],
    }
    
    average_reviews = ProductReview.objects.filter(product=product).aggregate(rating=Avg('rating'))
    
    return JsonResponse(
       {
        'bool': True,
        'context': context,
        'average_reviews' : average_reviews
       }
    )

def brand_product_list(request, bid):
    brand = Brand.objects.get(bid=bid)
    products = Product.objects.filter(product_status="publier", featured=True, brand=brand)
    categories = Category.objects.all()
    brands = Brand.objects.all()
    context = {
        'products':products,
        'categories':categories,
        'brands':brands,
        'brand':brand,
    }
    return render(request, 'app/marque-product.html', context)

def seach_view(request):
    query = request.GET.get('q')
    products = Product.objects.filter(product_status="publier", title__icontains=query)
    context = {
        'query':query,
        'products':products,
    }
    return render(request, 'app/search.html', context)


def filter_product(request):
    categories = request.GET.getlist("category[]")
    brands = request.GET.getlist("brand[]")
    
    min_price = request.GET["min_price"]
    max_price = request.GET["max_price"]
    
    products = Product.objects.filter(product_status="publier").order_by('-id').distinct()
    products = products.filter(price__gte=min_price)
    products = products.filter(price__lte=max_price)
    
    if len(categories) > 0:
        products =products.filter(category__id__in=categories).distinct()
        
    if len(brands) > 0:
        products = products.filter(brand__id__in=brands).distinct()
    
    context = {
        'products':products
    }
    data = render_to_string('app/async/product-list.html', context)
    
    return JsonResponse({
        'data':data
    })