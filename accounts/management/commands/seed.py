from django.core.management.base import BaseCommand

from accounts.factories import UserFactory, OrganizationFactory, MembershipFactory


class Command(BaseCommand):
    help = "Seed database with initial data for local development"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING("Start seeding"))

        user1 = UserFactory()
        user2 = UserFactory()

        org1 = OrganizationFactory(created_by=user1, is_personal=True)
        org2 = OrganizationFactory(created_by=user2, is_personal=True)
        org3 = OrganizationFactory(created_by=user1, is_personal=False)

        MembershipFactory(user=user1, organization=org1)
        MembershipFactory(user=user2, organization=org2)
        MembershipFactory(user=user1, organization=org3)
        MembershipFactory(user=user2, organization=org3)

        self.stdout.write(self.style.SUCCESS("Seeding finished"))
