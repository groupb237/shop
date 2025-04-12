from django.contrib import admin
from mptt.admin import MPTTModelAdmin

# Register your models here.
import main.models as models


@admin.register(models.Category)
class CategoryAdmin(MPTTModelAdmin):
    ...


@admin.register(models.ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    ...


class ProductImageInline(admin.TabularInline):
    model = models.ProductImage
    extra = 1


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    ...


@admin.register(models.OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    ...


@admin.register(models.RecentView)
class RecentViewAdmin(admin.ModelAdmin):
    ...


@admin.register(models.Banner)
class BannerAdmin(admin.ModelAdmin):
    ...
