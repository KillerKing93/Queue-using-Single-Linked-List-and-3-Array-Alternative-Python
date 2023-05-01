import os
class Node:                                         #Membuat Kelas Node     #ALIF NURHIDAYAT (G1A022073)
    def __init__(self, data = None, link = None):   #Inisialisasi instansi kelas Node
        self.data = data                            #Properti penyimpan data instansi kelas Node
        self.link = link                            #Properti pointer instansi kelas Node

class Queue:                            #Membuat Kelas Queue    #ALIF NURHIDAYAT (G1A022073)
    def __init__(self, size = 1):       #Inisialisasi instansi kelas Queue      #ALIF NURHIDAYAT (G1A022073)
        self.head = None                #Properti pointer instansi kelas Node
        self.tail = None                #Properti pointer instansi kelas Node   #ALIF NURHIDAYAT (G1A022073)
        self.size = size                #Properti integer instansi kelas Node
        self.currSize = 0               #Properti integer instansi kelas Node   #ALIF NURHIDAYAT (G1A022073)

    def isEmpty(self):                  #Fungsi untuk mengecek apakah Queue Kosong  #ALIF NURHIDAYAT (G1A022073)
        return self.head == None        #Mengembalikan True jika self.head bernilai None
    
    def isFull(self):                       #Fungsi untuk mengecek apakah Queue penuh   #ALIF NURHIDAYAT (G1A022073)
        return self.currSize == self.size   #Mengembalikan True jika ukuran saat ini sama dengan penyimpanan maksimal Queue
    
    def nbElmt(self):               #Fungsi untuk mengetahui jumlah element di dalam Queue  #ALIF NURHIDAYAT (G1A022073)
        return self.currSize        #Mengembalikan jumlah element di dalam Queue saat ini   #ALIF NURHIDAYAT (G1A022073)
    
    def createEmpty(self, size):    #Fungsi untuk membuat Queue baru    #ALIF NURHIDAYAT (G1A022073)
        return Queue(size)          #Mengembalikan Queue baru           #ALIF NURHIDAYAT (G1A022073)
    
    def Add(self, data):            #Fungsi untuk menambahkan element ke dalam Queue
        if self.isFull():           #Jika Queue penuh           #ALIF NURHIDAYAT (G1A022073)
            return "Queue Penuh!"   #Mengembalikan string "Queue Penuh!"
        new_node = Node(data)       #Membuat node baru yang berisi data
        if self.isEmpty():          #Jika Queue kosong          #ALIF NURHIDAYAT (G1A022073)
            self.head = new_node    #Menetapkan pointer head menuju Node yang baru dibuat
        else:                       #Jika kondisi if di atas tidak terpenuhi    ALIF NURHIDAYAT (G1A022073)
            self.tail.link = new_node   #Menetapkan self.tail.link untuk menunjuk ke Node yang baru dibuat
        self.tail = new_node        #Menetapkan self.tail untuk menunjuk ke Node yang baru dibuat
        self.currSize += 1          #Menambah ukuran Queue saat ini sebanyak 1

    def Del(self):                  #Fungsi untuk mengambil element dari dalam Queue
        if self.isEmpty():          #Jika Queue kosong    ALIF NURHIDAYAT (G1A022073)
            return "Queue tidak berisi!"    #Mengembalikan string "Queue tidak berisi!"
        data = self.head.data       #Menyimpan self.head.data ke dalam variabel data
        self.currSize -= 1          #Mengurangi ukuran Queue saat ini sebanyak 1
        if self.isEmpty():          #Jika Queue kosong   ALIF NURHIDAYAT (G1A022073)
            self.tail = None        #Membuat nilai self.tail menjadi None
        self.head = self.head.link  #Menyimpan self.head.link ke dalam self.head
        return data                 #Mengembalikan variabel data

class QueueRep1:    #Membuat Queue dengan representasi Array, versi 1
    def __init__(self, size = 1):   #Inisialisasi instansi kelas Queue  #ALIF NURHIDAYAT (G1A022073)
        self.arr = [None] * size    #Properti array instansi kelas Queue
        self.size = size            #Properti integer instansi kelas Queue
        self.currSize = 0           #Properti integer instansi kelas Queue
    
    def isEmpty(self):              #Fungsi untuk mengecek apakah Queue penuh
        return self.currSize == 0   #Mengembalikan True array kosong    #ALIF NURHIDAYAT (G1A022073)

    def isFull(self):                       #Fungsi untuk mengecek apakah Queue penuh
        return self.size == self.currSize   #mengembalikan True jika jumlah element sama dengan ukuran Queue
    
    def nbElmt(self):        #Fungsi untuk mengecek jumlah element Queue    #ALIF NURHIDAYAT (G1A022073)
        return self.currSize    #Mengembalikan jumlah element saat ini      #ALIF NURHIDAYAT (G1A022073)
    
    def createEmpty(self, size):    #Fungsi untuk membuat Queue baru    #ALIF NURHIDAYAT (G1A022073)
        return QueueRep1(size)      #Mengembalikan Queue baru           #ALIF NURHIDAYAT (G1A022073)
    
    def Add(self, data):                #Fungsi untuk menambahkan element ke dalam Queue
        if self.currSize < self.size:   #Jika jumlah elemen kurang dari ukuran array
            self.arr[self.currSize] = data  #Menambahkan data ke dalam array    #ALIF NURHIDAYAT (G1A022073)
            self.currSize += 1              #Menambahkan banyak element di dalam array
            return "Data berhasil ditambahkan ke dalam Queue!" #Mengembalikan string "Data berhasil ditambahkan ke dalam Queue!"
        else: return "Queue Penuh!"    #Mencetak teks Array Penuh!      #ALIF NURHIDAYAT (G1A022073)
    
    def Del(self):                  #Fungsi untuk mengambil element dari dalam Queue
        if self.isEmpty():          #Jika Queue penuh       #ALIF NURHIDAYAT (G1A022073)
            return "Queue tidak berisi!"    #Mengembalikan "Queue tidak berisi!"
        data = self.arr[0]                  #Menyimpan self.arr[0] ke dalam data
        i = 0                       #Variable penghitung i bernilai 0   #ALIF NURHIDAYAT (G1A022073)
        while i < self.currSize-1:  #Selama i kurang dari self.currSize dikurang 1
            self.arr[i] = self.arr[i+1] #Menyimpan self.arr[i+1] ke dalam self.arr[i]
            i += 1                  #Menambah variabel penghitung i sebanyak 1
        self.arr[self.currSize-1] = None    #Menetapkan self.arr[self.currSIze-1] dengan nilai None
        self.currSize -= 1        #Mengurangi self.currSize sebanyak 1  #ALIF NURHIDAYAT (G1A022073)
        return data               #Mengembalikan data       #ALIF NURHIDAYAT (G1A022073)
    
class QueueRep2: #Membuat Queue dengan representasi Array, versi 2
    def __init__(self, size=1):     #Inisialisasi instansi kelas Queue  #ALIF NURHIDAYAT (G1A022073)
        self.arr = [None] * size    #Properti array instansi kelas Queue
        self.size = size            #Properti integer instansi kelas Queue
        self.currSize = 0           #Properti integer instansi kelas Queue
        self.head = 0               #Properti integer instansi kelas Queue
        self.tail = 0               #Properti integer instansi kelas QUeue
    
    def isEmpty(self):              #Fungsi untuk mengecek apakah Queue kosong
        return self.currSize == 0   #Jika Ukuran Queue sama dengan 0    #ALIF NURHIDAYAT (G1A022073)
    
    def isFull(self):               #Fungsi untuk mengecek apakah Queue penuh
        return self.currSize == self.size   #Jika Ukuran Queue sama dengan ukuran maksimal
    
    def nbElmt(self):               #Fungsi untuk mengecek jumlah elemen di dalam queue
        return self.currSize        #Mengembalikan Ukuran Queue saat ini
    
    def createEmpty(self, size):    #Fungsi untuk membuat Queue Kosong  #ALIF NURHIDAYAT (G1A022073)
        return QueueRep2(size)      #Mengembalikan Objek instansi QueueRep2()
    
    def Add(self, data):            #Fungsi untuk menambah elemen ke dalam Queue
        if self.isFull():           #Jika Queue Penuh       #ALIF NURHIDAYAT (G1A022073)
            return "Queue Penuh!"   #Mencetak teks          
        if self.isEmpty():          #Jika Queue kosong      #ALIF NURHIDAYAT (G1A022073)
            self.head += 1          #Menambah variabel head sebanyak 1
            self.tail += 1          #Menambah variabel tail sebanyak 1      #ALIF NURHIDAYAT (G1A022073)
            self.currSize += 1      #Menambah ukuran Queue saat ini sebanyak 1
            self.arr[self.head] = data  #Menyimpan data ke dalam self.arr[self.head]
            return                      #Menghentikan fungsi            #ALIF NURHIDAYAT (G1A022073)
        if self.tail == self.size-1:    #Jika self.size-1 sama dengan self.tail
            i = self.head               #menyimpan self.head ke dalam variabel penghitung
            while i <= self.tail:       #Jika i kurang dari sama dengan self.tail
                self.arr[i - self.head] = self.arr[i]   #Menyimpan self.arr[i] ke dalam self.arr[i - self.head]
                i += 1                  #Menambahkan variabel i sebanyak 1          #ALIF NURHIDAYAT (G1A022073)
            self.arr[self.tail] = None  #Menetapkan nilai self.arr[self.tail] menjadi None
            self.tail = i - self.head   #Menyimpan hasil dari i - self.head ke dalam variabel self.tail
            self.head = 0           #Menetapkan variabel self.head menjadi 0        #ALIF NURHIDAYAT (G1A022073)
        else:                       #Jika kondisi if di atas tidak terpenuhi
            self.tail += 1          #Menambah variabel self.tail sebanyak 1         #ALIF NURHIDAYAT (G1A022073)
        self.arr[self.tail] = data  #Menyimpan data ke dalam self.arr[self.tail]
        self.currSize += 1          #Menambah variabel self.currSize sebanyak 1
    
    def Del(self):                  #Fungsi untuk mengambil elemen dari dalam QUeue
        if self.isEmpty():          #Jika Queue penuh                   #ALIF NURHIDAYAT (G1A022073)
            return "Queue tidak berisi!"    #Mengembalikan "Queue tidak berisi!"
        data = self.arr[self.head]  #Menyimpan self.arr[self.head] ke dalam variabel data
        self.arr[self.head] = None  #Menetapkan self.head menjadi None  #ALIF NURHIDAYAT (G1A022073)
        if self.head == self.size:  #Jika self.head sama dengan self.size
            self.head = 0           #Menetapkan self.head menjadi 0     #ALIF NURHIDAYAT (G1A022073)
        else:                       #Jika kondisi if di atas tidak terpenuhi
            self.head += 1          #Menambahkan self.head sebanyak 1   #ALIF NURHIDAYAT (G1A022073)
        self.currSize -= 1          #Mengurangkan self.currSize sebanyak 1
        return data                 #Mengembalikan data         #ALIF NURHIDAYAT (G1A022073)
    
class QueueRep3:    #Membuat Queue dengan representasi Array, versi 3       #ALIF NURHIDAYAT (G1A022073)
    def __init__(self, size = 1):   #Inisialisasi instansi kelas Queue      #ALIF NURHIDAYAT (G1A022073)
        self.arr = [None] * size    #Properti array instansi kelas Queue    
        self.currSize = 0           #Properti integer instansi kelas Queue  #ALIF NURHIDAYAT (G1A022073)
        self.size = size            #Properti integer instansi kelas Queue
        self.head = 0               #Properti integer instansi kelas Queue  #ALIF NURHIDAYAT (G1A022073)
        self.tail = 0               #Properti integer instansi kelas Queue
    
    def isEmpty(self):              #Fungsi untuk mengecek apakah Queue Kosong  #ALIF NURHIDAYAT (G1A022073)
        return self.currSize == 0   #Mengembalikan True jika array kosong       #ALIF NURHIDAYAT (G1A022073)

    def isFull(self):                       #Fungsi untuk mengecek apakah Queue penuh   #ALIF NURHIDAYAT (G1A022073)
        return self.size == self.currSize   #mengembalikan True jika jumlah element sama dengan ukuran Queue
    
    def nbElmt(self):           #Fungsi untuk mengecek jumlah element Queue     #ALIF NURHIDAYAT (G1A022073)
        return self.currSize    #Mengembalikan jumlah element saat ini          #ALIF NURHIDAYAT (G1A022073)
    
    def createEmpty(self, size):    #Fungsi untuk membuat Queue baru    #ALIF NURHIDAYAT (G1A022073)
        return QueueRep3(size)      #Mengembalikan Queue baru           #ALIF NURHIDAYAT (G1A022073)
    
    def Add(self, data):        #Fungsi untuk menambahkan elemen ke dalam Queue #ALIF NURHIDAYAT (G1A022073)
        if self.isFull():       #Jika Queue penuh                           
            return "Queue Penuh!"   #Mengembalikan string "Queue Penuh!"        #ALIF NURHIDAYAT (G1A022073)
        self.arr[self.tail] = data  #Menetapkan data ke self.arr[self.tail]
        self.tail = (self.tail + 1) % self.size #Menyimpan hasil operasi (self.tail + 1) % self.size ke dalam self.tail
        self.currSize += 1          #Menambah variabel penghitung sebanyak 1    #ALIF NURHIDAYAT (G1A022073)
        return "Data berhasil ditambahkan ke dalam Queue!"  #Mengembalikan string "Data berhasil ditambahkan ke dalam Queue!"

    def Del(self):              #Fungsi untuk mengambil elemen dari Queue
        if self.isEmpty():      #Jika Queue tidak berisi            #ALIF NURHIDAYAT (G1A022073)
            return "Queue tidak berisi!"    #Mengembalikan "Queue tidak berisi!"
        data = self.arr[self.head]          #Menyimpan self.arr[self.head] ke dalam data
        self.arr[self.head] = None          #Membuat nilai self.arr[self.head] menjadi None
        self.head = (self.head + 1) % self.size #Menyimpan hasil (self.head + 1) % self.size ke dalam self.head
        self.currSize -= 1          #Mengurangkan self.currSize sebanyak 1
        return data                 #Mengembalikan variabel data    #ALIF NURHIDAYAT (G1A022073)

class UnstableExecutor:     #Kelas UnstableExecutor, berfungsi untuk mengolah perintah masukan pengguna
    def __init__(self):     #Inisialisasi instansi kelas Executor       #ALIF NURHIDAYAT (G1A022073)
        self.dict = {}                  #Properti Dictionary milik instansi dari kelas Executor
        self.internal_Q0 = Queue()      #Properti instansi dari kelas Executor
        self.internal_Q1 = QueueRep1()  #Properti instansi dari kelas Executor  #ALIF NURHIDAYAT (G1A022073)
        self.internal_Q2 = QueueRep2()  #Properti instansi dari kelas Executor
        self.internal_Q3 = QueueRep3()  #Properti instansi dari kelas Executor

    def showInstance(self):             #Fungsi untuk mencetak Objek Instansi Queue yang pernah dibuat
        if self.dict == {}:             #Jika self.dict tidak berisi
                print("Tidak ada Queue yang pernah dibuat!")    #Mencetak teks
                return                      #Menghentikan fungsi    #ALIF NURHIDAYAT (G1A022073)
        print(self.dict)                #Mencetak Instansi Queue yang ada

    def cmnd(self, cmd, pmtr):            #Fungsi untuk memproses perintah yang dimasukkan
        if cmd == "showInstance":         #Jika pengguna memasukkan perintah showInstance()
            self.showInstance()           #mengeksekusi fungsi showInstance()
        elif cmd == "isEmpty":            #Jika pengguna memasukkan perintah isEmpty()
            if type(pmtr) is list:                  #Jika pmtr bertipe list, mengeksekusi:
                print("Parameter tidak Valid!")     #Mencetak "Parameter tidak Valid!"
                return                              #Menghentikan fungsi        #ALIF NURHIDAYAT (G1A022073)
            self.isEmpty(pmtr)          #Mengeksekusi fungsi isEmpty() dengan parameter pmtr
        elif cmd == "isFull":           #Jika pengguna memasukkan perintah isFull()
            if type(pmtr) is list:                  #Jika pmtr bertipe list, mengeksekusi:
                print("Parameter tidak Valid!")     #Mencetak "Parameter tidak Valid!"
                return                              #Menghentikan fungsi        #ALIF NURHIDAYAT (G1A022073)
            self.isFull(pmtr)           #Mengeksekusi fungsi isFully() dengan parameter pmtr
        elif cmd == "nbElmt":        #Jika pengguna memasukkan perintah nbElmt()
            if type(pmtr) is list:                  #Jika pmtr bertipe list, mengeksekusi:
                print("Parameter tidak Valid!")     #Mencetak "Parameter tidak Valid!"
                return                              #Menghentikan fungsi        #ALIF NURHIDAYAT (G1A022073)
            self.nbElmt(pmtr)           #Mengeksekusi fungsi nbElmt() dengan parameter pmtr
        elif cmd == "createEmpty":      #Jika pengguna memasukkan perintah createEmpty()
            try:                        #Mencoba eksekusi kode          #ALIF NURHIDAYAT (G1A022073)
                self.createEmpty(pmtr[0], pmtr[1], pmtr[2]) #Mengeksekusi fungsi createEmpty() dengan parameter pmtr[0], pmtr[1], dan pmtr[2]
            except(IndexError):         #Jika terjadi IndexError, mengeksekusi:
                print("Parameter tidak Valid!") #Cetak "Parameter tidak Valid!"     #ALIF NURHIDAYAT (G1A022073)
        elif cmd == "Add":                      #Jika pengguna memasukkan perintah Add()
            try:                                #Mencoba mengeksekusi kode
                if type(pmtr[1]) is list:       #Jike pmtr[1] bertipe list, akan:       #ALIF NURHIDAYAT (G1A022073)
                    self.inQ(pmtr[0], pmtr[1])  #Mengeksekusi fungsi inQ() dengan parameter pmtr[0] dan pmtr[1]
                else:                           #Jika kondisi if tidak terpenuhi, akan:
                    self.Add(pmtr[0], pmtr[1])  #Mengeksekusi fungsi Add() dengan parameter pmtr[0] dan pmtr[1]
            except(IndexError):                 #Jika terjadi IndexError, mengeksekusi:
                print("Parameter tidak Valid!") #Cetak "Parameter tidak Valid!"         #ALIF NURHIDAYAT (G1A022073)
        elif cmd == "Del":                      #Jika pengguna memasukkan perintah Del()
            try:                                #Mencoba mengeksekusi kode              #ALIF NURHIDAYAT (G1A022073)
                if type(pmtr) is list:          #Jike pmtr bertipe list, akan:          #ALIF NURHIDAYAT (G1A022073)
                    self.delQ(pmtr[0], pmtr[1]) #Mengeksekusi fungsi delQ() dengan parameter pmtr[0] dan pmtr[1]
                else:                           #Jika kondisi if tidak terpenuhi, akan: #ALIF NURHIDAYAT (G1A022073)
                    self.Del(pmtr)              #Mengeksekusi fungsi Del() dengan parameter pmtr
            except(IndexError):                 #Jika terjadi IndexError, mengeksekusi:
                print("Parameter tidak Valid!") #Cetak "Parameter tidak Valid!"         #ALIF NURHIDAYAT (G1A022073)
        elif cmd == "remove":               #Jika pengguna memasukkan perintah remove()
            self.remove(pmtr)               #Mengeksekusi fungsi remove() dengan parameter pmtr
        else:                               #Jika tidak ada perintah yang cocok         #ALIF NURHIDAYAT (G1A022073)
            print("Perintah tidak dikenal! Gunakan perintah help! untuk mencetak perintah yang tersedia !") #Mencetak "Perintah tidak dikenal"

    def isEmpty(self, Object):              #Fungsi untuk mengecek apakah Objek instansi yang dimaksud tidak berisi
        try:                                #Mencoba mengeksekusi kode  #ALIF NURHIDAYAT (G1A022073)
            if self.dict == {}:             #Jika self.dict tidak berisi
                print("Tidak ada Queue yang pernah dibuat!")    #Mencetak teks
                return                      #Menghentikan fungsi        #ALIF NURHIDAYAT (G1A022073)
            print("Queue", Object,"Kosong" if self.dict[Object].isEmpty() else "Tidak Kosong")  #Mencetak teks
        except(KeyError):                   #Jika terjadi KeyError      #ALIF NURHIDAYAT (G1A022073)
            print("Instansi {} Tidak ditemukan".format(Object))   #Mencetak teks             

    def isFull(self, Object):               #Fungsi untuk mengecek apakah Objek instansi yang dimaksud penuh
        try:                                #Mencoba mengeksekusi kode  #ALIF NURHIDAYAT (G1A022073)
            if self.dict == {}:             #Jika self.dict tidak berisi
                print("Tidak ada Queue yang pernah dibuat!")    #Mencetak teks
                return                      #Menghentikan fungsi        #ALIF NURHIDAYAT (G1A022073)
            print("Queue", Object,"Penuh" if self.dict[Object].isFull() else "Tidak Penuh") #Mencetak teks
        except(KeyError):                   #Jika terjadi KeyError      #ALIF NURHIDAYAT (G1A022073)
            print("Instansi {} Tidak ditemukan".format(Object))     #Mencetak teks                 

    def nbElmt(self, Object):               #Fungsi untuk mencetak jumlah elemen di dalam Queue
        try:                                #Mencoba mengeksekusi kode  #ALIF NURHIDAYAT (G1A022073)
            if self.dict == {}:             #Jika self.dict tidak berisi
                print("Tidak ada Queue yang pernah dibuat!")    #Mencetak teks
                return                      #Menghentikan fungsi        #ALIF NURHIDAYAT (G1A022073)
            print("Jumlah element di dalam Queue {} Adalah:".format(Object), self.dict[Object].nbElmt())    #Mencetak teks 
        except(KeyError):                   #Jika terjadi KeyError      #ALIF NURHIDAYAT (G1A022073)
            print("Instansi {} Tidak ditemukan".format(Object))     #Mencetak teks 

    def createEmpty(self, typ, Object, size):       #Fungsi untuk membuat Queue kosong
        if type(typ) is str and type(Object) is str:   #Jika typ dan Object merupakan string
            try:                    #Mencoba mengeksekusi kode      #ALIF NURHIDAYAT (G1A022073)
                size = int(size)    #Menyimpan hasil integer dari int(size) ke variable size
            except(ValueError):     #Jika terjadi ValueError        #ALIF NURHIDAYAT (G1A022073)
                print("Parameter tidak Valid!") #Mencetak Parameter tidak Valid!
                return              #Menghentikan fungsi
            if typ == '0':          #Jika typ sama dengan 0     #ALIF NURHIDAYAT (G1A022073)
                self.dict[Object] = self.internal_Q0.createEmpty(size)  #Menyimpan Queue tipe 0 dengan nama dari variabel Object
            elif typ == '1':        #Jika typ sama dengan 1     #ALIF NURHIDAYAT (G1A022073)
                self.dict[Object] = self.internal_Q1.createEmpty(size)  #Menyimpan Queue tipe 1 dengan nama dari variabel Object
            elif typ == '2':        #Jika typ sama dengan 2     #ALIF NURHIDAYAT (G1A022073)
                self.dict[Object] = self.internal_Q2.createEmpty(size)  #Menyimpan Queue tipe 2 dengan nama dari variabel Object
            elif typ == '3':        #Jika typ sama dengan 3     #ALIF NURHIDAYAT (G1A022073)
                self.dict[Object] = self.internal_Q3.createEmpty(size)  #Menyimpan Queue tipe 3 dengan nama dari variabel Object
            else:                   #Jika if dan elif di atas tidak terpenuhi
                print("Tipe Queue tidak diketahui") #Mencetak teks
                return              #Menghentikan fungsi        #ALIF NURHIDAYAT (G1A022073)
            print("Queue",Object,"Berhasil Dibuat!")    #Mencetak teks
        else:                       #Jika if di atas tidak terpenuhi
            print("Parameter tidak Valid!") #Mencetak teks      #ALIF NURHIDAYAT (G1A022073)

    def Add(self, Object, data):    #Fungsi untuk menambah elemen ke dalam Objek Instansi   #ALIF NURHIDAYAT (G1A022073)
        try:                        #Mencoba mengeksekusi kode      #ALIF NURHIDAYAT (G1A022073)
            if self.dict == {}:             #Jika self.dict tidak berisi
                print("Tidak ada Queue yang pernah dibuat!")    #Mencetak teks
                return                      #Menghentikan fungsi        #ALIF NURHIDAYAT (G1A022073)
            x = self.dict[Object].Add(data) #Menyimpan hasil eksekusi fungsi Add() dari instansi self.dict[Object] ke dalam variabel x
            if x == "Queue Penuh!":         #Jika x bernilai "Queue Penuh!"     #ALIF NURHIDAYAT (G1A022073)
                print("Pada saat memasukkan data {} ke Queue {}, menerima peringatan: {}".format(data, Object, x))  #Mencetak teks
                return              #Menghentikan fungsi                        #ALIF NURHIDAYAT (G1A022073)
            print("Data {} berhasil ditambahkan ke Queue {}!".format(data, Object))
        except(KeyError):           #Jika terjadi KeyError                      #ALIF NURHIDAYAT (G1A022073)
            print("Instansi {} Tidak ditemukan".format(Object)) #Mencetak teks

    def Del(self, Object):          #Fungsi untuk mengambil elemen dari Objek Instansi
        try:                        #Mencoba mengeksekusi kode
            if self.dict == {}:             #Jika self.dict tidak berisi
                print("Tidak ada Queue yang pernah dibuat!")    #Mencetak teks
                return                      #Menghentikan fungsi        #ALIF NURHIDAYAT (G1A022073)
            x = self.dict[Object].Del() #Menyimpan hasil eksekusi fungsi Del() dari instansi self.dict[Object] ke dalam variabel x
            if x == "Queue tidak berisi!":  #Jika x bernilai "Queue tidak berisi!"              #ALIF NURHIDAYAT (G1A022073)
                print("Pada saat mengeksekusi Del() pada Queue {}, menerima peringatan: {}".format(Object, x))  #Mencetak teks
                return              #Menghentikan fungsi 
            print("Mendapatkan data {} dari Queue {}".format(x, Object))    #Mencetak teks
        except(KeyError):           #Jika terjadi KeyError
            print("Instansi {} Tidak ditemukan".format(Object)) #Mencetak teks

    def remove(self, Object):       #Fungsi untuk menghapus objek instansi  #ALIF NURHIDAYAT (G1A022073)
        try:                        #Mencoba mengeksekusi kode
            if self.dict == {}:             #Jika self.dict tidak berisi
                print("Tidak ada Queue yang pernah dibuat!")    #Mencetak teks
                return                      #Menghentikan fungsi    #ALIF NURHIDAYAT (G1A022073)
            del self.dict[Object]   #Menghapus Objek Instansi
        except:                     #Jika terjadi Error             #ALIF NURHIDAYAT (G1A022073)
            print("Gagal menghapus Objek Instansi {}!".format(Object))  #Mencetak teks
    
    def inQ(self, Object, data):    #Fungsi untuk memasukkan banyak elemen ke dalam Queue
        i = 0                       #Variable penghitung bernilai 0     #ALIF NURHIDAYAT (G1A022073)
        while i < len(data):          #Selama i kurang dari panjang list data
            self.Add(Object, data[i]) #Mengeksekusi fungsi inQ()        #ALIF NURHIDAYAT (G1A022073)
            i += 1                  #Menambah variable penghitung sebanyak 1

    def delQ(self, Object, amnt):   #Fungsi untuk mengambil banyak elemen dari Queue
        i = 0                       #Variable penghitung bernilai 0     #ALIF NURHIDAYAT (G1A022073)
        while i < int(amnt):        #Selama i kurang dari int(amnt), amnt = banyak pengambilan
            self.Del(Object)        #Mengeksekusi fungsi Del()          #ALIF NURHIDAYAT (G1A022073)
            i += 1                  #Menambah variable penghitung sebanyak 1

def mainDebug():                            #Fungsi untuk mengeksekusi kode debug (untuk mengecek apakah Queue bekerja sesuai keinginan)
    exec = UnstableExecutor()               #Membuat instansi kelas UnstableExecutor    #ALIF NURHIDAYAT (G1A022073)
    exec.createEmpty("0", "debug_Q0", 3)    #Membuat Queue Tipe SLL dengan nama debug_Q0 dengan ukuran Queue 3
    exec.createEmpty("1", "debug_Q1", 3)    #Membuat Queue Tipe Array Alternatif 1 dengan nama debug_Q1 dengan ukuran Queue 3
    exec.createEmpty("2", "debug_Q2", 3)    #Membuat Queue Tipe Array Alternatif 2 dengan nama debug_Q2 dengan ukuran Queue 3
    exec.createEmpty("3", "debug_Q3", 3)    #Membuat Queue Tipe Array Alternatif 3 dengan nama debug_Q3 dengan ukuran Queue 3
    x = ["debug_Q0", "debug_Q1", "debug_Q2", "debug_Q3"]    #Menyimpan nama masing - masing Queue ke dalam list
    i = 0                                   #Membuat variable penghitung dengan nilai 0
    while i <= 3:                           #Selama i kurang dari sama dengan 3     #ALIF NURHIDAYAT (G1A022073)
        print("Operasi pada Queue", x[i])   #Mencetak "Operasi pada Queue x[i]"     #ALIF NURHIDAYAT (G1A022073)
        exec.isEmpty(x[i])                  #Mengeksekusi fungsi isEmpty() dari instansi exec
        exec.isFull(x[i])                   #Mengeksekusi fungsi isFull() dari instansi exec
        exec.inQ(x[i], [5, 7, 8, 10, 11])   #Mengeksekusi fungsi inQ() dari instansi exec
        exec.nbElmt(x[i])                   #Mengeksekusi fungsi nbElmnt() dari instansi exec
        exec.isEmpty(x[i])                  #Mengeksekusi fungsi isEmpty() dari instansi exec
        exec.isFull(x[i])                   #Mengeksekusi fungsi isFull() dari instansi exec
        exec.delQ(x[i], 2)                  #Mengeksekusi fungsi delQ() dari instansi exec
        exec.nbElmt(x[i])                   #Mengeksekusi fungsi nbElmnt() dari instansi exec
        exec.inQ(x[i], [10, 11, 13, 14])    #Mengeksekusi fungsi inQ() dari instansi exec
        exec.nbElmt(x[i])                   #Mengeksekusi fungsi nbElmnt() dari instansi exec
        exec.delQ(x[i], 5)                  #Mengeksekusi fungsi delQ() dari instansi exec
        exec.nbElmt(x[i])                   #Mengeksekusi fungsi nbElmnt() dari instansi exec
        print("\n\n\n")                     #Mencetak 3 garis kosong ke terminal
        i += 1                              #Menambah parameter penghitung sebanyak 1

def main():                     #Fungsi utama program, berfungsi sebagai pengambil input
    exec = UnstableExecutor()   #Membuat instansi kelas UnstableExecutor
    while True:                 #Selama True    #ALIF NURHIDAYAT (G1A022073)
        help = """              
Perintah yang dapat dimasukkan:
1. showInstance()                                       [Mengecek Instansi Queue yang ada]
2. isEmpty(Nama Queue)                                  [Mengecek apakah Queue Kosong]
3. isFull(Nama Queue)                                   [Mengecek apakah Queue Penuh]
4. nbElmt(Nama Queue)                                   [Mengecek Jumlah elemen di dalam Queue]
5. createEmpty(Tipe Queue, Nama Queue, Ukuran Queue)    [Membuat Queue baru]
    |           |->  Tipe Queue yang tersedia:
    |                   |-> Tipe '0', Queue dengan Single Linked List
    |                   |-> Tipe '1', Queue dengan Representasi Array, Alternatif 1
    |                   |-> Tipe '2', Queue dengan Representasi Array, Alternatif 1
    |                   |-> Tipe '3', Queue dengan Representasi Array, Alternatif 1
    |-> Contoh: createEmpty(0, Q, 2)

6. Add(Nama Queue, elemen) atau Add(Nama Queue, [element0, element1, ...])  [Menambahkan elemen ke dalam Queue]
    |-> Contoh: Add(Q, 202) atau Add(Q, [203, 405, 330])

7. Del(Nama Queue) atau Del(Nama Queue, jumlah pengambilan) [Mengambil elemen dari dalam Queue]
    |-> Contoh: Del(Q) atau Del(Q, 2)

8. remove(Nama Queue)                                       [Menghapus instansi Queue]
9. keluar
        """ #Variabel bernama help yang mengandung semua perintah yang dapat dieksekusi oleh instansi UnstableExecutor
        inp = input("\nMasukkan perintah: ") #Taking command from user          #ALIF NURHIDAYAT (G1A022073)
        os.system('cls')                    #Menghapus teks di terminal         #ALIF NURHIDAYAT (G1A022073)
        print("perintah yang dimasukkan: {}\n".format(inp)) #Mencetak kembali perintah yang dimasukkan pengguna
        if inp.lower() == "keluar":     #Jika string yang dimasukkan pengguna sama dengan "keluar"
            break                       #Menghentikan while loop                #ALIF NURHIDAYAT (G1A022073)
        if inp.lower() == "help!":      #Jika string yang dimasukkan pengguna sama dengan help!
            print(help)                 #Mencetak variabel help                 #ALIF NURHIDAYAT (G1A022073)
            continue                    #Melanjutkan while loop ke iterasi selanjutnya
        inp = inp.replace(" ,", " ")   #Mengubah " ," menjadi " "  #ALIF NURHIDAYAT (G1A022073)
        inp = inp.replace(", ", " ")  #Mengubah ", " menjadi " "
        inp = inp.replace(",", " ")   #Mengubah "," menjadi " "   #ALIF NURHIDAYAT (G1A022073)
        if not inp.count("(") == inp.count(")") or not inp.count("[") == inp.count("]"):    #Jika masukan pengguna tidak mengandung jumlah () dan [] yang sama
            print("perintah tidak Valid!")  #Cetak perintah tidak valid         #ALIF NURHIDAYAT (G1A022073)
            continue                        #Melanjutkan while loop ke iterasi selanjutnya
        i = inp.find("(")               #Variable yang berfungsi untuk menyimpan letak "(" pertama di dala masukan pengguna
        cmd = inp[0:i]                  #variable cmd yang menyimpan perintah pengguna
        parameter = inp[i+1:-1]     #Mengambil parameter perintah dari masukan pengguna
        if " " in inp:                  #Jika perintah pengguna mengandung " "      #ALIF NURHIDAYAT (G1A022073)
            if "[" in parameter:        #Jika parameter pengguna mengandung list
                x = parameter.find("[") #Simpan lokasi pertama "[" dari variable parameter ke variable x
                z = parameter.find("]") #Simpan lokasi pertama "]" dari variable parameter ke variable z
                pmtr = parameter[x:z+1] #menyimpan parameter yang bersifat list ke variable pmtr
                z = "[]-=-TempPlaceholder-=-[]" #Variable string parameter sementara        #ALIF NURHIDAYAT (G1A022073)
                parameter = parameter.replace(pmtr, z)  #mengganti string yang sama dengan string pmtr dengan string parameter sementara
                pmtr = pmtr[1:-1].split(" ")            #Memotong variable pmtr dan mengubahnya menjadi list
                parameter = parameter.split(" ")  #Membuat variable parameter menjadi list dengan pemotong yang berparameter " "
                parameter[parameter.index(z)] = pmtr    #Mengganti string parameter sementara dengan list pmtr
            else:                                   #Jika kondisi if tidak terpenuhi        #ALIF NURHIDAYAT (G1A022073)
                parameter = parameter.split(" ")    #Membuat variable parameter menjadi list dengan pemotong yang berparameter " "
        exec.cmnd(cmd, parameter)                   #Menjalankan fungsi cmnd() dari instansi exec

def program():      #Fungsi bernama program() yang berfungsi untuk menentukan jenis program yang dijaankan
    debug = 0       #Variable penentu jalan program         #ALIF NURHIDAYAT (G1A022073)
    while True:     #Selama True                            #ALIF NURHIDAYAT (G1A022073)
        dbg = input("Jalankan Program dengan mode Debug ? y/n: ")   #Meminta masukan dari pengguna
        if dbg.lower() == "y":          #Jika masukan pengguna sama dengan "y"  #ALIF NURHIDAYAT (G1A022073)
            debug = 1                   #Menetapkan nilai debug menjadi 1       #ALIF NURHIDAYAT (G1A022073)
            break                       #Menghentikan while loop                #ALIF NURHIDAYAT (G1A022073)
        elif dbg.lower() == "n":        #Jika kondisi if sebelumnya tidak memenuhi dan Jika masukan pengguna sama dengan "n"
            debug = 0                   #Menetapkan nilai debug menjadi 0
            break                       #Menghentikan while loop                #ALIF NURHIDAYAT (G1A022073)
        else:                           #Jika kondisi if dan elif sebelumnya tidak terpenuhi
            print("Masukan tidak dapat diproses!")  #Mencetak teks "Masukan tidak dapat diproses!" ke terminal
    if debug == 0:                      #Jika nilai debug sama dengan 0
        main()                          #Mengeksekusi fungsi main()             #ALIF NURHIDAYAT (G1A022073)
    else:                               #Jika kondisi if sebelumnya tidak terpenuhi
        mainDebug()                     #Menjalankan fungsi mainDebug()         #ALIF NURHIDAYAT (G1A022073)

if __name__ == "__main__":      #Jika program dieksekusi dan bukan diimpor sebagai library
    program()                   #Mengeksekusi fungsi program()                  #ALIF NURHIDAYAT (G1A022073)
    print("Program Selesai dijalankan!") #Mencetak teks "Program Selesai dijalankan!"
