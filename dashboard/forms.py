from django import forms
from products.models import Product, Category


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "name",
            "description",
            "categories",
            "price",
            "image",
            "available_stock",
        ]

        widgets = {
            "name": forms.TextInput(attrs={"class": "w-full px-3 py-2 border rounded"}),
            "description": forms.Textarea(
                attrs={
                    "class": "w-full px-3 py-2 border rounded resize-none",
                    "rows": 4,
                }
            ),
            "categories": forms.CheckboxSelectMultiple(
                attrs={"class": "space-y-2"}
            ),
            "price": forms.NumberInput(
                attrs={"class": "w-full px-3 py-2 border rounded"}
            ),
            "image": forms.ClearableFileInput(
                attrs={
                    "class": "block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-yellow-400 file:text-white hover:file:bg-yellow-500 transition"
                }
            ),
            "available_stock": forms.NumberInput(
                attrs={"class": "w-full px-3 py-2 border rounded"}
            ),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "w-full px-3 py-2 border rounded",
                }
            ),
        }
