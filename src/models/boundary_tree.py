import pygame
import cairo
import io

class BoundaryTree:
    """Pohon boundary menggunakan desain dari bound_tree.py dengan rendering solid"""
    
    def __init__(self, x, y, tree_size=80, tree_style="default"):
        self.x = x
        self.y = y
        self.tree_size = tree_size
        self.sprite = self._create_tree_sprite()
        self.rect = self.sprite.get_rect(center=(x, y))
    
    def _create_tree_sprite(self):
        """Membuat sprite pohon menggunakan cairo dengan RGB surface untuk warna solid"""
        WIDTH = int(self.tree_size * 1.2)
        HEIGHT = int(self.tree_size * 1.6)
        
        # PENTING: Gunakan FORMAT_RGB24 bukan ARGB32
        surface = cairo.ImageSurface(cairo.FORMAT_RGB24, WIDTH, HEIGHT)
        context = cairo.Context(surface)
        
        # Isi background dengan warna hijau game (akan dijadikan transparan nanti)
        bg_color = (34, 139, 34)  # GREEN_BG dari config
        context.set_source_rgb(bg_color[0]/255, bg_color[1]/255, bg_color[2]/255)
        context.paint()
        
        # Warna coklat untuk batang (BGR format untuk cairo RGB24!)
        # Cairo RGB24 sebenarnya menyimpan dalam urutan BGR, bukan RGB
        dark_brown = (33/255, 67/255, 101/255)      # BGR: Coklat gelap
        medium_brown = (43/255, 90/255, 139/255)    # BGR: Coklat sedang  
        light_brown = (70/255, 110/255, 160/255)    # BGR: Coklat terang
        dark_brown_detail = (25/255, 50/255, 80/255)
        light_brown_detail = (80/255, 120/255, 180/255)
        
        # Warna hijau untuk daun (BGR format untuk cairo RGB24!)
        dark_green = (20/255, 70/255, 30/255)       # BGR: Hijau gelap
        medium_green = (40/255, 120/255, 70/255)    # BGR: Hijau sedang
        light_green = (70/255, 180/255, 120/255)    # BGR: Hijau terang
        
        # === GAMBAR BATANG ===
        context.save()
        
        # Batang utama
        context.set_source_rgb(*medium_brown)
        context.move_to(WIDTH * 0.45, HEIGHT * 0.9)
        context.curve_to(WIDTH * 0.4, HEIGHT * 0.7, WIDTH * 0.48, HEIGHT * 0.5, WIDTH * 0.5, HEIGHT * 0.45)
        context.curve_to(WIDTH * 0.52, HEIGHT * 0.5, WIDTH * 0.6, HEIGHT * 0.7, WIDTH * 0.55, HEIGHT * 0.9)
        context.close_path()
        context.fill()
        
        # Bayangan batang
        context.set_source_rgb(*dark_brown)
        context.move_to(WIDTH * 0.5, HEIGHT * 0.45)
        context.curve_to(WIDTH * 0.52, HEIGHT * 0.5, WIDTH * 0.6, HEIGHT * 0.7, WIDTH * 0.55, HEIGHT * 0.9)
        context.line_to(WIDTH * 0.49, HEIGHT * 0.9)
        context.curve_to(WIDTH * 0.58, HEIGHT * 0.7, WIDTH * 0.5, HEIGHT * 0.5, WIDTH * 0.49, HEIGHT * 0.46)
        context.close_path()
        context.fill()
        
        # Highlight batang
        context.set_source_rgb(*light_brown)
        context.move_to(WIDTH * 0.45, HEIGHT * 0.9)
        context.curve_to(WIDTH * 0.42, HEIGHT * 0.8, WIDTH * 0.45, HEIGHT * 0.6, WIDTH * 0.48, HEIGHT * 0.48)
        context.line_to(WIDTH * 0.49, HEIGHT * 0.5)
        context.curve_to(WIDTH * 0.47, HEIGHT * 0.6, WIDTH * 0.44, HEIGHT * 0.8, WIDTH * 0.47, HEIGHT * 0.9)
        context.close_path()
        context.fill()
        
        context.restore()
        
        # === DETAIL BATANG ===
        context.save()
        
        # Retakan kayu
        context.set_source_rgb(*dark_brown_detail)
        context.set_line_width(2)
        context.move_to(WIDTH * 0.51, HEIGHT * 0.55)
        context.line_to(WIDTH * 0.53, HEIGHT * 0.65)
        context.line_to(WIDTH * 0.52, HEIGHT * 0.75)
        context.stroke()
        
        context.move_to(WIDTH * 0.47, HEIGHT * 0.6)
        context.line_to(WIDTH * 0.46, HEIGHT * 0.7)
        context.stroke()
        
        # Serat kayu
        context.set_source_rgb(*light_brown_detail)
        context.set_line_width(1.5)
        context.move_to(WIDTH * 0.48, HEIGHT * 0.5)
        context.line_to(WIDTH * 0.46, HEIGHT * 0.6)
        context.stroke()
        
        context.move_to(WIDTH * 0.50, HEIGHT * 0.68)
        context.line_to(WIDTH * 0.49, HEIGHT * 0.78)
        context.stroke()
        
        # Garis lengkung di ujung atas batang
        context.set_source_rgb(*light_brown)
        context.move_to(WIDTH * 0.49, HEIGHT * 0.45)
        context.curve_to(WIDTH * 0.495, HEIGHT * 0.448, WIDTH * 0.505, HEIGHT * 0.448, WIDTH * 0.51, HEIGHT * 0.45)
        context.set_line_width(1)
        context.stroke()
        
        context.restore()
        
        # === GAMBAR DAUN ===
        context.save()
        
        # Daun kiri atas - didekatkan ke batang
        context.set_source_rgb(*medium_green)
        context.move_to(WIDTH * 0.35, HEIGHT * 0.38)
        context.curve_to(WIDTH * 0.25, HEIGHT * 0.25, WIDTH * 0.4, HEIGHT * 0.2, WIDTH * 0.5, HEIGHT * 0.25)
        context.curve_to(WIDTH * 0.58, HEIGHT * 0.28, WIDTH * 0.45, HEIGHT * 0.42, WIDTH * 0.35, HEIGHT * 0.38)
        context.fill()
        
        # Daun kanan atas - didekatkan ke batang
        context.set_source_rgb(*medium_green)
        context.move_to(WIDTH * 0.5, HEIGHT * 0.25)
        context.curve_to(WIDTH * 0.6, HEIGHT * 0.2, WIDTH * 0.75, HEIGHT * 0.28, WIDTH * 0.65, HEIGHT * 0.42)
        context.curve_to(WIDTH * 0.58, HEIGHT * 0.45, WIDTH * 0.55, HEIGHT * 0.32, WIDTH * 0.5, HEIGHT * 0.25)
        context.fill()
        
        # Daun kiri tengah - didekatkan ke batang
        context.set_source_rgb(*medium_green)
        context.move_to(WIDTH * 0.3, HEIGHT * 0.48)
        context.curve_to(WIDTH * 0.2, HEIGHT * 0.4, WIDTH * 0.35, HEIGHT * 0.35, WIDTH * 0.45, HEIGHT * 0.42)
        context.curve_to(WIDTH * 0.42, HEIGHT * 0.52, WIDTH * 0.35, HEIGHT * 0.52, WIDTH * 0.3, HEIGHT * 0.48)
        context.fill()
        
        # Daun kanan tengah - didekatkan ke batang
        context.set_source_rgb(*medium_green)
        context.move_to(WIDTH * 0.7, HEIGHT * 0.48)
        context.curve_to(WIDTH * 0.8, HEIGHT * 0.4, WIDTH * 0.65, HEIGHT * 0.35, WIDTH * 0.55, HEIGHT * 0.42)
        context.curve_to(WIDTH * 0.58, HEIGHT * 0.52, WIDTH * 0.65, HEIGHT * 0.52, WIDTH * 0.7, HEIGHT * 0.48)
        context.fill()
        
        # Daun bawah kiri - didekatkan ke batang
        context.set_source_rgb(*dark_green)
        context.move_to(WIDTH * 0.25, HEIGHT * 0.52)
        context.curve_to(WIDTH * 0.15, HEIGHT * 0.48, WIDTH * 0.3, HEIGHT * 0.43, WIDTH * 0.38, HEIGHT * 0.5)
        context.curve_to(WIDTH * 0.35, HEIGHT * 0.56, WIDTH * 0.3, HEIGHT * 0.56, WIDTH * 0.25, HEIGHT * 0.52)
        context.fill()
        
        # Daun bawah kanan - didekatkan ke batang
        context.set_source_rgb(*dark_green)
        context.move_to(WIDTH * 0.75, HEIGHT * 0.52)
        context.curve_to(WIDTH * 0.85, HEIGHT * 0.48, WIDTH * 0.7, HEIGHT * 0.43, WIDTH * 0.62, HEIGHT * 0.5)
        context.curve_to(WIDTH * 0.65, HEIGHT * 0.56, WIDTH * 0.7, HEIGHT * 0.56, WIDTH * 0.75, HEIGHT * 0.52)
        context.fill()
        
        # Highlight daun (daun terang di tengah atas) - didekatkan ke batang
        context.set_source_rgb(*light_green)
        context.move_to(WIDTH * 0.45, HEIGHT * 0.3)
        context.curve_to(WIDTH * 0.42, HEIGHT * 0.26, WIDTH * 0.5, HEIGHT * 0.24, WIDTH * 0.55, HEIGHT * 0.3)
        context.curve_to(WIDTH * 0.52, HEIGHT * 0.36, WIDTH * 0.48, HEIGHT * 0.36, WIDTH * 0.45, HEIGHT * 0.3)
        context.fill()
        
        context.restore()
        
        # Convert cairo RGB surface ke pygame surface dengan handling stride yang benar
        # Cairo RGB24 menggunakan 32-bit per pixel dengan padding
        buf = surface.get_data()
        
        # Buat pygame surface dari buffer dengan format BGRX (cairo RGB24 format)
        img = pygame.image.frombuffer(buf, (WIDTH, HEIGHT), 'RGBX')
        
        # Convert ke RGB biasa dan set colorkey
        img = img.convert()
        img.set_colorkey(bg_color)
        
        return img
    
    def draw(self, surface, camera):
        """Gambar pohon ke surface dengan offset kamera"""
        screen_x = self.x - camera.x
        screen_y = self.y - camera.y
        screen_rect = self.sprite.get_rect(center=(screen_x, screen_y))
        surface.blit(self.sprite, screen_rect)


def create_boundary_trees(map_width, map_height, spacing=80, margin=50):
    """
    Membuat pohon-pohon di sekeliling boundary peta
    
    Args:
        map_width: lebar peta
        map_height: tinggi peta
        spacing: jarak antar pohon
        margin: jarak dari tepi peta
        
    Returns:
        List of BoundaryTree objects
    """
    trees = []
    
    # Pohon di sisi atas
    x = margin
    while x < map_width - margin:
        size = 60 + (hash(f"{x}_top") % 40)  # Variasi ukuran 60-100
        trees.append(BoundaryTree(x, margin, tree_size=size))
        x += spacing
    
    # Pohon di sisi bawah
    x = margin
    while x < map_width - margin:
        size = 60 + (hash(f"{x}_bottom") % 40)
        trees.append(BoundaryTree(x, map_height - margin, tree_size=size))
        x += spacing
    
    # Pohon di sisi kiri (lebih renggang)
    y = margin + spacing
    while y < map_height - margin - spacing:
        size = 60 + (hash(f"{y}_left") % 40)
        trees.append(BoundaryTree(margin, y, tree_size=size))
        y += spacing * 1.8  # Lebih renggang untuk sisi kiri
    
    # Pohon di sisi kanan (lebih renggang)
    y = margin + spacing
    while y < map_height - margin - spacing:
        size = 60 + (hash(f"{y}_right") % 40)
        trees.append(BoundaryTree(map_width - margin, y, tree_size=size))
        y += spacing * 1.8  # Lebih renggang untuk sisi kanan
    
    return trees
