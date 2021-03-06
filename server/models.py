from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.db.models.fields import related
from django.db.models.fields.related import OneToOneField

# class Players (models.Model):
#     #idPlayer = models.TextField(max_length=20)
#     namePlayer = models.TextField(max_length=100)
#     agePlayer = models.IntegerField()

# user table
# class User (models.Model):
#     _name = models.CharField(max_length=20)

#     def __str__(self):
#         return self._name

# person table
class Person (models.Model):
    uid = models.TextField(null= True)

    _name = models.CharField(max_length=20)

    personpicture = models.TextField(null = True)
    # age = models.DecimalField()

    # personName = models.CharField(max_length=20)

    # owner = models.OneToOneField(
    #     User, 
    #     on_delete=models.CASCADE,
    #     primary_key=True,
    # )

    matchedPerson = models.ManyToManyField('self',related_name='matched_person', symmetrical = True, blank = True)

    swipePerson = models.ManyToManyField('self', through='SwipePerson', symmetrical=False)
    interested = models.ManyToManyField('Interest')

    oriented = models.ForeignKey('Oriented', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self._name

class OneSignal (models.Model):
    oneSignalUID = models.TextField()
    
    owner = models.ForeignKey('Person', on_delete=models.CASCADE, null= True)

class Picture (models.Model):
    picture = models.TextField()

    owner = models.ForeignKey('Person', on_delete=models.CASCADE, null = False)

    def __str__(self):
        return self.picture

# class MatchPerson (models.Model):
#     person = models.ForeignKey(Person, related_name='person' ,on_delete=models.SET_NULL, null=True)
#     match = models.ForeignKey(Person, related_name='match', on_delete=models.SET_NULL, null=True)


# Person to Person third table
class SwipePerson (models.Model):
    fromPerson = models.ForeignKey(Person, related_name='from_person' ,on_delete=models.SET_NULL, null=True)
    toPerson = models.ForeignKey(Person, related_name='to_person', on_delete=models.SET_NULL, null=True)

    liked = models.BooleanField()

    def __str__(self):
        return "{} to {}".format(self.fromPerson, self.toPerson)

# Interest table
class Interest (models.Model):
    interestName = models.CharField(max_length=20)

    def __str__ (self):
        return self.interestName

# sex oriented table
class Oriented (models.Model):
    orientedType = models.CharField(max_length = 20)

    def __str__(self):
        return self.orientedType
