## VARIABLE
nim         = ['220101', '220102', '220103']
nama        = ['Bagas', 'Sekar', 'Krisn']
exam_1      = [100, 100, 100]
exam_2      = [90, 90, 90]
exam_3      = [80, 80, 80]
project_1   = [95, 95, 95]
project_2   = [85, 85, 85]
project_3   = [75, 75, 75]
logic_test  = [100, 100, 100]
nilai_akhir = []

# Function
def menuUtama () :
    print('--------------------LIST MENU UTAMA-------------------')
    print('______________________________________________________')
    print('|                                                    |')
    print('| 1. Report Data Nilai Mahasiswa Purwadhika          |')
    print('| 2. Tambah Data Nilai Mahasiswa Purwadhika          |')
    print('| 3. Update Data Nilai Mahasiswa Purwadhika          |')
    print('| 4. Delete Data Nilai Mahasiswa Purwadhika          |')
    print('| 5. Keluar Program Data Nilai Mahasiswa Purwadhika  |')
    print('|____________________________________________________|')

def perNilaiAkhir () :
    nilai_akhir.clear()
    for i in range(len(nim)) :
        nilai_akhir.append((((exam_1[i] + exam_2[i] + exam_3[i])/3) *0.45) + 
        (((project_1[i] + project_2[i] + project_3[i])/3)*0.45) + 
        (logic_test[i]*0.10))

def tampilkanData () :
    perNilaiAkhir()
    print('_________________________________________________________________________________________')
    print('| NIM        | NAMA     |       EXAM            |     PROJECT           | LOGIC | NILAI |')
    print('|            |          | 1     | 2     | 3     | 1     | 2     | 3     | TEST  | AKHIR |')
    print('|---------------------------------------------------------------------------------------|')
    for d_nim, d_nama, d_exam_1, d_exam_2, d_exam_3, d_pro_1, d_pro_2, d_pro_3, d_log, d_nil in zip(nim, nama, exam_1, exam_2, exam_3, project_1, project_2, project_3, logic_test, nilai_akhir) :
        print(f'| {d_nim}     | {d_nama}\t| {d_exam_1}\t| {d_exam_2}\t| {d_exam_3}\t| {d_pro_1}\t| {d_pro_2}\t| {d_pro_3}\t| {d_log}\t| {d_nil}\t|')
    print('----------------------------------------------------------------------------------------')

def tampilkanDataPanggil () :
    while True :
        panggilNim = input('Masukan NIM yang ingin di TAMPILKAN :')
        if panggilNim.isnumeric():
            break
        else:
            print('-----------------------------')
            print("HANYA MASUKAN ANGKA")
            print('-----------------------------')

    while (True) :
        if panggilNim in nim :    
            print('_________________________________________________________________________________________')
            print('| NIM        | NAMA     |       EXAM            |     PROJECT           | LOGIC | NILAI |')
            print('|            |          | 1     | 2     | 3     | 1     | 2     | 3     | TEST  | AKHIR |')
            print('|---------------------------------------------------------------------------------------|')
            i  = nim.index(panggilNim) 
            print(f'| {nim[i]}     | {nama[i]}\t| {exam_1[i]}\t| {exam_2[i]}\t| {exam_3[i]}\t| {project_1[i]}\t| {project_2[i]}\t| {project_3[i]}\t| {logic_test[i]}\t| {nilai_akhir[i]}\t|')
            print('-----------------------------------------------------------------------------------------')
            break
        else :
            print('-------------------------------------')
            print(f'Data NIM {panggilNim} TIDAK TERSEDIA')
            print('-------------------------------------')
            break

def reportData () :
    while (True) :
        print('-------------Menu Report Data Nilai Mahasiswa-------------')
        print('1. Tampilkan report semua Data Nilai Mahasiswa')
        print('2. Tampilkan report Data Nilai Mahasiswa Sesuai Dengan NIM')
        print('3. Kembali Ke menu Utama')
        print('----------------------------------------------------------')
        reportMenu = input('Masukan Angka (1~3) : ')
        if reportMenu == '1' :
            while (True) :
                if nim == [] :
                    print('-----------------------------------------')
                    print('TIDAK ADA DATA NILAI MAHASISWA PURWADHIKA')
                    print('-----------------------------------------')
                    break
                else :
                    tampilkanData ()
                    break
        
        elif reportMenu == '2' :
            tampilkanDataPanggil ()
        
        elif reportMenu == '3' :
            break

def tambahData () :
    while (True) :
        print('------Menu Tambah Data Nilai Mahasiswa------')
        print('1. Tambah Data Nilai Mahasiswa')
        print('2. Kembali Ke menu Utama')
        print('--------------------------------------------')
        tambahMenu = input('Masukan angka [1~2] : ')

        if tambahMenu == '1' :
            while (True) :
                tampilkanData ()
                while True :
                    tambahNim = input('Masukan NIM baru :')
                    if tambahNim.isnumeric():
                        break
                    else:
                        print('-----------------------------')
                        print("HANYA MASUKAN ANGKA")
                        print('-----------------------------')

                if tambahNim in nim :
                    print('--------------------------------')
                    print(f'data NIM {tambahNim} SUDAH ADA')
                    print('--------------------------------')
                    break
                else : 
                    while True :
                        tambahNama = input('Masukan Nama Mahasiswa : ')
                        if tambahNama.isalpha():
                            break
                        else :
                            print('-----------------------------')
                            print("HANYA MASUKAN ALPHABET")
                            print('-----------------------------')

                    while True:
                        tambahExam_1 = input('Masukan Nilai Exam 1 : ')
                        if tambahExam_1.isnumeric():
                            break
                        else:
                            print('-----------------------------')
                            print("HANYA MASUKAN ANGKA")
                            print('-----------------------------')
                    
                    while True:
                        tambahExam_2 = input('Masukan Nilai Exam 2 : ')
                        if tambahExam_2.isnumeric():
                            break
                        else:
                            print('-----------------------------')
                            print("HANYA MASUKAN ANGKA")
                            print('-----------------------------')                    
                    
                    while True:
                        tambahExam_3 = input('Masukan Nilai Exam 3 : ')
                        if tambahExam_3.isnumeric():
                            break
                        else:
                            print('-----------------------------')
                            print("HANYA MASUKAN ANGKA")
                            print('-----------------------------')
                    
                    while True:
                        tambahProj_1 = input('Masukan Nilai Project 1 : ')
                        if tambahProj_1.isnumeric():
                            break
                        else:
                            print('-----------------------------')
                            print("HANYA MASUKAN ANGKA")
                            print('-----------------------------')
                    
                    while True:
                        tambahProj_2 = input('Masukan Nilai Project 2 : ')
                        if tambahProj_2.isnumeric():
                            break
                        else:
                            print('-----------------------------')
                            print("HANYA MASUKAN ANGKA")
                            print('-----------------------------')                    
                    
                    while True:
                        tambahProj_3 = input('Masukan Nilai Project 3 : ')
                        if tambahProj_3.isnumeric():
                            break
                        else:
                            print('-----------------------------')
                            print("HANYA MASUKAN ANGKA")
                            print('-----------------------------')
                    
                    while True:
                        tambahLog = input('Masukan Nilai Logic Test : ')
                        if tambahLog.isnumeric():
                            break
                        else:
                            print('-----------------------------')
                            print("HANYA MASUKAN ANGKA")
                            print('-----------------------------')

                    tambahSimpan = input('Simpan Data (Y/N) :')
                    if tambahSimpan == 'Y' :                
                        nim.append(tambahNim)
                        nama.append(tambahNama)
                        exam_1.append(int(tambahExam_1))
                        exam_2.append(int(tambahExam_2))
                        exam_3.append(int(tambahExam_3))
                        project_1.append(int(tambahProj_1))
                        project_2.append(int(tambahProj_2))
                        project_3.append(int(tambahProj_3))
                        logic_test.append(int(tambahLog))
                        print('--------------------')
                        print('   DATA TERSIMPAN   ')
                        print('--------------------')
                        perNilaiAkhir ()
                        tampilkanData ()
                        break

                    elif tambahSimpan == 'N' :
                        print('--------------------')
                        print('Data Tidak Tersimpan')
                        print('--------------------')
                        break

        elif tambahMenu == '2' :
            break

def updateData () :
    while (True) :
        print('------Menu Update Data Nilai Mahasiswa------')
        print('1. Update Data Nilai Mahasiswa')
        print('2. Kembali Ke menu Utama')
        print('--------------------------------------------')
        updateMenu = input('Masukan angka [1~2] : ')
        if updateMenu == '1' :
            tampilkanData ()
            while True :
                updateNim = input('Masukan NIM yang ingin di UPDATE :')
                if updateNim.isnumeric():
                    break
                else:
                    print('-----------------------------')
                    print("HANYA MASUKAN ANGKA")
                    print('-----------------------------')

            if updateNim in nim :
                updateIndex = nim.index(updateNim)
                updateNama = nama[updateIndex]
                updateExam_1 = exam_1[updateIndex]
                updateExam_2 = exam_2[updateIndex]
                updateExam_3 = exam_3[updateIndex]
                updateProj_1 = project_1[updateIndex]
                updateProj_2 = project_2[updateIndex]
                updateProj_3 = project_3[updateIndex]
                updateLog = logic_test[updateIndex]
                updateNil = nilai_akhir[updateIndex]
                while True :
                    updateYesNo = input(f'Ingin Mengupdate Data pada NIM {updateNim} ? (Y/N) :')
                    if updateYesNo == "Y":
                        print('List Data Yang ingin di update : ')
                        print('1. Nama Mahasiswa')
                        print('2. Nilai Exam 1')
                        print('3. Nilai Exam 2')
                        print('4. Nilai Exam 3')
                        print('5. Nilai Project 1')
                        print('6. Nilai Project 2')
                        print('7. Nilai Project 3')
                        print('8. Nilai Logic Test')
                        print('9. Semua Data 1 ~ 8')
                        print('10. Tampilkan Perubahan')
                        print('11. Simpan Perubahan')
                        
                        updateMenu = input('Masukan angka sesuai data yang ingin di update [1~11] :')
                        while (True) :
                            if updateMenu == '1' :
                                while True :
                                    updateNama = input('Masukan Nama Mahasiswa : ')
                                    if updateNama.isalpha():
                                        break
                                    else :
                                        print('-----------------------------')
                                        print("HANYA MASUKAN ALPHABET")
                                        print('-----------------------------')
                                break
                            elif updateMenu == '2' :
                                while True:
                                    updateExam_1 = input('Masukan Nilai Exam 1 : ')
                                    if updateExam_1.isnumeric():
                                        break
                                    else:
                                        print('-----------------------------')
                                        print("HANYA MASUKAN ANGKA")
                                        print('-----------------------------')
                                break
                            elif updateMenu == '3' :
                                while True:
                                    updateExam_2 = input('Masukan Nilai Exam 2 : ')
                                    if updateExam_2.isnumeric():
                                        break
                                    else:
                                        print('-----------------------------')
                                        print("HANYA MASUKAN ANGKA")
                                        print('-----------------------------')
                                break
                            elif updateMenu == '4' :
                                while True:
                                    updateExam_3 = input('Masukan Nilai Exam 3 : ')
                                    if updateExam_3.isnumeric():
                                        break
                                    else:
                                        print('-----------------------------')
                                        print("HANYA MASUKAN ANGKA")
                                        print('-----------------------------')
                                break
                            elif updateMenu == '5' :
                                while True:
                                    updateProj_1 = input('Masukan Nilai Project 1 : ')
                                    if updateProj_1.isnumeric():
                                        break
                                    else:
                                        print('-----------------------------')
                                        print("HANYA MASUKAN ANGKA")
                                        print('-----------------------------')
                                break
                            elif updateMenu == '6' :
                                while True:
                                    updateProj_2 = input('Masukan Nilai Project 2 : ')
                                    if updateProj_2.isnumeric():
                                        break
                                    else:
                                        print('-----------------------------')
                                        print("HANYA MASUKAN ANGKA")
                                        print('-----------------------------')
                                break
                            elif updateMenu == '7' :
                                while True:
                                    updateProj_3 = input('Masukan Nilai Project 3 : ')
                                    if updateProj_3.isnumeric():
                                        break
                                    else:
                                        print('-----------------------------')
                                        print("HANYA MASUKAN ANGKA")
                                        print('-----------------------------')
                                break
                            elif updateMenu == '8' :
                                while True:
                                    updateLog = input('Masukan Nilai Logic Test : ')
                                    if updateLog.isnumeric():
                                        break
                                    else:
                                        print('-----------------------------')
                                        print("HANYA MASUKAN ANGKA")
                                        print('-----------------------------')
                                break
                            elif updateMenu == '9' :
                                while True :
                                    updateNama = input('Masukan Nama Mahasiswa : ')
                                    if updateNama.isalpha():
                                        break
                                    else :
                                        print('-----------------------------')
                                        print("HANYA MASUKAN ALPHABET")
                                        print('-----------------------------')

                                while True:
                                    updateExam_1 = input('Masukan Nilai Exam 1 : ')
                                    if updateExam_1.isnumeric():
                                        break
                                    else:
                                        print('-----------------------------')
                                        print("HANYA MASUKAN ANGKA")
                                        print('-----------------------------')
                                
                                while True:
                                    updateExam_2 = input('Masukan Nilai Exam 2 : ')
                                    if updateExam_2.isnumeric():
                                        break
                                    else:
                                        print('-----------------------------')
                                        print("HANYA MASUKAN ANGKA")
                                        print('-----------------------------')                    
                                
                                while True:
                                    updateExam_3 = input('Masukan Nilai Exam 3 : ')
                                    if updateExam_3.isnumeric():
                                        break
                                    else:
                                        print('-----------------------------')
                                        print("HANYA MASUKAN ANGKA")
                                        print('-----------------------------')
                                
                                while True:
                                    updateProj_1 = input('Masukan Nilai Project 1 : ')
                                    if updateProj_1.isnumeric():
                                        break
                                    else:
                                        print('-----------------------------')
                                        print("HANYA MASUKAN ANGKA")
                                        print('-----------------------------')
                                
                                while True:
                                    updateProj_2 = input('Masukan Nilai Project 2 : ')
                                    if updateProj_2.isnumeric():
                                        break
                                    else:
                                        print('-----------------------------')
                                        print("HANYA MASUKAN ANGKA")
                                        print('-----------------------------')                    
                                
                                while True:
                                    updateProj_3 = input('Masukan Nilai Project 3 : ')
                                    if updateProj_3.isnumeric():
                                        break
                                    else:
                                        print('-----------------------------')
                                        print("HANYA MASUKAN ANGKA")
                                        print('-----------------------------')
                                
                                while True:
                                    updateLog = input('Masukan Nilai Logic Test : ')
                                    if updateLog.isnumeric():
                                        break
                                    else:
                                        print('-----------------------------')
                                        print("HANYA MASUKAN ANGKA")
                                        print('-----------------------------')
                                break
                            elif updateMenu == '10' :
                                updateNil = (((int(updateExam_1) + int(updateExam_2) + int(updateExam_3))/3) *0.45) + (((int(updateProj_1) + int(updateProj_2) + int(updateProj_3))/3)*0.45) + (int(updateLog)*0.10)
                                print('_________________________________________________________________________________________')
                                print('| NIM        | NAMA     |       EXAM            |     PROJECT           | LOGIC | NILAI |')
                                print('|            |          | 1     | 2     | 3     | 1     | 2     | 3     | TEST  | AKHIR |')
                                print('|---------------------------------------------------------------------------------------|')
                                print(f'| {updateNim}     | {updateNama}\t| {updateExam_1}\t| {updateExam_2}\t| {updateExam_3}\t| {updateProj_1}\t| {updateProj_2}\t| {updateProj_3}\t| {updateLog}\t| {updateNil}  |')
                                break
                            elif updateMenu == '11' :
                                updateSimpan = input('Simpan Data (Y/N) :')
                                if updateSimpan == 'Y' : 
                                    nama[updateIndex]       = updateNama
                                    exam_1[updateIndex]     = int(updateExam_1)
                                    exam_2[updateIndex]     = int(updateExam_2)
                                    exam_3[updateIndex]     = int(updateExam_3)
                                    project_1[updateIndex]  = int(updateProj_1)
                                    project_2[updateIndex]  = int(updateProj_2)
                                    project_3[updateIndex]  = int(updateProj_3)
                                    logic_test[updateIndex] = int(updateLog)
                                    perNilaiAkhir ()
                                    tampilkanData ()
                                    break
                                elif updateSimpan == 'N' :
                                    print('Update Tidak Di Simpan')
                                    break
                    elif updateYesNo == "N":
                        break         
            else :
                print('------------------------------------')
                print(f'Data NIM {updateNim} TIDAK TERSEDIA')
                print('------------------------------------')          
        elif updateMenu == '2' :
            break

def deleteData () :
    while (True) :
        print('------Menu Delete Data Nilai Mahasiswa------')
        print('1. Delete Data Nilai Mahasiswa')
        print('2. Kembali Ke menu Utama')
        print('--------------------------------------------')
        deleteMenu = input('Masukan Angka [1~2] : ')
        if deleteMenu == '1' :
            while (True) :
                tampilkanData ()
                while True :
                    deleteNim = input('Masukan NIM yang ingin di DELETE :')
                    if deleteNim.isnumeric():
                        break
                    else:
                        print('-----------------------------')
                        print("HANYA MASUKAN ANGKA")
                        print('-----------------------------')

                if deleteNim in nim :
                    deleteIndex = nim.index(deleteNim)
                    del nim [deleteIndex]         
                    del nama [deleteIndex]       
                    del exam_1 [deleteIndex]     
                    del exam_2 [deleteIndex]     
                    del exam_3 [deleteIndex]     
                    del project_1 [deleteIndex]   
                    del project_2 [deleteIndex]  
                    del project_3 [deleteIndex]  
                    del logic_test [deleteIndex]
                    tampilkanData ()
                    break
                else :
                    print('------------------------------------')
                    print(f'Data NIM {deleteNim} TIDAK TERSEDIA')
                    print('------------------------------------')
                    break
        elif deleteMenu == '2' :
            break

# Coding Utama
while True :
    menuUtama ()
    menu = input('Masukan Nomer Menu (1~5) : ')

    if menu == '1' :
        reportData ()
    
    elif menu == '2' :
        tambahData ()

    elif menu == '3' :
        updateData ()

    elif menu == '4' :
        deleteData ()

    elif menu == '5' :
        print('---------------------------------------------------------------')
        print('KELUAR Program Akademik Score - Data Nilai Mahasiswa Purwadhika')
        print('---------------------------------------------------------------')
        break
    
    else :
        print('-----------------')
        print('Masukan Angka 1~5')
        print('-----------------')