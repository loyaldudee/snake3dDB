from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Player, Score
from .serializers import PlayerSerializer, ScoreSerializer

# --- 1. REGISTER PLAYER ---
@api_view(['POST'])
def register_player(request):
    username = request.data.get('name') 
    
    if not username:
        return Response({"error": "Name is required"}, status=status.HTTP_400_BAD_REQUEST)

    player = Player.objects.create(username=username)
    serializer = PlayerSerializer(player)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

# --- 2. SUBMIT SCORE ---
@api_view(['POST'])
def submit_score(request):
    player_code = request.data.get('player_code')
    points = request.data.get('score')

    if not player_code or points is None:
        return Response({"error": "Player code and score are required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        player = Player.objects.get(player_code=player_code)
    except Player.DoesNotExist:
        return Response({"error": "Invalid player code"}, status=status.HTTP_404_NOT_FOUND)

    Score.objects.create(player=player, points=points)
    
    return Response({"message": "Score submitted successfully"}, status=status.HTTP_201_CREATED)

# --- 3. GET GLOBAL LEADERBOARD ---
@api_view(['GET'])
def get_leaderboard(request):
    top_scores = Score.objects.select_related('player').order_by('-points')[:10]
    serializer = ScoreSerializer(top_scores, many=True)
    return Response(serializer.data)