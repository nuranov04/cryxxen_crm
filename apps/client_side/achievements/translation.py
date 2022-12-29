from modeltranslation.translator import translator, TranslationOptions

from apps.client_side.achievements.models import Achievement


class AchievementTranslationOptions(TranslationOptions):
    fields = ("content",)


translator.register(Achievement, AchievementTranslationOptions)
