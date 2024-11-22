from django.contrib import admin

from ringtones_app.models import Ringtone


class RingtoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'letter', 'uploaded_at')
    search_fields = ('name', 'letter')
    list_filter = ('letter', 'uploaded_at')


admin.site.register(Ringtone, RingtoneAdmin)