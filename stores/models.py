from django.db import models

class Store(models.Model):
    store_id = models.CharField(max_length=20, primary_key=True)
    timezone_str = models.CharField(max_length=50, default='UTC')

    def __str__(self):
        return f"Store ID: {self.store_id}, Timezone: {self.timezone_str}"


class StoreStatus(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, default=None)
    timestamp_utc = models.DateTimeField(default=None)
    status = models.CharField(max_length=50, default='')

    def __str__(self):
        return f"Store ID: {self.store.store_id}, Timestamp: {self.timestamp_utc}, Status: {self.status}"


class StoreHours(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, default=None)
    # store_id = models.CharField(max_length=20, null=True)  # Change to CharField
    day = models.IntegerField(choices=((0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')))
    start_time_local = models.TimeField(default=None)
    end_time_local = models.TimeField(default=None)

    def __str__(self):
        return f"Store ID: {self.store.store_id}, Day of Week: {self.get_day_of_week_display()}, Start Time: {self.start_time_local}, End Time: {self.end_time_local}"
