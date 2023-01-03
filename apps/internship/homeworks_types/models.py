# from django.db import models
#
# from apps.internship.groups.models import Bunch
#
#
# class HomeworkType(models.Model):
#     title = models.CharField(
#         max_length=256
#     )
#     group = models.ForeignKey(
#         Bunch,
#         on_delete=models.CASCADE,
#         related_name="group_homeworks_types"
#     )
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         verbose_name = "Homework type"
#         verbose_name_plural = "Homework types"
#         ordering = ("title",)
