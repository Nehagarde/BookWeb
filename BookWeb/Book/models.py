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


class book_data(models.Model):
    title = models.CharField(max_length=1000)
    author = models.CharField(max_length=1000)
    cover_type = models.CharField(max_length=1000)
    genre = models.CharField(max_length=1000)
    actual_price = models.DecimalField(max_digits=100,decimal_places=2)
    discounted_price = models.DecimalField(max_digits=100,decimal_places=2)
    current_date = models.DateField()
    img_url = models.CharField(max_length=1000)
    product_url = models.CharField(max_length=1000)
    count = models.IntegerField()
    wed_comp = models.CharField(max_length=1000)

    def get_title_and_author_data(self):
        title_author=[]
        cursor = connection.cursor()
        cursor.execute("select DISTINCT(title) from book_book_data where author <> 'nan' order by rand() limit 10000")
        title_author.append(cursor.fetchall())
        cursor.execute("select distinct title as CompleteAddress from book_book_data where author = 'nan' order by rand() limit 10000")
        title_author.append(cursor.fetchall())
        return title_author

    def get_all_fiction_books(self):
        title_author = []
        cursor = connection.cursor()
        cursor.execute(
            "select DISTINCT(title),img_url  from book_book_data where author <> 'nan' and `genre` = 'fiction' and `img_url` like '%.jpg' order by RAND() limit 100")
        title_author.append(cursor.fetchall())
        cursor.execute(
            "select distinct title as CompleteAddress,img_url  from book_book_data where author = 'nan' and `genre` = 'fiction' and `img_url` like '%.jpg' order by RAND() limit 100")
        title_author.append(cursor.fetchall())
        return title_author

    def get_all_non_fiction_books(self):
        title_author = []
        cursor = connection.cursor()
        cursor.execute(
            "select DISTINCT(title),img_url  from book_book_data where author <> 'nan' and `genre` = 'nonfiction' and `img_url` like '%.jpg' order by RAND() limit 100")
        title_author.append(cursor.fetchall())
        cursor.execute(
            "select distinct title as CompleteAddress,img_url  from book_book_data where author = 'nan' and `genre` = 'non-fiction' and `img_url` like '%.jpg' order by RAND() limit 100")
        title_author.append(cursor.fetchall())
        return title_author

    def get_all_education_books(self):
        title_author = []
        cursor = connection.cursor()
        cursor.execute(
            "select DISTINCT(title),img_url  from book_book_data where author <> 'nan' and `genre` = 'education' and `img_url` like '%.jpg' order by RAND() limit 100")
        title_author.append(cursor.fetchall())
        cursor.execute(
            "select distinct title as CompleteAddress,img_url  from book_book_data where author = 'nan' and `genre` = 'education' and `img_url` like '%.jpg' order by RAND() limit 100")
        title_author.append(cursor.fetchall())
        return title_author

    def get_all_romance_books(self):
        title_author = []
        cursor = connection.cursor()
        cursor.execute(
            "select DISTINCT(title),img_url  from book_book_data where author <> 'nan' and `genre` = 'romance' and `img_url` like '%.jpg' order by RAND() limit 100")
        title_author.append(cursor.fetchall())
        cursor.execute(
            "select distinct title as CompleteAddress,img_url  from book_book_data where author = 'nan' and `genre` = 'romance' and `img_url` like '%.jpg' order by RAND() limit 100")
        title_author.append(cursor.fetchall())
        return title_author

    def get_all_business_books(self):
        title_author = []
        cursor = connection.cursor()
        cursor.execute(
            "select DISTINCT(title),img_url  from book_book_data where author <> 'nan' and `genre` = 'business' and `img_url` like '%.jpg' order by RAND() limit 100")
        title_author.append(cursor.fetchall())
        cursor.execute(
            "select distinct title as CompleteAddress,img_url  from book_book_data where author = 'nan' and `genre` = 'business' and `img_url` like '%.jpg' order by RAND() limit 100")
        title_author.append(cursor.fetchall())
        return title_author

    def get_book_details(self, name):
        str1 = str(name).strip().upper()
        details = []
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM `book_book_data` WHERE title in (SELECT UCASE(title) from `book_book_data`) and title like \"" + str1 + "\" group by wed_comp")
        details.append(cursor.fetchall())
        return details

    def get_books(self, name):
        str1 = str(name)
        lst = str1.split(" ")
        j_name = '%' + '%'.join(lst) + '%'
        details = []
        cursor = connection.cursor()
        cursor.execute(
            "SELECT DISTINCT(title),img_url FROM `book_book_data` WHERE title in (SELECT UCASE(title) from `book_book_data`) and title like \"" + j_name + "\"")
        details.append(cursor.fetchall())
        return details

    def count_increment(self, url):
        with connection.cursor() as cursor:
            cursor.execute("UPDATE book_book_data SET count = count + 1 WHERE product_url = %s", [url])
        return 1

    def get_books_count(self):
        cursor = connection.cursor()
        cursor.execute("select count(DISTINCT title),genre from book_book_data GROUP BY genre")
        return cursor.fetchall()

    def get_book_price_for_price_check(self, book_name):
        date = "2019-02-04%"
        cursor = connection.cursor()
        cursor.execute(
            "select discounted_price,product_url,wed_comp from book_book_data where title = \"" + book_name + "\" and wed_comp='Flipkart'")
        return cursor.fetchall()

