from modeltranslation.translator import translator, TranslationOptions

from apps.client_side.our_services.models import Service


class ServiceTranslationOptions(TranslationOptions):
    fields = ("title",)


translator.register(Service, ServiceTranslationOptions)

