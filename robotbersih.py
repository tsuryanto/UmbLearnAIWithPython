# Array nama ruangan
rooms = ["A","B"]

# Lakukan pengulangan pada program
while True:

    # Tanya nama ruangan
    ruangan = input("Nama ruangan (A/B) ? ").upper()

    print("Saat ini anda berada di ruangan : ", ruangan)

    # Tanya kondisi ruangan
    kondisi = input("Kondisi kebersihan (bersih/kotor) ? ").upper()

    # Tampilkan ruangan dan kondisinya
    print("Konsisi saat ini di", ruangan , " : " , kondisi)

    # Tampilkan reaksi Robot
    print("####### REAKSI ROBOT #######")
    
    if kondisi == "KOTOR" :         
        print("Bersihkan", ruangan)        
    else :
        print("Pindah Ke " + rooms[ (rooms.index(ruangan)+1)%2 ])

    print("############################") 

    if (ruangan == "") : 
        break