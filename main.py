import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myblog.settings')
django.setup()

from blog.models import Post

Post(
    title='hello',
    content='hello world',
    published_date=''
).save()