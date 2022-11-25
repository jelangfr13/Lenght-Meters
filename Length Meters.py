import os
import csv
from sys import maxsize
from itertools import permutations

nama_file = 'history.csv'

def menu_utama():
    os.system('cls')
    print('='*100)
    print('{:^100}'.format('Selamat Datang Di Aplikasi Length Meters'))
    print('{:^100}'.format('Aplikasi Ini Dapat Mengukur Jarak/Rute Terpendek'))
    print('{:^100}'.format('Jika Ingin Pergi Ke Kota Kota Tertentu'))
    print('='*100)
    print()
    print('Silahkan Pilih Menu :')
    print('1. Ukur Jarak/Rute Tercepat')
    print('2. History')
    print('3. Keluar Aplikasi')

    inputan = input('=> ')

    if inputan == '1':
        menu_1()
    elif inputan == '2':
        menu_2()
    elif inputan == '3':
        os.system('cls')
        print('{:^100}'.format('Terimakasih Sudah Menggunakan Aplikasi Length Meters'))
        print()
        print('{:^100}'.format('=== APLIKASi KELUAR ==='))
        exit
    else:
        os.system('cls')
        print('{:^100}'.format('!!! Menu Yang Anda Input Tidak Tersedia !!!'))
        print()
        print('{:^100}'.format('=== APLIKASi KELUAR ==='))


def menu_1():
    os.system('cls')
    total_kota = 4
    
    print('{:^100}'.format('Silahkan Masukkan Jarak Setiap Kota Yang Akan Dituju (Km)'))
    print()
    print('Note : ')
    print('- Maksimal 4 (empat) Kota')
    print('- Jika Kurang Dari 4 Kota, Maka Cukup Masukkan Angka 0')
    print('='*100)
    print()

    print('Silahkan Masukkan Jarak Antara Kota-1 Ke Kota-2 :')
    jarak1 = int(input('=> '))
    print()

    print('Silahkan Masukkan Jarak Antara Kota-1 Ke Kota-3 :')
    jarak2 = int(input('=> '))
    print()
    
    print('Silahkan Masukkan Jarak Antara Kota-1 Ke Kota-4 :')
    jarak3 = int(input('=> '))
    print()

    print('Silahkan Masukkan Jarak Antara Kota-2 Ke Kota-3 :')
    jarak4 = int(input('=> '))
    print()
    
    print('Silahkan Masukkan Jarak Antara Kota-2 Ke Kota-4 :')
    jarak5 = int(input('=> '))
    print()

    print('Silahkan Masukkan Jarak Antara Kota-3 Ke Kota-4 :')
    jarak6 = int(input('=> '))
    print()

    def tsp(graph, s):
        vertex = []
        for i in range(total_kota):
            if i != s:
                vertex.append(i)
 
        min_path = maxsize
        next_permutation = permutations(vertex)
        for i in next_permutation:
            current_pathweight = 0
            k = s
            for j in i:
                current_pathweight += graph[k][j]
                k = j
            current_pathweight += graph[k][s]
            min_path = min(min_path, current_pathweight)
        return min_path

    if __name__ == "__main__":
        graph = [[0, jarak1, jarak2, jarak3], [jarak1, 0, jarak4, jarak5],
                [jarak2, jarak4, 0, jarak6], [jarak3, jarak5, jarak6, 0]]
        s = 0
        hasil = tsp(graph, s)
        print('Jarak atau Rute Terpendek Yang Akan Anda Tempuh Adalah Sejauh',hasil,'Kilometer')

        with open(nama_file, 'a', newline='') as file:
            tulis = csv.writer(file)
            tulis.writerow([hasil])
    
    print()
    print()
    print('Lanjut / Keluar :')
    x = input('l/k => ')
    if x == 'l':
        menu_utama()
    elif x == 'k':
        os.system('cls')
        print('{:^100}'.format('Terimakasih Sudah Menggunakan Aplikasi Length Meters'))
        print()
        print('{:^100}'.format('=== APLIKASi KELUAR ==='))
        exit
    else:
        os.system('cls')
        print('{:^100}'.format('!!! Menu Yang Anda Input Tidak Tersedia !!!'))
        print()
        print('{:^100}'.format('=== APLIKASi KELUAR ==='))


def menu_2():
    os.system('cls')
    print('Silahkan Pilih Menu :')
    print('1. Lihat History')
    print('2. Hapus History')
    print('3. Kembali')
    pilih = input('=> ')

    if pilih == '1':
        os.system('cls')
        print('History :')
        with open(nama_file, 'r') as file:
            baca = csv.reader(file, delimiter=',')
            for i in baca:
                print(i)

        print()
        print()
        print('Lanjut / Keluar :')
        x = input('l/k => ')
        if x == 'l':
            menu_2()
        elif x == 'k':
            os.system('cls')
            print('{:^100}'.format('Terimakasih Sudah Menggunakan Aplikasi Length Meters'))
            print()
            print('{:^100}'.format('=== APLIKASi KELUAR ==='))
            exit
        else:
            os.system('cls')
            print('{:^100}'.format('!!! Menu Yang Anda Input Tidak Tersedia !!!'))
            print()
            print('{:^100}'.format('=== APLIKASi KELUAR ==='))

    elif pilih == '2':
        os.system('cls')
        x = ''
        with open(nama_file, 'w', newline='') as file:
            tulis = csv.writer(file)
            tulis.writerow(x)
        print()
        print('{:^100}'.format('=== HISTORY BERHASIL DIHAPUS ==='))

        print()
        print()
        print('Lanjut / Keluar :')
        x = input('l/k => ')
        if x == 'l':
            menu_2()
        elif x == 'k':
            os.system('cls')
            print('{:^100}'.format('Terimakasih Sudah Menggunakan Aplikasi Length Meters'))
            print()
            print('{:^100}'.format('=== APLIKASi KELUAR ==='))
            exit
        else:
            os.system('cls')
            print('{:^100}'.format('!!! Menu Yang Anda Input Tidak Tersedia !!!'))
            print()
            print('{:^100}'.format('=== APLIKASi KELUAR ==='))

    elif pilih == '3':
        menu_utama()
    else:
        os.system('cls')
        print('{:^100}'.format('!!! Menu Yang Anda Input Tidak Tersedia !!!'))
        print()
        print('{:^100}'.format('=== APLIKASi KELUAR ==='))

menu_utama()