# pg_camouflage

**pg_camouflage**, PostgreSQL için veri maskeleme ve anonimleştirme aracıdır. Hassas verileri (isim, e-posta, telefon vb.) gizleyerek geliştirme ve test ortamlarında güvenle kullanılmasını sağlar.

## Özellikler

* Sütun bazlı maskeleme
* Kolay CLI kullanımı
* Yeni maskeleme fonksiyonları eklenebilir
* Linux üzerinde çalışır, uzak PostgreSQL’e bağlanabilir

## Hızlı Başlangıç

### 1. Repo klonla ve sanal ortam oluştur

```bash
git clone https://github.com/Brksy0/pg_camouflage.git
cd pg_camouflage
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. PostgreSQL’de veritabanı ve kullanıcı oluştur

```sql
CREATE DATABASE camouflage_db;
CREATE USER test WITH PASSWORD 'Test123';
GRANT ALL PRIVILEGES ON DATABASE camouflage_db TO test;
```

### 3. Örnek tablo oluştur ve veri ekle

```sql
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  full_name TEXT,
  email TEXT,
  phone TEXT
);

INSERT INTO users (full_name, email, phone) VALUES
('John Doe', 'john.doe@example.com', '555-1234'),
('Jane Smith', 'jane.smith@example.com', '555-5678');
```

### 4. Örnek maskeleme fonksiyonları ekle

```sql
CREATE OR REPLACE FUNCTION mask_email(email TEXT) RETURNS TEXT AS $$
BEGIN
  RETURN regexp_replace(email, '(^.).+(@.+$)', '\1***\2');
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION mask_phone(phone TEXT) RETURNS TEXT AS $$
BEGIN
  RETURN '***-****';
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION mask_name(full_name TEXT) RETURNS TEXT AS $$
BEGIN
  RETURN left(full_name, 1) || '***';
END;
$$ LANGUAGE plpgsql;
```

### 5. CLI ile veriyi maskele

```bash
python3 scripts/run_masking.py --host localhost --db camouflage_db --user test --password Test123 --table users --columns "full_name:mask_name,email:mask_email,phone:mask_phone"
```

## Lisans

MIT Lisansı
