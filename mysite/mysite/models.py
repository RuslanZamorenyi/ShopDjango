from django.db import models


class Sizes(models.Model):
    size = models.IntegerField()

    def __repr__(self):
        return self.size


class Colours(models.Model):
    colour = models.CharField(max_length=15)

    def __repr__(self):
        return self.colour


class Names(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=100)
    price = models.IntegerField()
    table_sizes = models.ManyToManyField(Sizes)
    table_colours = models.ManyToManyField(Colours)

    def __repr__(self):
        return self.name


class Bucket(models.Model):
    id_user = models.IntegerField()
    id_brand = models.IntegerField()
    id_sizes = models.IntegerField()
    id_colours = models.IntegerField()

    def __repr__(self):
        return self.id_user
