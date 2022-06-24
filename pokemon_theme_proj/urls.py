from django.urls import path, include

urlpatterns = [
    path('pokemon/', include('pokemon_theme_app.urls'))
]
