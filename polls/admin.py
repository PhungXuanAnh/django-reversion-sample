from django.contrib import admin
from reversion.admin import VersionAdmin
from reversion_compare.admin import CompareVersionAdmin

from .models import Choice, Question

@admin.register(Choice)
class ChoiceAdmin(CompareVersionAdmin):
    pass

@admin.register(Question)
class QuestionAdmin(CompareVersionAdmin):
    pass
