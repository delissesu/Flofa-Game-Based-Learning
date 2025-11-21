import pygame
import sys
import random
from src.config import FPS, MAP_WIDTH, MAP_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT
from src.models.player import Player
from src.models.tree import Tree
from src.models.animal import Animal
from src.models.cat import Cat
from src.models.grass import create_grass_clump_sprite, spawn_all_grass_clumps
from src.controllers.game_controller import GameController
from src.views.game_view import GameView
from src.utils.helpers import get_safe_random_pos

def main():
    """Main game function"""
    pygame.init()
    
    # audio disini : adit
    pygame.mixer.init() 
    
    # load musiknya
    pygame.mixer.music.load("assets\\audio\\Searching for a Body.mp3")
    
    # jalanin musik dengan infinite loop
    pygame.mixer.music.play(-1)
    
    # Setup display BEFORE loading any assets
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Exploration Game")
    
    clock = pygame.time.Clock()
    
    # INISIALISASI OBJEK GAME
    player = Player(MAP_WIDTH // 2, MAP_HEIGHT // 2)
    
    CX = MAP_WIDTH // 2
    CY = MAP_HEIGHT // 2

    trees = [
        Tree(CX - 800, CY - 500, "beringin", "Pohon Beringin", "Beringin adalah pohon besar yang tumbuh di daerah tropis. Pohon ini memiliki ciri khas berupa akar gantung yang banyak dan menjuntai seperti rambut. Beringin berasal dan banyak ditemukan di wilayah Asia Tenggara, termasuk Indonesia."),
        Tree(CX + 800, CY - 500, "oak", "Pohon Oak", "Pohon Oak merupakan pohon besar yang terkenal kokoh dan dapat hidup sangat lama. Ciri khasnya adalah batang tebal serta daun bercuping yang lebar. Pohon ini berasal dari wilayah beriklim sedang seperti Amerika Utara dan Eropa."),
        Tree(CX - 800, CY + 500, "maple", "Pohon Maple", "Pohon Maple adalah pohon berdaun lebar yang menghasilkan getah manis yang biasa diolah menjadi sirup maple. Ciri utamanya adalah bentuk daun bercabang yang bisa berubah warna saat musim gugur. Maple berasal dari Kanada dan negara beriklim dingin lainnya di Amerika Utara."),
        Tree(CX + 800, CY + 500, "pine", "Pohon Cemara", "Pohon Cemara (Pine) adalah pohon berdaun jarum yang tetap hijau sepanjang tahun. Ciri-cirinya meliputi bentuk pohon yang meruncing ke atas dan daun berbentuk jarum tipis. Pohon ini berasal dari daerah pegunungan serta wilayah beriklim sedang."),
        Tree(CX - 400, CY, "mangga", "Pohon Mangga", "Pohon Mangga merupakan pohon buah tropis yang sangat populer. Pohon ini memiliki ciri daun panjang dan buah manis beraroma khas. Mangga berasal dari Asia Selatan, tetapi kini telah tumbuh luas di berbagai daerah tropis, termasuk Indonesia."),
        Tree(CX + 400, CY, "alpukat", "Pohon Alpukat", "Pohon Alpukat adalah pohon buah yang menghasilkan buah bergizi dengan daging lembut berwarna hijau kekuningan. Ciri khasnya terletak pada daunnya yang lebar serta buah yang kaya lemak sehat. Alpukat berasal dari wilayah Amerika Tengah dan Selatan."),
        Tree(CX, CY - 400, "rambutan", "Pohon Rambutan", "Pohon Rambutan adalah pohon tropis yang menghasilkan buah unik dengan kulit berbulu dan rasa manis. Ciri buahnya yang berbulu menjadi tanda khas yang mudah dikenali. Rambutan berasal dari wilayah Asia Tenggara."),
        Tree(CX, CY + 400, "sakura", "Pohon Sakura", "Pohon Sakura merupakan pohon berbunga yang sangat terkenal di Jepang. Ciri utamanya adalah bunga berwarna merah muda lembut yang mekar di musim semi. Sakura berasal dari Jepang dan beberapa wilayah Asia Timur lainnya.")
    ]
    
    animals_data = [
        ("sapi", "Sapi", "Sapi adalah hewan ternak besar yang banyak dipelihara manusia. Hewan ini memiliki tubuh besar dan dikenal sebagai penghasil susu. Sapi biasanya hidup di lingkungan peternakan atau padang rumput."),
        ("anak_sapi", "Anak Sapi", "Anak sapi adalah sapi muda yang masih dalam masa pertumbuhan. Ciri utamanya adalah tubuh yang lebih kecil dan sifat yang masih bergantung pada induknya. Anak sapi hidup di peternakan bersama induknya."),
        ("itik", "Itik", "Itik adalah unggas air yang sering dipelihara maupun ditemukan di alam liar. Itik memiliki paruh lebar dan sangat suka berenang. Habitatnya biasanya berada di kolam, sungai, atau sawah."),
        ("domba", "Domba", "Domba adalah hewan ternak yang dikenal karena dapat menghasilkan bulu tebal dan lembut. Ciri khas domba adalah tubuhnya yang diselimuti bulu wol. Domba hidup di padang rumput, peternakan, atau daerah dataran tinggi."),
        ("babi", "Babi", "Babi merupakan hewan omnivora yang terkenal sangat cerdas. Ciri utamanya adalah hidung moncong dan sifatnya yang suka mengeksplor lingkungan. Babi biasanya hidup di peternakan atau hutan."),
        ("ayam", "Ayam", "Ayam adalah unggas yang sering dipelihara untuk diambil daging dan telurnya. Ciri khasnya adalah kebiasaan berkokok pada pagi hari, terutama ayam jantan. Ayam hidup di kandang atau pekarangan rumah."),
        ("kambing", "Kambing", "Kambing adalah hewan ternak yang lincah dan mudah beradaptasi. Ciri-cirinya termasuk tubuh ramping, tanduk kecil, dan kebiasaan suka memanjat tempat yang tinggi. Kambing hidup di perbukitan, peternakan, atau padang rumput."),
        ("pitik_walik", "Pitik Walik", "Pitik Walik adalah ayam unik asal Jawa yang memiliki ciri khas bulu tumbuh terbalik ke arah atas. Keunikan bulunya membuatnya mudah dikenali. Pitik Walik biasanya dipelihara di lingkungan pedesaan atau peternakan kecil.")
    ]

    animals = []
    for a_type, a_name, a_desc in animals_data:
        safe_x, safe_y = get_safe_random_pos(trees + animals, min_dist=100) 
        animals.append(Animal(safe_x, safe_y, a_type, a_name, a_desc))

    # Kucing
    cats = []
    safe_x, safe_y = get_safe_random_pos(trees + animals + cats, min_dist=120)
    cats.append(Cat(safe_x, safe_y, "Si Meng", "Kucing kesayangan."))

    print("Menyiapkan rumput...")
    grass_cache = [create_grass_clump_sprite(random.randint(25,40), random.randint(15,30)) for _ in range(5)]
    all_grass = spawn_all_grass_clumps(3000, grass_cache)
    
    # Inisialisasi MVC
    controller = GameController(player, trees, animals, cats, all_grass)
    view = GameView(screen)
    
    running = True
    
    # GAME LOOP
    while running:
        clock.tick(FPS)
        time_sec = pygame.time.get_ticks() / 1000.0
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                running = False
            controller.handle_event(event)
        
        # Update
        controller.handle_input(controller.popup is not None)
        controller.update_camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        controller.update_interactions()
        controller.update_cats(controller.popup is not None)
        
        # Render
        view.render(
            player,
            trees,
            animals,
            cats,
            all_grass,
            controller.camera,
            time_sec,
            controller.popup,
            controller.can_interact_with
        )
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
