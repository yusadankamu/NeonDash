import pygame 
import random
import os

# -- GLOBAL CONFIG --
WIDTH, HEIGHT = 800, 600
FPS = 60
BG_COLOR = (5, 5, 20)
PLAYER_COLOR = (0, 255, 255)
OBSTACLE_COLOR = (255, 0, 110)
SHIELD_COLOR = (100, 255, 100)

# -- INITIALIZATION --
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("NEON DASH: POWER-UP")
clock = pygame.time.Clock()

# -- FONTS --
font_main = pygame.font.SysFont("Consolas", 30, bold=True)
font_logo = pygame.font.SysFont("Verdana", 70, bold=True)

# -- LOAD AUDIO WITH SAFE CHECKS --
def load_sfx(path):
    if os.path.exists(path):
        return pygame.mixer.Sound(path)
    else:
        print(f"Warning: Sound file '{path}' not found.")
        return None

sfx_jump = load_sfx("assets/jump.wav")
sfx_die = load_sfx("assets/gameover.wav")

# -- OBJECT CLASSES --

class Particle:
    def __init__(self, x, y, color, is_explosion=False):
        self.x, self.y = x, y
        self.color = color
        self.vx = random.uniform(-5, 5) if is_explosion else random.uniform(-2, 0)
        self.vy = random.uniform(-5, 5) if is_explosion else random.uniform(-1, 1)
        self.lifetime = 255
        self.gravity = 0.1 if is_explosion else 0

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.y += self.gravity
        self.lifetime -= 10

    def draw(self, surf):
        if self.lifetime > 0:
            p_surf = pygame.Surface((6, 6), pygame.SRCALPHA)
            pygame.draw.circle(p_surf, (*self.color, self.lifetime), (3, 3), 3)
            surf.blit(p_surf, (int(self.x), int(self.y)))

class PowerUp:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH, random.randint(150, 450), 30, 30)
        self.speed = 5

    def update(self):
        self.rect.x -= self.speed

    def draw(self, surf):
        # Efek perisai berdenyut
        size = 30 + abs(int(10 * pygame.time.get_ticks() / 200 % 5))
        pygame.draw.rect(surf, SHIELD_COLOR, self.rect.inflate(size-30, size-30), 2, 15)
        pygame.draw.circle(surf, SHIELD_COLOR, self.rect.center, 8)

class Player:
    def __init__(self):
        self.rect = pygame.Rect(100, HEIGHT // 2, 40, 40)
        self.vel = 0
        self.gravity = 0.7
        self.particles = []
        self.has_shield = False
        self.is_alive = True

    def jump(self):
        if not self.is_alive: return
        self.vel = -11
        if sfx_jump: sfx_jump.play()
        for _ in range(5):
            self.particles.append(Particle(self.rect.centerx, self.rect.centery, PLAYER_COLOR))

    def update(self):
        if self.is_alive:
            self.vel += self.gravity
            self.rect.y += self.vel
            if self.rect.bottom > HEIGHT: self.rect.bottom = HEIGHT
            if self.rect.top < 0: self.rect.top = 0
        
        for p in self.particles[:]:
            p.update()
            if p.lifetime <= 0: self.particles.remove(p)

    def draw(self, surf):
        for p in self.particles: p.draw(surf)
        if self.is_alive:
            # Gambar Perisai jika aktif
            if self.has_shield:
                pygame.draw.circle(surf, SHIELD_COLOR, self.rect.center, 35, 2)
            
            # Gambar Player
            pygame.draw.rect(surf, PLAYER_COLOR, self.rect, border_radius=8)
            for i in range(1, 4):
                pygame.draw.rect(surf, (0, 50, 50), self.rect.inflate(i*4, i*4), 1, 8)

class Obstacle:
    def __init__(self, speed):
        self.width = 40
        self.height = random.randint(150, 350)
        self.is_top = random.choice([True, False])
        y = 0 if self.is_top else HEIGHT - self.height
        self.rect = pygame.Rect(WIDTH, y, self.width, self.height)
        self.speed = speed

    def update(self): self.rect.x -= self.speed
    def draw(self, surf):
        pygame.draw.rect(surf, OBSTACLE_COLOR, self.rect, border_radius=5)

# --- FUNGSI UTAMA GAME ---

def run_game():
    player = Player()
    obstacles = []
    powerups = []
    score = 0
    game_speed = 7
    spawn_timer = 0
    game_over = False
    explosion_time = 60

    while True:
        screen.fill(BG_COLOR)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: return "QUIT"
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                player.jump()

        if not game_over:
            player.update()
            
            # Spawn Rintangan
            spawn_timer += 1
            if spawn_timer > 50:
                obstacles.append(Obstacle(game_speed))
                spawn_timer = 0
                game_speed += 0.05
                # Peluang muncul Power-up (10%)
                if random.random() < 0.1:
                    powerups.append(PowerUp())

            # Update Power-ups
            for p in powerups[:]:
                p.update()
                if player.rect.colliderect(p.rect):
                    player.has_shield = True
                    powerups.remove(p)
                elif p.rect.right < 0:
                    powerups.remove(p)
                p.draw(screen)

            # Update Rintangan
            for obs in obstacles[:]:
                obs.update()
                if player.rect.colliderect(obs.rect):
                    if player.has_shield:
                        player.has_shield = False
                        obstacles.remove(obs) # Hancurkan rintangan
                    else:
                        if sfx_die: sfx_die.play()
                        game_over = True
                        player.is_alive = False
                        for _ in range(50):
                            player.particles.append(Particle(player.rect.centerx, player.rect.centery, PLAYER_COLOR, True))
                
                elif obs.rect.right < 0:
                    obstacles.remove(obs)
                    score += 1
                obs.draw(screen)
        else:
            player.update()
            for obs in obstacles: obs.draw(screen)
            explosion_time -= 1
            if explosion_time <= 0: return "MENU"

        player.draw(screen)
        
        # UI
        screen.blit(font_main.render(f"SCORE: {score}", True, (255, 255, 255)), (20, 20))
        if player.has_shield:
            screen.blit(font_main.render("SHIELD ACTIVE", True, SHIELD_COLOR), (20, 60))
            
        pygame.display.flip()
        clock.tick(FPS)

def main_menu():
    while True:
        screen.fill(BG_COLOR)
        title = font_logo.render("NEON DASH", True, PLAYER_COLOR)
        screen.blit(title, title.get_rect(center=(WIDTH//2, HEIGHT//3)))
        
        hint = font_main.render("PRESS SPACE TO START", True, (200, 200, 200))
        if pygame.time.get_ticks() % 1000 < 500:
            screen.blit(hint, hint.get_rect(center=(WIDTH//2, HEIGHT//2)))
            
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: return
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                res = run_game()
                if res == "QUIT": return

if __name__ == "__main__":
    main_menu()
    pygame.quit()