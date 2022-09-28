# Aplikasi Heroku: TODOLIST

> by Emily Rumia Naomi - 2106652700

Click [here](https://appkatalog.herokuapp.com/todolist/) to visit the app!
- [Login](https://appkatalog.herokuapp.com/todolist/login) 
- [Register](https://appkatalog.herokuapp.com/todolist/register) 
- [Create Task](https://appkatalog.herokuapp.com/todolist/create-task) 
- [Logout](https://appkatalog.herokuapp.com/todolist/logout/) 

## 💡Apa kegunaan `{% csrf_token %}` pada elemen `<form>`? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen `<form>`?

`{% csrf_token %}` adalah token yang digunakan untuk menjaga keamanan, khusunya melindungi dari CSRF (Cross Site Request Forgery) Attack. Tanpa adanya token ini, form akan tetap berjalan dengan baik, namun akan memudahkan pihak eksternal website tersebut mengakses data karena request akan diterima tanpa adanya verifikasi atau validasi. 

## 💡Apakah kita dapat membuat elemen `<form>` secara manual (tanpa menggunakan generator seperti `{{ form.as_table }}`)? Jelaskan secara gambaran besar bagaimana cara membuat `<form>` secara manual.

Kita tetap dapat membuat elemen `<form>` secara manual tanpa menggunakan generator seperti `{{ form.as_table }}`. Kita hanya perlu menambahkan manual elemen `<form>` disertai dengan `{% csrf_token %}` untuk keamanan. Setelah itu memasukan field dengan elemen `<input>` type nya disesuaikan dengan jenis data yang ingin diterima dan juga elemen `<input type="submit">` untuk mengirim data dari POST request kepada django database. 

## 💡Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

User akan mengisi data pada HTML form dan melakukan penyimpanan data pada database dengan mengklik input bertipe submit yang sebelumnya akan diperiksa. Jika data valid, form akan menjalankan request POST tersebut. Data tersebut setelah itu akan disimpan pada database sesuai dengan atribut-atribut `models.py` yang sudah ada. Dari penyimpanan data berdasarkan atribut-atribut tersebut kita bisa mengakses dan mengatur untuk menampilkan pada template HTML kita dengan menghubungkan atau memproses data tersebut pada `views.py`.

## 💡Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
Berikut merupakan tahapan-tahapan yang saya lakukan untuk melengkapi checklist diatas:
1. Membuat suatu aplikasi baru bernama todolist di proyek tugas Django yang sudah digunakan sebelumnya
   - Menjalankan virtual environment terlebih dahulu.
     ```shell
     python -m venv env
     source env/bin/activate
     pip install -r requirements.txt
     ```
   - Membuat aplikasi `django-app` bernama `todolist` pada repositori tugas 2 dengan perintah
     ```shell
     python manage.py startapp todolist
     ```
   - Menambahkan aplikasi todolist ke dalam variabel `INSTALLED_APPS` pada `settings.py` di folder `project_django`
     ```shell
     INSTALLED_APPS = [
     ...,
     'todolist',
     ]
     ```
   
2. Menambahkan path `todolist` sehingga pengguna dapat mengakses `http://localhost:8000/todolist`
   - Membuat sebuah folder bernama `templates` di dalam folder aplikasi `todolist` dan membuat sebuah berkas bernama `todolist.html`. Isi sesuai dengan ketentuan saya ingin menunjukan data.
   - Membuka views.py yang ada pada folder `todolist` dan membuat sebuah fungsi `show_todolist` yang menerima parameter request dan mengembalikan render(request, "todolist.html")
     ```shell
     def show_todolist(request):
      return render(request, "todolist.html", context)
     ```
   - Membuat sebuah file di dalam folder aplikasi `todolist` bernama `urls.py` untuk melakukan routing terhadap fungsi views yang telah dibuat. Isi dari `urls.py` tersebut adalah sebagai berikut:
     ```shell
     from django.urls import path
     from todolist.views import show_todolist
     
     app_name = 'todolist'

     urlpatterns = [
      path('', show_todolist, name='todolist'),
     ]
     ```
   - Menambahkan aplikasi `todolist` ke dalam `urls.py` yang ada pada folder `project_django` dengan menambahkan potongan kode berikut pada variabel `urlpatterns`
     ``` shell
     ...
     path('todolist/', include('todolist.urls')),
     ...
     ```
3. Membuat sebuah model yang memiliki atribut user, date, title, dan description:
   - Menambahkan kode pada `models.py` di folder `todolist` dengan atribut-atribut sebagai berikut:
     ```shell
     from django.contrib.auth.models import User

     class TaskList(models.Model):
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      date = models.DateField()
      title = models.CharField(max_length=255)
      description = models.TextField()
     ```
    - Menjalankan perintah tersebut untuk mempersiapkan migrasi skema model ke dalam database Django lokal
     ```shell
     python manage.py makemigrations
     ```
   - Menjalankan perintah tersebut untuk menerapkan skema model yang telah dibuat ke dalam database Django lokal
     ```shell
     python manage.py migrate
     ```
4. Mengimplementasikan form registrasi, login, dan logout agar pengguna dapat menggunakan todolist dengan baik.
   > Registrasi
   - Membuka `views.py` pada folder aplikasi `todolist` dan mengimport `redirect`, `UserCreationForm`, dan `messages`
     ```shell
     from django.shortcuts import redirect
     from django.contrib.auth.forms import UserCreationForm
     from django.contrib import messages
     ```
   - Membuat fungsi `register` untuk menghasilkan formulir registrasi secara otomatis dan menghasilkan akun pengguna ketika data di-submit dari form
     ```shell
     def register(request):
      form = UserCreationForm()

      if request.method == "POST":
        form = UserCreationForm(request.POST)
          if form.is_valid():
            form.save()
            messages.success(request, 'Account has been created successfully!')
            return redirect('todolist:login')
          else:
            messages.info(request, 'Check your input!')
      context = {'form':form}
      return render(request, 'register.html', context)
     ```
   - Membuat berkas HTML baru dengan nama `register.html` pada folder `templates`. Isi sesuai dengan ketentuan saya ingin meminta data registrasi.
   > Login
   - Membuka `views.py` pada folder aplikasi `todolist` dan mengimport `authenticate` dan `login`
     ```shell
     from django.contrib.auth import authenticate, login
     ```
   - Membuat fungsi `login` untuk mengautentikasi pengguna yang ingin login
     ```shell
     def login_user(request):
       if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todolist:todolist')
        else:
            messages.info(request, 'Wrong Username or Password!')
      context = {}
      return render(request, 'login.html', context)
     ```
   - Membuat berkas HTML baru dengan nama `login.html` pada folder `templates`. Isi sesuai dengan ketentuan saya ingin meminta data login.
   > Logout
   - Membuka `views.py` pada folder aplikasi `todolist` dan mengimport `logout`
     ```shell
     from django.contrib.auth import logout
     ```
   - Membuat fungsi `logout` untuk melakukan mekanisme logout
     ```shell
     def logout_user(request):
      logout(request)
      return redirect('todolist:login')
     ```
     
5. Membuat halaman utama todolist yang memuat username pengguna, tombol Tambah Task Baru, tombol logout, serta tabel berisi tanggal pembuatan task, judul task, dan deskripsi task.
   > Memuat Username Pengguna
   - Membuka `views.py` dan menambahkan kode berikut untuk mengakses data dari model `Task` dan mendapatkan `username`
     ```shell
     def show_todolist(request):
      data_todolist = Task.objects.filter(user=request.user)
      context = {
      'data_todolist': data_todolist,
      'username': request.user.get_username(),
      }
      return render(request, "todolist.html", context)
     ```
   - Menambahkan text berikut pada `todolist.html` untuk memuat `Username Pengguna` pada halaman utama todolist
     ```shell
     <h2>Welcome {{username}}!</h2>
     ```
   > Tombol Tambah Task Baru
   - Menambahkan `button` pada `todolist.html` untuk menambah task baru
     ```shell
     <button><a href="{% url 'todolist:create-task' %}">Create Task</a></button>
     ```
   > Tombol Logout
   - Menambahkan `button` pada `todolist.html` untuk melakukan `logout`
     ```shell
     <button><a href="{% url 'todolist:logout' %}">Logout</a></button>
     ```
   > Tabel berisi tanggal pembuatan task, judul task, dan deskripsi task
   - Menambahkan `table` pada `todolist.html` dengan kode sebagai berikut:
     ```shell
     <table>
      <tr>
        <th>Date</th>
        <th>Title Task</th>
        <th>Description</th>
      </tr>
      {% for list in data_todolist %}
          <tr>
              <th>{{list.date}}</th>
              <th>{{list.title}}</th>
              <th>{{list.description}}</th>
          </tr>
      {% endfor %}
     </table>
     ```
6. Membuat halaman form untuk pembuatan task. Data yang perlu dimasukkan pengguna hanyalah judul task dan deskripsi task.
   - Membuat file baru `forms.py` pada folder aplikasi `todolist` dengan isi sebagai berikut:
     ``` shell
     from django import forms

     class TaskForm(forms.Form):
       title = forms.CharField(label="Enter your task!", max_length=255)
       description = forms.CharField(label="Describe your task!", widget=forms.Textarea)
     ```
   - Membuka `views.py` pada folder aplikasi `todolist` dan membuat fungsi `show_create_task` untuk memproses data yang diterima Django website. Isi fungsi sebagai berikut:
     ``` shell
     def show_create_task(request):
      if request.method == 'POST':
          form = TaskForm(request.POST)
          if form.is_valid():
              user = request.user
              date = datetime.datetime.now()
              title = form.cleaned_data["title"]
              description = form.cleaned_data["description"]
              is_finished = False
              Task.objects.create(date=date, user=user, title=title, description=description, is_finished=is_finished)
              messages.success(request, 'Your new task has been added!')
              return redirect('todolist:todolist')
      else:
          form = TaskForm()
      return render(request, 'create-task.html', {'form': form})
     ```
   - Membuat file baru `create-user.html` pada folder `templates` untuk membuat halaman form pembuatan task. Isi sebagai berikut untuk menampilkan form dan lainnya sesuai dengan ketentuan saya mau meminta data pembuatan task:
     ``` shell
     <form action="" method="POST">
       {% csrf_token %}
         {% for field in form %}
            <div class= "fieldWrapper">
                <div>{{ field.label_tag }}</div>
                <div>{{ field }}</div>
            </div>
       {% endfor %}
       <input id ="btn" type="submit" value="Daftar">
     </form>
     ```
7. Membuat routing sehingga beberapa fungsi dapat diakses melalui URL `http://localhost:8000/todolist`, `http://localhost:8000/todolist/login`, `http://localhost:8000/todolist/register`, `http://localhost:8000/todolist/create-task`, dan `http://localhost:8000/todolist/logout`
   - Membuka `urls.py` pada foler aplikasi `todolist` dan mengimport fungsi-fungsi pada `views.py`. Isi sebagai berikut:
      ``` shell
     from todolist.views import register
     from todolist.views import login_user
     from todolist.views import logout_user
     from todolist.views import show_create_task
     from todolist.views import show_todolist
     ```
   - Menambahkan path-path fungsi tersebut ke dalam `urls.py` yang ada pada folder aplikasi `todolist` dengan menambahkan potongan kode berikut pada variabel `urlpatterns`
     ``` shell
     urlpatterns = [
      path('register/', register, name='register'),
      path('login/', login_user, name='login'),
      path('logout/', logout_user, name='logout'),
      path('create-task/', show_create_task, name='create-task'),
      path('', show_todolist, name='todolist'),
     ]
     ```
8. Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
   - Melakukan `git add`, `git commit` dan `git push` ke dalam repositori github
   - Dikarenakan sudah membuat aplikasi `heroku`, pada repository tugas 2 sudah ada file `dpl.yml`, dan sudah mengisi Secrets untuk GitHub Actions `(Settings -> Secrets -> Actions)` pada variabel repository secret untuk melakukan deployment. Maka deployment akan otomatis terjadi.
    ``` shell
    HEROKU_API_KEY: <VALUE_API_KEY_ANDA>
    HEROKU_APP_NAME: <NAMA_APLIKASI_HEROKU_ANDA>
    ```
9. Membuat dua akun pengguna dan tiga dummy data menggunakan model Task pada akun masing-masing di situs web Heroku.
   > Membuat dua akun
   - Registrasi Akun 1: `cleoasenna`
     ![Registrasi Akun 1](https://user-images.githubusercontent.com/112367959/192631439-e7639bf8-74d8-41be-a940-39b0cf7e5776.png)
   - Akun 1: `cleoasenna` berhasil ditambahkan
     ![Akun 1 berhasil](https://user-images.githubusercontent.com/112367959/192631476-4acab5be-bc19-4f08-a800-30a0c6bd49b2.png)
   - Registrasi Akun 1: `kesyenna`
     ![Registrasi Akun 2](https://user-images.githubusercontent.com/112367959/192631498-ed62349f-6276-4035-afda-02e05c60ac5d.png)
   - Akun 2: `kesyenna` berhasil ditambahkan
     ![Akun 2 berhasil](https://user-images.githubusercontent.com/112367959/192631505-42d8debc-3766-45ec-93ab-3b3c55641a60.png)
   > Tiga dummy data
   - Login Akun 1 : `cleoasenna`
     ![Login Akun 1](https://user-images.githubusercontent.com/112367959/192633436-57d416df-73e3-411d-826f-4bb21e1fa516.png)
   - Halaman awal (masih kosong) Akun 1 : `cleoasenna`
     ![Awal Akun 1](https://user-images.githubusercontent.com/112367959/192633205-876949f8-218f-431f-ab45-d39a72c03a83.png)
   - Create Task
     ![Task Akun 1](https://user-images.githubusercontent.com/112367959/192633217-e8a78027-430c-41bc-83d5-7c8965bb3482.png)
   - Halaman `todolist` Akun 1 setelah membuat 3 Tasks
     ![Akun 1](https://user-images.githubusercontent.com/112367959/192633514-41aea447-dd01-4db2-b2db-0d4033ea953b.png)
   - Login, Halaman Awal, Create Task Akun 2 sama prosesnya
   - Halaman `todolist` Akun 2 setelah membuat 3 Tasks
     ![Akun 2](https://user-images.githubusercontent.com/112367959/192633523-a160cd16-580e-448e-b16b-2265939a690a.png)
<hr>
Sekian, Terima Kasih!
