from django.contrib import admin
from .models import Source, JobDescription, GithubTask


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'created_at', 'updated_at')
    search_fields = ('name', 'url')


@admin.register(JobDescription)
class JobDescriptionAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_analyzed', 'criteria_status', 'url')
    list_filter = ('is_analyzed', 'source', 'criteria_status')
    search_fields = ('title', 'description')


@admin.register(GithubTask)
class GithubTaskAdmin(admin.ModelAdmin):
    list_display = ('source', 'created_at', 'updated_at')
    list_filter = ('source',)
