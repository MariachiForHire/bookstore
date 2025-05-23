from django.contrib import admin
from core.models import Product, Category, Vendor, CartOrder, CartOrderItems, wishListModel, ProductImages, productReview, Address, Coupon, becomeVendorModel
# Register your models here.

class ProductImagesAdmin(admin.TabularInline): 
    model = ProductImages

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesAdmin]
    list_display = ['user', 'title', 'product_image', 'price', 'category', 'vendor','featured', 'product_status']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category_image']

class VendorAdmin(admin.ModelAdmin):
    list_display = ['vendor_title', 'vendor_image']

# orderdate comes from Cart Order in models.py 
class CartOrderAdmin(admin.ModelAdmin):
    list_editable = ['paid_status', 'product_status', ]
    list_display = ['user', 'price', 'paid_status', 'order_date', 'product_status']

class CartOrderItemsAdmin(admin.ModelAdmin):
    list_display = ['order', 'invoice_no', 'item', 'image', 'qty', 'price', 'total']

class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'review', 'rating']

class WishlistsAdmin(admin.ModelAdmin):
    list_display = ['user', 'product']

class AddressAdmin(admin.ModelAdmin):
    list_editable = ['address','status',]
    list_display = ['user', 'address', 'status']

class VendorApplicationAdmin(admin.ModelAdmin):
    list_display = ['user', 'full_name', 'business_name', 'email', 'date']
    list_filter = ['date', 'user']
    search_fields = ['full_name', 'email', 'business_name', 'user__username']

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(CartOrder, CartOrderAdmin)
admin.site.register(CartOrderItems, CartOrderItemsAdmin)
admin.site.register(productReview, ProductReviewAdmin)
admin.site.register(wishListModel, WishlistsAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Coupon)
admin.site.register(becomeVendorModel, VendorApplicationAdmin)
