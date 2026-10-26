define narrator = Character(None)
define alya = Character("Alya")

image bg room = Solid("#1f1f1f")
image bg garden = Solid("#334d5c")
image bg street = Solid("#404040")

default trust = 0
default courage = 0
default curiosity = 0

label start:
    scene bg room
    with fade

    narrator "Suatu hari, hujan turun dengan lebat."
    narrator "Kamu duduk di kamar sambil menunggu telepon dari seseorang yang sudah lama tidak muncul."
    alya "Hei, aku sudah menunggu lama. Kamu datang tepat waktu."

    menu:
        "Apa yang sebenarnya terjadi?":
            $ curiosity += 1
            alya "Ada sesuatu yang harus kita selesaikan sebelum semuanya terlambat."
        "Kenapa kamu terlihat cemas?":
            $ trust += 1
            alya "Karena aku takut kehilangan orang yang paling penting bagiku."
        "Aku tidak yakin dengan semua ini.":
            $ courage += 1
            alya "Kalau begitu, kita cari tahu bersama."

    narrator "Alya menatapmu dengan serius."
    menu:
        "Ayo pergi ke taman sekarang.":
            $ courage += 1
            jump taman
        "Mungkin kita sebaiknya menunggu sebentar.":
            $ trust += 1
            jump rumah
        "Aku ingin pulang dan berpikir dulu.":
            $ curiosity += 1
            jump pulang

label taman:
    scene bg garden
    with fade

    alya "Aku ingin mengatakan sesuatu yang sangat penting."
    menu:
        "Dengarkan aku dulu.":
            $ trust += 1
            jump keputusan
        "Aku juga ingin jujur.":
            $ courage += 1
            jump keputusan
        "Aku tidak tahu harus berkata apa.":
            $ curiosity += 1
            jump keputusan

label rumah:
    scene bg room
    with fade

    alya "Aku tidak ingin kehilanganmu."
    menu:
        "Aku ada di sini, jangan takut.":
            $ trust += 1
            jump keputusan
        "Kita bisa bicara nanti.":
            $ courage += 1
            jump keputusan
        "Aku masih bingung.":
            $ curiosity += 1
            jump keputusan

label pulang:
    scene bg street
    with fade

    alya "Kalau begitu, apakah kita benar-benar masih bisa bersama?"
    menu:
        "Aku tidak ingin kehilanganmu.":
            $ trust += 1
            jump keputusan
        "Aku akan menghadapi semuanya.":
            $ courage += 1
            jump keputusan
        "Aku butuh waktu.":
            $ curiosity += 1
            jump keputusan

label keputusan:
    narrator "Alya menunggu jawabanmu."
    menu:
        "Aku memilih percaya padamu.":
            $ trust += 1
        "Aku memilih jujur tentang perasaanku.":
            $ courage += 1
        "Aku memilih tetap berhati-hati.":
            $ curiosity += 1

    jump akhir

label akhir:
    if trust >= 5:
        jump ending_bahagia
    elif courage >= 4:
        jump ending_berani
    elif curiosity >= 4:
        jump ending_netral
    else:
        jump ending_buruk

label ending_bahagia:
    scene black
    with fade

    narrator "ENDING BAHAGIA"
    narrator "Kamu dan Alya memilih saling percaya. Hujan berhenti, dan hari itu menjadi awal dari perjalanan baru yang indah."
    return

label ending_berani:
    scene black
    with fade

    narrator "ENDING BERANI"
    narrator "Kamu memilih menghadapi kenyataan dengan berani. Walau berat, keputusan itu membuka jalan menuju hubungan yang lebih jujur dan tulus."
    return

label ending_netral:
    scene black
    with fade

    narrator "ENDING NETRAL"
    narrator "Kamu tidak sepenuhnya yakin, tapi tetap melangkah. Cerita berakhir dengan banyak pertanyaan yang belum terjawab."
    return

label ending_buruk:
    scene black
    with fade

    narrator "ENDING BURUK"
    narrator "Keputusan yang kamu ambil membuat hubungan itu rusak. Semua berakhir dengan luka, kesedihan, dan penyesalan."
    return