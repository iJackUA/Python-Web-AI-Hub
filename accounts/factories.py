import factory
import random
from .models import User, Organization, Membership
from PIL import ImageColor


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("user_name")
    full_name = factory.Faker("name")
    email = factory.LazyAttribute(lambda o: "%s@example.com" % o.username)
    country_code = factory.Faker("country_code")
    avatar = factory.django.ImageField(color=random.choice(list(ImageColor.colormap)))


class OrganizationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Organization

    short_code = factory.Transformer(
        factory.Faker("pystr", min_chars=3, max_chars=3), transform=str.upper
    )
    title = factory.Faker("company")
    logo = factory.django.ImageField(color=random.choice(list(ImageColor.colormap)))
    is_personal = False
    created_by = factory.SubFactory(UserFactory)


class MembershipFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Membership

    organization = factory.SubFactory(OrganizationFactory)
    user = factory.SubFactory(UserFactory)
    role = "admin"
    created_by = factory.LazyAttribute(lambda o: o.user)
