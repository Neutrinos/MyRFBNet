import os  
import sys  
import time  
import random  
  
# Constants  
WIDTH, HEIGHT = 20, 10  
DELAY = 0.1  
  
# Directions  
UP, DOWN, LEFT, RIGHT = (0, -1), (0, 1), (-1, 0), (1, 0)  
  
def clear_screen():  
    os.system('cls' if os.name == 'nt' else 'clear')  
  
def print_screen(snake, food, score):  
    clear_screen()  
    for y in range(HEIGHT):  
        for x in range(WIDTH):  
            if (x, y) in snake:  
                print('O', end=' ')  
            elif (x, y) == food:  
                print('F', end=' ')  
            else:  
                print('.', end=' ')  
        print()  
    print(f"Score: {score}")  
  
def move_snake(snake, direction):  
    head_x, head_y = snake[0]  
    new_head = (head_x + direction[0], head_y + direction[1])  
    if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT or new_head in snake[1:]:  
        return snake  # Game over if snake hits wall or itself  
    return [new_head] + snake[:-1]  
  
def grow_snake(snake, food):  
    return [food] + snake  
  
def get_random_food_position(snake):  
    while True:  
        food = (random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1))  
        if food not in snake:  
            return food  
  
def main():  
    snake = [(WIDTH // 2, HEIGHT // 2)]  
    direction = RIGHT  
    food = get_random_food_position(snake)  
    score = 0  
  
    while True:  
        try:  
            prev_key = direction  
            if sys.platform == "win32":  
                # Use `msvcrt` to get key input without requiring Enter on Windows  
                import msvcrt  
                key = msvcrt.getch()  
            else:  
                # Use `sys.stdin.read` to get key input on other platforms (requires Enter)  
                key = sys.stdin.read(1)  
              
            if key == b'w' or key == 'w':  
                direction = UP  
            elif key == b's' or key == 's':  
                direction = DOWN  
            elif key == b'a' or key == 'a':  
                direction = LEFT  
            elif key == b'd' or key == 'd':  
                direction = RIGHT  
            # Prevent the snake from reversing  
            if (direction[0] == -prev_key[0]) and (direction[1] == -prev_key[1]):  
                direction = prev_key  
  
            snake = move_snake(snake, direction)  
            if snake[0] == food:  
                snake = grow_snake(snake, food)  
                food = get_random_food_position(snake)  
                score += 1  
  
            print_screen(snake, food, score)  
            time.sleep(DELAY)  
  
        except KeyboardInterrupt:  
            print("\nGame Over!")  
            break  
  
if __name__ == "__main__":  
    main()
