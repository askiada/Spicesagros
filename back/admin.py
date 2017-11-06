from django.contrib import admin
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin, PolymorphicChildModelFilter
from .models import Category, Tag, Document, PrivateDocument, PublicDocument, Note
from mptt.admin import DraggableMPTTAdmin

from django.conf import settings

# Register your models here.


# class CategoryInline(admin.TabularInline):
    # model = Category.subcategories.through
    # fk_name = 'from_category'
    # filter_horizontal = ('Category',)
    # show_change_link = True

    
class CategoryAdmin(DraggableMPTTAdmin):
    class Media:   
        css = {
             'all': (settings.STATIC_URL + 'back/vendor/font-awesome/css/font-awesome.min.css',)
        }
    list_display = ('tree_actions',
        'indented_title', 'icon_display',)
    def icon_display(self, obj):
        return '<i class="fa fa-%s"  style="color:green"> </i>' % (obj.icon)
    icon_display.allow_tags = True
    
    
@admin.register(PublicDocument)
class PublicDocumentAdmin(PolymorphicChildModelAdmin):
    base_model = PublicDocument
    exclude = ['qrcode']
 
@admin.register(PrivateDocument)
class PrivateDocumentAdmin(PolymorphicChildModelAdmin):
    base_model = PrivateDocument 
    exclude = ['qrcode']

    
@admin.register(Document)
class DocumentAdmin(PolymorphicParentModelAdmin):
    base_model = Document
    child_models = (PrivateDocument, PublicDocument)
    list_filter = (PolymorphicChildModelFilter,)

admin.site.register(Category, CategoryAdmin,
    list_display_links=(
        'indented_title', 
    ),)
admin.site.register(
    Tag,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
        # ...more fields if you feel like it...
    ),
    list_display_links=(
        'indented_title',
    ),
)

admin.site.register(Note)
