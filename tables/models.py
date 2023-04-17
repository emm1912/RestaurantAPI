from django.db import models
from django.db import models

class tables(models.Model):
    TABLE_AVAILABLE = 'Available'
    TABLE_RESERVED = 'Reserved'
    TABLE_OCCUPIED = 'Occupied'
    AVAILABILITY_CHOICES = [
        (TABLE_AVAILABLE, 'Available'),
        (TABLE_RESERVED, 'Reserved'),
        (TABLE_OCCUPIED, 'Occupied'),
    ]
    table_number = models.PositiveIntegerField(unique=True)
    seating_capacity = models.PositiveIntegerField()
    availability_status = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES, default=TABLE_AVAILABLE)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)
