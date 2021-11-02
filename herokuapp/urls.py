from django.urls import path
from herokuapp import views  as v
app_name = 'aplication'
urlpatterns = [
    path("", v.inicio, name = "inicio"),
    # path("detail_<int:id>/", v.detail, name = "detalle"),
    path("agregar/", v.crear, name = "crear")

]
