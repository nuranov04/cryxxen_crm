from modeltranslation.translator import translator, TranslationOptions

from apps.client_side.our_team.models import Team


class TeamTranslationOptions(TranslationOptions):
    fields = ("first_name", "last_name", "age", "position")


translator.register(Team, TeamTranslationOptions)

