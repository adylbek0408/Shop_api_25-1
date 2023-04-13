from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    @property
    def product_count(self):
        return self.products_set.all().count()

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()
    director = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def filtered_reviews(self):
        return self.reviews.filter(stars__gt=3)

    @property
    def rating(self):
        count = self.reviews.all().count()
        stars = sum([i.stars for i in self.reviews.all()])
        if count == 0:
            return None
        return stars // count


class Review(models.Model):
    text = models.TextField()
    products = models.ForeignKey(Products, on_delete=models.CASCADE, null=True, related_name='reviews')
    stars = models.IntegerField(choices=([i, i * '*'] for i in range(1, 6)), default=1)

    def __str__(self):
        return f"{self.products.name} - {self.text[:50]}..."