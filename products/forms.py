from django import forms
from .models import Product,Comment
from django.core.exceptions import ValidationError

class ProductForms(forms.ModelForm):
    class Meta:
        model=Product
        fields='__all__'

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price <= 0:
            raise ValidationError("Price must be greater than zero.")
        return price

    def clean_name(self):
        name = self.cleaned_data.get('name')
        qs = Product.objects.filter(name__iexact=name)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise ValidationError("Product with this name already exists.")
        return name

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            if image.size > 3 * 1024 * 1024:
                raise ValidationError("Image size must not exceed 3 MB.")
        return image


class CommentForm(forms.ModelForm):
    rate=forms.IntegerField(min_value=0,max_value=5,required=False)
    class Meta:
        model=Comment
        fields=['text','rate','image_comment']

