from django import forms;

from .models import Product

class ProductForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
            'summary'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if "Stefan" in title:
            return self.cleaned_data.get('title');
        else:
            raise forms.ValidationError("Not valid; must contain Stefan")

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        if not "x" in email:
            raise forms.ValidationError("No x present in email")

class RawProductForm(forms.Form):
    title = forms.CharField(label="Test")
    description = forms.CharField(required=False)
    price = forms.DecimalField()
    summary = forms.CharField()
