from django.db import models

# Create your models here.
class card(models.Model):
    player_name = models.charField(maxLength = 50)
    card_company = models.charField(maxLength = 20)
    card_set = models.charField(maxLenght = 20)
    year = models.PositiveSmallIntegerField(blank=True, null=True)
    sport = models.charField(maxLength = 15)
    team = models.charField(maxLength = 50)
    rookie_card = models.BooleanField()
    auto = models.BooleanField()
    relic = models.BooleanField()
    relic_type = models.charField(maxLength = 25)
    numbered = models.BooleanField()
    numbered_to = models.PositiveSmallIntegerField()
    card_img = models.ImageField(upload_to='images/')