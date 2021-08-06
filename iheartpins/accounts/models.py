from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone

class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have a valid email address.')
        if not username:
            raise ValueError('Users must have a username.')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=254, null=False, unique=True)
    username = models.CharField(max_length=30, null=False, unique=True)
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    user_date_created = models.DateTimeField(verbose_name='date created', auto_now_add=True)
    user_last_edit = models.DateTimeField(verbose_name='last edit', default=timezone.now)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_active = models.BooleanField(verbose_name='active', default=True)
    is_superuser = models.BooleanField(verbose_name='superuser', default=False)
    is_admin = models.BooleanField(verbose_name='administrator', default=False)
    is_staff = models.BooleanField(verbose_name='staff', default=False)
    user_type = models.CharField(max_length=60, blank=True, null=True)
    user_status = models.CharField(max_length=60, blank=True, null=True)
    warning_flag = models.CharField(max_length=60, blank=True, null=True)
    # time_zone = models.CharField(max_length=255, default=timezone.get_default_timezone)
    uom_pref = models.CharField(max_length=30, blank=True, null=True)
    bal_trade_credits = models.IntegerField(blank=True, null=True)
    current_rating = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    user_notes = models.TextField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to='images', blank=True, null=True)

    objects = UserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class Person(models.Model):
    firstname = models.CharField(max_length=30, null=False)
    lastname = models.CharField(max_length=30, null=False)
    phone = models.CharField(max_length=30, blank=True, null=True)
    is_cellphone = models.BooleanField(default=True)
    user = models.OneToOneField(User, related_name='name', on_delete=models.CASCADE, primary_key=True)

    def fullname(self):
        return '{} {}'.format(self.firstname, self.lastname)

    def __str__(self):
        return self.fullname()



class Address(models.Model):
    person = models.ForeignKey(Person, related_name='address', on_delete=models.CASCADE)
    street1 = models.CharField(max_length=100)
    street2 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=75)
    state = models.CharField(max_length=30)
    postalcode = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    is_shipping = models.BooleanField(default=True)
    is_billing = models.BooleanField(default=True)
    is_inactive = models.BooleanField(default=False)


class TradeCredits(models.Model):
    user = models.ForeignKey(User, related_name='trade_credits', on_delete=models.CASCADE)
    credit = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Trade Credits'
        verbose_name_plural = 'Trade Credits'

