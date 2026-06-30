# PayGate-Mini

PayGate-Mini, temel ödeme işlemlerini simüle eden bir API projesidir. Bu projenin temel amacı, sadece kod yazmak değil; yazılan kodun otomatik olarak test edilip, paketlenip, canlı sunucuya hatasız bir şekilde aktarılmasını (CI/CD) sağlamaktır.

## Kullanılan Teknolojiler

* **Yazılım Dili:** Python, Flask
* **Test Aracı:** PyTest
* **Paketleme:** Docker
* **Otomasyon:** Jenkins
* **Versiyon Kontrolü:** Git & GitHub

## Sistem Nasıl Çalışıyor? (Otomasyon Süreci)

Projeye yeni bir kod eklenip GitHub'a gönderildiğinde (push), Jenkins arka planda şu 4 adımı otomatik olarak çalıştırır:

1. **Kodu İndirme:** Sistemdeki en güncel kodlar GitHub'dan alınır.
2. **Paketleme (Docker Build):** Uygulamanın her bilgisayarda ve sunucuda sorunsuz çalışması için kodlar bir Docker kutusu (imajı) haline getirilir.
3. **Otomatik Test:** Sistemin çökmesini engellemek için ödeme kuralları izole bir ortamda test edilir. Testte hata çıkarsa süreç durdurulur ve hatalı kodun yayına çıkması engellenir.
4. **Canlıya Alma:** Testler başarıyla geçerse, eski çalışan sistem kapatılır ve güncel versiyon kesintisiz olarak yayına alınır.

## 🚀 Projeyi Kendi Bilgisayarında Çalıştırma

Projeyi bilgisayarınıza indirip Docker ile hemen ayağa kaldırmak için aşağıdaki komutları sırasıyla terminale yazabilirsiniz:

**1. Projeyi İndirin**
```bash
git clone [https://github.com/GuvenUlger/PayGate-Mini.git](https://github.com/GuvenUlger/PayGate-Mini.git)
cd PayGate-Mini
```

**2.Docker Paketini Oluşturun**
```bash
docker build -t paygate-mini:latest .
```

**3. Uygulamayı Başlatın**
```bash
docker run -d -p 8080:8080 --name paygate-container paygate-mini:latest
```

**API Kullanımı**
Uygulama çalıştıktan sonra 8080 portu üzerinden istekleri dinlemeye başlar.

İstek Adresi: POST /api/v1/pay

Geliştirici: Güven Ülger