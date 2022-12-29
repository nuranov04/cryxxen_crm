from modeltranslation.translator import translator, TranslationOptions

from apps.client_side.our_projects.models import Project


class ProjectTranslationOptions(TranslationOptions):
    fields = ("title",)


translator.register(Project, ProjectTranslationOptions)
