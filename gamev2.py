import pygame
import sys
import math
import cairo
import random


pygame.init()


SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
FPS = 60
PLAYER_SPEED = 3
INTERACTION_DISTANCE = 70

MAP_WIDTH = SCREEN_WIDTH * 3
MAP_HEIGHT = SCREEN_HEIGHT * 3
MAP_RECT = pygame.Rect(0, 0, MAP_WIDTH, MAP_HEIGHT)


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (34, 139, 34)
DARK_GREEN = (0, 100, 0)
BROWN = (101, 67, 33)
LIGHT_BLUE = (173, 216, 230)
GRAY = (200, 200, 200)
YELLOW = (255, 255, 0)


GRASS_COLORS = [
    (30, 100, 40), (40, 120, 50), (50, 140, 60),
    (60, 150, 70), (25, 90, 35) # Tambah variasi
]


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game Eksplorasi Alam (Rumput Sprite)")
clock = pygame.time.Clock()


pygame.font.init()
font_title = pygame.font.Font(None, 32)
font_text = pygame.font.Font(None, 24)
font_small = pygame.font.Font(None, 20)


# 1. FUNGSI GENERASI SPRITE

def create_player_sprite(size=40):
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, size, size)
    ctx = cairo.Context(surface)
    ctx.set_source_rgba(0, 0, 0, 0)
    ctx.paint()
    ctx.set_source_rgb(0.95, 0.8, 0.7) 
    ctx.arc(size/2, size/3, size/6, 0, 2 * math.pi)
    ctx.fill()
    ctx.set_source_rgb(0.2, 0.4, 0.8) 
    ctx.rectangle(size/2 - size/8, size/3 + size/8, size/4, size/3)
    ctx.fill()
    ctx.set_source_rgb(0.3, 0.2, 0.1) 
    ctx.rectangle(size/2 - size/10, size/3 + size/2.3, size/12, size/6)
    ctx.fill()
    ctx.rectangle(size/2 + size/30, size/3 + size/2.3, size/12, size/6)
    ctx.fill()
    buf = surface.get_data()
    pygame_surface = pygame.image.frombuffer(buf, (size, size), 'ARGB')
    return pygame_surface

def create_tree_sprite(size=60, tree_type="oak"):
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, size, size)
    ctx = cairo.Context(surface)
    ctx.set_source_rgba(0, 0, 0, 0)
    ctx.paint()
    if tree_type == "oak":
        ctx.set_source_rgb(0.4, 0.26, 0.13)
        ctx.rectangle(size/2 - size/12, size/2, size/6, size/2.5)
        ctx.fill()
        ctx.set_source_rgb(0.13, 0.55, 0.13)
        ctx.arc(size/2, size/2.5, size/3, 0, 2 * math.pi)
        ctx.fill()
    elif tree_type == "pine":
        ctx.set_source_rgb(0.4, 0.26, 0.13)
        ctx.rectangle(size/2 - size/15, size/1.8, size/7.5, size/2.2)
        ctx.fill()
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


def create_grass_clump_sprite(width, height):
    """
    Membuat satu gambar (Surface) gumpalan rumput dengan PyCairo.
    """
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    ctx = cairo.Context(surface)
    
   
    ctx.set_source_rgba(0, 0, 0, 0)
    ctx.paint()

    num_blades = random.randint(7, 12) 
    
    for i in range(num_blades):
       
        if i < num_blades // 2:
            color = random.choice(GRASS_COLORS)[:3] 
            color = (color[0]*0.7, color[1]*0.7, color[2]*0.7) 
        else:
            color = random.choice(GRASS_COLORS)
        
        ctx.set_source_rgb(color[0]/255, color[1]/255, color[2]/255)

    
        base_x = width / 2 + random.uniform(-width * 0.4, width * 0.4)
        base_y = height 
        

        tip_x = base_x + random.uniform(-width * 0.2, width * 0.2)
        tip_y = random.uniform(height * 0.1, height * 0.4) #
        
    
        ctrl_x1 = base_x + random.uniform(-width * 0.1, width * 0.1)
        ctrl_y1 = height * 0.7
        ctrl_x2 = tip_x + random.uniform(-width * 0.1, width * 0.1)
        ctrl_y2 = height * 0.3

        
        ctx.move_to(base_x - 2, base_y) 
        ctx.curve_to(ctrl_x1, ctrl_y1, ctrl_x2, ctrl_y2, tip_x, tip_y) 
        ctx.line_to(base_x + 2, base_y) 
        ctx.close_path()
        ctx.fill()

    buf = surface.get_data()
    pygame_surface = pygame.image.frombuffer(buf, (width, height), 'ARGB')
    return pygame_surface


def spawn_all_grass_clumps(total_clumps, sprite_cache):
    """Menyebar gumpalan rumput di SELURUH MAP."""
    clumps = []
    for _ in range(total_clumps):
        x_base = random.randint(0, MAP_WIDTH)
        y_base = random.randint(0, MAP_HEIGHT)
        

        sprite = random.choice(sprite_cache)
        
        amplitude = random.randint(3, 8)
        speed = random.uniform(0.5, 1.5)
        offset = random.uniform(0, 2 * math.pi)
        

        clumps.append({
            "x": x_base,
            "y": y_base,
            "sprite": sprite,
            "amp": amplitude,
            "spd": speed,
            "off": offset
        })
    return clumps


def draw_swaying_clump(surface, clump_data, time_sec, camera):
    """Menggambar satu GUMPALAN sprite rumput yang bergoyang."""
    

    sway = math.sin(time_sec * clump_data["spd"] + clump_data["off"]) * clump_data["amp"]
 
    sprite = clump_data["sprite"]
    sprite_width = sprite.get_width()
    sprite_height = sprite.get_height()

    screen_x = clump_data["x"] - camera.x - (sprite_width / 2) + sway
    screen_y = clump_data["y"] - camera.y - sprite_height 
    

    if screen_x < -sprite_width or screen_x > SCREEN_WIDTH or \
       screen_y < -sprite_height or screen_y > SCREEN_HEIGHT:
        return
    

    surface.blit(sprite, (screen_x, screen_y))


# 3. CLASSES OBJEK GAME

def calculate_distance(obj1_rect, obj2_rect):
    x1 = obj1_rect.centerx
    y1 = obj1_rect.centery
    x2 = obj2_rect.centerx
    y2 = obj2_rect.centery
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

class Player:
    def __init__(self, x, y):
        self.sprite = create_player_sprite()
        self.rect = self.sprite.get_rect(center=(x, y))
        self.speed = PLAYER_SPEED
    
    def move(self, dx, dy):
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed
        self.rect.clamp_ip(MAP_RECT)
    
    def draw(self, surface, camera):
        screen_pos_rect = self.rect.move(-camera.x, -camera.y)
        surface.blit(self.sprite, screen_pos_rect)

class Tree:
    def __init__(self, x, y, tree_type, name, desc):
        self.sprite = create_tree_sprite(tree_type=tree_type)
        self.rect = self.sprite.get_rect(center=(x, y))
        self.name = name
        self.description = desc
        self.type = "tree"
        self.highlight = False
    
    def draw(self, surface, camera):
        screen_pos_rect = self.rect.move(-camera.x, -camera.y)
        if self.highlight:
            pygame.draw.circle(surface, YELLOW, screen_pos_rect.center, 35, 3)
        surface.blit(self.sprite, screen_pos_rect)
    
    def get_info(self):
        return {"name": self.name, "description": self.description}

class Animal:
    def __init__(self, x, y, animal_type, name, desc, color):
        self.rect = pygame.Rect(x, y, 40, 40)
        self.animal_type = animal_type
        self.name = name
        self.description = desc
        self.color = color
        self.type = "animal"
        self.highlight = False
    
    def draw(self, surface, camera):
        screen_rect = self.rect.move(-camera.x, -camera.y)
        if self.highlight:
            pygame.draw.circle(surface, YELLOW, screen_rect.center, 30, 3)
        if self.animal_type == "rabbit":
            pygame.draw.ellipse(surface, self.color, (screen_rect.x, screen_rect.y + 10, 35, 25))
            pygame.draw.circle(surface, self.color, (screen_rect.x + 27, screen_rect.y + 12), 10)
            pygame.draw.ellipse(surface, self.color, (screen_rect.x + 22, screen_rect.y, 6, 15))
            pygame.draw.ellipse(surface, self.color, (screen_rect.x + 30, screen_rect.y, 6, 15))
        elif self.animal_type == "deer":
            pygame.draw.ellipse(surface, self.color, (screen_rect.x, screen_rect.y + 10, 40, 25))
            pygame.draw.circle(surface, self.color, (screen_rect.x + 35, screen_rect.y + 8), 8)
            pygame.draw.line(surface, BROWN, (screen_rect.x + 35, screen_rect.y + 8), 
                                 (screen_rect.x + 32, screen_rect.y), 2)
            pygame.draw.line(surface, BROWN, (screen_rect.x + 35, screen_rect.y + 8), 
                                 (screen_rect.x + 38, screen_rect.y), 2)
        elif self.animal_type == "bird":
            pygame.draw.ellipse(surface, self.color, (screen_rect.x + 10, screen_rect.y + 15, 20, 15))
            pygame.draw.circle(surface, self.color, (screen_rect.x + 25, screen_rect.y + 18), 7)
            pygame.draw.polygon(surface, self.color, [
                (screen_rect.x + 10, screen_rect.y + 20),
                (screen_rect.x, screen_rect.y + 15),
                (screen_rect.x + 5, screen_rect.y + 25)
            ])
    
    def get_info(self):
        return {"name": self.name, "description": self.description}

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
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 128))
        surface.blit(overlay, (0, 0))
        pygame.draw.rect(surface, WHITE, (self.x, self.y, self.width, self.height), border_radius=10)
        pygame.draw.rect(surface, BLACK, (self.x, self.y, self.width, self.height), 3, border_radius=10)
        title_surf = font_title.render(self.name, True, BLACK)
        surface.blit(title_surf, (self.x + 20, self.y + 20))
        info_text = font_small.render("(Tekan ESC atau berjalan menjauh untuk menutup)", True, GRAY)
        surface.blit(info_text, (self.x + 20, self.y + 55))
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


# 4. INISIALISASI OBJEK GAME


player = Player(MAP_WIDTH // 2, MAP_HEIGHT // 2)


trees = [
    Tree(MAP_WIDTH // 2 - 400, MAP_HEIGHT // 2 - 200, "oak", "Pohon Oak", "Pohon oak adalah pohon besar yang kokoh dengan daun lebar. Kayunya sering digunakan untuk furniture dan konstruksi. Pohon ini dapat hidup hingga ratusan tahun."),
    Tree(MAP_WIDTH // 2 + 300, MAP_HEIGHT // 2 - 150, "pine", "Pohon Pinus", "Pohon pinus memiliki daun berbentuk jarum dan menghasilkan kerucut. Mereka tumbuh subur di iklim dingin dan sering digunakan sebagai pohon Natal."),
    Tree(MAP_WIDTH // 2 - 100, MAP_HEIGHT // 2 + 200, "oak", "Pohon Maple", "Pohon maple terkenal dengan daun berwarna cerah di musim gugur. Getahnya dapat diolah menjadi sirup maple yang manis dan lezat."),
    Tree(MAP_WIDTH // 2 + 500, MAP_HEIGHT // 2 + 250, "pine", "Pohon Cemara", "Pohon cemara adalah pohon hijau abadi yang tetap hijau sepanjang tahun. Mereka memiliki aroma khas dan sering ditanam sebagai tanaman hias."),
]
animals = [
    Animal(MAP_WIDTH // 2, MAP_HEIGHT // 2 - 100, "rabbit", "Kelinci", "Kelinci adalah hewan herbivora yang lincah dengan telinga panjang. Mereka hidup dalam liang dan aktif pada pagi dan sore hari.", (200, 200, 200)),
    Animal(MAP_WIDTH // 2 + 200, MAP_HEIGHT // 2 + 100, "deer", "Rusa", "Rusa adalah hewan mamalia anggun dengan tanduk bercabang (pada jantan). Mereka hidup berkelompok dan memakan dedaunan serta rumput.", (160, 120, 80)),
    Animal(MAP_WIDTH // 2 - 300, MAP_HEIGHT // 2 + 200, "bird", "Burung Pipit", "Burung pipit adalah burung kecil yang sering ditemui di sekitar pemukiman. Mereka memakan biji-bijian dan serangga kecil.", (100, 150, 200)),
    Animal(MAP_WIDTH // 2 + 400, MAP_HEIGHT // 2 - 200, "rabbit", "Kelinci Hutan", "Kelinci hutan lebih besar dari kelinci peliharaan dan memiliki bulu coklat keabu-abuan. Mereka sangat waspada terhadap predator.", (150, 130, 100)),
]


print("Membuat sprite rumput... (Mungkin butuh beberapa detik)")
grass_clump_sprites_cache = []
for _ in range(5): 
    w = random.randint(25, 40)
    h = random.randint(15, 30)
    grass_clump_sprites_cache.append(create_grass_clump_sprite(w, h))
print("Sprite rumput selesai dibuat.")


all_grass_clumps = spawn_all_grass_clumps(2500, grass_clump_sprites_cache)

camera = pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)


popup = None
current_nearby_object = None
running = True


# 5. MAIN GAME LOOP


while running:
    clock.tick(FPS)
    time_sec = pygame.time.get_ticks() / 1000.0
    
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if popup:
                    popup = None
                    current_nearby_object = None
  
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
    
   
    camera.center = player.rect.center
    camera.left = max(0, camera.left)
    camera.right = min(MAP_WIDTH, camera.right)
    camera.top = max(0, camera.top)
    camera.bottom = min(MAP_HEIGHT, camera.bottom)

   
    nearest_object = None
    nearest_distance = float('inf')
    for tree in trees:
        tree.highlight = False
    for animal in animals:
        animal.highlight = False
    for tree in trees:
        distance = calculate_distance(player.rect, tree.rect)
        if distance < INTERACTION_DISTANCE and distance < nearest_distance:
            nearest_distance = distance
            nearest_object = tree
    for animal in animals:
        distance = calculate_distance(player.rect, animal.rect)
        if distance < INTERACTION_DISTANCE and distance < nearest_distance:
            nearest_distance = distance
            nearest_object = animal
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
    

    screen.fill(GREEN)
    
  
    drawables = []
    
  
    drawables.append(("sprite", player.rect.bottom, player))
    for tree in trees:
        drawables.append(("sprite", tree.rect.bottom, tree))
    for animal in animals:
        drawables.append(("sprite", animal.rect.bottom, animal))

 
    for clump_data in all_grass_clumps:
        drawables.append(("grass", clump_data["y"], clump_data))
    

    drawables.sort(key=lambda item: item[1])
    

    for (type, y_pos, data) in drawables:
        if type == "sprite":
            data.draw(screen, camera)
            
        elif type == "grass":
            
            draw_swaying_clump(screen, data, time_sec, camera)
    

    
    
    if popup:
        popup.draw(screen)
    

    inst_text = font_small.render("Gunakan WASD/Arrow keys untuk bergerak. Dekati pohon/hewan untuk melihat info.", True, BLACK)
    inst_bg = pygame.Surface((inst_text.get_width() + 20, inst_text.get_height() + 10))
    inst_bg.fill(WHITE)
    inst_bg.set_alpha(200)
    screen.blit(inst_bg, (10, 10))
    screen.blit(inst_text, (20, 15))
    
    pygame.display.flip()

pygame.quit()
sys.exit()