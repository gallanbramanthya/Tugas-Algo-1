"""
Nama    : Gallan Damarrio Arya Bramanthya
NIM     : 222410102009
Tugas   : tugas 2 soal nomor 1
"""

print('\r\n', 10*'>', 'PROGRAM SELISIH ANTAR HURUF', 10*'<', '\r\n')
inputan = int(input('Berapa huruf yang akan anda input : '))
x = 0
emptylist  = []

while x < inputan :
    x += 1
    input_user = input(f'Masukkan kata ke-{x} : ')
    emptylist.append(input_user)
for word in emptylist :
    print('\r\n', 3*'=', 'Hasil : ', '\r\n')
    for x in range(len(word)):
        if x == len(word)-1:
            break
        kata = word[x]
        konv = ord(kata) 
        hasil = abs(konv - (ord(word[x + 1])))
        if konv < ord(word[x + 1]):
            print(f'{kata} kurang dari {word[x + 1]}, selisih ialah {hasil}')
        else :
            print(f'{kata} lebih dari {word[x + 1]}, selisih ialah {hasil}')

print('\r\n', 20*'>', 'TERIMAKASIH', 20*'<', '\r\n')