import pygame
import sys
import math
import cairo

# Inisialisasi Pygame
pygame.init()

# Konstanta
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
FPS = 60
PLAYER_SPEED = 3
INTERACTION_DISTANCE = 70  # Jarak untuk memunculkan popup

# Warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (34, 139, 34)
DARK_GREEN = (0, 100, 0)
BROWN = (101, 67, 33)
LIGHT_BLUE = (173, 216, 230)
GRAY = (200, 200, 200)
YELLOW = (255, 255, 0)

# Setup display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game Eksplorasi Alam")
clock = pygame.time.Clock()

# Font
pygame.font.init()
font_title = pygame.font.Font(None, 32)
font_text = pygame.font.Font(None, 24)
font_small = pygame.font.Font(None, 20)

# Fungsi untuk membuat sprite karakter menggunakan PyCairo
def create_player_sprite(size=40):
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, size, size)
    ctx = cairo.Context(surface)
    
    # Background transparan
    ctx.set_source_rgba(0, 0, 0, 0)
    ctx.paint()
    
    # Gambar kepala (lingkaran)
    ctx.set_source_rgb(0.95, 0.8, 0.7)  # Warna kulit
    ctx.arc(size/2, size/3, size/6, 0, 2 * math.pi)
    ctx.fill()
    
    # Gambar badan (rectangle dengan rounded corners)
    ctx.set_source_rgb(0.2, 0.4, 0.8)  # Baju biru
    ctx.rectangle(size/2 - size/8, size/3 + size/8, size/4, size/3)
    ctx.fill()
    
    # Gambar kaki
    ctx.set_source_rgb(0.3, 0.2, 0.1)  # Celana coklat
    ctx.rectangle(size/2 - size/10, size/3 + size/2.3, size/12, size/6)
    ctx.fill()
    ctx.rectangle(size/2 + size/30, size/3 + size/2.3, size/12, size/6)
    ctx.fill()
    
    # Convert Cairo surface ke Pygame surface
    buf = surface.get_data()
    pygame_surface = pygame.image.frombuffer(buf, (size, size), 'ARGB')
    
    return pygame_surface

# Fungsi untuk membuat sprite pohon menggunakan PyCairo
def create_tree_sprite(size=60, tree_type="oak"):
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, size, size)
    ctx = cairo.Context(surface)
    
    ctx.set_source_rgba(0, 0, 0, 0)
    ctx.paint()
    
    if tree_type == "oak":
        # Batang pohon
        ctx.set_source_rgb(0.4, 0.26, 0.13)
        ctx.rectangle(size/2 - size/12, size/2, size/6, size/2.5)
        ctx.fill()
        
        # Daun (lingkaran besar)
        ctx.set_source_rgb(0.13, 0.55, 0.13)
        ctx.arc(size/2, size/2.5, size/3, 0, 2 * math.pi)
        ctx.fill()
        
    elif tree_type == "pine":
        # Batang
        ctx.set_source_rgb(0.4, 0.26, 0.13)
        ctx.rectangle(size/2 - size/15, size/1.8, size/7.5, size/2.2)
        ctx.fill()
        
        # Daun segitiga (pine tree)
        ctx.set_source_rgb(0.0, 0.4, 0.0)
        ctx.move_to(size/2, size/6)
        ctx.line_to(size/4, size/2)
        ctx.line_to(size*3/4, size/2)
        ctx.close_path()
        ctx.fill()
        
        ctx.move_to(size/2, size/3)
        ctx.line_to(size/5, size/1.5)
        ctx.line_to(size*4/5, size/1.5)
        ctx.close_path()
        ctx.fill()
    
    buf = surface.get_data()
    pygame_surface = pygame.image.frombuffer(buf, (size, size), 'ARGB')
    
    return pygame_surface

# Fungsi untuk menghitung jarak antara dua objek
def calculate_distance(obj1_rect, obj2_rect):
    x1 = obj1_rect.centerx
    y1 = obj1_rect.centery
    x2 = obj2_rect.centerx
    y2 = obj2_rect.centery
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Class untuk Player
class Player:
    def __init__(self, x, y):
        self.sprite = create_player_sprite()
        self.rect = self.sprite.get_rect(center=(x, y))
        self.speed = PLAYER_SPEED
    
    def move(self, dx, dy):
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed
        
        # Batasi movement dalam screen
        self.rect.x = max(0, min(self.rect.x, SCREEN_WIDTH - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, SCREEN_HEIGHT - self.rect.height))
    
    def draw(self, surface):
        surface.blit(self.sprite, self.rect)

# Class untuk Tree
class Tree:
    def __init__(self, x, y, tree_type, name, desc):
        self.sprite = create_tree_sprite(tree_type=tree_type)
        self.rect = self.sprite.get_rect(center=(x, y))
        self.name = name
        self.description = desc
        self.type = "tree"
        self.highlight = False
    
    def draw(self, surface):
        # Gambar highlight circle jika dekat
        if self.highlight:
            pygame.draw.circle(surface, YELLOW, self.rect.center, 35, 3)
        surface.blit(self.sprite, self.rect)
    
    def get_info(self):
        return {"name": self.name, "description": self.description}

# Class untuk Animal (menggunakan Pygame drawing)
class Animal:
    def __init__(self, x, y, animal_type, name, desc, color):
        self.rect = pygame.Rect(x, y, 40, 40)
        self.animal_type = animal_type
        self.name = name
        self.description = desc
        self.color = color
        self.type = "animal"
        self.highlight = False
    
    def draw(self, surface):
        # Gambar highlight circle jika dekat
        if self.highlight:
            pygame.draw.circle(surface, YELLOW, self.rect.center, 30, 3)
            
        if self.animal_type == "rabbit":
            # Badan
            pygame.draw.ellipse(surface, self.color, (self.rect.x, self.rect.y + 10, 35, 25))
            # Kepala
            pygame.draw.circle(surface, self.color, (self.rect.x + 27, self.rect.y + 12), 10)
            # Telinga
            pygame.draw.ellipse(surface, self.color, (self.rect.x + 22, self.rect.y, 6, 15))
            pygame.draw.ellipse(surface, self.color, (self.rect.x + 30, self.rect.y, 6, 15))
            
        elif self.animal_type == "deer":
            # Badan
            pygame.draw.ellipse(surface, self.color, (self.rect.x, self.rect.y + 10, 40, 25))
            # Kepala
            pygame.draw.circle(surface, self.color, (self.rect.x + 35, self.rect.y + 8), 8)
            # Tanduk
            pygame.draw.line(surface, BROWN, (self.rect.x + 35, self.rect.y + 8), 
                           (self.rect.x + 32, self.rect.y), 2)
            pygame.draw.line(surface, BROWN, (self.rect.x + 35, self.rect.y + 8), 
                           (self.rect.x + 38, self.rect.y), 2)
            
        elif self.animal_type == "bird":
            # Badan
            pygame.draw.ellipse(surface, self.color, (self.rect.x + 10, self.rect.y + 15, 20, 15))
            # Kepala
            pygame.draw.circle(surface, self.color, (self.rect.x + 25, self.rect.y + 18), 7)
            # Sayap
            pygame.draw.polygon(surface, self.color, [
                (self.rect.x + 10, self.rect.y + 20),
                (self.rect.x, self.rect.y + 15),
                (self.rect.x + 5, self.rect.y + 25)
            ])
    
    def get_info(self):
        return {"name": self.name, "description": self.description}

# Class untuk Info Popup
class InfoPopup:
    def __init__(self, name, description):
        self.active = True
        self.name = name
        self.description = description
        self.width = 400
        self.height = 250
        self.x = (SCREEN_WIDTH - self.width) // 2
        self.y = (SCREEN_HEIGHT - self.height) // 2
    
    def draw(self, surface):
        # Background semi-transparent
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 128))
        surface.blit(overlay, (0, 0))
        
        # Popup box
        pygame.draw.rect(surface, WHITE, (self.x, self.y, self.width, self.height), border_radius=10)
        pygame.draw.rect(surface, BLACK, (self.x, self.y, self.width, self.height), 3, border_radius=10)
        
        # Title
        title_surf = font_title.render(self.name, True, BLACK)
        surface.blit(title_surf, (self.x + 20, self.y + 20))
        
        # Info text
        info_text = font_small.render("(Tekan ESC atau berjalan menjauh untuk menutup)", True, GRAY)
        surface.blit(info_text, (self.x + 20, self.y + 55))
        
        # Description (word wrap)
        words = self.description.split()
        lines = []
        current_line = ""
        
        for word in words:
            test_line = current_line + word + " "
            if font_text.size(test_line)[0] < self.width - 40:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word + " "
        lines.append(current_line)
        
        y_offset = self.y + 90
        for line in lines:
            text_surf = font_text.render(line, True, BLACK)
            surface.blit(text_surf, (self.x + 20, y_offset))
            y_offset += 30

# Inisialisasi game objects
player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

# Buat trees
trees = [
    Tree(150, 150, "oak", "Pohon Oak", "Pohon oak adalah pohon besar yang kokoh dengan daun lebar. Kayunya sering digunakan untuk furniture dan konstruksi. Pohon ini dapat hidup hingga ratusan tahun."),
    Tree(700, 200, "pine", "Pohon Pinus", "Pohon pinus memiliki daun berbentuk jarum dan menghasilkan kerucut. Mereka tumbuh subur di iklim dingin dan sering digunakan sebagai pohon Natal."),
    Tree(400, 500, "oak", "Pohon Maple", "Pohon maple terkenal dengan daun berwarna cerah di musim gugur. Getahnya dapat diolah menjadi sirup maple yang manis dan lezat."),
    Tree(800, 550, "pine", "Pohon Cemara", "Pohon cemara adalah pohon hijau abadi yang tetap hijau sepanjang tahun. Mereka memiliki aroma khas dan sering ditanam sebagai tanaman hias."),
]

# Buat animals
animals = [
    Animal(300, 300, "rabbit", "Kelinci", "Kelinci adalah hewan herbivora yang lincah dengan telinga panjang. Mereka hidup dalam liang dan aktif pada pagi dan sore hari.", (200, 200, 200)),
    Animal(600, 400, "deer", "Rusa", "Rusa adalah hewan mamalia anggun dengan tanduk bercabang (pada jantan). Mereka hidup berkelompok dan memakan dedaunan serta rumput.", (160, 120, 80)),
    Animal(200, 500, "bird", "Burung Pipit", "Burung pipit adalah burung kecil yang sering ditemui di sekitar pemukiman. Mereka memakan biji-bijian dan serangga kecil.", (100, 150, 200)),
    Animal(850, 150, "rabbit", "Kelinci Hutan", "Kelinci hutan lebih besar dari kelinci peliharaan dan memiliki bulu coklat keabu-abuan. Mereka sangat waspada terhadap predator.", (150, 130, 100)),
]

# Game variables
popup = None
current_nearby_object = None
running = True

# Main game loop
while running:
    clock.tick(FPS)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if popup:
                    popup = None
                    current_nearby_object = None
    
    # Player movement
    keys = pygame.key.get_pressed()
    dx = dy = 0
    
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        dx = -1
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        dx = 1
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        dy = -1
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        dy = 1
    
    player.move(dx, dy)
    
    # Check proximity to objects
    nearest_object = None
    nearest_distance = float('inf')
    
    # Reset highlights
    for tree in trees:
        tree.highlight = False
    for animal in animals:
        animal.highlight = False
    
    # Check trees
    for tree in trees:
        distance = calculate_distance(player.rect, tree.rect)
        if distance < INTERACTION_DISTANCE and distance < nearest_distance:
            nearest_distance = distance
            nearest_object = tree
    
    # Check animals
    for animal in animals:
        distance = calculate_distance(player.rect, animal.rect)
        if distance < INTERACTION_DISTANCE and distance < nearest_distance:
            nearest_distance = distance
            nearest_object = animal
    
    # Update popup based on nearest object
    if nearest_object:
        nearest_object.highlight = True
        if current_nearby_object != nearest_object:
            current_nearby_object = nearest_object
            info = nearest_object.get_info()
            popup = InfoPopup(info["name"], info["description"])
    else:
        if popup:
            popup = None
        current_nearby_object = None
    
    # Drawing
    screen.fill(GREEN)  # Grass background
    
    # Draw all objects
    for tree in trees:
        tree.draw(screen)
    
    for animal in animals:
        animal.draw(screen)
    
    player.draw(screen)
    
    # Draw popup if active
    if popup:
        popup.draw(screen)
    
    # Draw instructions
    inst_text = font_small.render("Gunakan WASD/Arrow keys untuk bergerak. Dekati pohon/hewan untuk melihat info.", True, BLACK)
    inst_bg = pygame.Surface((inst_text.get_width() + 20, inst_text.get_height() + 10))
    inst_bg.fill(WHITE)
    inst_bg.set_alpha(200)
    screen.blit(inst_bg, (10, 10))
    screen.blit(inst_text, (20, 15))
    
    pygame.display.flip()

pygame.quit()
sys.exit()
