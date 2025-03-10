from bankApp.models.account import Account
from rest_framework import serializers

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['balance','lastChangeDate','isActive']
