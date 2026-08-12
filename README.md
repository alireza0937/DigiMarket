                         ┌─────────────┐
                         │    Nginx    │  (reverse proxy + static/media)
                         └──────┬──────┘
                                │
                         ┌──────▼──────┐
                         │   Gunicorn  │
                         │   + Django  │
                         └──┬───────┬──┘
                            │       │
              ┌─────────────┘       └──────────────┐
              │                                    │
      ┌───────▼───────┐                    ┌───────▼───────┐
      │  PostgreSQL   │                    │ Elasticsearch │
      │ (source of    │                    │ (search index)│
      │  truth)       │                    └───────────────┘
      └───────────────┘
              │
      ┌───────▼────────┐       ┌───────────────┐
      │     Redis      │◄──────┤ Celery Worker │
      │ (cache + broker│       │ + Celery Beat │
      │  + cart store) │       └───────────────┘
      └────────────────┘