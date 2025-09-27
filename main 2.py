from prettytable import PrettyTable
import pwinput
projek = [("Teaser PKKMB", "Vlog", "120", "20-09-2025", "Belum"),
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
    
}

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

def list(projek):
    try:
        tabel = PrettyTable()
        tabel.field_names = ["No", "Judul Projek", "Jenis", "Durasi", "Deadline", "Status"]

        for idx, p in enumerate(projek, start=1):
            tabel.add_row([idx, p[0], p[1], p[2], p[3], p[4]])

        print(tabel)
    except Exception as e:
        print(f"Terjadi kesalahan saat menampilkan projek: {e}")

print ("""                                                                                 
,--.   ,--.,--. ,--.,--.,--------.,--.,--.   ,--.,------.,------.  ,--.  ,---.   
|   `.'   ||  | |  ||  |'--.  .--'|  ||   `.'   ||  .---'|  .-.  \ |  | /  O  \  
|  |'.'|  ||  | |  ||  |   |  |   |  ||  |'.'|  ||  `--, |  |  \  :|  ||  .-.  | 
|  |   |  |'  '-'  '|  '--.|  |   |  ||  |   |  ||  `---.|  '--'  /|  ||  | |  | 
`--'   `--' `-----' `-----'`--'   `--'`--'   `--'`------'`-------' `--'`--' `--'  """)

#perulangan agar program tetap berjalan sampai user menginput keluar

terlogin, status = login()
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
                print("Data Tersimpan..") 
                break    
            else:
                print("Masukan input yang valid!")
        except EOFError:
            print ("Error CTRL + Z")
        except KeyboardInterrupt:
            print("Errorr CTRL + C")