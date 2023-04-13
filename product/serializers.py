from rest_framework import serializers
from .models import Category, Products, Review


def get_movie_count(category):
    return category.product_count


class CategorySerializer(serializers.ModelSerializer):
    product_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'product_count']

    @staticmethod
    def get_product_count(category):
        return category.product_count


class MovieSerializer(serializers.ModelSerializer):
    director = CategorySerializer()

    class Meta:
        model = Products
        fields = ['id', 'name', 'description', 'duration', 'director']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'text', 'products')


class ProductsReviewSerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Products
        fields = "__all__"

    def get_reviews(self, products):
        return [i.stars for i in products.views.all()]

    def get_rating(self, products):
        return products.rating


class ProductsValidatorsCreate(serializers.Serializer):
    name = serializers.CharField(min_length=1, max_length=100)
    description = serializers.CharField(min_length=1)
    duration = serializers.IntegerField(min_value=1)
    director_id = serializers.IntegerField(min_value=1)


class ProductsDetailValidatorCreate(ProductsValidatorsCreate):
    pass


class ReviewValidatorCreate(serializers.Serializer):
    text = serializers.CharField(min_length=2)
    movie_id = serializers.IntegerField(min_value=1)


class ProductsValidatorCreate(serializers.Serializer):
    name = serializers.CharField(max_length=150)