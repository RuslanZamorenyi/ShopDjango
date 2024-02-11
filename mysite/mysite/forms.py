from django import forms

from .models import Names, Sizes, Colours, Bucket


class AddBrand(forms.ModelForm):

    class Meta:
        model = Names

        fields = ('name', 'description', 'price', 'table_sizes', 'table_colours')

        # print(topics.queryset)


class AddSize(forms.ModelForm):

    class Meta:
        model = Sizes
        fields = ('size', )


class AddColour(forms.ModelForm):

    class Meta:
        model = Colours

        fields = ('colour', )


class AddToBucket(forms.ModelForm):

    class Meta:
        model = Bucket

        fields = ("id_user", "id_brand", "id_sizes", "id_colours")

