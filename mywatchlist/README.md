# Aplikasi Heroku: MYWATCHLIST

> by Emily Rumia Naomi - 2106652700

Click [here]() to visit the app!

## 💡Jelaskan perbedaan antara JSON, XML, dan HTML!


## 💡Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

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
    {
        "model":"mywatchlist.watchlist",
        "pk":1,
        "fields":{
            "title_movie":"The Invisible Guest",
            "release_date":"January 6, 2017",
            "rating_movie": "8/10",
            "review_movie" :"The first half of the movie is flawless, the characters seem interesting enough, and the plot is enthralling. You know you're  in for some really good movie time. As the movie progresses, the mystery starts to unravel, but then there are sudden plot twists that you probably didn't see coming.",
            "watched_status" :"Watched"
        }
    },
    {
        "model":"mywatchlist.watchlist",
        "pk":2,
        "fields":{
            "title_movie":"Orphan: First Kill",
            "release_date":"August 31, 2022",
            "rating_movie":"6/10",
            "review_movie" :"Absolutely brilliant. This is exactly how psychological horrors should be produced. This felt just as suspenseful and impactful as the original 2009 movie. Smart, witty script followed by brilliant acting from the cast and the main protagonist who slipped back into her role without any noticeable difference.",
            "watched_status" :"Haven't watch"
        }
    },
    {
        "model":"mywatchlist.watchlist",
        "pk":3,
        "fields":{
            "title_movie":"The Dark Knight Rises",
            "release_date":"July 20, 2012",
            "rating_movie": "8.4/10",
            "review_movie" :"'Dark Knight' was a whole new beast altogether be it storyline, plot, visuals, character development everything was etched to  perfection there was not a single thing that I disliked about the movie. It is when superheros are made more human more susceptible to damage mentally or physically who have relationship, fellings, shortcomings, fear, despair is when you as audience connect with them you find a part of yourself within them as if they are real people",
            "watched_status":"Watched"
        }
    },
    {
        "model":"mywatchlist.watchlist",
        "pk":4,
        "fields":{
            "title_movie":"Collateral",
            "release_date":"August 6, 2004",
            "rating_movie":"7.5/10", 
            "review_movie" :"The screenplay is brilliant and has all the makings of a perfect action thriller. While there is some compelling character drama, there are also a few twists which are thrown in very well. Cinematography is excellent, especially during the action sequences.",
            "watched_status":"Haven't watch"
        }
    },
    {
        "model":"mywatchlist.watchlist",
        "pk":5,
        "fields":{
            "title_movie":"May the Devil Take You Too",
            "release_date":"February 27, 2020 ",
            "rating_movie":"6/10",
            "review_movie" :"There are some creepy moments, but ultimately ruined by nonsensical character behaviour, mostly not running whenever they get the chance, falling and dragging across the floor for no reason and screaming in anger followed by being passive.",
            "watched_status" :"Watched"
        }
    },
    {
        "model":"mywatchlist.watchlist",
        "pk":6,
        "fields":{
            "title_movie":"why did you kill me?",
            "release_date":"April 14, 2021",
            "rating_movie":"5.6/10",
            "review_movie":"A good mockumentary, but the irritating thing about it is the fact that it highlights how disgusting society has become & the absolute lack of discipline; it's like stating the absolute obvious",
            "watched_status":"Haven't watch"
        }
    },
    {
        "model":"mywatchlist.watchlist",
        "pk":7,
        "fields":{
            "title_movie":"Do Revenge",
            "release_date":"September 16, 2022",
            "rating_movie":"6.5/10", 
            "review_movie":"It's funny, a little hint of sadness, and whole lot of REVENGE! It's definitely a must watch",
            "watched_status":"Haven't watch"
        }
    },
    {
        "model":"mywatchlist.watchlist",
        "pk":8,
        "fields":{
            "title_movie":"Friendzone",
            "release_date":"March 20, 2019",
            "rating_movie":"7.2/10",
            "review_movie":"One of the most well done Thai romcoms! All encapsulating the well-written script, a heartwarming yet emotional story of Gink and Palm navigating the ups and downs of friendship and romance.",
            "watched_status":"Watched"
        }
    },
    {
        "model":"mywatchlist.watchlist",
        "pk":9,
        "fields":{
            "title_movie":"Impetigore",
            "release_date":"October 17, 2019",
            "rating_movie":"6.6/10",
            "review_movie":"The storyline makes the viewer anticipating and wondering, also it has a fast pace of storyline where you don't have to wait for a 'horror silent moment' to past throught to go to the next scene. The cinematography is terrifyingly great!",
            "watched_status":"Haven't watch"
        }
    },
    {
        "model":"mywatchlist.watchlist",
        "pk":10,
        "fields":{
            "title_movie":"White Chicks",
            "release_date":"June 23, 2004",
            "rating_movie":"5.7/10",
            "review_movie":"White chicks is one of those daft 'put your brain on hold' films that makes you laugh because it's genuinely silly, and great fun. Doesn’t matter how many times I watch this movie, it always puts a smile on my face.",
            "watched_status": "Watched"
        }
    }
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
    insert!!!
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
    path(...),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    ...
    ```
 
## 💡Mengakses tiga URL menggunakan Postman

<hr>
Sekian, Terima Kasih!
