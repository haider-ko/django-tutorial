from django.db import IntegrityError
from django.forms import ValidationError
from rest_framework import serializers
from .models import Competencies, CompetenciesProfiency, PerformanceIndicator


class CompetenciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competencies
        fields = '__all__'


class CompetenciesProficiencySerializer(serializers.ModelSerializer):
    class Meta:
        model = CompetenciesProfiency
        fields = ('competency_id', 'proficiency_level')


class PerformanceIndicatorSerializer(serializers.ModelSerializer):
    # A nested list of 'edit' items.
    competencies = CompetenciesProficiencySerializer(many=True)

    class Meta:
        model = PerformanceIndicator
        fields = (
            'id',
            'designation',
            'department',
            'competencies',
            'active',
            'created_at',
            'updated_at',
        )

    def create(self, validated_data):
        competencies_data = validated_data.pop('competencies')

        # Use a transaction to ensure atomicity
        performance_indicator = PerformanceIndicator.objects.create(
            **validated_data)

        # Create CompetenciesProfiency instances
        for competency_data in competencies_data:
            CompetenciesProfiency.objects.create(
                performance_indicator=performance_indicator,
                **competency_data
            )

        return performance_indicator
