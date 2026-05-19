# Turing Makinesi ile Araç Plaka Tanıyıcı 

Bu proje, belirli bir dilin (formatın) geçerliliğini kontrol eden deterministik bir **Turing Makinesi Tanıyıcısı** simülatörüdür. Python ile geliştirilen bu sistem, `NNLLNNN` (N: Rakam, L: Büyük Harf) formatındaki araç plakalarını, hiçbir geleneksel koşul yapısı (`if-else`, `regex` vb.) kullanmadan tamamen **Otomata Teorisi durum geçişleriyle** doğrular.

## 🎯 Projenin Amacı ve Özellikleri

* **Durum Tabanlı Doğrulama:** Karakter analizleri if-else bloklarıyla değil, Turing makinesinin deterministik geçiş tablosu üzerinden yapılır.
* **Katı Format Kontrolü:** Makine; küçük harfleri, özel karakterleri ve format dizilimi hatalarını (örneğin harf beklenen yerde rakam olmasını) anında tespit ederek `q_reject` (RED) durumuna geçer.
* **Girdi Uzunluğu Denetimi:** Plakanın tam 7 karakter olduğunu doğrulamak için, 7. karakterden sonra bir Boşluk (`B`) sembolü bekler. Eksik veya fazla karakter girilmesi durumunda makine yine reddeder.
* **Tek Yönlü Okuma:** Bant üzerindeki kafa, modifiye işlemi yapmadan salt okunur mantığıyla soldan sağa ilerler.

## 🧠 Çalışma Mantığı (Durum Geçişleri)

Makinenin kullandığı durum (State) rotası şu şekildedir:
* `q0` -> 1. Karakter (Rakam bekleniyor)
* `q1` -> 2. Karakter (Rakam bekleniyor)
* `q2` -> 3. Karakter (Büyük harf bekleniyor)
* `q3` -> 4. Karakter (Büyük harf bekleniyor)
* `q4` -> 5. Karakter (Rakam bekleniyor)
* `q5` -> 6. Karakter (Rakam bekleniyor)
* `q6` -> 7. Karakter (Rakam bekleniyor)
* `q7` -> Uzunluk Kontrolü (Boşluk 'B' bekleniyor) -> **KABUL (q_accept)**

Makine, bulunduğu durumda beklediği sembol kümesi dışında herhangi bir karakter okursa, işlemi anında durdurarak **RED (q_reject)** çıktısı verir.

