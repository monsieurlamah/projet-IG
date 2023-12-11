from django import forms
from app.models import ProductReview

class ProductReviewForm(forms.ModelForm):
    review =forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Écrire un commentaire...', 'class':'form-control form-control-sm','id':'review'}))
    
    class Meta:
        model = ProductReview
        fields = ['review', 'rating']