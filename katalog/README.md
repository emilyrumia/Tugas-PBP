# Aplikasi Heroku: KATALOG

> by Emily Rumia Naomi - 2106652700

Click [here](https://appkatalog.herokuapp.com/katalog/) to visit the app!


## 💡Buatlah dan Jelaskan bagan yang berisi request client ke web aplikasi berbasis Django
![Bagan Request Client](https://user-images.githubusercontent.com/112367959/190242874-d3a7e15e-a8ee-4234-9df5-c34594e5b2e7.png)


## 💡Jelaskan kenapa menggunakan virtual environment?
Virtual Environment adalah sebuah ruang lingkup virtual untuk menampung semua kebutuhan (seperti pustaka serta modul) dalam suatu proyek pekerjaan agar terisolasi.

Virtual Environment sangat berguna ketika kita membutuhkan dependencies yang berbeda-beda antara satu project dengan yang lainnya yang berjalan pada satu system operasi yang sama dikarenakan ada update atau perbedaan versi.

Virtual Environment biasa digunakan dalam Project menggunakan python. Dikarenakan, perbedaan versi python pada setiap perangkat sering berbeda-beda. Sehingga akan mengakibatkan masalah jika suatu project bergantung pada versi tertentu. Untuk mengatasi masalah tersebut, butuh sebuah wadah khusus, yaitu Virtual Enviroment yang akan menampung teknologi-teknologi yang digunakan untuk membuat suatu proyek. Gambarannya adalah jika kita membuat sebuah proyek 1 dan kita buat sebuah virtual environment 1 dan setelah itu ada juga proyek 2 dengan virtual environment 2. Maka semua kebutuhan proyek 1 bisa kita install pada virtual enviroment 2 dan dengan kebutuhuan proyek 2 kita dapat menginstall pada virtual enviroment 2. Contoh virtual enviroment pada python adalah venv.

## 💡Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Kita membuat aplikasi web berbasis Django menggunakan Development Environment dari framework Django. Development Enviroment ini memuat semua kebutuhan yang dibutuhkan Django pada komputer lokal kita. Jadi, sudah sangat lengkap dalam proses pengembangan dan pengujian aplikasi meggunakan Django sebelum proses publikasi di server utama (production environment).

Tools utama yang disediakan Django terdiri dari:
1. Seperangkat skrip python untuk memanage projek Django
2. Development server yang bisa digunakan untuk pengujian aplikasi Django di lokal komputer menggunakan browser di satu mesin yang sama 

Tools yang juga disediakan development environtment terdiri dari:
1. Text editor/ IDE 
2. Source control management, contohnya Git

Namun, untuk menjalankan proyek yang dibuat tanpa virtual enviroment kita harus menyiapkan file requirements.txt agar Heroku dapat mengenali semua kebutuhan yang harus di install dan dependensi Python. Dengan virtual enviroment, requirements.txt lebih mudah untuk dibuat sehingga  walau bisa tanpa virtual enviroment, tapi lebih baik menggunakan virtual enviroment, seperti venv.

## 💡Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.
Hasil pengimplementasian poin 1 dan 4 merupakan applikasi heroku [katalog](https://appkatalog.herokuapp.com/katalog/) yang sudah dicantumkan diatas. Cara-cara pengimplementasikan app tersebut, sebagai berikut:

1. Clone repositori yang sudah disiapkan pada Github
2. Masuk ke dalam repositori yang sudah diclone dan buatlah sebuah virtual environment (venv env)
3. Menyalakan virtual enviroment 
4. Menginstall dependecies yang dibutuhkan proyek 
5. Masukan proyek pada project_django
6. Membuat models.py yang berisikan fungsi dengan atribut-atribut untuk data
7. Melakukan migrasi skema model
8. Menghubungkan model dengan database untuk mengolah data yang akan ditampilkan
9. Membuat file views.py yang menerima parameter request dan render HTML yang akan dihasilkan dari template dan mengimport fungsi yang sudah di buat models.py
10. Membuat template HTML dengan desain UI yang kita mau tampilkan pada web browser
11. Membuat urls.py untuk routing terhadap fungsi views yang telah  dibuat sehingga nantinya halaman HTML dapat ditampilkan lewat browser
12. Setelah itu menjalankan proyek dengan run manage.py dan bisa cek melalui http://localhost:8000 
13. Menghubungkan Models dengan views dengan meng import models pada fungsi views
14. Menghubungjan Models dengan template dengan melakukan mapping terhadap data pada views.py sesuai variable dan juga dari database 
15. Jika semua sudah sesuai, melakukan add, commit, push untuk menyimpannya ke dalam repositori GitHub
16. Buat aplikasi baru pada heroku
17. Siapkan berkas dpl.yml di .github/workflows 
18. Masukan Heroku API Key dan App name pada bagian secrets GitHub
19. Jalankan deploy dpl.yml 
20. Setelah deploy berhasil, app sudah bisa diakses 

<hr>
Sekian, Terima Kasih!
