# 🚀 Remix ile Deploy - Kolay Yol!

## Adım 1: Remix'i Aç
Yeni tab aç: **https://remix.ethereum.org**

## Adım 2: Yeni Dosya Oluştur
1. Sol tarafta "contracts" klasörüne sağ tıkla
2. "New File" seç
3. İsim: `MonadAccess.sol`

## Adım 3: Contract Kodunu Kopyala
`contracts/MonadAccess.sol` dosyasını aç, **TÜM KODU** kopyala (Ctrl+A, Ctrl+C)
Remix'teki `MonadAccess.sol` dosyasına yapıştır (Ctrl+V)

## Adım 4: Compile Et
1. Sol panelde **🔨 Solidity Compiler** ikonuna tıkla
2. Compiler version: **0.8.20** seç
3. Mavi **Compile MonadAccess.sol** butonuna tıkla
4. ✅ Yeşil tik görmeli

## Adım 5: Deploy Et

### 5a. MetaMask Hazırla
- MetaMask'ı aç
- **Monad Testnet**'e geç
- Cüzdanında MON var mı kontrol et (deployment için gas gerekli)

### 5b. Remix'te Deploy
1. Sol panelde **📦 Deploy & Run Transactions** ikonuna tıkla
2. **Environment**: `Injected Provider - MetaMask` seç
3. MetaMask popup açılacak → **Connect** tıkla
4. **CONTRACT**: `MonadAccess` seçili olmalı
5. **🟠 Deploy** butonuna tıkla
6. MetaMask popup → **Confirm** tıkla
7. ⏳ Birkaç saniye bekle...
8. ✅ "Deployed Contracts" altında göreceksin!

## Adım 6: Contract Address'i Kaydet

Deploy edildikten sonra:
1. "Deployed Contracts" altında contract'ı gör
2. Contract address'in yanındaki **📋 copy** ikonuna tıkla
3. Address'i not et (ör: `0x1234...5678`)

---

## 🎉 Başardın!

Contract başarıyla Monad Testnet'te!

**Contract Address'i bana ver,** frontend entegrasyonunu yapayım! 🚀

---

## 🔍 Contract'ı Kontrol Et

Monad Explorer'da kontrol et:
```
https://testnet.monadexplorer.com/address/SENIN_CONTRACT_ADDRESS
```

---

## ⚠️ Sorun Yaşarsan

- **MetaMask açılmıyor?** → Environment'i tekrar seç
- **Gas yok?** → Monad faucet'ten token al
- **Compile hatası?** → Version 0.8.20 olduğundan emin ol
