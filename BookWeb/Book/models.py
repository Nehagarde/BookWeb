from django.db import models
from django.db import connection
# Create your models here.

class notify_me(models.Model):
    user_mail = models.CharField(max_length=1000)
    alert_price = models.DecimalField(max_digits=100,decimal_places=2)
    book_title = models.CharField(max_length=1000)

    def is_user_notified_already_book(self, user_email, book_title):
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM book_notify_me where user_mail = '" + user_email + "' AND book_title = '" + book_title + "' ")
        return cursor.fetchall()

    def update_ac_price(self, user_email, book_title, ac_price):
        with connection.cursor() as cursor:
            cursor.execute("UPDATE book_notify_me SET alert_price = " + ac_price +" WHERE user_mail=" + user_email + " and book_title='" + book_title + "'" )

        return 1

    def user_data_all(self):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM book_notify_me")

        return cursor.fetchall()

    def updated_is_notified(self, user_email, book_title):
        with connection.cursor as cursor:
            cursor.execute("UPDATE book_notify_me SET is_notified = 'F' WHERE user_mail = '" + user_email + "' AND book_title='" + book_title + "' ")

        return 1
