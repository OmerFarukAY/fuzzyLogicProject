<<<<<<< HEAD
import skfuzzy as fuzzy
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
import numpy as np

# Girdi ve çıktı değişkenlerinin tanımlandığı yer
aracinHizi = ctrl.Antecedent(np.arange(0, 181, 1), 'Aracin Hizi')
takipMesafesi = ctrl.Antecedent(np.arange(0, 101, 1), 'Takip Mesafesi')
frenSiddeti = ctrl.Consequent(np.arange(0, 101, 1), 'Fren Siddeti')


# Üyelik fonk. tanımlandığı yer
# Üyelik fonk. üçgen olarak ayarlandı

# Aracin Hizi için üyelik fonk.
aracinHizi['yavas'] = fuzzy.trimf(aracinHizi.universe, [0, 0, 70])
aracinHizi['normal'] = fuzzy.trimf(aracinHizi.universe, [50, 90, 130])
aracinHizi['hizli'] = fuzzy.trimf(aracinHizi.universe, [110, 180, 180])

# Takip Mesafesi için üyelik fonk.
takipMesafesi['cok_yakin'] = fuzzy.trimf(takipMesafesi.universe, [0, 0, 40])
takipMesafesi['yakin'] = fuzzy.trimf(takipMesafesi.universe, [20, 50, 80])
takipMesafesi['uzak'] = fuzzy.trimf(takipMesafesi.universe, [60, 100, 100])

# Frenin Şiddeti için üyelik fonk.
frenSiddeti['yok'] = fuzzy.trimf(frenSiddeti.universe, [0, 0, 20])
frenSiddeti['hafif'] = fuzzy.trimf(frenSiddeti.universe, [10, 30, 50])
frenSiddeti['orta'] = fuzzy.trimf(frenSiddeti.universe, [40, 60, 80])
frenSiddeti['sert'] = fuzzy.trimf(frenSiddeti.universe, [70, 100, 100])

# Grafikler için
=======
import numpy as np
import skfuzzy as fuzzy
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# 1. Girdi ve Çıktı Değişkenlerini Tanımlama (Universes)
# Antecedent: Girdi, Consequent: Çıktı
mesafe = ctrl.Antecedent(np.arange(0, 101, 1), 'mesafe') # 0-100 metre
hiz = ctrl.Antecedent(np.arange(0, 181, 1), 'hiz')       # 0-180 km/s
fren = ctrl.Consequent(np.arange(0, 101, 1), 'fren')     # 0-100 % şiddet

# 2. Üyelik Fonksiyonlarını Otomatik veya Manuel Tanımlama
# Kolaylık olması için otomatik (automf) tanımlayalım (3'lü: poor, average, good)
# Ama biz isimlerini Türkçeleştireceğiz.

# Mesafe için üyelik fonksiyonları (Üçgen)
mesafe['cok_yakin'] = fuzzy.trimf(mesafe.universe, [0, 0, 40])
mesafe['yakin'] = fuzzy.trimf(mesafe.universe, [20, 50, 80])
mesafe['uzak'] = fuzzy.trimf(mesafe.universe, [60, 100, 100])

# Hız için üyelik fonksiyonları (Üçgen)
hiz['yavas'] = fuzzy.trimf(hiz.universe, [0, 0, 70])
hiz['normal'] = fuzzy.trimf(hiz.universe, [50, 90, 130])
hiz['hizli'] = fuzzy.trimf(hiz.universe, [110, 180, 180])

# Fren Şiddeti için üyelik fonksiyonları (Üçgen)
fren['yok'] = fuzzy.trimf(fren.universe, [0, 0, 20])
fren['hafif'] = fuzzy.trimf(fren.universe, [10, 30, 50])
fren['orta'] = fuzzy.trimf(fren.universe, [40, 60, 80])
fren['sert'] = fuzzy.trimf(fren.universe, [70, 100, 100])

# --- GÖRSELLEŞTİRME (Sunum için) ---
# Bu satırları grafik görmek istiyorsan aktif et
>>>>>>> 01992f7a14335d27b6d7a5e8846c3ff377b3ee3e
#mesafe.view()
#hiz.view()
#fren.view()
#plt.show()
<<<<<<< HEAD

# Fuzzy kuralların tanımlandığı yer

# Takip Mesafesinin çok yakın olduğu durumlar
rule1 = ctrl.Rule(takipMesafesi['cok_yakin'] & aracinHizi['hizli'], frenSiddeti['sert'])
rule2 = ctrl.Rule(takipMesafesi['cok_yakin'] & aracinHizi['normal'], frenSiddeti['sert'])
rule3 = ctrl.Rule(takipMesafesi['cok_yakin'] & aracinHizi['yavas'], frenSiddeti['orta'])



# Takip Mesafesinin yakın olduğu durumlar
rule4 = ctrl.Rule(takipMesafesi['yakin'] & aracinHizi['hizli'], frenSiddeti['sert'])
rule5 = ctrl.Rule(takipMesafesi['yakin'] & aracinHizi['normal'], frenSiddeti['orta'])
rule6 = ctrl.Rule(takipMesafesi['yakin'] & aracinHizi['yavas'], frenSiddeti['hafif'])



# Takip Mesafesinin uzak olduğu durumlar
rule7 = ctrl.Rule(takipMesafesi['uzak'] & aracinHizi['hizli'], frenSiddeti['hafif'])
rule8 = ctrl.Rule(takipMesafesi['uzak'] & aracinHizi['normal'], frenSiddeti['yok'])
rule9 = ctrl.Rule(takipMesafesi['uzak'] & aracinHizi['yavas'], frenSiddeti['yok'])




# Kontrol sistemini oluşturmak için bütün kuralları girdik
frenlemeSistemi = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])
frenSimulasyonu = ctrl.ControlSystemSimulation(frenlemeSistemi)

#girdilerin alındığı yer
print("\n--Otonom Frenleme Başladı--")
print("Çıkmak için 'q' harfine basabilirsiniz.\n")

while True:
    hizGirdisi = input("Aracınızın hızını girin (0-180 km/s): ")

    # Çıkış yapılmak isteniyor mu kontrol et
    if hizGirdisi.lower() == 'q':
        print("Sistem kapatılıyor. Görüşmek üzere!")
        break


    mesafeGirdisi = input("Önünüzdeki araçla aranızdaki mesafeyi girin. (0-100 m): ")

    # Çıkış yapılmak isteniyor mu kontrol et
    if mesafeGirdisi.lower() == 'q':
        print("Sistem kapatılıyor. Görüşmek üzere!")
        break


    try:
        mesafeDegeri = float(mesafeGirdisi)
        hizDegeri = float(hizGirdisi)

        # Belirlenen sınırlar içinde girdi verildi mi kontrol ediyoruz
        if not (0 <= hizDegeri <= 180) or not (0 <= mesafeDegeri <= 100):
            print("Lütfen verilern sınırlar içinde bir değer giriniz!!! (Mesafe: 0-100, Hız: 0-180)\n")
            continue

        # Girilen değerler hesaplanıyor
        frenSimulasyonu.input['Aracin Hizi'] = hizDegeri
        frenSimulasyonu.input['Takip Mesafesi'] = mesafeDegeri
        frenSimulasyonu.compute()

        # Sonuç yazdırma
        fren_sonucu = frenSimulasyonu.output['Fren Siddeti']
        print(f" FREN ŞİDDETİ: %{fren_sonucu:.2f}\n")

    except ValueError:
        print("ERROR: Lütfen girdiğiniz değerin bir sayı olmasına dikkat edin!\n")
=======
# -----------------------------------

# 3. Bulanık Kuralları Tanımlama (Tam 3x3 Matris - 9 Kural)
# UZAK DURUMLARI
kural1 = ctrl.Rule(mesafe['uzak'] & hiz['yavas'], fren['yok'])
kural2 = ctrl.Rule(mesafe['uzak'] & hiz['normal'], fren['yok'])
kural3 = ctrl.Rule(mesafe['uzak'] & hiz['hizli'], fren['hafif']) # Hızlıysa uzak olsa bile hafif fren hazırda beklesin

# YAKIN DURUMLARI
kural4 = ctrl.Rule(mesafe['yakin'] & hiz['yavas'], fren['hafif'])
kural5 = ctrl.Rule(mesafe['yakin'] & hiz['normal'], fren['orta'])
kural6 = ctrl.Rule(mesafe['yakin'] & hiz['hizli'], fren['sert']) # Hızlı ve yakınsa sert fren!

# ÇOK YAKIN DURUMLARI
kural7 = ctrl.Rule(mesafe['cok_yakin'] & hiz['yavas'], fren['orta'])
kural8 = ctrl.Rule(mesafe['cok_yakin'] & hiz['normal'], fren['sert'])
kural9 = ctrl.Rule(mesafe['cok_yakin'] & hiz['hizli'], fren['sert']) # Çok yakın ve hızlıysa acil fren!

# 4. Kontrol Sistemini Oluşturma (Tüm 9 Kuralı Ekliyoruz)
fren_kontrol_sistemi = ctrl.ControlSystem([kural1, kural2, kural3, kural4, kural5, kural6, kural7, kural8, kural9])
fren_simulasyonu = ctrl.ControlSystemSimulation(fren_kontrol_sistemi)

# ---------------------------------------------------------
# 5. İNTERAKTİF SİSTEM TESTİ (Kullanıcı Girişi)
# ---------------------------------------------------------
print("\n--- Otonom Fren Sistemi Başlatıldı ---")
print("Çıkış yapmak için 'q' harfine basabilirsiniz.\n")

while True:
    mesafe_giris = input("Öndeki araca olan mesafeyi giriniz (0-100 metre): ")

    # Çıkış kontrolü
    if mesafe_giris.lower() == 'q':
        print("Sistemden çıkılıyor. İyi günler!")
        break

    hiz_giris = input("Aracın hızını giriniz (0-180 km/s): ")

    # Çıkış kontrolü
    if hiz_giris.lower() == 'q':
        print("Sistemden çıkılıyor. İyi günler!")
        break

    try:
        # Girilen metinleri ondalıklı sayıya (float) çeviriyoruz
        mesafe_degeri = float(mesafe_giris)
        hiz_degeri = float(hiz_giris)

        # Mantıksız değerler girilmesini engellemek için sınırları kontrol edelim
        if not (0 <= mesafe_degeri <= 100) or not (0 <= hiz_degeri <= 180):
            print("Lütfen belirlenen sınırlar içinde değer giriniz! (Mesafe: 0-100, Hız: 0-180)\n")
            continue

        # Değerleri sisteme verip hesaplatıyoruz
        fren_simulasyonu.input['mesafe'] = mesafe_degeri
        fren_simulasyonu.input['hiz'] = hiz_degeri
        fren_simulasyonu.compute()

        # Sonucu ekrana yazdırıyoruz
        fren_sonucu = fren_simulasyonu.output['fren']
        print(f">>> HESAPLANAN FREN ŞİDDETİ: %{fren_sonucu:.2f}\n")

    except ValueError:
        print("Hata: Lütfen sadece sayısal bir değer giriniz!\n")
>>>>>>> 01992f7a14335d27b6d7a5e8846c3ff377b3ee3e
