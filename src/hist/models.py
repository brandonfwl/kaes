from django.db import models

class Freezer61(models.Model):
    temp = models.FloatField(blank=True, null=True)
    time_stamp = models.BigIntegerField(blank=True, null=True)
    p_key = models.AutoField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'freezer61'

class Freezer62(models.Model):
    temp = models.FloatField(blank=True, null=True)
    time_stamp = models.BigIntegerField(blank=True, null=True)
    p_key = models.AutoField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'freezer62'
