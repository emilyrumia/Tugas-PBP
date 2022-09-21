# Aplikasi Heroku: MYWATCHLIST

> by Emily Rumia Naomi - 2106652700

Click [here](https://appkatalog.herokuapp.com/mywatchlist/) to visit the app!
- [HTML](https://appkatalog.herokuapp.com/mywatchlist/html/)
- [XML](https://appkatalog.herokuapp.com/mywatchlist/xml/)
- [JSON](https://appkatalog.herokuapp.com/mywatchlist/json/)

## 💡Jelaskan perbedaan antara JSON, XML, dan HTML!
- JSON (JavaScript Object Notation)
  - JSON menyimpan semua datanya dalam format map (key / value) yang rapi dan lebih mudah untuk dipahami
  - JSON adalah format pertukaran data ringan yang jauh lebih mudah bagi komputer untuk mengurai data yang sedang dikirim
  - Lebih sulit dibaca dari XML
  - Ekstensi file XML adalah .json
- XML (Extensible Markup Language)
  - XML menawarkan kalian untuk menentukan elemen markup dan menghasilkan bahasa markup yang disesuaikan
  - XML digunakan untuk menyimpan dan mengangkut data dari satu aplikasi ke aplikasi lain melalui Internet, namun lebih lama dari JSON
  - XML menyimpan data dalam format teks mirip dengan HTML sehingga mudah dibaca manusia
  - Ekstensi file XML adalah .xml
- HTML (HyperText Markup Language)
  - HTML menyajikan data dengan format teks dilengkapi dengan tag
  - Format penampilan data HTML ditujukan dalam pembuatan sebuah aplikasi web browser.
  - Ekstensi file XML adalah .html

## 💡Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
   Dalam penggunaan sebuah platform, sering terjadi pertukaran data. Data delivery ini dibutuhkan untuk memudahkan proses pertukaran data tersebut. Data yang dikirimkan mempunyai beberapa format, seperti HTML, XML, dan JSON. Format-format ini membantu agar data mudah dibaca oleh manusia, bahasa pemrograman, dan juga API. 

## 💡Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
Berikut merupakan tahapan-tahapan yang saya lakukan untuk melengkapi checklist diatas dan menghasilkan aplikasi mywatchlist
1. Membuat aplikasi `django-app` bernama `mywatchlist` pada repositori tugas 2 dengan perintah 
   > poin 1
   ```shell
   python -m venv env
   source env/bin/activate
   pip install -r requirements.txt
   python manage.py startapp mywatchlist
   ```
2. Menambahkan aplikasi `mywatchlist` ke dalam variabel `INSTALLED_APPS` pada `settings.py` di folder `project_django`
   ```shell
   INSTALLED_APPS = [
    ...,
    'mywatchlist',
   ]
   ```
3. Menambahkan kode pada `models.py` di folder `mywatchlist` dengan atribut-atribut sebagai berikut:
   > poin 3
   ```shell
   class WatchList(models.Model):
    title_movie = models.TextField()
    release_date = models.CharField(max_length=800)
    rating_movie = models.CharField(max_length=4)
    review_movie = models.TextField()
    watched_status = models.CharField(max_length=200)
   ```
4. Menjalankan perintah tersebut untuk mempersiapkan migrasi skema model ke dalam database Django lokal
   ```shell
   python manage.py makemigrations
   ```
5. Menjalankan perintah tersebut untuk menerapkan skema model yang telah dibuat ke dalam database Django lokal
   ```shell
   python manage.py migrate
   ```
6. Membuat sebuah folder `fixture` di dalam aplikasi `mywatchlist` dan membuat file `initial_mywatchlist_data.json` untuk memberikan data kepada atribut      pada `models.py` yang berisi 10 data
   > poin 4
   ```shell
   [
   ...
    {
        "model":"mywatchlist.watchlist",
        "pk":1,
        "fields":{
            "title_movie":"...",
            "release_date":"...",
            "rating_movie": ".../10",
            "review_movie" :"...",
            "watched_status" :"Watched/Haven't watch"
        }
    }, 
    ...
   ]
   ```
7. Menjalankan perintah tersebut untuk memasukkan data ke dalam database Django lokal
   ``` shell
   python manage.py loaddata initial_wishlist_data.json
   ```
8. Membuat sebuah folder bernama `templates` di dalam folder aplikasi `mywatchlist` dan buatlah sebuah berkas bernama `mywatchlist.html` untuk mengatur letak data yang akan ditampilkan pada aplikasi
9. Menambahkan kode sebuah fungsi pada `views.py` yang ada pada folder `mywatchlist`
   ``` shell
   from mywatchlist.models import WatchList
   def show_mywatchlist(request):
    return render(request, "mywatchlist.html", context)

   data_movie_mywatchlist = WatchList.objects.all()
   context = {
    'data_movies': data_movie_mywatchlist,
    'nama': 'Emily Rumia Naomi',
    'npm' : '2106652700',
   }
   ```
10. Membuat sebuah berkas di dalam folder aplikasi `mywatchlist` bernama `urls.py` untuk melakukan routing terhadap fungsi views yang dibuat buat sehingga  nantinya halaman HTML dapat ditampilkan lewat browser-mu. Isi dari `urls.py` tersebut adalah sebagai berikut
    ``` shell
    from django.urls import path
    from mywatchlist.views import show_mywatchlist
   
    app_name = 'mywatchlist'
   
    urlpatterns = [
     path('', show_mywatchlist, name='show_mywatchlist'),
    ]
    ```
11. Menambahkan aplikasi `mywatchlist` ke dalam `urls.py` yang ada pada folder `project_django` dengan menambahkan potongan kode berikut pada variabel `urlpatterns`
    > poin 2
    ``` shell
    ...
    path('mywatchlist/', include('mywatchlist.urls')),
    ...
    ```
12. Pada file `views.py` yang ada pada folder `mywatchlist`, import `HttpResponse` dan `Serializer` pada bagian paling atas
    ``` shell
    from django.http import HttpResponse
    from django.core import serializers
    ```
13. Untuk menembalikan data pada format `HTML`, tambahkan sebuah fungsi `show_html` pada `views.py` yang berisi
    > poin 5.1
    ``` shell
    def show_html(request):
    return render(request, "mywatchlist.html", context)
    ```
14. Untuk mengembalikan data pada format `XML`, tambahkan sebuah fungsi `show_xml` pada `views.py` yang berisi
    > poin 5.2
    ``` shell
    def show_xml(request):
    data = WatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    ```
15. Untuk menembalikan data pada format `JSON`, tambahkan sebuah fungsi `show_json` pada `views.py` yang berisi
    > poin 5.3
    ``` shell
    def show_json(request):
    data = WatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    ```
16. Menambahkan path `'html/'`, `'xml/'`, dan `'json/'` ke dalam `urls.py` yang ada pada folder `mywatchlist` dengan menambahkan potongan kode berikut pada variabel `urlpatterns`
    > poin 6
    ``` shell
    ...
    path('html/', show_html, name='show_html'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    ...
    ```
 17. Setelah itu melakukan `git add`, `git commit`, dan `git push` ke dalam repository yang ada di github
 18. Dikarenakan repository pada tugas 2, sudah ada file `dpl.yml`, membuat aplikasi `heroku` dan sudah mengisi Secrets untuk GitHub Actions `(Settings -> Secrets -> Actions)` pada variabel repository secret untuk melakukan deployment. Maka deployment akan otomatis terjadi.
    > poin 7
    ``` shell
    HEROKU_API_KEY: <VALUE_API_KEY_ANDA>
    HEROKU_APP_NAME: <NAMA_APLIKASI_HEROKU_ANDA>
    ```

## 💡Mengakses tiga URL menggunakan Postman
- [HTML](https://appkatalog.herokuapp.com/mywatchlist/html/)
  ![Postman HTML](https://user-images.githubusercontent.com/112367959/191556649-5d26cba4-6a47-4317-8b5a-a11330768705.png)
- [XML](https://appkatalog.herokuapp.com/mywatchlist/xml/)
  ![Postman XML](https://user-images.githubusercontent.com/112367959/191557825-254eb404-f884-4783-adc7-51a4fd7dd65c.png)
- [JSON](https://appkatalog.herokuapp.com/mywatchlist/json/)
  ![Postman JSON](https://user-images.githubusercontent.com/112367959/191557417-32a8543c-e01d-4362-a527-3e718f818ba6.png)
  
## 💡Menambahkan unit test pada tests.py untuk menguji bahwa tiga URL di poin 6 dapat mengembalikan respon HTTP 200 OK
   1. Menambahkan kode berikut pada `tests.py` dalam folder `mywatchlist`
      ``` shell
      from django.test import TestCase, Client
      from django.urls import resolve
       class test_watchlist(TestCase):
        def test_html_url(self):
           client = Client()
           response = client.get('/mywatchlist/html/')
           self.assertEqual(response.status_code, 200)

        def test_xml_url(self):
           client = Client()
           response = client.get('/mywatchlist/xml/')
           self.assertEqual(response.status_code, 200)

        def test_json_url(self):
           client = Client()
           response = client.get('/mywatchlist/json/')
           self.assertEqual(response.status_code, 200)
      ``` 
   2. Setelah itu menjalan `python manage.py tests` dan menghasilkan seperti screenshoot dibawah ini
      ![Test](https://user-images.githubusercontent.com/112367959/191558762-1d504d56-af7b-4e97-876a-952f30859d09.png)
    
<hr>
Sekian, Terima Kasih!
