# Inside models.py
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # if len(postData['first_name']) < 2:
        #     errors["first_name"] = "First name should be more than 1 characters"
        # if len(postData['last_name']) < 2:
        #     errors["first_name"] = "Last name should be more than 1 characters"
        # if len(postData['email_address']) < 4:
        #     errors["email"] = "Email should be more than 10 characters"
        # first_name should be letters only, at least 2 characters and that it was submitted
        if len(postData['name']) < 3 or postData['name'].isalpha() is not True:
            # flash("First name cannot be less than 2 characters and must be alphabetical.")
            errors["name"] = "Name should be more than 2 characters."
            print "Name cannot be less than 3 characters and must be alphabetical."
        # email should be letters only, at least 2 characters and that it was submitted
        if len(postData['email']) < 3:
            # flash("Email cannot be blank!")
            errors["email"] = "Email cannot be blank."
            print "Email cannot be blank!"
        # check if the user provided email is already in the database
        query = User.objects.filter(email=postData['email'])
        if query:
            errors["email_in_use"] = "This email is already in use."
            print "We already have this email in our database."
        if len(postData['password']) < 8 or postData['password'] != postData['password_confirm']:
            # flash("Passwords must be at least 6 characters and must match.")
            errors["password"] = "Passwords must be at least 6 characters and must match."
            print "Passwords must be at least 6 characters and must match."
        return errors

class ItemManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # if user provided a new author, check them against the DB
        # if len(postData['new_author']) > 0:
        #     # check if the user provided author is already in the database
        #     query = Author.objects.filter(name=postData['new_author'])
        #     if query:
        #         errors["repeat_author"] = "This author is already in our database. Please select this author from the dropdown menu."
        #         print "This item is already in our database. Please select this author from the dropdown menu."
        if len(postData['name']) < 4:
            # flash("Email cannot be blank!")
            errors["name"] = "Item name must be at least 4 characters."
            print "Item name must be at least 4 characters."
        return errors

class User(models.Model):
    name = models.CharField(max_length=255)
    # usernames are emails
    email = models.CharField(max_length=255)
    # email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    date_hired = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

class Item(models.Model):
    item_name = models.CharField(max_length=255)
    users = models.ManyToManyField(User, related_name="items")
    added_by = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = ItemManager()
