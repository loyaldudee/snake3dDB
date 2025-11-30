from rest_framework import serializers
from .models import Player, Score

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['username', 'player_code', 'created_at']
        read_only_fields = ['player_code', 'created_at']

class ScoreSerializer(serializers.ModelSerializer):
    # We want to show the player's name in the score list, not just their ID
    player_name = serializers.CharField(source='player.username', read_only=True)

    class Meta:
        model = Score
        fields = ['player_name', 'points', 'played_at']