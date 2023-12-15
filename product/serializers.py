from django.db.models import Avg
from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from category.models import Category
from rating.serializers import RatingSerializer
from .models import Product


class ProductListSerializer(serializers.ModelSerializer):
    owner_email = serializers.ReadOnlyField(source='owner.email')
    # rating = serializers.SerializerMethodField()
    #
    # def get_rating(self, obj):
    #     ratings = obj.ratings.all()
    #     total_ratings = ratings.count()
    #     if total_ratings > 0:
    #         rating_values = sum(rating.rating for rating in ratings) // ratings.count()
    #     else:
    #         rating_values = 0
    #     return rating_values

    class Meta:
        model = Product
        # fields = ('id', 'owner', 'owner_email', 'title', 'price', 'image', 'rating')
        fields = ('id', 'owner', 'owner_email', 'title', 'price', 'image')

    def to_representation(self, instance):
        repr = super(ProductListSerializer, self).to_representation(instance)
        try:
            repr['rating_avg'] = round(instance.ratings.aggregate(Avg('rating'))["rating__avg"], 1)
        except TypeError:
            repr['rating_avg'] = None
        return repr


class ProductSerializer(serializers.ModelSerializer):
    owner_email = serializers.ReadOnlyField(source='owner.email')
    owner = serializers.ReadOnlyField(source='owner.id')
    category = serializers.PrimaryKeyRelatedField(required=True, queryset=Category.objects.all())

    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        repr = super(ProductListSerializer, self).to_representation(instance)
        try:
            repr['rating_avg'] = round(instance.ratings.aggregate(Avg('rating'))["rating__avg"], 1)
        except TypeError:
            repr['rating_avg'] = None
        return repr