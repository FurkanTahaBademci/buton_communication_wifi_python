# Buton Device Reader

# Gerekli Kütüphaneleri Kurun

```
pip install -r requirements.txt
```

# Kullanım

```
python main.py
```

# Açıklamlar

Bu iki satır, gerekli modülleri (ButtonComm ve time) içe aktarır. ButtonComm, ESP8266 ile iletişim kurmak için kullanılacak özel bir modül olabilir. time, zaman fonksiyonlarını kullanmamıza izin verir.

```
import ButtonComm
import time
```

Bu satırlar, ESP8266'nın IP adresini tanımlar. Bu IP adresi, ESP8266 modülünün bulunduğu ağdaki adresi olmalıdır.

```
# Kullanımı
# Buton IP adresisini giriniz
esp_ip = "192.168.4.1"
```

run() adında bir fonksiyon tanımlanıyor. Bu fonksiyon, sürekli olarak ESP8266 ile iletişim kurarak pin durumunu kontrol eder. Sonsuz bir döngü (while True) içindedir, bu da programın bu işlevi sürekli olarak gerçekleştireceği anlamına gelir.

```
def run():
    """
    Sürekli olarak ESP8266 ile iletişim kurarak pin durumunu kontrol eder.
    """
    while True:
```

ButtonComm.ButtonClient(esp_ip) çağrısı, ESP8266 ile iletişim kurar ve butonun durumunu döndürür. Bu durum, result değişkenine atanır ve ardından ekrana yazdırılır.

```
result = ButtonComm.ButtonClient(esp_ip)
print(result)
```

result'ın değerine göre, butona basılıp basılmadığını veya butonun serbest olup olmadığını belirten bir mesaj yazdırılır.

```
if result == "1":
    print("Butona basıldı")
elif result == "0":
    print("Buton serbest")
```

Eğer result içinde "bağlanılamadı" veya "zaman aşımına uğradı" gibi bir hata mesajı varsa, program 3 saniye bekler (time.sleep(3)). Aksi halde, normal sorgu döngüsü için kısa bir bekleme süresi olan 0.05 saniye bekler (time.sleep(0.05)).

```
if "bağlanılamadı" in result or "zaman aşımına uğradı" in result:
    # Bağlantı hatasında belirlenen süre kadar bekle
    time.sleep(3)
else:
    # Normal sorgu döngüsü için kısa bir bekleme süresi
    time.sleep(0.05)

```

Bu kod parçası, betiğin doğrudan çalıştırılması durumunda run() fonksiyonunu çağırır. Bu, modül olarak da kullanılabileceği anlamına gelir ve bu durumda run() fonksiyonu başka bir dosya tarafından çağrılabilir.

```
if __name__ == "__main__":
    run()
```
