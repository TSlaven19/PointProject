from django.db import models


class Point(models.Model):
    point_name = models.CharField(max_length=200)
    point_value = models.SmallIntegerField(default=1)
    point_cooldown = models.SmallIntegerField(default=0)
    point_active = models.BooleanField(default=True)

    def __str__(self):
        return "'%s' is %i pt(s)" % (self.point_name, self.point_value)

    def save(self, *args, **kwargs):
        # if self.point_value < 1:
        # return
        # else:
        super().save(*args, **kwargs)


class Event(models.Model):
    point = models.ForeignKey(Point, on_delete=models.CASCADE)
    event_time = models.DateField(auto_now=True)
    both = "BTH"
    SCOREE_CHOICES = (("AMK", "Annaleise"), ("TDS", "Tobin"), (both, "We both"))
    event_scoree = models.CharField(max_length=3, choices=SCOREE_CHOICES, default=both)

    def __str__(self):
        return "%s scored %i pt(s)" % (self.event_scoree, self.point.point_value)

