class PlakaTaniyiciTuringMakinesi:
    def __init__(self, plaka_string):
        # Bantı oluşturuyoruz ve sonuna boşluk (B) karakterleri ekliyoruz
        self.bant = list(plaka_string) + ['B'] * 3 
        self.kafa = 0
        self.durum = 'q0'
        self.kabul_durumu = 'q_accept'
        self.red_durumu = 'q_reject'
        self.gecis_tablosu = {}
        self._tabloyu_olustur()

    def _tablo_ekle(self, durum, okunan, yeni_durum, yazilan, yon):
        self.gecis_tablosu[(durum, okunan)] = (yeni_durum, yazilan, yon)

    def _tabloyu_olustur(self):
        # Rakamlar (0-9) ve Büyük Harfler (A-Z) listeleri
        rakamlar = [str(i) for i in range(10)]
        harfler = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

        # --- GEÇERLİ DURUM (STATE) GEÇİŞLERİ ---
        
        # q0: 1. Karakter (Rakam bekleniyor)
        for r in rakamlar:
            self._tablo_ekle('q0', r, 'q1', r, 'R')
            
        # q1: 2. Karakter (Rakam bekleniyor)
        for r in rakamlar:
            self._tablo_ekle('q1', r, 'q2', r, 'R')
            
        # q2: 3. Karakter (Büyük harf bekleniyor)
        for h in harfler:
            self._tablo_ekle('q2', h, 'q3', h, 'R')
            
        # q3: 4. Karakter (Büyük harf bekleniyor)
        for h in harfler:
            self._tablo_ekle('q3', h, 'q4', h, 'R')
            
        # q4: 5. Karakter (Rakam bekleniyor)
        for r in rakamlar:
            self._tablo_ekle('q4', r, 'q5', r, 'R')
            
        # q5: 6. Karakter (Rakam bekleniyor)
        for r in rakamlar:
            self._tablo_ekle('q5', r, 'q6', r, 'R')
            
        # q6: 7. Karakter (Rakam bekleniyor)
        for r in rakamlar:
            self._tablo_ekle('q6', r, 'q7', r, 'R')
            
        # q7: Bitiş (Uzunluk kontrolü için Boşluk 'B' bekleniyor)
        self._tablo_ekle('q7', 'B', self.kabul_durumu, 'B', 'R')

        # NOT: Geçersiz karakterler (küçük harfler, özel karakterler, 
        # beklenmeyen rakam/harfler) geçiş tablosuna BİLEREK eklenmedi. 
        # Makine tabloda karşılığını bulamazsa otomatik olarak RED yiyecektir.

    def bandi_yazdir(self):
        bant_str = "".join(self.bant).rstrip('B')
        if not bant_str:
            bant_str = "B"
        print(f"Bant: [{bant_str}]")
        print(" " * (self.kafa + 7) + "^")

    def calistir(self):
        adim = 1
        print("\n--- PLAKA KONTROLÜ BAŞLIYOR ---")
        
        while self.durum != self.kabul_durumu and self.durum != self.red_durumu:
            okunan_sembol = self.bant[self.kafa]
            gecis_anahtari = (self.durum, okunan_sembol)

            # EĞER OKUNAN KARAKTER O DURUM İÇİN GEÇİŞ TABLOSUNDA YOKSA -> RED!
            if gecis_anahtari not in self.gecis_tablosu:
                print(f"\nAdım {adim}:")
                print(f"Mevcut Durum: {self.durum} | Okunan: '{okunan_sembol}' -> BEKLENMEYEN KARAKTER!")
                self.durum = self.red_durumu
                break

            # Tabloda varsa işlemi yap ve sağa ilerle
            yeni_durum, yazilan_sembol, yon = self.gecis_tablosu[gecis_anahtari]

            print(f"\nAdım {adim}:")
            print(f"Mevcut Durum: {self.durum} | Okunan: {okunan_sembol} | Yazılan: {yazilan_sembol} | Yön: {yon}")
            
            self.bant[self.kafa] = yazilan_sembol
            self.durum = yeni_durum
            
            if yon == 'R':
                self.kafa += 1
                
            self.bandi_yazdir()
            adim += 1
            
        print("\n" + "="*30)
        if self.durum == self.kabul_durumu:
            print("SONUÇ: KABUL (Geçerli Plaka)")
        else:
            print("SONUÇ: RED (Geçersiz Plaka)")
        print("="*30)

def main():
    print("Turing Makinesi - Araç Plaka Tanıyıcı (Format: NNLLNNN)")
    print("Çıkmak için 'q' tuşuna basın.\n")
    
    while True:
        girdi = input("Kontrol edilecek plakayı girin: ")
        
        if girdi.lower() == 'q':
            print("Çıkış yapılıyor...")
            break
            
        if not girdi:
            print("Lütfen bir plaka girin!")
            continue

        tm = PlakaTaniyiciTuringMakinesi(girdi)
        tm.calistir()
        print("\n")

if __name__ == "__main__":
    main()
