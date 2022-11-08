"""
Nama    : Gallan Damarrio Arya Bramanthya
NIM     : 222410102009
Tugas   : Tugas 2 soal Nomor 3
"""

print('\r\n', 10*'=', ' PROGRAM KETIKAN ', 10*'=' , '\r\n')
UserInp = input("Masukkan kata : ")
condition = False
KeyboardKiri = ['q','w','e','r','t','a','s','d','f','g','z','x','c','v','b']
KeyboardKanan = ['y','u','i','o','p','h','j','k','l','n','m']

for x in range(len(UserInp) - 1):
    if UserInp[x] in KeyboardKanan and UserInp[x + 1] in KeyboardKanan:
        condition = False
        keterangan = f'Penjelasan: Karakter yang berdempetan yakni {UserInp[x]} dan {UserInp[x + 1]} berada di satu tangan (kanan)'
        break
    elif UserInp[x] in KeyboardKiri and UserInp[x + 1] in KeyboardKiri :
        condition = False
        keterangan = f'Penjelasan: Karakter yang berdempetan yakni {UserInp[x]} dan {UserInp[x + 1]} berada di satu tangan (kiri)'
        break
    else :
        condition = True
        keterangan = 'Penjelasan: Setiap karakter selalu bergantian tangan.'

print(condition, keterangan, sep="\r\n")

