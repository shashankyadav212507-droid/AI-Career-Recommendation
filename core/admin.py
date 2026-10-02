from django.contrib import admin

from .models import CareerProfile, CareerRecommendation


# =========================================================
# CAREER PROFILE ADMIN
# =========================================================

@admin.register(CareerProfile)
class CareerProfileAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'user',
        'education',
        'preferred_domain',
        'cgpa',
        'experience_level',
        'work_type',
        'created_at',
    )

    list_filter = (
        'education',
        'preferred_domain',
        'experience_level',
        'work_type',
    )

    search_fields = (
        'user__username',
        'education',
        'programming_languages',
        'technical_skills',
        'interests',
    )

    ordering = ('-created_at',)


# =========================================================
# CAREER RECOMMENDATION ADMIN
# =========================================================

@admin.register(CareerRecommendation)
class CareerRecommendationAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'user',
        'career',
        'confidence',
        'created_at',
    )

    list_filter = (
        'career',
        'created_at',
    )

    search_fields = (
        'user__username',
        'career',
        'career_summary',
        'description',
    )

    ordering = ('-created_at',)

    readonly_fields = (
        'created_at',
    )