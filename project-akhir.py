# Ujian Akhir Semester - Universitas Teknologi Yogyakarta
# Nomer 1
list_angka = [1, 2, 3, 4, 5, 7, 12, 111, 4, 43, 32, 40, -11]
genap = []
ganjil = []

for value in list_angka:
    if value % 2 == 0:
        genap.append(value)
    elif value %2 == 1:
        ganjil.append(value)

print("MENCARI ANGKA GANJIL & GENAP")
print("List Angka =", list_angka)
print("Angka Genap =", genap)
print("Angka Ganjil =", ganjil)
print("")

# Nomer 2 dan Nomer 3
dataMhs = {
    0:{'nim' : 220002,'nama' : 'Putri Oktavia','nilai' : 80},
    1:{'nim' : 220003,'nama' : 'Ani Meriana','nilai' : 75},
    2:{'nim' : 220004,'nama' : 'Agus Adetya','nilai' : 50},
    3:{'nim' : 220005,'nama' : 'Hari Purnama','nilai' : 30},
    4:{'nim' : 220006,'nama' : 'Ridwan Maulana','nilai' : 85},
    5:{'nim' : 220007,'nama' : 'Dyah Prameswari','nilai' : 59},
    6:{'nim' : 220008,'nama' : 'Abid Taufiqur','nilai' : 79},
    7:{'nim' : 220009,'nama' : 'Ayu Wulan Sari','nilai' : 44},
}

def nilaiHuruf(nilai):
    if nilai >= 80:
        return 'A'
    elif nilai >=60 and nilai <= 79:
        return 'B'
    elif nilai >= 45 and nilai <= 59:
        return 'C'
    elif nilai >= 30 and nilai <= 44:
        return 'D'
    else :
        return 'E'

def cetakNilai(dataMhs={}):
    print("DAFTAR NILAI")
    print("="*60)
    print("{:<8}{:<14}{:<20}{:<10}{:<8}".format("ID", "Nim", "Nama", "Nilai", "Huruf"))
    print("-"*60)

    for id, data in dataMhs.items():
        print("{:<8}{:<14}{:<20}{:>5}{:>8}".format((id+1), data['nim'], data['nama'], data['nilai'], nilaiHuruf(data['nilai'])))
cetakNilai(dataMhs)
print("="*60)
# Created By - Rifky Verryan Dhika




