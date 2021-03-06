import factory
from factory.django import DjangoModelFactory

from ..models.repository import Repository


class RepositoryFactory(DjangoModelFactory):
    url = factory.Faker('url')
    display_name = factory.Faker('pystr', max_chars=80)
    team = factory.SubFactory('v1.teams.factories.team.TeamFactory')

    class Meta:
        model = Repository
