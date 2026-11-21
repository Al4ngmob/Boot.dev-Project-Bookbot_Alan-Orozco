# Boot.dev-Project-Bookbot_Alan-Orozco
this repository is where i have my bookbot project from boot.dev:

## Bookbot

Bookbot is a command-line Python tool that analyzes `.txt` books and generates a detailed word and character frequency report.

### How to Use

1. Place your `.txt` book files inside the `books/` directory.
2. Run the program from your terminal by passing the file path as an argument:
   ```bash
   python3 main.py <path_to_book>
   ```
   * **Example:** `python3 main.py books/prideandprejudice.txt`

### Features & Behavior

* **Missing File Path Handling**
  * If you run the script without providing a book path, it displays the correct usage instructions and terminates with exit code `1`:
    ```text
    Usage: python3 main.py <path_to_book>
    ```
* **Book Analysis Report**
  * When a valid book path is provided, Bookbot prints a structured report containing:
    * **Book Path:** The file path of the analyzed text.
    * **Total Word Count:** The total number of words found in the book.
    * **Character Frequency Count:**
      * Converts all characters to lowercase so uppercase and lowercase letters are counted together.
      * Counts alphabetical characters only, ignoring spaces, numbers, and punctuation symbols.
      * Displays the results sorted from most frequently used to least frequently used.


[![Boot.dev Build a BookBot in Python certificate](https://qvault-webapp-dynamic-assets.storage.googleapis.com/certificates/ee83b57a-0490-405b-9276-d306f51c645f.jpeg?v=1794782096)](https://www.boot.dev/certificates/ee83b57a-0490-405b-9276-d306f51c645f)

## Asteroids

Asteroids is a 2D space shooter built with Python and Pygame. Pilot a triangular ship, shoot asteroids, and split them apart before they hit you.

### Requirements & Setup

1. Ensure you have **Python 3** installed.
2. Install **Pygame** from your terminal:
   ```bash
   pip install pygame
   ```

### How to Run

1. Clone the repository and move into the project directory.
2. Start the game from your terminal:
   ```bash
   python3 main.py
   ```

### Controls

- **W / S:** Move forward / backward
- **A / D:** Rotate left / right
- **Space:** Shoot (with a short cooldown)
- **Close Window:** Quit the game

### Gameplay & Behavior

- **Asteroid Spawning & Splitting**
  - Asteroids drift in from the edges of the screen.
  - Shooting an asteroid splits it into smaller pieces.
- **Collision & Boundaries**
  - Colliding with an asteroid ends the game.
  - Shots that leave the screen are automatically removed.

### Project Structure

- `main.py`: Game loop, input handling, and collision checks
- `player.py`: Player ship movement, rotation, and shooting
- `asteroid.py`: Asteroid behavior and splitting
- `asteroidfield.py`: Spawns asteroids along the screen edges
- `shot.py`: Projectile behavior
- `circleshape.py`: Shared base class with position, radius, and collision detection
- `constants.py`: Screen size, speeds, and other tuning values
- `logger.py`: Event and state logging

### Future Updates

- Add a scoring system
- Implement multiple lives and respawning
- Add an explosion effect for asteroids
- Add acceleration to player movement
- Wrap objects around the screen instead of removing them at the edges
- Add a background image
- Create different weapon types
- Make asteroids lumpy instead of perfectly round
- Give the ship a triangular hitbox instead of a circular one
- Add a shield power-up
- Add a speed power-up
- Add bombs that can be dropped

[![Boot.dev Build Asteroids using Python and Pygame certificate](https://api.boot.dev/v1/static/certificate/24d46176-52b6-438b-b4c5-a1ecb0beed9e)](https://www.boot.dev/certificates/24d46176-52b6-438b-b4c5-a1ecb0beed9e)
