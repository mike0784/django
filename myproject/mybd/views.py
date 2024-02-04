from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponse
from .models import User, Order, Product
from datetime import datetime, timedelta
from .forms import Product_Update

class ProductsOrder(View):
    def get(self, request):
        users = User.objects.values("id", "surname", "name", "patronymic")
        day = request.GET.get("period")
        user_id = request.GET.get("user")
        if day == "" or user_id == "":
            #orders = Order.objects.filter(customer = user).values("name", )
            context = {"title": "Просмотр заказов",
                   "day": "Нет",
                   "user": "Нет",
                   "users": users}
        else:
            now = datetime.now()
            new_date = now - timedelta(days=int(day))
            user = User.objects.filter(pk=int(user_id)).first()
            orders = Order.objects.filter(customer = user, date_ordered__gte = new_date).all().values("products", "products__name", "products__price").order_by("-date_ordered")
            res = []
            temp = []
            for item in orders:
                i = int(item["products"])
                if i not in temp:
                    temp.append(i)
                    res.append({"Product": item["products__name"], "price": float(item["products__price"])})
            #product = Product.objects.filter(order__customer = user)
            context = {"title": "Просмотр заказов",
                   "day": day,
                   "user": user,
                   "users": users,
                   "order": res,
                   "orders": orders}
        #return HttpResponse(f'За последние {day} дни!!!')
        return render(request, "mybd/index.html", context)

class ProductUpdate(View):
    def get(self, request):
        if request.method == 'POST':
            context = {'id':request['id']}
            return render(request, "mybd/product_update.html", context)
        else:
            prod_id = request.GET.get("prod_id")
            product = Product.objects.filter(pk=int(prod_id))
            form = Product_Update()
            ll = list(product)
            form.fields['id'].initial = prod_id
            form.fields['name'].initial = ll[0].name
            form.fields['description'].initial = ll[0].description
            form.fields['price'].initial = ll[0].price
            form.fields['quantity'].initial = ll[0].quantity
            form.fields['image'].initial = ll[0].image
            context = {'id': prod_id,
                    "prod": product,
                    'form': form}
            return render(request, "mybd/product_update.html", context)
    
    def post(self, request):
        if request.method == 'POST':
            id = request.POST["id"]
            name = request.POST["name"]
            description = request.POST["description"]
            price = request.POST["price"]
            quantity = request.POST["quantity"]
            img = request.POST["image"]
            obj = Product.objects.filter(pk=id).first()
            obj.name = name
            obj.description = description
            obj.price = price
            obj.quantity = quantity
            obj.image = img
            obj.save()
            context = {'id': request.POST["id"]}
            return render(request, "mybd/product_update.html", context)

