from django.urls import path

import blog.views as blog_views

urlpatterns = [
    path('', blog_views.info_list, name='post_list')
]