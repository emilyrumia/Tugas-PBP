# Aplikasi Heroku: TODOLIST

> by Emily Rumia Naomi - 2106652700

Click [here](https://appkatalog.herokuapp.com/todolist/) to visit the app!

## Tugas 6

## 💡Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
Pada Synchronous Programming Programming, kode dieksekusi secara berurutan. Suatu fungsi harus selesai dieksekusi terlebih dahulu baru fungsi selanjurnya bisa dieksekusi dan sama untuk selanjutnya. Namun pada Asynchronous Programming, sebaliknya, kode dieksekusi secara bersamaan. Walau suatu fungsi belum selesai dieksekusi, fungsi setelahnya dan seterusnya sudah bisa dieksekusi juga.

## 💡Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Event-driven programming adalah salah satu teknik pemogramman. Teknik yang dilakukan adalah dengan mengeksekusi program berdasarkan kejadian atau event tertentu.
Contoh penggunaan teknik ini pada tugas 6 adalah saat memencet tombol submit pada form addTask maka data akan ditambahkan dan ditampilkan dengan card.

## 💡Jelaskan penerapan asynchronous programming pada AJAX.
AJAX akan dijalankan saat terjadi sebuah kejadian atau event. Saat proses menjalankan, AJAX akan langsung mengeksekusi fungsi pada `views.py` yang dicantumkan melalui url di AJAX. Eksekusi langsung ini dapat langsung dilakukan secara bersamaan tanpa harus melewati proses client-request .

## 💡Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

**AJAX GET**
- Buatlah view baru yang mengembalikan seluruh data task dalam bentuk JSON.
  Membuka `views.py` pada folder aplikasi `todolist` dan membuat fungsi `show_json` untuk memproses data yang ada pada file `json`. Isi fungsi sebagai berikut:
     ``` shell
     def show_json(request):
      data_todolist = TaskList.objects.filter(user=request.user)   
      return HttpResponse(serializers.serialize('json', data_todolist), content_type="application/json")
     ```
- Buatlah path /todolist/json yang mengarah ke view yang baru kamu buat.
  Membuka `urls.py` pada foler aplikasi `todolist` dan mengimport fungsi baru diatas pada `views.py`. Isi sebagai berikut:
     ``` shell
     from todolist.views import show_json
     ```
  Menambahkan path fungsi tersebut ke dalam `urls.py` yang ada pada folder aplikasi `todolist` dengan menambahkan potongan kode berikut pada variabel `urlpatterns`
     ``` shell
     urlpatterns = [
      ...
      path('json/', show_json, name='json'),
      ...
     ]
     ```
- Lakukan pengambilan task menggunakan AJAX GET.
  Membuka `todolist.html` pada foler `templates` dan Menambahkan kode berikut untuk menggunakan AJAX
     ``` shell
     <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
     ```
  Membuat fungsi `ajax` untuk pengambilan data dan menampilkan dari file `json` di antara tag `<script>...</script>`
   > function load dan refresh pada file tugas 6 saya
   Menambahkan kode berikut untuk mendeteksi apakah DOM pada halaman HTML / web kita sudah siap digunakan. Jika sudah akan langsung menjalan fungsi sehingga memunculkan data 
     ``` shell
     $(document).ready(function() {
            refresh();
     });
     ```
**AJAX POST**
- Buatlah sebuah tombol Add Task yang membuka sebuah modal dengan form untuk menambahkan task.
  Membuka `todolist.html` pada foler `templates` dan menambahkan button add task untuk mentrigger munculnya modal
  Membuat modal menggunakan bootstrap dan didalam terdapat form untuk menambahkan task
- Buatlah view baru untuk menambahkan task baru ke dalam database.
   Membuka `views.py` pada folder aplikasi `todolist` dan membuat fungsi `show_add_task`. Isi fungsi sebagai berikut:
     ``` shell
     def show_add_task(request):
      if request.method == 'POST':
          user = request.user
          date = datetime.datetime.now()
          title = request.POST.get('title')
          description = request.POST.get('description')
          is_finished = False
          TaskList.objects.create(date=date, user=user, title=title, description=description, is_finished=is_finished)
          return JsonResponse({"Message": 'Your new task has been added!'},status=200)
      return redirect('todolist:todolist')
     ```
- Buatlah path /todolist/add yang mengarah ke view yang baru kamu buat.
  Membuka `urls.py` pada foler aplikasi `todolist` dan mengimport fungsi baru diatas pada `views.py`. Isi sebagai berikut:
     ``` shell
     from todolist.views import show_add_task
     ```
  Menambahkan path fungsi tersebut ke dalam `urls.py` yang ada pada folder aplikasi `todolist` dengan menambahkan potongan kode berikut pada variabel `urlpatterns`
     ``` shell
     urlpatterns = [
      ...
      path('add/', show_add_task, name='add-task'),
      ...
     ]
     ```
- Hubungkan form yang telah kamu buat di dalam modal kamu ke path /todolist/add
  Membuka `todolist.html` pada foler `templates` dan menambahkan fungsi AJAX untuk melakukan penambahan task melalui form dan didalam nya ada kode berikut untuk menghubungkan dengan path
  > function addTask pada file Tugas 6 saya
     ``` shell
     ...
     url: "{% url 'todolist:add-task' %}",
     ...
     ```
- Tutup modal setelah penambahan task telah berhasil dilakukan.
  Menambahkan kode berikut setelah berhasil submit form
     ``` shell
     ...
     $("#addModal").modal('hide')
     ...
     ```
  > function hideForm dalam file Tugas 6 saya
- Lakukan refresh pada halaman utama secara asinkronus untuk menampilkan list terbaru tanpa reload seluruh page
  Selalu menambahkan fungsi `refresh` setiap kali melakukan perubahan
