# 🚀 Monad Access - Blockchain Integration Guide

## ✅ Yapılan Değişiklikler

### 1. Admin Cüzdan Adresi Güncellendi
```javascript
const ADMIN_ADDRESS = '0x864EdC950468f3d1e1F103fd13DaD7D79dcD8b0C';
```
Tüm ödemeler bu adrese gidecek.

### 2. Test Mode Davranışı İyileştirildi
- **Test Mode AÇIK:** Servisleri ödeme yapmadan kullanabilirsin
- **Test Mode KAPALI:** Her servis kullanımında gerçek MON ödemesi yapılır

### 3. Cüzdan Bağlantısı
- MetaMask bağlantısı her zaman aktif
- Bağlantı başarılı olunca cüzdan adresi görünür
- "Connected" durumu gösterilir

### 4. Blockchain Ödemeleri
- Gerçek Monad Testnet transaction'ları
- Transaction hash gösteriliyor
- Monad Explorer linki veriliyor
- Blockchain confirmation bekleniyor

---

## 🎮 Nasıl Kullanılır?

### Adım 1: MetaMask Kurulumu
1. [MetaMask](https://metamask.io/) uzantısını tarayıcına kur
2. Cüzdan oluştur veya import et

### Adım 2: Monad Testnet Ekleme
Uygulama otomatik olarak Monad Testnet'i ekleyecek, ama manuel eklemek istersen:

```
Network Name: Monad Testnet
RPC URL: https://testnet-rpc.monad.xyz/
Chain ID: 10143 (0x279f)
Currency Symbol: MON
Block Explorer: https://testnet.monadexplorer.com/
```

### Adım 3: Test Token Alma
Monad Testnet tokenları almak için:
- Monad Discord'una katıl
- Faucet kanalından token iste
- Veya Monad ekibinden test tokenları talep et

### Adım 4: Uygulamayı Kullan

#### Test Mode ile (Ücretsiz)
1. Test Mode toggle'ını AÇIK bırak
2. Servisleri kullan - ödeme yapılmaz
3. Sadece API'leri test et

#### Gerçek Blockchain ile
1. "Connect Wallet" butonuna tıkla
2. MetaMask'ta onay ver
3. Monad Testnet'e geç (otomatik)
4. Test Mode'u KAPAT
5. Servis kullan:
   - MetaMask açılır
   - Ödeme miktarını gösterir
   - Onayla
   - Transaction blockchain'e gönderilir
   - Confirmation bekle
   - Servis çalışır!

---

## 💰 Ödeme Akışı

### Test Mode KAPALI:
```
1. Servis butonuna tıkla
2. MetaMask açılır (örn: 0.005 MON)
3. Transaction'ı onayla
4. Blockchain'e gönderilir
5. Admin cüzdanına para gider: 0x864EdC950468f3d1e1F103fd13DaD7D79dcD8b0C
6. Confirmation bekle (birkaç saniye)
7. Servis çalışır ve sonuç gösterilir
```

### Servis Fiyatları:
- 🤖 GPT-Pro: **0.005 MON**
- 🧠 Gemini AI: **0.003 MON**
- 🔒 Nano VPN: **0.002 MON/min**
- 🎨 Imagine: **0.05 MON**
- 📱 Ghost SMS: **0.01 MON**

---

## 🔍 Transaction Takibi

Her ödeme sonrası terminal panelinde:
```
✅ Transaction confirmed on Monad Testnet!
💰 0.005 MON sent to admin wallet
View on Explorer: https://testnet.monadexplorer.com/tx/0x...
```

Explorer linkine tıklayarak:
- Transaction detaylarını görebilirsin
- Gönderen/alıcı adresleri
- Miktar
- Gas fee
- Block numarası

---

## 🐛 Sorun Giderme

### "Please connect your wallet first!"
- MetaMask yüklü mü kontrol et
- "Connect Wallet" butonuna tıkla
- MetaMask'ta onay ver

### "Insufficient funds"
- Cüzdanında yeterli MON var mı kontrol et
- Monad faucet'ten token al

### "Transaction rejected by user"
- MetaMask'ta "Reject" yerine "Confirm" tıkla

### "Wrong network"
- Uygulama otomatik olarak Monad Testnet'e geçecek
- Manuel geçiş: MetaMask → Networks → Monad Testnet

### MetaMask açılmıyor
- Test Mode'u KAPAT
- Sayfayı yenile
- Tekrar dene

---

## 🔮 Sonraki Adımlar

### Smart Contract Geliştirme
1. Solidity ile payment contract yaz
2. Monad Testnet'e deploy et
3. Contract ile entegrasyon
4. Otomatik refund mekanizması
5. Subscription modeli

### API Entegrasyonları
- OpenAI GPT-4 gerçek entegrasyonu
- Google Gemini API
- VPN provider entegrasyonu
- SMS provider entegrasyonu
- Image generation API

### Özellikler
- Transaction history
- User dashboard
- Referral system
- Bulk credit packages
- Multi-token support (USDC, ETH)

---

## 📞 Destek

Sorun yaşarsan:
1. Terminal panelini kontrol et (hata mesajları)
2. Browser console'u aç (F12)
3. MetaMask'ı kontrol et
4. Monad Testnet'te olduğundan emin ol

**Admin Wallet:** `0x864EdC950468f3d1e1F103fd13DaD7D79dcD8b0C`

---

**Built with 💜 for Monad Testnet**
