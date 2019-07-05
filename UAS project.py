class buku(object) :
    """Class mahasiswa dengan berbagai metode"""
    def __init__ (self, nama, judul, penerbit, harga):
        self.nama = nama
        self.judul = judul
        self.penerbit = penerbit
        self.harga = harga

    def __str__ (self) :
        s = 'Nama Pengarang :  ' + self.nama \
            + ', Judul Buku :  ' + self.judul \
            + ', Penerbit :  ' + self.penerbit \
            + ', Harga : Rp  ' + str(self.harga)
        return s
    
    def ambilNama(self) :
        return self.nama
    
    def ambilJudulBuku(self) :
        return self.judul

    def ambilPenerbit(self):
        return self.penerbit

    def ambilHarga(self):
        return self.harga

a0 = buku("Abdul Kadir Ibrahim", "Nadi Hang Tuah", "Gramedia", 40000 )
a1 = buku("Abu Bakar", "Dolanan", "Gagas Media",  18000)
a2 = buku("Abu Bakar", "Kabut Kelam", "Navila",  29000)
a3 = buku("Agit Yogi Subandi", "Sebait Pantun Bujang", "DKL", 23000)
a4 = buku("Ahda Imran", "Penunggang Kuda Negeri Malam", "Navila",  27000)
a5 = buku("Clara Ng", "Gerhana Kembar", "Gramedia",  40000)
a6 = buku("Ahmad Munif ", "Perempuan Jogja", "Navila",  52000)
a7 = buku("Hamdy Salad", "Sebuah Kampung di Pedalaman Waktu", "Bentang",  20000)
a8 = buku("Iman Budhi Santosa", "Kalimantang", "Jendela",  20000)
a9 = buku("Ita Sembiring", "Reuni Tsunami", "Grasindo",  20000)
a10 = buku("Ivan Turgenev", "First Love", "Selasar",  20000)
a11 = buku("Jean Genet", "Les Paravents", "Pustaka Pelajar",  20000)
a12 = buku("Jostein Gaarder", "Cecilia & Malaikat Ariel", "Mizan",  20000)
a13 = buku("Julius Lester", "Long Journey Home", "Mara Pustaka",  38000)
a14 = buku("Karno Kartadibrata", "Picnic", "Kiblat",  13000)
a15 = buku("Matdon", "Mailbox ", "Kiblat",  15000)
a16 = buku("Maulana Syamsuri", "Perempuan Merajut Gelombang", "Gamamedia",  22000)
a17 = buku("Naguib Mahfoud", "Demit ", "Pustaka Alief",  20000)
a18 = buku("Nur Wahida Idris", "Mata Air Akar Pohon", "SIC",  21000)
a19 = buku("Pinto Anugrah", " Kumis Penyaring Kopi", " Ning ",  45000)

daftar = [a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19]

def menu():
    print("Pilihan : ")      
    print("1. Cari Buku")
    print("2. Daftar Buku")
    print("3. Daftar Harga Buku Termurah")
    inputan = int(input("Masukkan Pilihan : "))

    while True:
        if inputan == 1:
            target = input("Masukkan Kata Kunci : ")
            def cari(daftar, target):
                a = []
                indeks = 0
                for i in daftar: #melakukan perulangan selama i ada di daftar
                    if i.judul.lower() == target.lower(): #jika judul = target,
                        a.append(i)                       #masukkan i ke a disimpan dalam bentuk list
                    elif i.nama.lower() == target.lower() : #jika nama = target,
                        a.append(i)                         #masukkan i ke a disimpan dalam bentuk list
                    indeks += 1
                return a #mengembalikan nilai a disimpan dalam list
            a  = cari(daftar, target)
            for x in a:
                print (x)
            menu()
        elif inputan == 2 :
            for s in daftar: 
                print (s)
            print("\n")
            menu()


        elif inputan == 3 :
                

            def swap (A, p, q):
                A[p], A[q] = A[q], A[p] #menukar posisi A[p],A[q] menjadi A[q],A[p]
            
        ##    b = []
        ##    for a in daftar : #melakukan perulangan selama a ada di daftar
        ##        b.append(a.ambilHarga()) #masukkan harga ke b disimpan dalam bentuk list
            def bubbleSort(A):
                n = len(A)
                for i in range(n-1): #melakukan bubblesort sebanyak n-1
                    for j in range (n-i-1): #dorong elemen terbesar ke ujung kanan
                        if A[j].ambilHarga() > A[j+1].ambilHarga(): #jika kiri lebih besar dari kanan,
                            swap(A,j,j+1) #tukar posisi elemen ke j dan ke j+1
            bubbleSort(daftar)
            for s in daftar: 
                print (s)
            menu()

menu()
