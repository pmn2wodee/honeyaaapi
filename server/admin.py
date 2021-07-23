from django.contrib import admin
from .models import OneSignal, Picture, Person, SwipePerson, Interest, Oriented

# admin.site.register(User)
admin.site.register(Person) 
admin.site.register(OneSignal)
admin.site.register(SwipePerson)
admin.site.register(Interest)
admin.site.register(Oriented) 
admin.site.register(Picture)

# Register your models here.
