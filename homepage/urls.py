from django.contrib import admin
from django.urls import path,include
from homepage import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="homepage"),
    path('billArea.html',views.billArea,name="Bill Area"),
    path('sellings.html',views.sellings,name="Sellings"),
    path('stocks.html',views.stocks,name="Stocks")
]