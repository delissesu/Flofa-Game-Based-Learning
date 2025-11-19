<p align="center">
  <h1 align="center">🌿 FLOFA 🌿</h1>
  <p align="center"><i>Game Eksplorasi Alam</i></p>
</p>

<p align="center">
<a href="#"><img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="Python Version"></a>
<a href="#"><img src="https://img.shields.io/badge/pygame-2.0+-green.svg" alt="Pygame"></a>
<a href="#"><img src="https://img.shields.io/badge/license-MIT-brightgreen.svg" alt="License"></a>
</p>

## Tentang Flofa

Flofa adalah game eksplorasi 2D yang dibangun dengan Pygame dan PyCairo, menampilkan arsitektur MVC (Model-View-Controller) yang bersih. Game ini menyediakan pengalaman eksplorasi alam yang imersif di mana pemain dapat:

- **Menjelajahi** dunia terbuka yang luas dengan rendering rumput dinamis
- **Berinteraksi** dengan pohon dan hewan untuk belajar tentang alam
- **Bernavigasi** dengan mulus menggunakan kontrol WASD/Arrow keys
- **Menemukan** informasi melalui interaksi berbasis kedekatan

Flofa mendemonstrasikan pola arsitektur perangkat lunak profesional sambil mempertahankan mekanik gameplay yang menarik.

## Belajar Flofa

Codebase Flofa mengikuti arsitektur MVC standar industri, menjadikannya sumber belajar yang sangat baik untuk:

- **Pengembangan Game** - Dibangun dengan Pygame, memanfaatkan sprite rendering dan sistem kamera
- **Design Patterns** - Pemisahan yang jelas antara concerns dengan struktur MVC
- **Vector Graphics** - Generasi sprite dinamis menggunakan PyCairo
- **Python Best Practices** - Organisasi kode modular dan import yang tepat

Dokumentasi lengkap tersedia di [ARCHITECTURE.md](ARCHITECTURE.md), menjelaskan detail dependency graph dan alur data.

## Instalasi

Flofa membutuhkan Python 3.8+ dan dependencies berikut:

```bash
# Clone repository
git clone https://github.com/ariear/flofa.git
cd flofa

# Buat virtual environment
python -m venv venv

# Aktifkan virtual environment
# Di Windows:
venv\Scripts\activate
# Di macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install pygame pycairo
```

## Menjalankan Game

Setelah dependencies terinstall, jalankan game dengan:

```bash
python main.py
```

## Struktur Proyek

```
flofa/
├── main.py                      # Entry point aplikasi
├── src/
│   ├── config.py               # Konstanta global dan konfigurasi
│   ├── models/                 # Entitas game (Player, Tree, Animal, Grass)
│   ├── views/                  # Layer rendering (GameView, InfoPopup)
│   ├── controllers/            # Business logic (GameController)
│   └── utils/                  # Fungsi helper
├── ARCHITECTURE.md             # Dokumentasi arsitektur detail
└── README.md                   # File ini
```

## Kontrol

| Tombol | Aksi |
|--------|------|
| <kbd>W</kbd> / <kbd>↑</kbd> | Gerak Atas |
| <kbd>A</kbd> / <kbd>←</kbd> | Gerak Kiri |
| <kbd>S</kbd> / <kbd>↓</kbd> | Gerak Bawah |
| <kbd>D</kbd> / <kbd>→</kbd> | Gerak Kanan |
| <kbd>ESC</kbd> | Tutup Popup Informasi |

Berjalan mendekati pohon atau hewan untuk melihat informasi tentang mereka.

## Arsitektur

Flofa mengimplementasikan pola **Model-View-Controller (MVC)**:

### Models
Mengelola entitas game dan perilakunya:
- `Player` - Pergerakan karakter dan rendering sprite
- `Tree` - Pohon Oak dan Pinus dengan sprite dari PyCairo
- `Animal` - Kelinci, rusa, dan burung dengan rendering unik
- `Grass` - Rumput bergoyang dinamis dengan generasi prosedural

### Views
Menangani semua rendering dan presentasi:
- `GameView` - Rendering game utama dengan depth sorting
- `InfoPopup` - Tampilan informasi modal dengan word wrapping

### Controllers
Mengorkestrasi logika game dan input user:
- `GameController` - Handling input, kontrol kamera, dan deteksi interaksi

### Utils
Fungsi helper yang dapat digunakan kembali:
- `calculate_distance` - Kalkulasi jarak Euclidean untuk deteksi kedekatan

Lihat [ARCHITECTURE.md](ARCHITECTURE.md) untuk pemetaan dependency yang detail.

## Fitur

- **Generasi Sprite Prosedural** - Semua sprite dihasilkan menggunakan PyCairo untuk skalabilitas
- **Sistem Kamera Dinamis** - Kamera mengikuti pemain dengan smooth dan ada batasan
- **Depth Sorting** - Layering sprite yang tepat berdasarkan posisi Y
- **Rendering Teroptimasi** - Culling untuk gumpalan rumput di luar layar
- **Arsitektur Modular** - Pemisahan concerns yang jelas mengikuti MVC
- **Desain Extensible** - Mudah menambahkan entitas dan perilaku baru

## Konfigurasi

Semua konstanta game terpusat di `src/config.py`:

```python
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
FPS = 60
PLAYER_SPEED = 3
INTERACTION_DISTANCE = 70
```

Modifikasi nilai-nilai ini untuk menyesuaikan perilaku game tanpa menyentuh logika inti.

## Kontribusi

Kontribusi sangat diterima! Silakan kirim Pull Request.

1. Fork repository ini
2. Buat feature branch (`git checkout -b feature/FiturKeren`)
3. Commit perubahan (`git commit -m 'Tambah fitur keren'`)
4. Push ke branch (`git push origin feature/FiturKeren`)
5. Buka Pull Request

## Lisensi

Game Flofa adalah perangkat lunak open-source yang dilisensikan di bawah [lisensi MIT](https://opensource.org/licenses/MIT).

## Kredit

- **Developer**: [ariear](https://github.com/ariear)
- **Framework**: [Pygame](https://www.pygame.org/)
- **Graphics**: [PyCairo](https://pycairo.readthedocs.io/)
