import pygame

class BoundaryTree:
    
    def __init__(self, x, y, tree_size=80, tree_style="default"):
        self.x = x
        self.y = y
        self.tree_size = tree_size
        self.tree_style = tree_style
        self.sprite = self._create_tree_sprite()
        self.rect = self.sprite.get_rect(center=(x, y))
    
    def _create_tree_sprite(self):
        size = int(self.tree_size * 1.5)
        
        img = pygame.Surface((size, size), pygame.SRCALPHA)
        img.fill((0, 0, 0, 0))
        
        # Gambar pohon berdasarkan style
        if self.tree_style == "pine":
            self._draw_pine_tree_pygame(img, size)
        elif self.tree_style == "oak":
            self._draw_oak_tree_pygame(img, size)
        else:
            self._draw_default_tree_pygame(img, size)
        
        return img
    
    def _draw_default_tree_pygame(self, surface, size):
        center_x = int(size / 2)
        center_y = int(size / 2)
        
        dark_brown = (60, 40, 20, 255)
        medium_brown = (90, 60, 30, 255)
        light_brown = (110, 75, 40, 255)
        dark_green = (20, 50, 15, 255)
        medium_green = (25, 65, 20, 255)
        light_green = (30, 80, 25, 255)
        
        trunk_width = int(size * 0.15)
        trunk_height = int(size * 0.4)
        trunk_x = center_x - trunk_width // 2
        trunk_y = int(center_y + size * 0.1)
        
        pygame.draw.rect(surface, medium_brown, (trunk_x, trunk_y, trunk_width, trunk_height))
        
        shadow_x = trunk_x + int(trunk_width * 0.6)
        shadow_width = int(trunk_width * 0.4)
        pygame.draw.rect(surface, dark_brown, (shadow_x, trunk_y, shadow_width, trunk_height))
        
        highlight_width = int(trunk_width * 0.3)
        pygame.draw.rect(surface, light_brown, (trunk_x, trunk_y, highlight_width, trunk_height))
        
        crown_radius = int(size * 0.35)
        crown_y = int(center_y - size * 0.15)
        
        pos1_x = int(center_x - crown_radius * 0.3)
        pos1_y = int(crown_y + crown_radius * 0.2)
        radius1 = int(crown_radius * 0.8)
        pygame.draw.circle(surface, dark_green, (pos1_x, pos1_y), radius1)
        
        pygame.draw.circle(surface, medium_green, (center_x, crown_y), crown_radius)
        
        pos3_x = int(center_x + crown_radius * 0.3)
        pos3_y = int(crown_y - crown_radius * 0.2)
        radius3 = int(crown_radius * 0.6)
        pygame.draw.circle(surface, light_green, (pos3_x, pos3_y), radius3)
    
    
    def _draw_pine_tree_pygame(self, surface, size):
        center_x = int(size / 2)
        center_y = int(size / 2)
        
        medium_brown = (90, 60, 30, 255)
        dark_green = (20, 50, 15, 255)
        medium_green = (25, 65, 20, 255)
        light_green = (30, 80, 25, 255)
        
        trunk_width = int(size * 0.1)
        trunk_height = int(size * 0.3)
        trunk_x = center_x - trunk_width // 2
        trunk_y = int(center_y + size * 0.15)
        
        pygame.draw.rect(surface, medium_brown, (trunk_x, trunk_y, trunk_width, trunk_height))
        
        triangle_configs = [
            (int(center_y + size * 0.25), int(size * 0.4), dark_green),      
            (int(center_y + size * 0.1), int(size * 0.35), medium_green),    
            (int(center_y - size * 0.05), int(size * 0.3), light_green),     
        ]
        
        for tri_y, tri_width, color in triangle_configs:
            top = (center_x, tri_y - int(tri_width * 0.6))  
            left = (center_x - tri_width // 2, tri_y)  
            right = (center_x + tri_width // 2, tri_y)  
            pygame.draw.polygon(surface, color, [top, left, right])
    
    def _draw_oak_tree_pygame(self, surface, size):
        center_x = int(size / 2)
        center_y = int(size / 2)
        
        medium_brown = (90, 60, 30, 255)
        dark_green = (20, 50, 15, 255)
        medium_green = (25, 65, 20, 255)
        light_green = (30, 80, 25, 255)
        
        trunk_width = int(size * 0.18)
        trunk_height = int(size * 0.35)
        trunk_x = center_x - trunk_width // 2
        trunk_y = int(center_y + size * 0.1)
        
        pygame.draw.rect(surface, medium_brown, (trunk_x, trunk_y, trunk_width, trunk_height))
        
        crown_configs = [
            (int(center_x - size * 0.15), int(center_y - size * 0.1), int(size * 0.25), dark_green),
            (int(center_x + size * 0.15), int(center_y - size * 0.05), int(size * 0.22), dark_green),
            (int(center_x - size * 0.05), int(center_y - size * 0.25), int(size * 0.28), medium_green),
            (int(center_x + size * 0.08), int(center_y - size * 0.22), int(size * 0.24), medium_green),
            (center_x, int(center_y - size * 0.15), int(size * 0.2), light_green),
        ]
        
        for cx, cy, radius, color in crown_configs:
            pygame.draw.circle(surface, color, (cx, cy), radius)
    
    def _draw_pine_tree(self, ctx, size):
        center_x = size / 2
        center_y = size / 2
        
        dark_brown = (60/255, 40/255, 20/255)      
        dark_brown = (60/255, 40/255, 20/255)      # Coklat gelap solid
        medium_brown = (90/255, 60/255, 30/255)    
        dark_green = (20/255, 50/255, 15/255)      
        medium_green = (25/255, 65/255, 20/255)    
        light_green = (30/255, 80/255, 25/255)     
        
        trunk_width = size * 0.1
        trunk_height = size * 0.3
        trunk_x = center_x - trunk_width / 2
        trunk_y = center_y + size * 0.15
        
        ctx.set_source_rgba(*medium_brown, 1.0)
        ctx.rectangle(trunk_x, trunk_y, trunk_width, trunk_height)
        ctx.fill()
        
        triangle_configs = [
            (center_y + size * 0.1, size * 0.4, dark_green),
            (center_y - size * 0.05, size * 0.35, medium_green),
            (center_y - size * 0.2, size * 0.3, light_green),
        ]
        
        for tri_y, tri_width, color in triangle_configs:
            ctx.set_source_rgba(*color, 1.0)
            ctx.move_to(center_x, tri_y - tri_width * 0.6)  # Puncak
            ctx.line_to(center_x - tri_width / 2, tri_y)     # Kiri bawah
            ctx.line_to(center_x + tri_width / 2, tri_y)     # Kanan bawah
            ctx.close_path()
            ctx.fill()
    
    def _draw_oak_tree(self, ctx, size):
        center_x = size / 2
        center_y = size / 2
        
        dark_brown = (60/255, 40/255, 20/255)      
        medium_brown = (90/255, 60/255, 30/255)    
        dark_green = (20/255, 50/255, 15/255)      
        medium_green = (25/255, 65/255, 20/255)    
        light_green = (30/255, 80/255, 25/255)     
        
        trunk_width = size * 0.18
        trunk_height = size * 0.35
        trunk_x = center_x - trunk_width / 2
        trunk_y = center_y + size * 0.1
        
        ctx.set_source_rgba(*medium_brown, 1.0)
        ctx.rectangle(trunk_x, trunk_y, trunk_width, trunk_height)
        ctx.fill()
        
        crown_configs = [
            (center_x - size * 0.15, center_y - size * 0.1, size * 0.25, dark_green),
            (center_x + size * 0.15, center_y - size * 0.05, size * 0.22, dark_green),
            (center_x - size * 0.05, center_y - size * 0.25, size * 0.28, medium_green),
            (center_x + size * 0.08, center_y - size * 0.22, size * 0.24, medium_green),
            (center_x, center_y - size * 0.15, size * 0.2, light_green),
        ]
        
        for cx, cy, radius, color in crown_configs:
            ctx.set_source_rgba(*color, 1.0)
            ctx.arc(cx, cy, radius, 0, 2 * 3.14159)
            ctx.fill()
    
    def draw(self, surface, camera):
        screen_x = self.x - camera.x
        screen_y = self.y - camera.y
        screen_rect = self.sprite.get_rect(center=(screen_x, screen_y))
        surface.blit(self.sprite, screen_rect)


def create_boundary_trees(map_width, map_height, spacing=150, margin=50):
    trees = []
    tree_styles = ["default", "pine", "oak"]
    
    x = margin
    while x < map_width - margin:
        style = tree_styles[len(trees) % len(tree_styles)]
        size = 60 + (hash(f"{x}_top") % 40)  # Variasi ukuran 60-100
        trees.append(BoundaryTree(x, margin, tree_size=size, tree_style=style))
        x += spacing
    
    x = margin
    while x < map_width - margin:
        style = tree_styles[len(trees) % len(tree_styles)]
        size = 60 + (hash(f"{x}_bottom") % 40)
        trees.append(BoundaryTree(x, map_height - margin, tree_size=size, tree_style=style))
        x += spacing
    
    y = margin + spacing
    while y < map_height - margin - spacing:
        style = tree_styles[len(trees) % len(tree_styles)]
        size = 60 + (hash(f"{y}_left") % 40)
        trees.append(BoundaryTree(margin, y, tree_size=size, tree_style=style))
        y += spacing
    
    y = margin + spacing
    while y < map_height - margin - spacing:
        style = tree_styles[len(trees) % len(tree_styles)]
        size = 60 + (hash(f"{y}_right") % 40)
        trees.append(BoundaryTree(map_width - margin, y, tree_size=size, tree_style=style))
        y += spacing
    
    return trees
