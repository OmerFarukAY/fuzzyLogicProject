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
#mesafe.view()
#hiz.view()
#fren.view()
#plt.show()
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