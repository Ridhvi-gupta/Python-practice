import pygame
import sys
import random

# Initialize Pygame and the font module
pygame.init()
pygame.font.init()

# --- Game Constants ---
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
BIRD_X = 100
BIRD_RADIUS = 15
GRAVITY = 0.4
FLAP_STRENGTH = -8
PIPE_WIDTH = 70
PIPE_GAP = 150
PIPE_SPEED = 3
PIPE_FREQUENCY = 1500  # milliseconds

# --- Colors ---
COLOR_SKY = (135, 206, 235)  # A nice light blue
COLOR_BIRD = (255, 255, 0)  # Yellow
COLOR_PIPE = (0, 128, 0)  # Green
COLOR_TEXT = (0, 0, 0)  # Black
COLOR_WHITE = (255, 255, 255)

# --- Setup Game Window ---
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()
score_font = pygame.font.SysFont("Arial", 30, bold=True)
game_over_font = pygame.font.SysFont("Arial", 40, bold=True)
restart_font = pygame.font.SysFont("Arial", 20)

# --- Game Variables ---
bird_y = SCREEN_HEIGHT // 2
bird_velocity = 0
pipes = []  # List to store all active pipe dictionaries
score = 0
game_active = True

# --- Pipe Spawning Timer ---
# Create a custom event for spawning pipes
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, PIPE_FREQUENCY)


# --- Helper Functions ---

def draw_bird(y):
    """Draws the bird (a yellow circle) on the screen."""
    pygame.draw.circle(screen, COLOR_BIRD, (BIRD_X, int(y)), BIRD_RADIUS)


def create_pipe():
    """Creates a new pair of pipe rectangles with a random gap position."""
    # Randomly determine the height of the bottom pipe
    gap_top = random.randint(150, SCREEN_HEIGHT - 150 - PIPE_GAP)

    # Create the top pipe rectangle
    top_pipe_rect = pygame.Rect(SCREEN_WIDTH, 0, PIPE_WIDTH, gap_top)

    # Create the bottom pipe rectangle
    bottom_pipe_rect = pygame.Rect(SCREEN_WIDTH, gap_top + PIPE_GAP, PIPE_WIDTH, SCREEN_HEIGHT - (gap_top + PIPE_GAP))

    # Return a dictionary for the new pipe pair
    return {'top': top_pipe_rect, 'bottom': bottom_pipe_rect, 'passed': False}


def move_pipes(pipes_list):
    """Moves all pipes to the left and removes off-screen pipes."""
    new_pipes = []
    for pipe in pipes_list:
        pipe['top'].centerx -= PIPE_SPEED
        pipe['bottom'].centerx -= PIPE_SPEED

        # Only keep pipes that are still visible on the screen
        if pipe['top'].right > 0:
            new_pipes.append(pipe)

    return new_pipes


def draw_pipes(pipes_list):
    """Draws all pipes (green rectangles) on the screen."""
    for pipe in pipes_list:
        pygame.draw.rect(screen, COLOR_PIPE, pipe['top'])
        pygame.draw.rect(screen, COLOR_PIPE, pipe['bottom'])


def check_collision(pipes_list, bird_rect):
    """Checks for collisions with pipes or screen boundaries."""
    # Check collision with pipes
    for pipe in pipes_list:
        if bird_rect.colliderect(pipe['top']) or bird_rect.colliderect(pipe['bottom']):
            return True

    # Check collision with screen top or bottom
    if bird_rect.top <= 0 or bird_rect.bottom >= SCREEN_HEIGHT:
        return True

    return False


def update_score(pipes_list, current_score):
    """Updates the score as the bird passes pipes."""
    for pipe in pipes_list:
        # Check if the pipe is past the bird and hasn't been scored yet
        if pipe['top'].centerx < BIRD_X and not pipe['passed']:
            current_score += 1
            pipe['passed'] = True
    return current_score


def display_score(current_score):
    """Renders and displays the current score."""
    score_surface = score_font.render(f"Score: {current_score}", True, COLOR_WHITE)
    score_rect = score_surface.get_rect(center=(SCREEN_WIDTH // 2, 50))
    screen.blit(score_surface, score_rect)


def display_game_over(final_score):
    """Displays the Game Over message and final score."""
    # Game Over text
    game_over_surface = game_over_font.render("GAME OVER", True, COLOR_TEXT)
    game_over_rect = game_over_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
    screen.blit(game_over_surface, game_over_rect)

    # Final Score text
    final_score_surface = score_font.render(f"Final Score: {final_score}", True, COLOR_TEXT)
    final_score_rect = final_score_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(final_score_surface, final_score_rect)

    # Restart instruction text
    restart_surface = restart_font.render("Press SPACE to Restart", True, COLOR_TEXT)
    restart_rect = restart_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
    screen.blit(restart_surface, restart_rect)


# --- Main Game Loop ---
while True:

    # --- Event Handling ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if game_active:
                    # Flap the bird
                    bird_velocity = FLAP_STRENGTH
                else:
                    # Restart the game
                    game_active = True
                    bird_y = SCREEN_HEIGHT // 2
                    bird_velocity = 0
                    pipes = []
                    score = 0

        if event.type == SPAWNPIPE and game_active:
            # Add a new pipe to the list
            pipes.append(create_pipe())

    # --- Drawing the Scene ---
    screen.fill(COLOR_SKY)  # Fill the background with sky blue

    if game_active:
        # --- Game Active Logic ---

        # Apply gravity
        bird_velocity += GRAVITY
        bird_y += bird_velocity

        # Create the bird's rectangle for collision detection
        bird_rect = pygame.Rect(BIRD_X - BIRD_RADIUS, bird_y - BIRD_RADIUS, BIRD_RADIUS * 2, BIRD_RADIUS * 2)

        # Move and draw pipes
        pipes = move_pipes(pipes)
        draw_pipes(pipes)

        # Draw the bird
        draw_bird(bird_y)

        # Update and display score
        score = update_score(pipes, score)
        display_score(score)

        # Check for collisions
        if check_collision(pipes, bird_rect):
            game_active = False

    else:
        # --- Game Over Logic ---

        # Draw all elements from the last active frame
        draw_pipes(pipes)
        draw_bird(bird_y)

        # Display the game over screen
        display_game_over(score)

    # --- Update the Display ---
    pygame.display.update()

    # --- Frame Rate Control ---
    clock.tick(60)  # Limit the game to 60 frames per second