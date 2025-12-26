import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', password='admin123')
    print("Superuser created: admin / admin123")
else:
    u = User.objects.get(username='admin')
    u.set_password('admin123')
    u.save()
    print("Superuser password updated to: admin123")
