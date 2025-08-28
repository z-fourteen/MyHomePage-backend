from django.contrib.auth import get_user_model

User = get_user_model()

username = "z-fourteen"
password = "986051zgh"
email = "zgh1016@mail.ustc.edu.cn"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print("Superuser created.")
else:
    print("Superuser already exists.")
