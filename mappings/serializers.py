
from rest_framework import serializers

from .models import PatientDoctorMapping


class PatientDoctorMappingSerializer(serializers.ModelSerializer):
    # Read-only details included in API responses
    patient_name = serializers.CharField(
        source="patient.name",
        read_only=True,
    )
    doctor_name = serializers.CharField(
        source="doctor.name",
        read_only=True,
    )
    doctor_specialization = serializers.CharField(
        source="doctor.specialization",
        read_only=True,
    )

    class Meta:
        model = PatientDoctorMapping
        fields = (
            "id",
            "patient",
            "patient_name",
            "doctor",
            "doctor_name",
            "doctor_specialization",
            "assigned_at",
        )
        read_only_fields = ("id", "assigned_at")

    def validate(self, data):
        request = self.context.get("request")

        if request is None or not request.user.is_authenticated:
            raise serializers.ValidationError(
                "Authentication required."
            )

        # For partial updates, retain existing values when omitted.
        instance = getattr(self, "instance", None)
        patient = data.get(
            "patient",
            instance.patient if instance else None,
        )
        doctor = data.get(
            "doctor",
            instance.doctor if instance else None,
        )

        if patient is None or doctor is None:
            raise serializers.ValidationError(
                "Both patient and doctor are required."
            )

        if patient.created_by_id != request.user.id:
            raise serializers.ValidationError(
                "You can only assign doctors to your own patients."
            )

        # Exclude this record when checking an existing mapping.
        duplicates = PatientDoctorMapping.objects.filter(
            patient=patient,
            doctor=doctor,
        )

        if instance is not None:
            duplicates = duplicates.exclude(pk=instance.pk)

        if duplicates.exists():
            raise serializers.ValidationError(
                "This doctor is already assigned to this patient."
            )

        return data
