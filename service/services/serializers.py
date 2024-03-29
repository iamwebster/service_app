from rest_framework import serializers
from .models import Subsctiption, Plan


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = "__all__"


class SubscriptionSerializer(serializers.ModelSerializer):
    plan = PlanSerializer()
    client_name = serializers.CharField(source="client.company_name")
    email = serializers.CharField(source="client.user.email")
    price = serializers.SerializerMethodField()

    def get_price(self, instance):
        # return instance.service.full_price - instance.service.full_price * (
        #     instance.plan.discount_percent / 100
        # )
        return instance.price

    class Meta:
        model = Subsctiption
        fields = ("id", "plan", "client_name", "email", 'price')
