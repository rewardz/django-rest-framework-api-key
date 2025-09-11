from django.contrib import admin
from django.contrib import messages
from rest_framework_api_key.models import APIKey, KeyOwner
from rest_framework_api_key.helpers import generate_key


class ApiKeyAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'name', 'created', 'modified')

    fieldsets = (
        ('Required Information', {'fields': ('name', "owner")}),
        ('Additional Information', {'fields': ('old_key_message', 'key_message',)}),
    )
    readonly_fields = ('key_message', 'old_key_message')

    search_fields = ('id', 'name',)

    actions = ["generate_new_key"]

    # def generate_new_key(self, request, queryset):
    #     for obj in queryset:
    #         key, generated_key = APIKey.objects.create_key(name=obj.name)
    #         messages.success(request, f"New key for {obj.name}: {generated_key}")
    # generate_new_key.short_description = "Generate new API key"

    def has_delete_permission(self, request, obj=None):
        return False

    def key_message(self, obj):
        if obj.key or obj.old_key:
            return "Hidden"
        return "The API Key will be generated once you click save."
    
    def old_key_message(self, obj):
        if obj.old_key:
            return "Hidden"
        return "The API Key will be generated once you click save."

    def save_model(self, request, obj, form, change):
        if not obj.key:
            obj.key = generate_key()
            messages.add_message(request, messages.WARNING, (
                'The API Key for %s is %s. Please note it since you will not be able to see it again.' % (obj.name, obj.key)))
        obj.save()


admin.site.register(APIKey, ApiKeyAdmin)


class KeyOwnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'path_re')


admin.site.register(KeyOwner, KeyOwnerAdmin)
