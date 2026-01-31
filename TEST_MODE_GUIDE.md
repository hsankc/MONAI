# 🧪 Test Mode Kullanım Kılavuzu

## Test Mode Nedir?

Test Mode, Monad Access platformunu **cüzdan bağlamadan** ve **para ödemeden** test etmenizi sağlayan özel bir moddur. Hackathon demoları ve geliştirme için idealdir.

---

## ✨ Yeni Özellikler

### 1. **TESTNET Badge**
- Header'da "MONAD ACCESS" logosunun yanında sarı **TESTNET** işareti
- Projenin testnet üzerinde çalıştığını gösterir
- Yanıp sönen animasyon ile dikkat çeker

### 2. **Test Mode Toggle**
- Header'da yeşil/kırmızı toggle switch
- **Yeşil (ON)**: Test Mode aktif - Cüzdan gerekmez
- **Kırmızı (OFF)**: Production Mode - MetaMask gerekli

---

## 🎮 Nasıl Kullanılır?

### Test Mode Aktifken (Varsayılan)

1. **Sayfayı Açın**: `http://localhost:5000`
2. **Test Mode Açık**: Toggle yeşil olmalı (varsayılan)
3. **Servisi Seçin**: 5 servisten birini seçin
4. **Input Girin**: Gerekli bilgileri girin
5. **Butona Tıklayın**: Servis butonuna tıklayın
6. **Sonucu Görün**: Terminal'de sonuçları izleyin

**ÖNEMLİ**: 
- ❌ Cüzdan bağlamanıza gerek YOK
- ❌ MetaMask popup çıkmaz
- ❌ Para ödemezsiniz
- ✅ Tüm servisler çalışır
- ✅ Terminal'de `[TEST MODE]` mesajları görürsünüz

### Production Mode (Test Mode Kapalı)

1. **Toggle'ı Kapatın**: Test Mode toggle'ına tıklayın (kırmızı olur)
2. **Cüzdan Bağlayın**: "Connect Wallet" butonuna tıklayın
3. **MetaMask Onaylayın**: MetaMask'ta bağlantıyı onaylayın
4. **Servisi Kullanın**: Artık gerçek transaction'lar yapılır

---

## 📸 Ekran Görüntüleri

### Test Mode Aktif

![Test Mode UI](C:/Users/hasan/.gemini/antigravity/brain/aacbdfce-7784-4bba-ba6e-cf4d246fa084/initial_load_testmode_check_1769700956297.png)

**Görünenler:**
- ✅ TESTNET badge (sarı)
- ✅ Test Mode toggle (yeşil/aktif)
- ✅ Connect Wallet butonu (soluk, opsiyonel)

### Terminal Çıktısı (Test Mode)

![Terminal Output](C:/Users/hasan/.gemini/antigravity/brain/aacbdfce-7784-4bba-ba6e-cf4d246fa084/terminal_output_test_mode_1769701027240.png)

**Terminal Mesajları:**
```
[18:36:42] Test Mode is ACTIVE - No wallet or payment required!
[18:36:42] Toggle Test Mode OFF to use real MetaMask transactions
[18:36:50] [TEST MODE] Initiating gpt-pro service...
[18:36:50] [TEST MODE] Payment skipped (would be 0.005 MON)
[18:36:50] Calling gpt-pro API...
[18:36:51] GPT-Pro completed successfully!
[18:36:51] Query: What is blockchain?
[18:36:51] Response: Based on advanced AI analysis...
[18:36:51] Tokens used: 342
```

---

## 🔄 Test Mode vs Production Mode

| Özellik | Test Mode (ON) | Production Mode (OFF) |
|---------|---------------|---------------------|
| **Cüzdan Gerekli** | ❌ Hayır | ✅ Evet |
| **MetaMask Popup** | ❌ Çıkmaz | ✅ Çıkar |
| **Para Ödemesi** | ❌ Yok | ✅ Gerçek MON |
| **Servis Çalışır** | ✅ Evet | ✅ Evet |
| **Terminal Mesajı** | `[TEST MODE]` | Normal log |
| **Kullanım Senaryosu** | Demo, Test | Production |

---

## 🎯 Hackathon Demo İçin İpuçları

### Demo Akışı

1. **Açılış** (10 saniye)
   - "Bu bir testnet projesi" diye başlayın
   - TESTNET badge'i gösterin
   - Test Mode'un aktif olduğunu belirtin

2. **Test Mode Demo** (1 dakika)
   - "Cüzdan bağlamadan çalışıyor" deyin
   - 2-3 servisi hızlıca test edin
   - Terminal'deki `[TEST MODE]` mesajlarını gösterin

3. **Production Mode Demo** (1 dakika)
   - Toggle'ı kapatın
   - MetaMask bağlayın
   - Bir servis için gerçek transaction başlatın
   - "Gerçek blockchain'de çalışıyor" deyin

4. **Kapanış** (30 saniye)
   - "İki mod da çalışıyor" vurgusunu yapın
   - Test Mode'un demo için ideal olduğunu söyleyin

---

## 💡 Önemli Notlar

> [!TIP]
> **Hackathon için**: Test Mode'u açık bırakın. Jüri üyeleri cüzdan bağlamadan tüm özellikleri görebilir.

> [!IMPORTANT]
> **Production'da**: Test Mode'u kapatın ve gerçek MetaMask transaction'ları kullanın.

> [!WARNING]
> Test Mode'da "ödeme yapıldı" gibi görünse de, gerçekte hiçbir transaction blockchain'e gönderilmez.

---

## 🔧 Teknik Detaylar

### JavaScript Değişiklikleri

```javascript
let testMode = true; // Varsayılan olarak açık

// Test Mode Toggle Event
document.getElementById('testModeToggle').addEventListener('change', (e) => {
    testMode = e.target.checked;
    if (testMode) {
        addLog('INFO', 'Test Mode ENABLED');
    } else {
        addLog('WARNING', 'Test Mode DISABLED');
    }
});

// Service Function
async function useService(service, amount) {
    if (testMode) {
        // Cüzdan kontrolü YOK
        // MetaMask transaction YOK
        // Direkt API çağrısı
        await callServiceAPI(service);
        return;
    }
    
    // Production mode: Normal akış
    if (!userAddress) {
        alert('Please connect wallet!');
        return;
    }
    // ... MetaMask transaction
}
```

### CSS Değişiklikleri

- **TESTNET Badge**: Sarı, yanıp sönen
- **Toggle Switch**: Yeşil (ON) / Kırmızı (OFF)
- **Smooth Animations**: 0.4s transition

---

## 🚀 Hızlı Başlangıç

```bash
# 1. Sunucuyu başlat
cd C:\Users\hasan\.gemini\antigravity\scratch\monad-access
python app.py

# 2. Browser'ı aç
# http://localhost:5000

# 3. Test Mode açık olduğunu kontrol et (yeşil toggle)

# 4. Herhangi bir servisi test et (cüzdan gerekmez!)
```

---

## ❓ Sık Sorulan Sorular

**S: Test Mode'da gerçek para harcanır mı?**
A: Hayır! Test Mode'da hiçbir blockchain transaction yapılmaz.

**S: Servisler gerçekten çalışıyor mu?**
A: Evet! Backend API'ler çalışıyor, sadece ödeme adımı atlanıyor.

**S: Production mode'da ne değişiyor?**
A: MetaMask bağlantısı ve gerçek transaction gerekiyor.

**S: Toggle'ı değiştirince ne oluyor?**
A: Sayfa yenilenmeden mod değişiyor, terminal'de bilgi mesajı görünüyor.

---

## 📝 Özet

✅ **Test Mode eklendi** - Cüzdan gerekmeden test  
✅ **TESTNET badge eklendi** - Testnet olduğu belli  
✅ **Toggle switch eklendi** - Kolay mod değiştirme  
✅ **Terminal mesajları** - `[TEST MODE]` ile belirtiliyor  
✅ **Hackathon ready** - Demo için mükemmel  

**Artık projenizi kimse cüzdan bağlamadan test edebilir!** 🎉
