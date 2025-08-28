import os
from django.contrib.auth import get_user_model

User = get_user_model()
password = os.environ.get('SUPERUSER_PASSWORD')
if not password:
    raise ValueError("SUPERUSER_PASSWORD environment variable is not set.")

if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('z-fourteen', 'zgh1016@mail.ustc.edu.cn', password)
    print("Superuser created successfully!")