from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponse
from .models import User, Order, Product
from datetime import datetime, timedelta

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

