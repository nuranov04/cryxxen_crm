from modeltranslation.translator import translator, TranslationOptions

from apps.v1.client_side.partners.models import Partner


class PartnerTranslationOptions(TranslationOptions):
    fields = ("title",)


translator.register(Partner, PartnerTranslationOptions)

