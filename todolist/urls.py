from django.urls import path
from todolist.views import delete, register
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import show_create_task
from todolist.views import show_todolist
from todolist.views import update_status
from todolist.views import delete

app_name = 'todolist'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', show_create_task, name='create-task'),
    path('', show_todolist, name='todolist'),
    path('update_status/<int:id>/', update_status, name='update_status'),
    path('delete/<int:id>/', delete, name='delete'),
]