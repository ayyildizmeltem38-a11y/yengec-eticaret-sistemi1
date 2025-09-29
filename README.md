# 🛍️ Yengeç E-ticaret Yönetim Sistemi

XML tabanlı çoklu pazaryeri ürün yönetim sistemi

## 🚀 Özellikler
- XML kaynak yönetimi  
- Otomatik fiyatlandırma (×1.20 + 105 TL)
- 5 pazaryeri desteği
- API entegrasyonları

## 📥 Kurulum
```bash
git clone https://github.com/ayyildizmeltem38-a11y/yengec-eticaret-sistemi.git
cd yengec-eticaret-sistemi
cd frontend && npm install && npm start
cd ../backend && pip install -r requirements.txt
uvicorn server:app --host 0.0.0.0 --port 8001
