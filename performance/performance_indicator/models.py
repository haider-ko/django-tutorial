from django.db import models


class Competencies(models.Model):
    COMPETENCY_TYPES = [
        ('technical', 'Technical'),
        ('organizational', 'Organizational')
    ]
    id = models.AutoField(primary_key=True)  # Add the ID field
    competency_name = models.CharField(max_length=100)
    competency_definition = models.TextField()
    competency_type = models.CharField(max_length=20, choices=COMPETENCY_TYPES)

    def __str__(self):
        return self.competency_name


class PerformanceIndicator(models.Model):
    PROFICIENCY_CHOICES = [
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
        ('Expert/Leader', 'Expert/Leader')
    ]
    id = models.AutoField(primary_key=True)  # Add the ID field
    designation = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.designation


class CompetenciesProfiency(models.Model):
    PROFICIENCY_CHOICES = [
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
        ('Expert/Leader', 'Expert/Leader')
    ]
    competency_id = models.ForeignKey(Competencies, on_delete=models.CASCADE)
    proficiency_level = models.CharField(
        max_length=20, choices=PROFICIENCY_CHOICES)
    performance_indicator = models.ForeignKey(
        PerformanceIndicator, related_name='competencies', on_delete=models.CASCADE, null=True, blank=True)
