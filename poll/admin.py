from django.contrib import admin
from django.forms import Textarea
from django.db import models
from poll.models import Poll


class PollsAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 6, 'cols': 50})},
    }
    list_display = ('Poll_Title', 'Option1', 'Option2', 'Option3', 'Option4', 'Option5',)
    list_filter = ('Created_At', 'Updated_At',)
    search_fields = ('Poll_Title',)

admin.site.register(Poll, PollsAdmin)


