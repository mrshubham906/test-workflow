from django.urls import path
from test_app.views import CreateUserView


urlpatterns = [
    path('create-user', CreateUserView.as_view(), name='CreateUserView'),
]