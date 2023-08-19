#Import Socket
import socket
#Import Datetime
from datetime import datetime

#Membaca File database_location.py Sebagai Database Kota dan Nama Bandara Lokasi Transit
with open("database_location.py", "r") as f:
    loc = f.readlines()
    loc = [item.replace("\n", "") for item in loc]
    
#Membaca File database_board.py Sebagai Database Tanggal dan Waktu Jadwal Boarding
with open("database_board.py", "r") as f:
    board = f.readlines()
    board = [item.replace("\n", "") for item in board]

#Deklarasi IP, Port, Buffer Size
tcp_ip = '26.58.170.203' #IP Server VPN
tcp_port = 8085
buffer_size = 4096

#Penggunaan TCP Socket & Membuat Objek Socket Baru
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Memautkan Socket Dengan Address dan Port
s.bind(('26.58.170.203', 8085))
#Membuat Socket Dalam Posisi “mendengarkan” Koneksi Yang Ingin Terhubung
s.listen(1)

#Deklarasi Variabel now Berisi Tanggal dan Waktu Sekarang
now = datetime.now()

#Print Ouput
print("\n Tanggal dan Waktu hari ini :", str(now))

#Deklarasi Variabel reschedule Bernilai False
reschedule = False

#Kondisi Dimana Waktu Sekarang Lebih Dari Waktu Yang Sudah Ditentukan
#Maka Variabel reschedule Bernilai True
if datetime.now() >= datetime(2023, 1, 3, 19, 30, 00):
    reschedule = True

#Kondisi Dimana Variabel reschedule True atau False
#Jika Kondisi reschedule Bernilai True, Maka Akan Menampilkan Lokasi Transit Ke-1 dan Jadwal Boarding Index Ke-2
#Location & Board Akan Berubah Sesuai Dengan Index Yang Diset
if reschedule == True:
    location = loc[1]
    date1 = board[3]
    date2 = datetime.strptime(date1, "%Y, %m, %d, %H, %M, %S")
    boarding = date2.strftime("%B %d %Y %H:%M:%S")
#Jika Kondisi reschedule Bernilai False, Maka Akan Menampilkan Lokasi Transit Ke-3 dan Jadwal Boarding Index Ke-0
#Location & Board Akan Berubah Sesuai Dengan Index Yang Diset
else:
    location = loc[3]
    date1 = board[0]
    date2 = datetime.strptime(date1, "%Y, %m, %d, %H, %M, %S")
    boarding = date2.strftime("%B %d %Y %H:%M:%S")

while 1:
    #Mengeluarkan Informasi Alamat Yang Terpaut
    conn, addr = s.accept()
    #Print Alamat Client
    print("\n Alamat:", addr)
    #Mengirim Data Melalui Socket
    conn.sendall(str.encode("\n".join([boarding, location])))
    #Menerima Data Dari Socket
    data = conn.recv(buffer_size)
    #Print Output Jadwal Boarding dan Lokasi Transit Penumpang Lion Air Group Yang Diterima Client
    print("Mengirim pesan berisi :", data.decode())

#Menutup Socket
conn.close()