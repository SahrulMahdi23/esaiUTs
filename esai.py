import datetime as brth

def hitung_umur():
    print('silahkan masukkan tanggal, \nbulan lahir anda\n')
    tanggal = int(input('Tanggal \t:'))
    bulan = int(input('Bulan \t\t:'))
    tahun = int(input('Tahun \t\t:'))

    tanggal_lahir = brth.date(tahun,bulan,tanggal)
    print(f'Tanggal lahir anda adalah  {tanggal_lahir}')
    print(f"a day is {tanggal_lahir:%A}")
    print('\n')

    hari_ini = brth.date.today()
    print(f'hari ini adalah {hari_ini}')
    print('\n')

    umur_hari = hari_ini - tanggal_lahir

    umur_thn = umur_hari.days // 365

    umur_bln = (umur_hari.days % 365)//31

    umur_Hari =(umur_hari.days % 365)//7
    if umur_Hari >31:
      print('Umur anda sekarang adalah:',umur_thn,'tahun',umur_bln,'bulan',(umur_Hari-30),'hari ')
    else:
        print('Umur anda sekarang adalah:',umur_thn,'tahun',umur_bln,'bulan',umur_Hari,'hari ')



def BMI_pengukuran_Metrik(berat,tinggi):
    berat = float(input("Masukkan berat badan (kg): "))
    tinggi = float(input("Masukkan tinggi badan (m): "))
    bmi = berat / (tinggi ** 2)
    if bmi < 18.5:
        print( f"BMI anda :{bmi}\nberat badan anda kurang")
    elif bmi < 24.9:
        print( f"BMI anda :{bmi}\nberat badan anda normal")
    elif bmi < 29.9:
        print( f"BMI anda :{bmi}\nBerat badan berlebih")
    elif bmi < 34.9:
        print( f"BMI anda :{bmi}\nObesitas tingkat 1")
    elif bmi < 39.9:
        print( f"BMI anda :{bmi}\nObesitas tingkat 2")
    else:
        print( f"BMI anda :{bmi}\n Obesitas tingkat 3")

def BMI_pengukuran_Imperal(berat,tinggi):
    berat = float(input("Masukkan berat badan anda(pound): ")) 
    tinggi = float(input("Masukkan  badan anda(inci): "))
    bmi = (berat / tinggi**2)*703

    if bmi < 18.5:
        print( )
    elif bmi < 24.9:
        print( f"BMI anda :{bmi},\nberat badan anda kurang")
    elif bmi < 29.9:
        print( f"BMI anda :{bmi},\nBerat badan berlebih")
    elif bmi < 34.9:
        print( f"BMI anda :{bmi},\nObesitas tingkat 1")
    elif bmi < 39.9:
        print( f"BMI anda :{bmi},\nObesitas tingkat 2")
    else:
        print( f"BMI anda :{bmi},\n Obesitas tingkat 3")
 
def hitung_sisa_tahun_angsuran(tahun_mulai, durasi_angsuran):
    tahun_sekarang = brth.today().year
    sisa_tahun_angsuran = tahun_mulai + durasi_angsuran - tahun_sekarang
    if sisa_tahun_angsuran < 0:
        return "Anda telah melunasi angsuran."
    else:
        return sisa_tahun_angsuran

    tahun_mulai = int(input("Masukkan tahun mulai angsuran: "))
    durasi_angsuran = int(input("Masukkan durasi angsuran (dalam tahun): "))

    sisa_tahun = hitung_sisa_tahun_angsuran(tahun_mulai, durasi_angsuran)
    print("Sisa tahun angsuran:", sisa_tahun)


def main():
  while True:
    print('=====Menu Aplikasi=====\n')
    print('1.Aplikasi Hitung Umur')
    print('2.Aplikasi Hitung sisa tahun angsuran')
    print('3.Aplikasi Hitung BMI Metrik')
    print('4.Aplikasi Hitung BMI imperal')
    print('5.QUIT')
    
    menu = (input('Silahkan pilih Menu yang tersedia\n '))
    if menu == '1':
      hitung_umur()
    elif menu == '2':
      hitung_sisa_tahun_angsuran()
    elif menu == '3':
      BMI_pengukuran_Metrik('berat','tinggi')
    elif menu == '4':
      BMI_pengukuran_Imperal('berat','tinggi')
    elif menu == 'D':
      print('terima kasih........')  
      break
    else:
      print('pilihan anda tidak valid,silahkan pilih menu yang tersedia') 

main()