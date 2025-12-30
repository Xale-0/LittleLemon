from django.db import models
from django.core.validators import MinValueValidator

class Booking(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID')

    name = models.CharField(max_length=255, db_column='Name')
    no_of_guests = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        db_column='No_of_guests',
    )
    booking_date = models.DateTimeField(db_column='BookingDate')

    class Meta:
        db_table = 'Booking'

    def __str__(self) -> str:
        return f'{self.name} ({self.no_of_guests}) @ {self.booking_date}'


class Menu(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID')

    title = models.CharField(max_length=255, db_column='Title')
    price = models.DecimalField(max_digits=10, decimal_places=2, db_column='Price')
    inventory = models.PositiveIntegerField(
        validators=[MinValueValidator(0)],
        db_column='Inventory',
    )

    class Meta:
        db_table = 'Menu'

    def __str__(self) -> str:
        return f'{self.title} - ${self.price}'