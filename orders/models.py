from django.db import models
from django.contrib.auth.models import User

class FoodCategory(models.Model):
    name = models.CharField(max_length = 32, unique = True)

    def __str__(self):
        return (f"{self.name}")


class Topping(models.Model):
    name = models.CharField(max_length = 32, unique = True)

    def __str__(self):
        return (f"{self.name}")    

class Pizza(models.Model):
    # determine what pizza type, true = regular pizza, false = sicilian pizza
    regular = models.BooleanField(default = True)

    sizeChoices = [
        ("Small", "Small"),
        ("Large", "Large"),
    ]

    size = models.CharField(max_length = 5, choices = sizeChoices, default = "Small")

    toppings = models.ManyToManyField(Topping)

    price = models.DecimalField(max_digits = 4, decimal_places = 2, default = 00.00)

    def getType(self):
        return ("pizza")

    def getPrice(self):
        # price for regular pizza
        if self.regular:
            # price for small
            if self.size == "Small":
                # price depending on toppings
                if self.toppings.count() == 0:
                    return (12.70)
                elif self.toppings.count() == 1:
                    return (13.70)
                elif self.toppings.count() == 2:
                    return (15.20)
                else:
                    return (16.20)
            # price for large
            else:
                if self.toppings.count() == 0:
                    return (17.95)
                elif self.toppings.count() == 1:
                    return (19.95)
                elif self.toppings.count() == 2:
                    return (21.95)
                else:
                    return (23.95)
        # price for sicilian pizza
        else:
            # price for small
            if self.size == "Small":
                # price depending on toppings
                if self.toppings.count() == 0:
                    return (24.45)
                elif self.toppings.count() == 1:
                    return (26.45)
                elif self.toppings.count() == 2:
                    return (28.45)
                else:
                    return (29.45)
            # price for large
            else:
                if self.toppings.count() == 0:
                    return (38.70)
                elif self.toppings.count() == 1:
                    return (40.70)
                elif self.toppings.count() == 2:
                    return (42.70)
                else:
                    return (44.70)

    def __str__(self):
        name = "Regular" if self.regular else "Sicilian"
        if self.toppings.count() == 0:
            return (f"{self.size} {name} Pizza")
        # get list of toppings
        toppings = list(self.toppings.all())
        # convert to string
        toppings = ', '.join([str(elem) for elem in toppings]) 

        return (f"{self.size} {name} Pizza w/ {toppings}")

    class Meta:
        verbose_name_plural = "pizza"

class AddOn(models.Model):
    name = models.CharField(max_length = 32, unique = True)

    def __str__(self):
        return (f"{self.name}")

class SubType(models.Model):
    name = models.CharField(max_length = 32, unique = True)

    small = models.DecimalField(max_digits = 4, decimal_places = 2, default = None)

    large = models.DecimalField(max_digits = 4, decimal_places = 2, default = None)


    def __str__(self):
        return (f"{self.name}")

class Subs(models.Model):
    name = models.ManyToManyField(SubType)

    sizeChoices = [
        ("Small", "Small"),
        ("Large", "Large"),
    ]
    size = models.CharField(max_length = 5, choices = sizeChoices, default = "Small")

    addons = models.ManyToManyField(AddOn)

    price = models.DecimalField(max_digits = 4, decimal_places = 2, default = 00.00)

    def getType(self):
        return ("subs")

    def getPrice(self):
        # get the subtype object
        sub = SubType.objects.get(name = self.name.first())

        if self.size == "Small":
            price = sub.small
        else:
            price = sub.large

        # price is of type decimal.Decimal so convert it to float
        return float(price) + (self.addons.count() * 0.50)
        

    class Meta:
        verbose_name_plural = "Subs"

    def __str__(self):
        if self.addons.count() == 0:
            return (f"{self.size} {self.name.first()}")

        # get list of addons
        addons = list(self.addons.all())
        # convert to string
        addons = ', '.join([str(elem) for elem in addons]) 

        return (f"{self.size} {self.name.first()} w/ {addons}")

class PastaType(models.Model):
    name = models.CharField(max_length = 32, unique = True)

    price = models.DecimalField(max_digits = 4, decimal_places = 2, default = None)

    def __str__(self):
        return (f"{self.name}")

class Pasta(models.Model):
    name = models.ManyToManyField(PastaType)

    price = models.DecimalField(max_digits = 4, decimal_places = 2, default = None)

    def getType(self):
        return ("pasta")

    def __str__(self):
        return (f"{self.name.first()}")

class SaladType(models.Model):
    name = models.CharField(max_length = 32, unique = True)

    price = models.DecimalField(max_digits = 4, decimal_places = 2, default = None)

    def __str__(self):
        return (f"{self.name}")

class Salad(models.Model):
    name = models.ManyToManyField(SaladType)

    price = models.DecimalField(max_digits = 4, decimal_places = 2, default = None)

    def getType(self):
        return ("salad")

    def __str__(self):
        return (f"{self.name.first()}")

class PlatterType(models.Model):
    name = models.CharField(max_length = 32, unique = True)

    small = models.DecimalField(max_digits = 4, decimal_places = 2, default = None)

    large = models.DecimalField(max_digits = 4, decimal_places = 2, default = None)

    def __str__(self):
        return (f"{self.name}")

class Platters(models.Model):
    name = models.ManyToManyField(PlatterType)    

    sizeChoices = [
        ("Small", "Small"),
        ("Large", "Large"),
    ]
    size = models.CharField(max_length = 5, choices = sizeChoices, default = "Small")

    price = models.DecimalField(max_digits = 4, decimal_places = 2, default = 00.00)

    def getType(self):
        return ("platters")

    def getPrice(self):
        platter = PlatterType.objects.get(name = self.name.first())

        if self.size == "Small":
            price = platter.small
        else:
            price = platter.large

        return price

    def __str__(self):
        return (f"{self.size} {self.name.first()} Platter")

    class Meta:
        verbose_name_plural = "Platters"

class Order(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    pizza = models.ManyToManyField(Pizza)

    subs = models.ManyToManyField(Subs)

    pasta = models.ManyToManyField(Pasta)

    salad = models.ManyToManyField(Salad)

    platters = models.ManyToManyField(Platters)

    # get price of entire order
    def getPrice(self):
        price = 0

        for item in self.pizza.all():
            price += item.price

        for item in self.subs.all():
            price += item.price

        for item in self.pasta.all():
            price += item.price

        for item in self.salad.all():
            price += item.price

        for item in self.platters.all():
            price += item.price

        return (price)

    def __str__(self):
        return (f"{self.user}")
    