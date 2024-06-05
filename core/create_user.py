# Create users
from django.contrib.auth.models import User, Permission

user1 = User.objects.create_user('user1', 'user1@example.com', 'password123')
user2 = User.objects.create_user('user2', 'user2@example.com', 'password123')
user3 = User.objects.create_user('user3', 'user3@example.com', 'password123')

# Create permissions
permission1 = Permission.objects.get_or_create(codename='can_view_posta_and_Su', name='can view posta and Su')[0]
permission2 = Permission.objects.get_or_create(codename='Can_view_AT_and_Su', name='Can view AT and Su')[0]
permission3 = Permission.objects.get_or_create(codename='Can_view_mobile', name='Can view mobile')[0]

# Assign permissions to users
user1.user_permissions.add(permission1)
user2.user_permissions.add(permission2)
user3.user_permissions.add(permission3)