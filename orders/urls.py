from django.urls import path

from . import views

from users import views as usersViews

urlpatterns = [
    path("", views.home, name = "home"),
    path("menu", views.menu, name = "menu"),
    path("menu/pizza", views.pizza, name = "pizza"),
    path("menu/pizza/<str:pizza>", views.topping, name = "topping"),
    path("menu/subs", views.subs, name = "subs"),
    path("menu/subs/<str:subs>", views.addons, name = "addon"),
    path("menu/salads", views.salads, name = "salads"),
    path("menu/pasta", views.pasta, name = "pasta"),
    path("menu/platters", views.platters, name = "platters"),
    path("menu/platters/<str:platter>", views.platterSize, name = "platterSize"),
    path("order", views.order, name = "order"),
    path("cancel", views.cancelOrder, name = "cancel"),
    path("purchase", views.purchase, name = "purchase"),
    path("login", usersViews.loginUser, name = "login"),
    path("logout", usersViews.logoutUser, name = "logout"),
    path("register", usersViews.register, name = "register")
]
