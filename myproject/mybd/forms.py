from django import forms

class Product_Update(forms.Form):
    id = forms.DecimalField(label='ID', max_digits=8)
    name = forms.CharField(label='Наименование продукта', max_length = 100)
    description = forms.CharField(label = 'Описание', widget=forms.Textarea(attrs={'class':'form-control'}))
    price = forms.DecimalField(label='Цена', max_digits=8, decimal_places=2)
    quantity = forms.DecimalField(label = 'Количество', max_digits = 8, decimal_places=0)
    image = forms.ImageField()
    #create_at = forms.DateField(label = 'Дата создания')
