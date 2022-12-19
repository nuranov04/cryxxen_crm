from django.db import models

from utils.models import BaseModel


class Achievement(BaseModel):
    pass

    def __str__(self):
        return str(self.id)
