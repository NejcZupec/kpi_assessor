from django.contrib import admin

from polls.models import Field
from polls.models import Poll
from polls.models import Template
from polls.models import Vote


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ('title', 'template')


@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    list_display = ('title', 'template')


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('poll', 'field', 'value')
