from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


"""
    Interest Model
"""
# class Interest(models.Model):
#     name = models.CharField( max_length=100, unique=True)
#     # member = models.ManyToManyField(Member, related_name='member', blank=True)

#     def __str__(self) -> str:
#         return self.name

"""
    MyMemberManager Model
"""
class MyMemberManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, password=None):
        if not email:
            raise ValueError('Members must have an email address')
        if not username:
            raise ValueError('Members must have a username')

        user = self.model(
                email=self.normalize_email(email),
                username=username,
                first_name=first_name,
                last_name=last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, first_name, last_name, password):
        user = self.create_user(
                email=self.normalize_email(email),
                password=password,
                username=username,
                first_name=first_name,
                last_name=last_name, 
            )

        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
        
"""
    Member model
"""
class Member(AbstractBaseUser):
    # Constants
    GENDER_C = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other")
    ]

    ED_LEVEL_C = [
        ("Secondary", "Secondary"),
        ("Post-Secondary", "Post-Secondary"),
        ("Tertiary", "Tertiary"),
        ("Masters", "Masters"),
        ("PhD", "PhD"),
    ]

    BELIEFS_C = [
        ("Christianity", "Christianity"),
        ("Muslim", "Muslim"),
        ("Other", "Other"),
    ]

    ROLE_C = [
        ('Lister', "Lister"),
        ('Tenant', "Tenant"),
        ('Landlord', "Landlord")
    ]


    # required fields
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(
        verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # other fields
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    age = models.IntegerField(null=True)
    preferred_location = models.CharField(max_length=300, null=True)
    gender = models.CharField(
        max_length=50, blank=True, null=True, choices=GENDER_C)
    display_photo = models.ImageField(
        upload_to='members/', default='members/default_dp.jpg', null=True, blank=True)
    banner_photo = models.ImageField(
        upload_to='members/', default='members/default_bp.jpg', null=True, blank=True)
    description = models.TextField(null=True, max_length=400)
    education_level = models.CharField(
        max_length=20, choices=ED_LEVEL_C, default=None, null=True, blank=True)
    occupation = models.CharField(
        max_length=500, null=True)
    beliefs = models.CharField(
        max_length=12, choices=BELIEFS_C, default=None, null=True, blank=True)
    current_address = models.CharField(max_length=600, blank=True, null=True)
    interests = models.CharField(max_length=600, blank=True, null=True)
    budget = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)
    role = models.CharField(max_length=50, choices=ROLE_C, default=None, null=True, blank=True)
    # liked_apartments = models.ManyToOneRel(
    #     INTERESTS_C, related_name='liked_apartments', blank='true')
    # favourites = models.ManyToManyField(
    #     settings.AUTH_USER_MODEL, related_name='favourites', blank='true')
    # rejected_connections = models.ManyToManyField(
    #     settings.AUTH_USER_MODEL, related_name='rejected_connections', blank='true')

    # email
    # age
    # prefered location
    # gender
    # display photo
    # banner photo
    # description
    # education
    # occupation
    # beliefs
    # interests
    # address
    # favourites
    # connections
    # rejected_connections
    # liked apartments

    # phone number
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    # REQUIRED_FIELDS = []


    objects = MyMemberManager()


    def __str__(self) -> str:
        return self.email

    def get_full_name(self):
        # The user is identified by their email address
        return self.last_name + ', ' + self.first_name

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True


