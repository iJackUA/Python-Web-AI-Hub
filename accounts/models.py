from django.db import models


class User(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=200)
    country_code = models.CharField(max_length=2)
    avatar = models.ImageField(default="default_avatar.png", upload_to="avatars")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.username} [{self.email}]"


class Organization(models.Model):
    short_code = models.CharField(max_length=3, unique=True)
    title = models.CharField(max_length=200)
    logo = models.ImageField(default="default_org_logo.png", upload_to="org_logos")
    users = models.ManyToManyField(
        User,
        related_name="memberships",
        through="Membership",
        through_fields=("organization", "user"),
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="created_organizations"
    )
    is_personal = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.short_code} [{self.title}]"


class Membership(models.Model):
    ROLES_CHOICES = (
        ("member", "Member"),
        ("owner", "Owner"),
        ("admin", "Admin"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="created_memberships"
    )
    role = models.CharField(max_length=20, choices=ROLES_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.user} - {self.organization}"
