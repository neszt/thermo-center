from django.contrib import admin
from heatcontrol import models

admin.site.register(models.DayType)
admin.site.register(models.Calendar)
admin.site.register(models.Control)
admin.site.register(models.Profile)
admin.site.register(models.ScheduledOverride)
admin.site.register(models.InstantProfile)
admin.site.register(models.InstantProfileEntry)
admin.site.register(models.InstantOverride)