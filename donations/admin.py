from django.contrib import admin

from .models import Category, Institution, Donation


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

    class Meta:
        verbose_name_plural = 'categories'


@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ('name', 'type',)


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('quantity', 'user',)
