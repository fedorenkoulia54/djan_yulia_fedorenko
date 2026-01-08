from django.db import models

class Post(models.Model):
    date = models.DateField("Дата")
    temperature = models.FloatField("Температура, °C")
    pressure = models.FloatField("Тиск, мм рт. ст.")
    wind_speed = models.FloatField("Швидкість вітру, м/с")
    precipitation = models.FloatField("Ймовірність опадів, %")

    def __str__(self):
        return str(self.date)
