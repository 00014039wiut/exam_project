from django import forms

from shop.models import Comment, Order, Product, Category


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'image', 'description', 'quantity', 'category', 'rating', 'discount']

    name = forms.CharField(max_length=50)
    description = forms.CharField(widget=forms.Textarea)
    price = forms.DecimalField(max_digits=5, decimal_places=2)
    discount = forms.IntegerField()
    image = forms.ImageField()
    quantity = forms.IntegerField()
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    rating = forms.IntegerField(min_value=0, max_value=5)


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'phone_number', 'quantity']
