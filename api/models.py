from djongo import models

SEX = (
    ('M', 'M'),
    ('F', 'F'),
)


class Athlete(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    sex = models.CharField(max_length=100, choices=SEX, default=None, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)


class Events(models.Model):
    age = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    games = models.CharField(max_length=100)
    season = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    sport = models.CharField(max_length=100)
    event = models.CharField(max_length=100)
    medal = models.CharField(max_length=20, blank=True, null=True)
    athlete_id = models.IntegerField()
    noc = models.CharField(max_length=3, blank=True, null=True)
    team = models.CharField(max_length=60, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)