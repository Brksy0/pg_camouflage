# pg_camouflage

**pg_camouflage**, PostgreSQL için veri maskeleme ve anonimleştirme aracıdır.  
Hassas verileri (isim, e-posta, telefon vb.) gizleyerek geliştirme ve test ortamlarında güvenle kullanılmasını sağlar.

---

## Özellikler

- Sütun bazlı maskeleme
- CLI ile kolay kullanım
- Yeni maskeleme fonksiyonları eklenebilir
- Linux üzerinde çalışır, uzak PostgreSQL’e bağlanabilir

---

## Hızlı Başlangıç

1. Repo klonla ve virtual environment oluştur:
```bash
git clone https://github.com/<kullanici-adiniz>/pg_camouflage.git
cd pg_camouflage
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
