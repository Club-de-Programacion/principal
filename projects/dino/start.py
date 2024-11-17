import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Dino settings
DINO_WIDTH = 40
DINO_HEIGHT = 60
DINO_JUMP_HEIGHT = 10

# Game objects
class Dino:
    def __init__(self):
        self.rect = pygame.Rect(100, SCREEN_HEIGHT - DINO_HEIGHT, DINO_WIDTH, DINO_HEIGHT)
        self.is_jumping = False
        self.jump_count = DINO_JUMP_HEIGHT
        self.dead = False

    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True

    def move(self):
        if self.is_jumping:
            if self.jump_count >= -DINO_JUMP_HEIGHT:
                neg = 1 if self.jump_count >= 0 else -1
                self.rect.y -= (self.jump_count ** 2) * 0.5 * neg
                self.jump_count -= 1
            else:
                self.is_jumping = False
                self.jump_count = DINO_JUMP_HEIGHT

    def draw(self, screen):
        color = RED if self.dead else GREEN
        pygame.draw.rect(screen, color, self.rect)

class Obstacle:
    def __init__(self):
        self.rect = pygame.Rect(SCREEN_WIDTH, SCREEN_HEIGHT - 40, 20, 40)

    def move(self):
        self.rect.x -= 10

    def draw(self, screen):
        pygame.draw.rect(screen, BLACK, self.rect)

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Dino Runner")
    clock = pygame.time.Clock()

    dino = Dino()
    obstacles = []
    score = 0
    font = pygame.font.Font(None, 36)

    run = True
    while run:
        clock.tick(FPS)
        screen.fill(WHITE)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            dino.jump()

        # Move and draw dino
        dino.move()
        dino.draw(screen)

        # Add obstacles
        if random.randint(1, 60) == 1:
            obstacles.append(Obstacle())

        # Move and draw obstacles
        for obstacle in obstacles:
            obstacle.move()
            obstacle.draw(screen)

            # Check for collision
            if dino.rect.colliderect(obstacle.rect):
                dino.dead = True

        # Remove off-screen obstacles and update score
        obstacles = [obs for obs in obstacles if obs.rect.x > 0]
        score += 1

        # Draw score
        score_text = font.render(f'Score: {score}', True, BLACK)
        screen.blit(score_text, (10, 10))

        # Check if dino is dead
        if dino.dead:
            death_text = font.render('Game Over', True, BLACK)
            screen.blit(death_text, (SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 - 20))
            pygame.display.flip()
            pygame.time.delay(2000)
            run = False

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
