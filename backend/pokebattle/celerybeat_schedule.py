from celery.schedules import crontab  # noqa


CELERYBEAT_SCHEDULE = {
    # Internal tasks
    "clearsessions": {"schedule": crontab(hour=3, minute=0), "task": "users.tasks.clearsessions"},
    "save_pokemon_from_pokeapi_weekly": {
        "schedule": crontab(minute="*/2"),
        "task": "pokemon.tasks.save_pokemon_from_pokeapi_weekly",
    },
}
