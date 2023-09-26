from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(username, email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    session_expiry = models.DateTimeField(default=timezone.now() + timezone.timedelta(days=1))

    objects = UserManager()

    def set_session_expiry(self):
        # Set session expiry to one day from the current time
        self.session_expiry = timezone.now() + timezone.timedelta(days=1)
        self.save()

    def is_session_expired(self):
        # Check if the session has expired
        if self.session_expiry is None:
            return True  # Session expiry not set, treat as expired
        return timezone.now() >= self.session_expiry

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
