# Balanced Brackets Checker

## Deskripsi

Program ini memeriksa apakah sebuah string tanda kurung (brackets) seimbang. String tanda kurung dianggap **seimbang** jika:

- Setiap tanda kurung buka memiliki pasangan tutup dari jenis yang sama.
- Tanda kurung tutup muncul dalam urutan yang benar (nested properly).

Tanda kurung yang didukung meliputi:

- `()`
- `[]`
- `{}`

## Cara Kerja Program

1. **Input**: Pengguna memasukkan string tanda kurung.
   - Spasi dalam input akan diabaikan.
2. **Proses**: Program memeriksa setiap karakter dalam string menggunakan struktur data **stack**.
   - Jika karakter adalah tanda kurung buka (`(`, `{`, `[`), maka ditambahkan ke stack.
   - Jika karakter adalah tanda kurung tutup (`)`, `}`, `]`), maka:
     - Program memeriksa apakah stack kosong. Jika kosong, string **tidak seimbang**.
     - Jika tidak kosong, program memeriksa apakah tanda kurung tutup tersebut cocok dengan tanda kurung buka di atas stack.
     - Jika cocok, tanda kurung buka dihapus dari stack.
3. **Output**:
   - Jika setelah memproses semua karakter stack kosong, maka string **seimbang** (`YES`).
   - Jika tidak, maka string **tidak seimbang** (`NO`).

## Kompleksitas

### Waktu

- Operasi iterasi untuk memproses setiap karakter dalam string memiliki kompleksitas **O(n)**, dengan `n` adalah panjang string.
- Operasi push dan pop pada stack masing-masing memiliki kompleksitas **O(1)**.
- Secara keseluruhan, kompleksitas waktu program adalah **O(n)**.

### Ruang

- Kompleksitas ruang bergantung pada ukuran stack, yang dalam kasus terburuk dapat mencapai **O(n)**, jika semua karakter dalam string adalah tanda kurung buka.

## Contoh Penggunaan

### Input:

```
Masukkan string tanda kurung: { [ ( ) ] }
```

### Output:

```
YES
```

### Input:

```
Masukkan string tanda kurung: { [ ( ] ) }
```

### Output:

```
NO
```

## Penjelasan Kode

### Penjelasan Detail

1. **Stack untuk Pelacakan**
   - Stack digunakan untuk menyimpan tanda kurung buka yang belum dipasangkan.
2. **Mapping Bracket**
   - Dictionary `matching_bracket` digunakan untuk mencocokkan tanda kurung tutup dengan tanda kurung buka yang sesuai.
3. **Logika Pengecekan**
   - Jika tanda kurung tutup tidak sesuai dengan tanda kurung buka di atas stack, string tidak seimbang.
   - Jika semua tanda kurung sudah dipasangkan, maka stack akan kosong.

## Cara Menjalankan Program

1. Jalankan script Python menggunakan interpreter Python:
   ```bash
   python balanced_brackets.py
   ```
2. Masukkan string tanda kurung sesuai prompt.
3. Program akan mengembalikan output `YES` atau `NO` berdasarkan keseimbangan tanda kurung.

## Catatan

- Program hanya mendukung tanda kurung `()`, `[]`, dan `{}`.
- Program mengabaikan karakter selain tanda kurung, seperti spasi.
