2509116050

<pre> 
 __          __ ______  _       _____  ____   __  __  ______ 
 \ \        / /|  ____|| |     / ____|/ __ \ |  \/  ||  ____|
  \ \  /\  / / | |__   | |    | |    | |  | || \  / || |__   
   \ \/  \/ /  |  __|  | |    | |    | |  | || |\/| ||  __|  
    \  /\  /   | |____ | |____| |____| |__| || |  | || |____ 
     \/  \/    |______||______|\_____|\____/ |_|  |_||______| 
     </pre>

# Program Manajemen Projek Multimedia

Program sederhana berbasis **Python (CLI)** untuk mengelola daftar projek multimedia (Video Editing).  
Dengan fitur **CRUD** (Create, Read, Update, Delete) dan Login Pengguna dengan Hak yang Berbeda
# Alur Program

## 1.Login Page
Menu ini akan tampil pada saat pertama kali program dijalankan, User di minta untuk login username beserta password
<img width="748" height="171" alt="image" src="https://github.com/user-attachments/assets/1247c280-be68-4a28-b6b9-0af6e46cd363" /><br/>
User di beri 3x kesempatan untuk login, jika gagal maka program akan terhenti<br/>
<img width="600" height="378" alt="image" src="https://github.com/user-attachments/assets/703af855-b708-4d1b-91ea-198e0547c71a" />
<br/>Jika login berhasil maka user akan di bawa ke menu Utama 
 
## 2. Menu Utama
Menu ini akan tampil setelah user login dengan akun ini adalah laman utama untuk memilih opsi, terdapat juga keterangan Role,  sebagai Viewer / Admin <br/>
<img width="566" height="273" alt="image" src="https://github.com/user-attachments/assets/a3daf656-49f3-4fbe-85f0-38dfe104de8f" />


                        
## 3.Menu Tambah Projek 
Menu ini berfungsi untuk menambahkan projek baru dengan detail:
- **Judul**
- **Jenis Konten** (Vlog, Short Movie, Dokumenter, Youtube, Reels, dll.)
- **Durasi** (detik)
- **Deadline** (DD-MM-YYYY)
- **Status** (Selesai/Belum)
<img width="751" height="435" alt="image" src="https://github.com/user-attachments/assets/1b3e6d22-6bdb-40d7-8e90-851943708784" />
<br/>Apabila akun hanya sebagai viewer maka tidak bisa menambahkan projek
<img width="516" height="224" alt="image" src="https://github.com/user-attachments/assets/d1bdba0d-ad1f-454e-948c-2d0b7b6581e3" />




## 4.Menu Hapus Projek
Menu ini berfungsi untuk menghapus projek dengan memasukan Nomor projek

<br/>**Alur:**
- Masukkan **nomor** projek yang ingin hapus.  
- Jika ditemukan, maka projek dengan nomor tersebut akan di hapus  
- Menampilkan pesan berhasil
  
> Catatan: Pencarian berdasarkan **nomor** projek
<img width="558" height="273" alt="image" src="https://github.com/user-attachments/assets/7bdd973b-7a12-484b-bdd9-3dcbbf466696" />
<br/>Jika login sebagai viewer maka tidak bisa menghapus projek
<br/><img width="467" height="281" alt="image" src="https://github.com/user-attachments/assets/923bb576-23f7-458a-b7e9-c79c750e533d" />


## 5.Menu Perbarui Projek  
Alur:
- Masukkan **nomor** projek yang ingin diperbarui.  
- Jika ditemukan, masukkan **status baru** (Selesai/Belum).  
- Data lain (judul/jenis/durasi/deadline) **tetap**, hanya status yang berubah.

> Catatan: Pencarian berdasarkan **nomor** projek

<img width="543" height="337" alt="image" src="https://github.com/user-attachments/assets/dffe3302-7b45-407d-b8ea-7c24f9aa8864" />
<br/>Jika login sebagai viewer maka tidak bisa memperbarui projek
<br/><img width="483" height="260" alt="image" src="https://github.com/user-attachments/assets/6dbcbf68-c093-4fee-a585-fcb4e2fc46f0" />

## 6.Menu List Projek 
Menu ini berfungsi untuk menampilkan seluruh projek yang tersimpan dalam bentuk tabel yang rapi.  
<img width="674" height="303" alt="image" src="https://github.com/user-attachments/assets/67fabafe-2b73-4159-a9c6-c7c69780ffc5" />



## 7.Menu Keluar 
Menu ini berfungsi untuk keluar dari program 

<br/>
<img width="234" height="112" alt="image" src="https://github.com/user-attachments/assets/2cc2d4c2-17af-4b80-afe9-f12dc6a1375e" />



# Error Handling

>Keyboardinterrupt dan EOFError dan exception info

<br/>
<img width="658" height="235" alt="image" src="https://github.com/user-attachments/assets/3f504316-bf9a-4a53-bd39-1bc4e0535c8e" />
<br/>
<img width="411" height="337" alt="image" src="https://github.com/user-attachments/assets/fe26d21b-de79-478a-bbf9-f28c825d87fe" />
<br/>
<img width="288" height="121" alt="image" src="https://github.com/user-attachments/assets/ce96492f-64d1-4301-8cb3-2c7172c2444f" />
<br/>
<img width="876" height="141" alt="image" src="https://github.com/user-attachments/assets/2cfed562-1ccc-43a8-b63e-055791e7dcd5" />
<br/>
>Input tidak valid / ValueError
<br/>
<img width="220" height="88" alt="image" src="https://github.com/user-attachments/assets/8f0a7999-6a5e-4e22-aa1b-f4f3b8352cd4" />
<br/>
<img width="445" height="125" alt="image" src="https://github.com/user-attachments/assets/fe11af31-0d6f-480c-a7d4-513d3510c2a6" />
<br/>
<img width="454" height="133" alt="image" src="https://github.com/user-attachments/assets/0c461e6a-fb09-4fd7-ab3b-81bdfc42dbc3" />
<br/>

<br/>





# Penjelasan Kode <br/>

## Import LIbrary, Inisiasi Data list of tuples dan dictionary akun
Prettytable di gunakan untuk mencetak tabel dengan rapih sementara itu pwinput digunakan untuk sensor password dengan bintang *
<br/>Variabel projek adalah list berisi tuple (judul, jenis, durasi, deadline, status). Ini jadi “database” awal sebelum ada penambahan/perubahan di runtime.
<br/>Daftar akun disimpan dalam dictionary akun agar mudah dicek saat login.
```
from prettytable import PrettyTable
import pwinput
projek = [
    ("Teaser PKKMB", "Vlog", "120", "20-09-2025", "Belum"),
    ("Short Film Desa", "Short Movie", "600", "30-09-2025", "Selesai"),
    ("Cinematic Motor", "Reels", "180", "25-09-2025", "-"),
    ("Dokumentasi Kampus", "Dokumenter", "900", "15-10-2025", "Belum"),
    ("Konten Tutorial Editing", "Youtube", "420", "05-10-2025", "-"),
    ("Tutorial Masak Royco", "Vlog", "90", "20-08-2020", "Selesai"),
    ("Podcast with Windah Batubara", "Youtube", "390", "20-08-2022", "Selesai"),
    ("Makan bang ft Young lex", "Vlog", "1390", "03-02-2020", "Belum"),
]

akun = {"fareru": "farel123",
        "relfa" : "rafel123",
        "admin123" : "bestofriendo"

```

##  Fungsi login dan role akun
- Program ini mengimplementasikan sistem login sebelum menu utama ditampilkan
- Pengguna harus memasukkan username dan password.
- Jika gagal login setelah 3x percobaan, program terhenti dan tidak menampilkan menu
- Jika login berhasil, program mengembalikan dua nilai, yaitu *terlogin* (nama pengguna) dan *status* (role pengguna: Owner atau Viewer).
- Setiap Fungsi CRUD Akan melakukan pengecekan jika akun tersebut hanya viewer maka tidak dapat mengaksesnya
 ```
if status == "Viewer":
            print("Maap Anda tidak ada ijin untuk memperbarui projek!")
            return
```



```
def login():
    kesempatan = 3
    while True:
        try:
            print("masukan username dan password!")
            username = input("Username:")
            password = pwinput.pwinput(prompt="Password: ", mask="*")
            if username in akun and akun[username] == password:
                print (f"login berhasil sebagai {username}")
                if username == "admin123":
                    return username,"Owner"
                else:
                    return username, "Viewer"
            else: 
                print ("Username/Password salah!!")
                kesempatan -=1
                print ("Sisa kesempatan:", kesempatan)
                if kesempatan <= 0 :
                    print("anda telah mencapai limit login sebanyak 3x")
                    break
                else:
                    continue
        except KeyboardInterrupt:
            print("Errorr CTRL + C")
        except EOFError:
            print ("Error CTRL + Z")
        except Exception as e:
            print (f"Terjadi kesalahan: {e}")
            
```

## Fungsi Tambah (Create)
Pada bagian ini, user diminta memasukkan lima komponen utama dari suatu projek yaitu:
- judul
- jenis
- durasi
- deadline
- status.
<br/>Data yang dimasukkan akan disimpan dalam bentuk list of tuple, kemudian ditambahkan ke dalam list projek dengan menggunakan fungsi .append().
Program menampilkan kembali data yang baru ditambahkan sebagai bentuk konfirmasi bahwa proses "Create" telah berhasil.
```
    def tambah(projek, status):
    try:
        if status == "Viewer":
            print("Maap Anda tidak ada ijin untuk menambah projek!")
            return
        namaprojek = input("Masukan nama projek:\n>>>")
        jeniskonten = input("Masukan jenis konten: \n Vlog, Short Movie, Dokumenter, Youtube, Reels, lainnya \n>>>")
        durasi = input ("Masukan durasi konten (dalam detik):\n>>>")
        deadline= input("Masukan deadline projek (DD-MM-YYYY):\n>>>")
        status_input = input("Masukan status:\n>>>")
        projek.append((namaprojek, jeniskonten, durasi, deadline, status_input))
        print(f"Berhasil menambahkan: {namaprojek}")
    except EOFError:
            print ("Error CTRL + Z")
    except KeyboardInterrupt:
        print("Errorr CTRL + C")
    except Exception as e:
        print(f"Terjadi kesalahan saat menambah projek: {e}")
        
```


## Fungsi Hapus (Delete)
- User diminta memasukkan nomor projek yang ingin dihapus.
- Program ini menggunakan input integer, kemudian di kurangi 1 agar sama urutannya dengan index []. Jika nomor tidak ditemukan, maka akan menampilkan pesan kesalahan.
Jika ditemukan, projek nya akan dihapus dengan metode .pop(), dan program menampilkan judul projek yang berhasil dihapus.
```
    def delete(projek, status):
    try:
        if status == "Viewer":
            print("Maap Anda tidak ada ijin untuk menghapus projek!")
            return
        try:
            cari = int(input("Masukkan Nomor projek yang mau dihapus: "))
        except ValueError:
            print("Input tidak valid! Nomor projek harus berupa angka.")
            return
        cari -=1
        if cari  < 0 or cari >= len(projek):
            print("Nomor projek tidak valid!")
            return
        terhapus = projek.pop(cari)
        print(f"Projek '{terhapus[0]}' berhasil dihapus.")
    except EOFError:
            print ("Error CTRL + Z")
    except KeyboardInterrupt:
        print("Errorr CTRL + C")
    except Exception as e:
        print(f"Terjadi kesalahan saat menghapus projek: {e}")
```

## Fungsi Perbarui (Update)
- user memasukkan nomor projek yang ingin diperbarui statusnya.
- program menggunakan input integer untuk menemukan indeks projek yang dimaksud.
- Jika ditemukan, elemen status pada tuple diganti dengan input yang dimasukkan oleh user, dan elemen lainnya hanya di duplikat  
- Program kemudian menampilkan pesan konfirmasi bahwa status telah berhasil diperbarui.
- jika tidak di temukan nomor proyek maka akan menampilkan pesan invalid
```
      def update(projek, status):
    try:
        if status == "Viewer":
            print("Maap Anda tidak ada ijin untuk memperbarui projek!")
            return
        try:
            update= int(input("Masukan nomor projek yang ingin di perbarui\n>>"))
        except ValueError:
            print("Input tidak valid! Nomor projek harus berupa angka.")
            return
        except EOFError:
            print ("Error CTRL + Z")
        except KeyboardInterrupt:
            print("Errorr CTRL + C")
            
        update -= 1
        if update < 0 or update >= len(projek):
            print("Nomor projek tidak valid!")
            return
        inputstatus = input("Update Status (Selesai/Belum) \n>>") 
        print("Menyimpan...")
        projek[update] = (    
            projek[update][0],
            projek[update][1],
            projek[update][2],
            projek[update][3],   
            inputstatus
        )
        print(f"projek '{projek[update][0]}' berhasil di perbarui ")
    except KeyboardInterrupt:
        print("\nDibatalkan oleh pengguna.")
    except Exception as e:
        print(f"Terjadi kesalahan saat memperbarui projek: {e}")

```



## Fungsi List Projek (Read)
Program menampilkan seluruh data projek dalam bentuk tabel dengan kolom:
- Nomor
- Judul
- Jenis
- Durasi
- Deadline
- Status
Pencetakan list disini menggunakan Library pretty table agar output tercetak dengan bentuk tabel yang rapi 
```
   def list(projek):
    try:
        tabel = PrettyTable()
        tabel.field_names = ["No", "Judul Projek", "Jenis", "Durasi", "Deadline", "Status"]

        for idx, p in enumerate(projek, start=1):
            tabel.add_row([idx, p[0], p[1], p[2], p[3], p[4]])

        print(tabel)
    except Exception as e:
        print(f"Terjadi kesalahan saat menampilkan projek: {e}")

```

## Menu Utama Program
- Mencetak ASCII ART bertuliskan "MULTIMEDIA"  
```
print ("""                                                                                 
,--.   ,--.,--. ,--.,--.,--------.,--.,--.   ,--.,------.,------.  ,--.  ,---.   
|   `.'   ||  | |  ||  |'--.  .--'|  ||   `.'   ||  .---'|  .-.  \ |  | /  O  \  
|  |'.'|  ||  | |  ||  |   |  |   |  ||  |'.'|  ||  `--, |  |  \  :|  ||  .-.  | 
|  |   |  |'  '-'  '|  '--.|  |   |  ||  |   |  ||  `---.|  '--'  /|  ||  | |  | 
`--'   `--' `-----' `-----'`--'   `--'`--'   `--'`------'`-------' `--'`--' `--'  """)

```

- Pemangilan Fungsi Login 1x saja 
```
terlogin, status = login()
```


- Kode Menu Utama menggunakan Pengulangan hingga user meminta menu 5 atau keluar dan menggunakan prettytable agar rapi
- Saat user memilih keluar, Menampilkan pesan penyimpanan data.
Menghentikan loop dengan break.
```
while True:
    
    if terlogin is None:
        print("Coba Lagi Nanti!")
        break
    
    else:
        tabel = PrettyTable()
        tabel.field_names = ["No", "Menu"]
        tabel.add_row(["1", "Tambah projek"])
        tabel.add_row(["2", "Hapus projek"])
        tabel.add_row(["3", "Update projek"])
        tabel.add_row(["4", "List projek"])
        tabel.add_row(["5", "Keluar"])
        print(tabel)
        print (f"Hallo {terlogin}! \nRole:{status}")
        try:
            userchoice = input("Pilih 1-5 atau Ketik opsi\n>>>") 
            if userchoice == "1" or userchoice == "Tambah":
                tambah(projek, status)

            elif userchoice =="2" or userchoice== "Hapus":
                delete(projek, status)

            elif userchoice == "3" or userchoice=="Update":
                update(projek, status)

            elif userchoice =="4" or userchoice=="List":
                list(projek)
                
            elif userchoice == "5" or userchoice=="Keluar":
                print("Menyimpan data....")
                #simpan data pakai json (next update)
                print("Data Tersimpan..") 
                break    
            else:
                print("Masukan input yang valid!")
        except EOFError:
            print ("Error CTRL + Z")
        except KeyboardInterrupt:
            print("Errorr CTRL + C")

```


## Mekanisme Error Handling 

Kode di atas di bagian input selalu di beri error handling try dan except gunanya untuk:
- 1.Jika user menekan Ctrl+Z / Ctrl+D, maka akan masuk ke blok except EOFError dan tampil pesan.
- 2.Jika user menekan Ctrl+C, maka program akan masuk ke except KeyboardInterrupt dengan pesan jelas.
- Jika user mengetik huruf atau simbol (contoh: abc), maka int("abc") akan gagal, dan ditangani oleh except ValueError.
-Jika ada error lain (misalnya karena bug internal), maka except Exception as e akan menangkap dan menampilkan pesan error.
```
try:
except EOFError:
 print ("Error CTRL + Z")
except KeyboardInterrupt:
 print("Errorr CTRL + C")
except ValueError:
 print("Input tidak valid! Nomor projek harus berupa angka.")
```

# Flowchart

![flowchart minpr2](https://github.com/user-attachments/assets/978f5b36-209b-4cff-9926-344bd1759bce)

