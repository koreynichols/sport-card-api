from django.db import models

# Create your models here.
class card(models.Model):
    player_name = models.CharField(max_length = 50)
    card_company = models.CharField(max_length = 20)
    card_set = models.CharField(max_length = 20)
    year = models.PositiveSmallIntegerField(blank=True, null=True)
    sport = models.CharField(max_length = 15)
    team = models.CharField(max_length = 50)
    rookie_card = models.BooleanField()
    auto = models.BooleanField()
    relic = models.BooleanField()
    relic_type = models.CharField(max_length = 25)
    numbered = models.BooleanField()
    numbered_to = models.PositiveSmallIntegerField()
    card_img = models.ImageField(upload_to='images/')