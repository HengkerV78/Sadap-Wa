#coding=utf-8

# Created By Thonxyzz404'Cyber
# Member Ngapak Code!
# Thanks To BiiDev, Rizki-X, Kang Code, Code Jawa
# Males Encrypt Bang, Kalo Mah Ganti Author Ganti Ajah!
import sys,os,time,random

#color
h = "\033[1;32m"
m = "\033[1;91m"
p = "\033[1;37m"

# logo doang
def logo():
    print("""
%s  |  | |_   _  |_  _  /\   _   _  
%s  |/\| | ) (_| |_ _) /--\ |_) |_) %sKhusus Nomer Indosat Saja!!!%s• %sThonxyzz404'Cyber
%s     HACK AKUN WHATSAPP  %s |   |   """%(p,p,h,p,h,h,p))

# Kalo Ada Yang Ribet Ngapain Yang Ezz?
code1 = "1"
code2 = "2"
code3 = "3"
code4 = "4"
code5 = "5"
code6 = "6"
code7 = "7"
code8 = "8"
code9 = "9"

# Random Code
random1 = random.choice([code1,code2,code3,code4,code5,code6,code7,code8,code9])
random2 = random.choice([code1,code2,code3,code4,code5,code6,code7,code8,code9])
random3 = random.choice([code1,code2,code3,code4,code5,code6,code7,code8,code9])
random4 = random.choice([code1,code2,code3,code4,code5,code6,code7,code8,code9])

# Konfir Code
codeconfir = (random1+random2+random3+random4)
generate = codeconfir

#prank1
dahlah = ("""\n %s[%s•%s] Gw : Woyy 🙄
 %s[%s•%s] Dia : Apaan Anjg 😒
 %s[%s•%s] Gw : Besok Bantuin Gua 😁
 %s[%s•%s] Dia : Bantuiin Apa? 🤔
 %s[%s•%s] Gw : Biasa Brantem Ama Gang Sebelah 😈
 %s[%s•%s] Dia : Emang Lu Ada Masalah Apa? 🗿
 %s[%s•%s] Gw : Udh Besok Gua Jelasin 😑
 %s[%s•%s] Dia : Ya Udh Jam Berpa? 🤨
 %s[%s•%s] Gw : Malam Biasa Jangan Sore, Masih Banyak Bocah Soalnya
 %s[%s!%s] System Sibuk Mohon Ulangi Lagi!"""%(p,h,p,p,h,p,p,h,p,p,h,p,p,h,p,p,h,p,p,h,p,p,h,p,p,h,p,p,m,p))

#disconnet
ngentot = ("""
 %s[%s!%s]  Maaf Ingfo WhatsApp Tidak Terjangkau, Mohon Ulangi Lagii!"""%(p,m,p))

#prank2
waduh = ("""\n %s[%s•%s] Aku : Sayang Lagi Ngapain? 😇
 %s[%s•%s] Kamu : Lagi Makan Klo Kamu yang? 🤨
 %s[%s•%s] Aku : Kalo Aku Lagi Duduk 😌
 %s[%s•%s] Kamu : Owhh, Besok Kamu Ada Waktu Gak? 🤔
 %s[%s•%s] Aku : Enggk Emang Knpa Yang? 🙄
 %s[%s•%s] Kamu : Besok Ayng Mau Gak Jalan Jalan Sore, Sama Aku 😏
 %s[%s•%s] Aku : Mauu Tapi Jam Berapa Yang? 🤔
 %s[%s•%s] Kamu : Jam 4 Ajah Di Tempat Biasa 😁
 %s[%s•%s] Aku : Y udh Besok Aku Tunggu Ya 😇
 %s[%s!%s] System Sibuk Mohon Ulangi Lagi!"""%(p,h,p,p,h,p,p,h,p,p,h,p,p,h,p,p,h,p,p,h,p,p,h,p,p,h,p,p,m,p))

#gabungan
kontolmu = random.choice([ngentot,waduh,dahlah])

#hackwa
def hackwa():
    os.system('clear');logo();print(50*"~")
    print("%s [%s✓%s] Ex No: %s0896××7×8×7×%s"%(p,h,p,h,p))
    no = input("%s [%s•%s] Nomor Kamu: "%(p,h,p))
    wame = input("%s [%s•%s] Nomor Target: "%(p,h,p))
    if len(no) < 12:
        print("\n%s [%s!%s] Nomor Kamu Harus 12 Digit Tidak Boleh Kurang!"%(p,m,p));os.sys.exit()
    elif len(wame) < 12:
        print("\n%s [%s!%s] Nomor Target Harus 12 Digit Tidak Boleh Kurang!"%(p,m,p));os.sys.exit()
    elif len(no) !=12:
        print("\n%s [%s!%s] Nomor Kamu Harus 12 Digit Tidak Boleh Lebih!"%(p,m,p));os.sys.exit()
    elif len(wame) !=12:
        print("\n%s [%s!%s] Nomor Target Harus 12 Digit Tidak Boleh Lebih!"%(p,m,p));os.sys.exit()
    elif len(no) and len(wame) == 12:
        print("%s [%s•%s] Sedang Verifikasi Code..."%(p,h,p));time.sleep(5)
        print("%s [%s•%s] Code: %s%s%s"%(p,h,p,h,generate,p));time.sleep(1)
        print("\n%s [%s•%s] Masukan Kode WhatsApp Yang Terkirim Ke No Kamu"%(p,h,p));time.sleep(1)
        kodenya=input("%s [%s•%s] Kode: "%(p,h,p))
        if kodenya == "":
            print("\n%s [%s!%s] Maaf Tidak Boleh Kosong!"%(p,m,p));os.sys.exit()
        elif len(kodenya) < 4:
            print("\n%s [%s!%s] Maaf Kode Harus 4 Digit Tidak Boleh Kurang!"%(p,m,p));os.sys.exit()
        elif len(kodenya) != 4:
            print("\n%s [%s!%s] Maaf Kode Harus 4 Digit Tidak Boleh Lebih!"%(p,m,p));os.sys.exit()
        elif kodenya == generate:
            print("\n%s [%s•%s] Get Ingfo WhatssApp"%(p,h,p));time.sleep(7)
            if kontolmu == waduh:
                print("%s [%s•%s] Berhasil Mengambil Ingfo WhatsApp Target"%(p,h,p));time.sleep(1)
                print(waduh)
            elif kontolmu == ngentot:
                print(ngentot)
            elif kontolmu == dahlah:
                print("%s [%s•%s] Berhasil Mengambil Ingfo WhatsApp Target"%(p,h,p));time.sleep(1)
                print(dahlah)
            else:time.sleep(1);print("\n%s [%s!%s] Maaf System WhatsApp Sedang Sibuk!"%(p,m,p));os.sys.exit()
        else:print("\n%s [%s!%s] Maaf Kode Tidak Valid!"%(p,m,p));os.sys.exit()
    else:print("\n%s [%s!%s] Terjadi Kesalahan!"%(p,m,p));os.sys.exit()

if __name__ == '__main__':
	hackwa()
