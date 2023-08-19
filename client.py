#Import Socket 
import socket
#Import Datetime
from datetime import datetime

#Deklarasi IP, Port, Buffer Size
tcp_ip = '26.58.170.203' #IP VPN Server
tcp_port = 8085
buffer_size = 4096

#Penggunaan TCP Socket & Membuat Objek Socket Baru
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Menghubungkan Socket Dengan Host dan Port
s.connect((tcp_ip, tcp_port))

#Menerima Data Dari Socket
data1, data2 = [str.encode(i) for i in s.recv(buffer_size).decode('utf-8').split('\n')]

#Print Output Jadwal Boarding dan Lokasi Transit Penumpang Lion Air Group
print("!!! PEMBERITAHUAN KEPADA SELURUH PENUMPANG LION AIR GROUP !!!")
print("Jadwal Boarding dan Lokasi Transit Penumpang Lion Air Group : \n")
#Print Output data1 Yang Merupakan Data Tanggal dan Waktu Penumpang Lion Air Group
print(data1.decode('utf-8'))
#Print Output data2 Yang Merupakan Kota dan Nama Bandara Penumpang Lion Air Group
print(data2.decode('utf-8'), "\n")

#Mengirim Data Melalui Socket
s.sendall(b'\n'.join([data1,data2]))

#Mebuat File boarding.txt Yang Berisi Tanggal dan Waktu Jadwal Boarding
f1 = open("boarding.txt", "a")
#Membaca dan Menulis File boarding.txt Yang Berisi Tanggal dan Waktu Jadwal Boarding
f1 = open("boarding.txt", "r+")
#Membaca File boarding.txt Per Baris
isi = f1.readlines()
#Mengubah "\n" Menjadi " "
isi = [item.replace("\n", "") for item in isi]

#Inisialisasi Found = False
found = False
#For Ini Digunakan Pada Kondisi Apabila Jadwal Boarding dan Lokasi Transit Sama Dengan Sebelumnya Maka Data Tidak Dikirim
for line in isi :
    #Kondisi Dimana data1 Akan Dibandingkan Dengan Isi Dari File boarding.txt
    if data1.decode() == line :
        #Jika Data Sama Maka Akan Print "Pemeberitahuan Sudah Di Notifikasikan"
        f1.write("Pemberitahuan Sudah Di Notifikasikan")
        f1.write('\n')
        #Inisialisasi Found Menjadi True
        found = True
        
#Kondisi Dimana Found == False Dan Antara data1 Dengan Isi Array File boarding.txt Berbeda        
if found == False :
    #Menulis data1 Yang Merupakan Data Tanggal dan Waktu Penumpang Lion Air Group Pada File boarding.txt
    f1.write(''.join(data1.decode()))
    f1.write('\n')
    f1.close()

#Mebuat File lokasi.txt Yang Berisi Kota dan Nama Bandara Lokasi Transit
f2 = open("lokasi.txt", "a")
#Membaca dan Menulis File boarding.txt Yang Berisi Kota dan Nama Bandara Lokasi Transit
f2 = open("lokasi.txt", "r+")
#Membaca File lokasi.txt Per Baris
isi = f2.readlines()
#Mengubah "\n" Menjadi " "
isi = [item.replace("\n", "") for item in isi]

#Inisialisasi Found = False
found = False
#For Ini Digunakan Pada Kondisi Apabila Jadwal Boarding dan Lokasi Transit Sama Dengan Sebelumnya Maka Data Tidak Dikirim
for line in isi :
    #Kondisi Dimana data2 Akan Dibandingkan Dengan Isi Dari File lokasi.txt
    if data2.decode() == line :
        #Jika Data Sama Maka Akan Print "Pemeberitahuan Sudah Di Notifikasikan"
        f2.write("Pemberitahuan Sudah Di Notifikasikan")
        f2.write('\n')
        #Inisialisasi Found Menjadi True
        found = True

#Kondisi Dimana Found == False Dan Antara data1 Dengan Isi Array File lokasi.txt Berbeda 
if found == False :
    #Menulis data2 Yang Merupakan Kota dan Nama Bandara Penumpang Lion Air Group Pada File lokasi.txt
    f2.write(''.join(data2.decode()))
    f2.write('\n')
    f2.close()

#Menutup Socket
s.close()