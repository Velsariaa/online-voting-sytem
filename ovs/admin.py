from django.contrib import admin
from .models import Candidate

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'cotn', 'emailaddr', 'position']  # Add fields you want to display
