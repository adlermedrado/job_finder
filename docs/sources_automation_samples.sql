INSERT INTO sources (id, name, url, description, created_at, updated_at) VALUES ('0156edd4-b9b7-42fb-8e26-e101125d8e6f', 'backend-br/vagas', 'https://github.com/backend-br/vagas/issues', 'backend-br''s open source job listing', '2025-01-26 18:50:25.075348 +00:00', '2025-01-26 18:50:25.075358 +00:00');
INSERT INTO sources (id, name, url, description, created_at, updated_at) VALUES ('069f8e57-2a24-4981-a92c-ab19bedc1e9e', 'brasil-php/vagas', 'https://github.com/brasil-php/vagas/issues', 'brasil-php''s open source job board', '2025-01-26 18:51:05.801860 +00:00', '2025-01-26 18:51:05.801868 +00:00');
INSERT INTO sources (id, name, url, description, created_at, updated_at) VALUES ('93a5ad98-abb8-4ca7-b7aa-ca5ec49c314c', 'Empregos-dev/Vagas-dev', 'https://github.com/Empregos-dev/Vagas-dev/issues', 'Empregos-Dev''s open source job listing', '2025-01-26 18:52:05.572847 +00:00', '2025-01-26 18:52:05.572856 +00:00');

INSERT INTO django_celery_beat_periodictasks (ident, last_update) VALUES (1, '2025-01-30 01:38:32.006913 +00:00');
INSERT INTO django_celery_beat_periodictask (id, name, task, args, kwargs, queue, exchange, routing_key, expires, enabled, last_run_at, total_run_count, date_changed, description, crontab_id, interval_id, solar_id, one_off, start_time, priority, headers, clocked_id, expire_seconds) VALUES (2, 'celery.backend_cleanup', 'celery.backend_cleanup', '[]', '{}', null, null, null, null, true, null, 0, '2025-01-30 01:38:32.006288 +00:00', '', 1, null, null, false, null, null, '{}', null, 43200);
INSERT INTO django_celery_beat_periodictask (id, name, task, args, kwargs, queue, exchange, routing_key, expires, enabled, last_run_at, total_run_count, date_changed, description, crontab_id, interval_id, solar_id, one_off, start_time, priority, headers, clocked_id, expire_seconds) VALUES (3, 'Sanitize Job Descriptions', 'jobs.tasks.sanitize_jobs_descriptions', '[]', '{}', null, null, null, null, true, '2025-01-30 01:41:32.210284 +00:00', 44, '2025-01-30 01:42:05.307289 +00:00', 'Sanitize Job descriptions removing unnecessary text to send less tokens to openai api', null, 1, null, false, null, null, '{}', null, null);
INSERT INTO django_celery_beat_periodictask (id, name, task, args, kwargs, queue, exchange, routing_key, expires, enabled, last_run_at, total_run_count, date_changed, description, crontab_id, interval_id, solar_id, one_off, start_time, priority, headers, clocked_id, expire_seconds) VALUES (4, 'Analyze jobs descriptions', 'jobs.tasks.analyze_jobs_descriptions', '[]', '{}', null, null, null, null, true, '2025-01-30 01:41:32.195173 +00:00', 20, '2025-01-30 01:42:05.321020 +00:00', 'Analyze job descriptions using openai api according to criteria', null, 1, null, false, null, null, '{}', null, null);
INSERT INTO django_celery_beat_periodictask (id, name, task, args, kwargs, queue, exchange, routing_key, expires, enabled, last_run_at, total_run_count, date_changed, description, crontab_id, interval_id, solar_id, one_off, start_time, priority, headers, clocked_id, expire_seconds) VALUES (1, 'Fetch Jd from Github', 'jobs.tasks.fetch_github_issues', '[]', '{}', null, null, null, null, true, '2025-01-30 01:41:32.163675 +00:00', 46, '2025-01-30 01:42:05.328854 +00:00', 'Fetch and Save job descriptions from Github Repositories', null, 1, null, false, null, null, '{}', null, null);
INSERT INTO django_celery_beat_intervalschedule (id, every, period) VALUES (1, 1, 'minutes');
