from django.db import models


# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=100)
    open_time = models.TimeField(null=True, blank=True)
    close_time = models.TimeField(null=True, blank=True)
    capacity = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    # def __str__(self):
    #     return '(%s) %s' % (self.room.title, self.text)

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.PROTECT)
    date = models.DateField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    STATUSS = (
        ('A' , 'Approved'),
        ('P' , 'Pending approval'),
    )
    status = models.CharField(max_length=1, choices=STATUSS)
    status_remark = models.BooleanField(default=False)
    book_by = models.ForeignKey(User, on_delete=models.PROTECT)
    book_date = models.DateField(null=True, blank=True) 

    def __str__(self):
        return '(%s) %s' % (self.room.name, self.text)



