from modeltranslation.translator import translator, TranslationOptions

from apps.v1.client_side.our_mission.models import OurMission


class OurMissionTranslationOptions(TranslationOptions):
    fields = ("content",)


translator.register(OurMission, OurMissionTranslationOptions)
