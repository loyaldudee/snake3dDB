from rest_framework import serializers
from .models import Player, Score

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['username', 'player_code', 'created_at']
        read_only_fields = ['player_code', 'created_at']

class ScoreSerializer(serializers.ModelSerializer):
    # RENAME FIELDS TO MATCH UNITY:
    # Unity expects 'name', 'score', and 'date'
    name = serializers.CharField(source='player.username', read_only=True)
    score = serializers.IntegerField(source='points', read_only=True)
    date = serializers.DateTimeField(source='played_at', format="%Y-%m-%d", read_only=True)

    class Meta:
        model = Score
        # We list the "new" names here
        fields = ['name', 'score', 'date']