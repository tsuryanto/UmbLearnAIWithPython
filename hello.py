from datetime import date, timedelta

# tanggal mulai belajar
begin_date = date(2019, 9, 12)

# Mengambil tanggal hari ini
today = date.today()

# Cetak teks 
print("--------------------------------------------------------------")
print("Hari ini adalah hari ke" , (begin_date - today).days ,"saya belajar python.")
print("Saya belajar python sejak" , begin_date.strftime('%d/%m/%Y'))
print("--------------------------------------------------------------")