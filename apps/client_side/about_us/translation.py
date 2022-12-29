from modeltranslation.translator import translator, TranslationOptions

from apps.client_side.about_us.models import AboutUs


class AboutUsTranslationOptions(TranslationOptions):
    fields = ("content",)


translator.register(AboutUs, AboutUsTranslationOptions)
