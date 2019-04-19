from django.db import models
from django.contrib.postgres.fields import JSONField


class Human(models.Model):
    group_matched = models.BooleanField()
    distance_mi = models.IntegerField()
    content_hash = models.TextField()
    common_friends = JSONField()
    common_likes = JSONField()
    common_friend_count = models.IntegerField()
    common_like_count = models.IntegerField()
    connection_count = models.IntegerField()
    t_id = models.TextField()
    bio = models.TextField()
    birth_date = models.DateTimeField()
    name = models.TextField()
    ping_time = models.DateTimeField()
    photos = JSONField(null=True)
    jobs = JSONField()
    schools = JSONField()
    teaser = JSONField()
    teasers = JSONField()
    gender = models.IntegerField()
    birth_date_info = models.TextField()
    s_number = models.IntegerField()
    spotify_theme_track = JSONField(null=True)
    is_traveling = models.BooleanField(null=True)
    hide_age = models.BooleanField(null=True)
    hide_distance = models.BooleanField(null=True)
    instagram = JSONField(null=True)
    spotify_top_artists = JSONField(null=True)
    show_gender_on_profile = models.BooleanField(null=True)
    custom_gender = models.TextField(null=True)
    label = models.TextField(null=True)

    def __str__(self):
        return self.name
