from django.db import models
import random
import string

# Helper function to generate a random code (e.g., 'X7B9')
def generate_player_code():
    length = 6
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choices(chars, k=length))

class Player(models.Model):
    # The name typed by the user in Unity
    username = models.CharField(max_length=50)
    
    # The permanent random code (e.g., "A1B2")
    # unique=True ensures no two players have the exact same code globally
    # editable=False means it cannot be changed in the admin panel easily
    player_code = models.CharField(
        max_length=10, 
        default=generate_player_code, 
        unique=True, 
        editable=False
    )
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username}#{self.player_code}"

class Score(models.Model):
    # Links the score to a specific Player
    # on_delete=models.CASCADE means if the Player is deleted, their scores are too
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='scores')
    
    points = models.IntegerField()
    played_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.player.username} - {self.points}"
    
    class Meta:
        # Default ordering: Newest scores first
        ordering = ['-played_at']