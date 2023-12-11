from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name="app-home"),
    
    #product
    path('produits/', views.product_list_view, name="app-product-list"),
    path('produits/<pid>', views.product_detail_view, name="app-product-detail"),
    
    #category
    path('categories/', views.category_list_view, name="app-category-list"),
    path('categorie/<cid>/', views.category_product_list, name="app-category-product"),
    
    #Add review
    path('ajax-add-review/<pid>/', views.ajax_add_review, name="app-ajax-add-review"),
    
    #Tags
    path('products/tag/<slug:tag_slug>/', views.tag_list, name="app-tags"),
    
    #Brand
    path('marque/<bid>/', views.brand_product_list, name="app-brand-product"),
    
    #Seach
    path('recherche/', views.seach_view, name="app-search"),
    
    #filter product
    path('filter-product/', views.filter_product, name="filter-product"),
    
]