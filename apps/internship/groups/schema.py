import graphene

from graphene_django.types import DjangoObjectType

from apps.internship.groups.models import Bunch


class BunchType(DjangoObjectType):
    class Meta:
        model = Bunch


class Query(graphene.AbstractType):
    all_bunch = graphene.List(BunchType)

    def resolve_all_bunch(self, args):
        return Bunch.objects.all()
