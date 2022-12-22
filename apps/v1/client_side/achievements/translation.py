from modeltranslation.translator import translator, TranslationOptions

from apps.v1.client_side.achievements.models import Achievement


class AchievementTranslationOptions(TranslationOptions):
    fields = ("content",)


translator.register(Achievement, AchievementTranslationOptions)
