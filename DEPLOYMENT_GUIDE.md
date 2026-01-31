# Smart Contract Deployment Guide

## ✅ Tamamlananlar

1. **MonadAccess.sol Smart Contract** ✅
   - GPT-Pro servisi (0.005 MON)
   - Gemini AI servisi (0.003 MON)
   - Ödeme fonksiyonu
   - Admin withdraw fonksiyonu
   - Fiyat güncelleme

2. **Contract Compiled** ✅
   - Solidity 0.8.20
   - Hardhat ile başarıyla compile edildi
   - Artifacts oluşturuldu

3. **Hazırlıklar** ✅
   - Private key configured
   - .env dosyası oluşturuldu
   - .gitignore eklendi

---

## 🚀 Deployment Seçenekleri

### Seçenek 1: Remix IDE (En Kolay - Önerilen)

1. **Contract Kopyala:**
   - `contracts/MonadAccess.sol` dosyasını aç
   - Tüm kodu kopyala

2. **Remix'e Git:**
   - https://remix.ethereum.org aç
   - Yeni dosya oluştur: `MonadAccess.sol`
   - Kodu yapıştır

3. **Compile Et:**
   - Sol panelde "Solidity Compiler" tıkla
   - Compiler version: 0.8.20 seç
   - "Compile" butonuna tıkla

4. **Deploy Et:**
   - "Deploy & Run Transactions" tab'ına geç
   - Environment: "Injected Provider - MetaMask" seç
   - MetaMask'ta Monad Testnet'i seç
   - CONTRACT: "MonadAccess" seç
   - "Deploy" butonuna tıkla
   - MetaMask'ta confirm et

5. **Contract Address Kaydet:**
   - Deploy edilen contract address'i kopyala
   - `contract-address.txt` dosyasına kaydet

### Seçenek 2: Hardhat (Gelişmiş)

**Not:** Hardhat 3.x ile ethers plugin uyumsuzluğu var. Şu adımları dene:

```bash
# Hardhat 2.x'e downgrade
npm install --save-dev hardhat@2.22.0 @nomicfoundation/hardhat-toolbox@4.0.0

# Compile
npx hardhat compile

# Deploy
npx hardhat run scripts/deploy.js --network monadTestnet
```

### Seçenek 3: Manuel ethers.js Script

Contract'ı manuel olarak deploy etmek için:

```javascript
import { ethers } from "ethers";
import fs from "fs";

const PRIVATE_KEY = "0x5323fb9cb56c539cbab12814af29f866151ea870a1924bfc709c54b9c15649c0";
const RPC_URL = "https://testnet-rpc.monad.xyz/";

// Contract ABI ve bytecode'u artifacts'tan al
const artifact = JSON.parse(fs.readFileSync("artifacts/contracts/MonadAccess.sol/MonadAccess.json"));

const provider = new ethers.providers.JsonRpcProvider(RPC_URL);
const wallet = new ethers.Wallet(PRIVATE_KEY, provider);

const factory = new ethers.ContractFactory(artifact.abi, artifact.bytecode, wallet);
const contract = await factory.deploy();
await contract.deployed();

console.log("Contract deployed to:", contract.address);
```

---

## 📋 Frontend Entegrasyonu (Deploy Sonrası)

Contract deploy edildikten sonra:

1. **Contract Address Al:**
   - Deploy edilen contract address'i kaydet

2. **Contract ABI Al:**
   - `artifacts/contracts/MonadAccess.sol/MonadAccess.json` dosyasını aç
   - `abi` array'ini kopyala

3. **Frontend'e Ekle:**
   - `templates/index.html` aç
   - Contract address ve ABI ekle
   - Direct transfer yerine contract call yap

---

## 🔗 Yararlı Linkler

- **Monad Testnet Explorer:** https://testnet.monadexplorer.com/
- **Remix IDE:** https://remix.ethereum.org
- **Monad Docs:** https://docs.monad.xyz

---

## 💡 Sonraki  Adımlar

1. Contract'ı deploy et (Remix önerilen)
2. Contract address'i kaydet
3. Frontend entegrasyonu yap
4. Test ödemesi yap
5. Hackathon'da göster! 🎉
