import tkinter as tk
import json

from tkinter import messagebox

gorevler = []
def gorev_ekle():
    yeni_gorev = gorev_girisi.get()
    onem_puani_girisi_veri = onem_puani_girisi.get()
    if not yeni_gorev.strip():
        messagebox.showwarning("Uyarı", "Lütfen bir görev girin.")
        return
    try:
        onem_puani = int(onem_puani_girisi_veri)
        if onem_puani < 0 or onem_puani > 3:
            messagebox.showwarning("Uyarı", "Önem puanı 0-3 arasında bir rakam olmalıdır.")
            return
        gorevler.append({"gorev": yeni_gorev, "tamamlandi": False, "onem_puani": onem_puani})
        liste_guncelle()
    except(ValueError):
        messagebox.showwarning("Uyarı", "Önem puanı 0-3 arasında bir rakam olmalıdır.")
        return

def gorev_sil():
    try:
        secilen_gorev_indexi = int(gorev_listesi1.curselection()[0])
        del gorevler[secilen_gorev_indexi]
        liste_guncelle()
    except (IndexError,ValueError):
        pass
def gorev_iptal_et():
    try:
        secilen_gorev_indexi = int(gorev_listesi.curselection()[0])
        del gorevler[secilen_gorev_indexi]
        liste_guncelle()
    except (IndexError,ValueError):
        pass
def gorev_durumunu_degistir():
    try:
        secili_gorev_indexi = int(gorev_listesi.curselection()[0])
        gorevler[secili_gorev_indexi]["tamamlandi"] = not gorevler[secili_gorev_indexi]["tamamlandi"]
        liste_guncelle()
    except IndexError:
        pass
def liste_guncelle():
    gorevler.sort(key=lambda x: x['onem_puani'] -x['tamamlandi'], reverse=True)
    gorev_listesi.delete(0, tk.END)
    gorev_listesi1.delete(0, tk.END)

    for i, gorev_bilgisi in enumerate(gorevler):
        gorev_metni = gorev_bilgisi["gorev"]
        if gorev_bilgisi["tamamlandi"]:
            gorev_metni = f"[Tamamlandi] {gorev_metni}"
            gorev_listesi1.insert(tk.END, gorev_metni)
        else:
            gorev_metni = f"[Tamamlanmadi] {gorev_metni}"
            gorev_listesi.insert(tk.END, gorev_metni)
def gorevleri_kaydet():
    with open('gorevler.json', 'w') as dosya:
        json.dump(gorevler, dosya)
def gorevleri_yukle():
    global gorevler
    try:
        with open('gorevler.json', 'r') as dosya:
            gorevler = json.load(dosya)
    except (FileNotFoundError, json.JSONDecodeError):
        gorevler = []

gorevleri_yukle()
pencere = tk.Tk()
pencere.title("Yapilacaklar Listesi")

cerceve = tk.Frame(pencere)
cerceve.pack()
Görevler= tk.Label(cerceve, width=25,text="Görevler", font=("Arial", 12))
Görevler.pack()
gorev_listesi = tk.Listbox(cerceve, width=48, height=10, font=("Arial", 12))
gorev_listesi.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

kaydirici = tk.Scrollbar(cerceve, orient=tk.VERTICAL)
kaydirici.config(command=gorev_listesi.yview)
kaydirici.pack(side=tk.RIGHT, fill=tk.Y)

gorev_listesi.config(yscrollcommand=kaydirici.set)

cerceve5 = tk.Frame(pencere)
cerceve5.pack()
tamamlananlar= tk.Label(cerceve5, width=25,text="Tamamlananlar", font=("Arial", 12))
tamamlananlar.pack()
gorev_listesi1 = tk.Listbox(cerceve5, width=48, height=10, font=("Arial", 12))
gorev_listesi1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

kaydirici = tk.Scrollbar(cerceve5, orient=tk.VERTICAL)
kaydirici.config(command=gorev_listesi1.yview)
kaydirici.pack(side=tk.RIGHT, fill=tk.Y)

gorev_listesi1.config(yscrollcommand=kaydirici.set)

cerceve2 = tk.Frame(pencere)
cerceve2.pack()
gorev_girisi = tk.Entry(cerceve2, width=25, font=("Arial", 12))
gorev_girisi.pack(side=tk.RIGHT)
gorev_girisi_etiket = tk.Label(cerceve2, width=25,text="Görev Girişi :", font=("Arial", 12))
gorev_girisi_etiket.pack(side=tk.RIGHT)
cerceve3 = tk.Frame(pencere)
cerceve3.pack()
onem_puani_girisi = tk.Entry(cerceve3, width=25, font=("Arial", 12))
onem_puani_girisi.pack(side=tk.RIGHT)

onem_puani_etiket = tk.Label(cerceve3,width=25, text="Önem Puanı(1,2,3):", font=("Arial", 12))
onem_puani_etiket.pack(side=tk.RIGHT)

gorev_ekle_buton = tk.Button(pencere, text="Gorev Ekle", width=50, command=gorev_ekle,font=("Arial", 12))
gorev_ekle_buton.pack()
cerceve6 = tk.Frame(pencere)
cerceve6.pack()
gorev_sil_buton = tk.Button(cerceve6, text="Gorev iptal et", width=24, command=gorev_iptal_et,font=("Arial", 12))
gorev_sil_buton.pack(side=tk.LEFT)
gorev_iptal_buton=tk.Button(cerceve6, text="Gorev sil", width=24, command=gorev_sil,font=("Arial", 12))
gorev_iptal_buton.pack(side=tk.RIGHT)
gorev_durum_degistir_buton = tk.Button(pencere, text="Görevi Tamamla", width=50, command=gorev_durumunu_degistir,font=("Arial", 12))
gorev_durum_degistir_buton.pack()
def gorevleri_kaydet_ve_cik():
    gorevleri_kaydet()
    pencere.destroy()

pencere.protocol("WM_DELETE_WINDOW", gorevleri_kaydet_ve_cik)

liste_guncelle()

pencere.mainloop()
