from django import forms
from .models import RecommendationPost, Author
from products.models import Album


class RecommendationPostForm(forms.ModelForm):

    class Meta:
        model = RecommendationPost
        fields = ['title', 'sub_title', 'product', 'content', 'article_image' ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
       
        
        products = Album.objects.all()


        product_names = [(product.id, product.title) for product in products]
       
        

        self.fields['product'].choices = product_names
        
        
        
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'checkout-input'