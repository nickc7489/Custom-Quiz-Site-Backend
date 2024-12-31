from django.contrib import admin

# import the model Todo
from .models import Quiz

# create a class for the admin-model integration


class QuizAdmin(admin.ModelAdmin):

    # add the fields of the model here
    list_display = ("title", "description", "questions", "author", "username", "attempts", "id")


# we will need to register the
# model class and the Admin model class
# using the register() method
# of admin.site class
admin.site.register(Quiz, QuizAdmin)
