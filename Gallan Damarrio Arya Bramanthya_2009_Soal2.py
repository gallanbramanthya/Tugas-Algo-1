"""
Nama    : Gallan Damarrio Arya Bramanthya
NIM     : 222410102009
Tugas   : Tugas 2 soal nomor 2
"""

print('\r\n', 'List Kode Sapi:')
print('1.    Sapi Warrior    : 690 hari')
print('2.    Sapi Mage       : 420 hari')
print('3.    Sapi Assassin   : 530 hari')
print('4.    Sapi Nolep      : 330 hari', '\r\n')
sapi_Warrior    = 690
sapi_Mage       = 420
sapi_Assassin   = 530
sapi_Nolep      = 330
JSapi = int(input("Masukkan jumlah sapi : "))
end = 0
totalakhir = 0
while end < JSapi :
    inputUser = int(input("Masukkan kode sapi : "))
    if inputUser == 1 :
        totalakhir += sapi_Warrior
    elif inputUser == 2 :
        totalakhir += sapi_Mage
    elif inputUser == 3 :
        totalakhir += sapi_Assassin
    elif inputUser == 4 :
        totalakhir += sapi_Nolep
    else :
        print(f"Maaf code sapi {inputUser} tidak ditemukan")
    end += 1
print('\r\n')
print(f'Jumlah hari yang diperlukan ialah {totalakhir//365} tahun {(totalakhir%365)//30} bulan {((totalakhir%365)%30)} hari')
print('\r\n')