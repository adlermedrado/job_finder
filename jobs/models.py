import uuid
from django.db import models


class Source(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True, db_index=True)
    url = models.URLField(max_length=2048, unique=True, db_index=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'sources'
        indexes = [
            models.Index(fields=['name'], name='idx_source_name'),
            models.Index(fields=['url'], name='idx_source_url'),
        ]

    def __str__(self):
        return self.name


class JobDescription(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    external_id = models.CharField(max_length=100, null=True, blank=True)
    is_analyzed = models.BooleanField(default=False)
    criteria_status = models.CharField(max_length=20, null=True, blank=True)
    source = models.ForeignKey(Source, on_delete=models.CASCADE, related_name='job_descriptions')
    url = models.URLField(max_length=2048, null=True, blank=True)
    is_sanitized = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'job_descriptions'
        indexes = [
            models.Index(fields=['title'], name='idx_job_title'),
            models.Index(fields=['is_analyzed'], name='idx_job_is_analyzed'),
        ]

    def __str__(self):
        return self.title


class GithubTask(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    source = models.ForeignKey(Source, on_delete=models.CASCADE, related_name='github_tasks')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'github_tasks'
        indexes = [
            models.Index(fields=['source'], name='idx_source_id'),
            models.Index(fields=['created_at'], name='idx_created_at'),
            models.Index(fields=['updated_at'], name='idx_updated_at'),
        ]
