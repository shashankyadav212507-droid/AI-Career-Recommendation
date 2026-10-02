from django.db import models
from django.contrib.auth.models import User


# =========================================================
# CAREER PROFILE
# =========================================================

class CareerProfile(models.Model):

    # User who submitted the profile
    # null=True allows existing records to remain safe
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='career_profiles',
        null=True,
        blank=True
    )

    # Education
    education = models.CharField(
        max_length=100
    )

    # Programming languages
    programming_languages = models.TextField()

    # Technical skills
    technical_skills = models.TextField()

    # Career interests
    interests = models.TextField()

    # Experience level
    experience_level = models.CharField(
        max_length=50
    )

    # Preferred domain
    preferred_domain = models.CharField(
        max_length=100
    )

    # CGPA
    cgpa = models.DecimalField(
        max_digits=4,
        decimal_places=2
    )

    # Problem solving level
    problem_solving = models.CharField(
        max_length=50
    )

    # Work preference
    work_preference = models.CharField(
        max_length=50
    )

    # Work type
    work_type = models.CharField(
        max_length=50
    )

    # Date and time
    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):

        if self.user:

            return (
                f"{self.user.username} - "
                f"{self.preferred_domain}"
            )

        return (
            f"Guest - "
            f"{self.preferred_domain}"
        )


# =========================================================
# CAREER RECOMMENDATION HISTORY
# =========================================================

class CareerRecommendation(models.Model):

    # User who received this recommendation
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='career_recommendations'
    )

    # Recommended career
    career = models.CharField(
        max_length=100
    )

    # AI confidence percentage
    confidence = models.FloatField()

    # Top 3 career recommendations
    top_careers = models.JSONField(
        default=list
    )

    # AI generated career summary
    career_summary = models.TextField()

    # Career description
    description = models.TextField()

    # Relevant skills
    skills = models.JSONField(
        default=list
    )

    # Skills to learn
    learn = models.JSONField(
        default=list
    )

    # Career roadmap
    roadmap = models.JSONField(
        default=list
    )

    # Date and time
    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):

        return (
            f"{self.user.username} - "
            f"{self.career}"
        )