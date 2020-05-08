from django.urls import include, path


app_name = "api"

urlpatterns = [
    path("", include("api.pokemon.urls")),
    path("", include("api.battles.urls")),
    path("", include("api.users.urls")),
]
