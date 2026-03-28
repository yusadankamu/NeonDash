# 🎮 NEON DASH: POWER-UP

A high-octane arcade-style avoidance game with a synthwave aesthetic! Jump, dodge, and survive the endless stream of obstacles while collecting power-ups to maximize your score.

![Python](https://img.shields.io/badge/Python-3.14+-blue.svg)
![Pygame](https://img.shields.io/badge/Pygame-CE%202.5.7-orange.svg)
![Game](https://img.shields.io/badge/Game-Arcade%20Action-brightgreen.svg)

---

## 🚀 Quick Start

### Prerequisites
- Python 3.10+ (tested with Python 3.14)
- pip (Python package manager)

### Installation

1. **Clone or download this repository**
   ```bash
   cd NeonDashGame
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment**
   - **Windows:**
     ```bash
     .venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source .venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install pygame-ce
   ```

5. **Run the game**
   ```bash
   python main.py
   ```

---

## 🎮 How to Play

### Objective
Avoid incoming obstacles for as long as possible while collecting power-ups to increase your chances of survival!

### Controls
- **SPACEBAR** – Jump to evade obstacles
- **CLOSE WINDOW** – Exit the game

### Game Mechanics

| Element | Description |
|---------|-------------|
| 🔷 **Cyan Player** | Your character. Jump with SPACEBAR to avoid obstacles |
| 🔴 **Red Obstacles** | Deadly barriers that move from right to left. Avoid them! |
| 🟢 **Green Shield** | Temporary protection. Absorb ONE obstacle hit without losing |
| 📊 **Score** | Earn 1 point for each obstacle you successfully avoid |
| ⚡ **Difficulty** | The game gets progressively harder as your score increases |

### Game Over
Your game ends when you hit an obstacle without a shield. Watch the explosion particle effects as your attempt concludes!

---

## 🎨 Features

✨ **Eye-Catching Neon Visuals**
- Cyan player with glowing rings
- Hot pink obstacles
- Green shield power-ups with pulsing effects
- Dark background with smooth animations

🎵 **Audio Feedback**
- Jump sound effects
- Game over crash sound
- Dynamic audio system (gracefully handles missing audio files)

💫 **Particle Effects**
- Jump particles when you leap
- Explosion effects on collision

⏱️ **Progressive Difficulty**
- Obstacles spawn faster as your score increases
- Smooth difficulty curve keeps the game engaging

🛡️ **Power-Up System**
- Random shield drops (10% chance per obstacle spawn)
- Protection from a single collision

---

## 📁 Project Structure

```
NeonDashGame/
├── main.py              # Main game file (800x600 window, 60 FPS)
├── assets/              # Game assets folder
│   ├── jump.wav         # Jump sound effect
│   └── gameover.wav     # Game over sound effect
└── README.md            # This file
```

### Key Game Parameters

```python
WIDTH, HEIGHT = 800, 600      # Window size
FPS = 60                       # Frame rate
PLAYER_COLOR = (0, 255, 255)  # Cyan
OBSTACLE_COLOR = (255, 0, 110) # Hot pink
SHIELD_COLOR = (100, 255, 100) # Green
```

---

## 🏗️ Game Architecture

### Classes

**Player**
- Manages player position, velocity, and physics
- Handles jumping and gravity
- Tracks shield status
- Generates particle effects

**Obstacle**
- Random height and position
- Moves across screen
- Can be destroyed by shield

**PowerUp**
- Spawn with 10% chance per obstacle
- Pulsing visual effect
- Grants temporary shield protection

**Particle**
- Visual effects for jumps and explosions
- Applies gravity and velocity physics
- Fades out over time

---

## 🎯 Tips & Tricks

1. **Time Your Jumps** – Press spacebar at the right moment to clear obstacles
2. **Monitor the Shield** – The UI shows "SHIELD ACTIVE" when protected
3. **Expect Patterns** – Obstacles come in predictable waves with increasing speed
4. **Use Power-ups Wisely** – Shade automatically activates, but plan your dodges for when it expires
5. **High Score Challenge** – How long can you survive? Share your records!

---

## 🔧 Customization

Want to make the game your own? Edit these values in `main.py`:

```python
# Adjust difficulty
game_speed = 7              # Initial obstacle speed
spawn_timer = 50            # Lower = faster spawns

# Change colors
BG_COLOR = (5, 5, 20)       # Background color
PLAYER_COLOR = (0, 255, 255) # Your character
OBSTACLE_COLOR = (255, 0, 110) # Enemies
SHIELD_COLOR = (100, 255, 100) # Shield effect

# Modify physics
gravity = 0.7               # Player gravity
jump_velocity = -11         # Jump strength
```

---

## 🐛 Troubleshooting

### "ModuleNotFoundError: No module named 'pygame'"
Install pygame-ce:
```bash
pip install pygame-ce
```

### Sound files not found
The game gracefully handles missing audio files. Place `.wav` files in the `assets/` folder:
- `assets/jump.wav`
- `assets/gameover.wav`

### Game runs slowly
- Close other programs
- Ensure you have a dedicated GPU
- Reduce window size (edit WIDTH and HEIGHT in main.py)

---

## 📊 Game Balance

| Score Range | Speed Multiplier | Spawning Rate |
|-------------|------------------|---------------|
| 0-10       | 1.0x             | Normal        |
| 11-25      | 1.35x            | Fast          |
| 26-50      | 1.75x            | Very Fast     |
| 50+        | 2.0x+            | Insane        |

---

## 💡 Future Enhancement Ideas

- 🎵 Background music track
- 🌈 Color themes/skins for the player
- 💾 High score leaderboard with save file
- 🎁 Different power-up types (Double Score, Slow Motion, etc.)
- 🎮 Multiple difficulty modes
- 📱 Mobile/touch support
- 🏆 Achievement system

---

## 📜 License

This project is open-source and available for personal and educational use. Feel free to modify and share!

---

## 🤝 Contributing

Have ideas to make NEON DASH even better?
1. Fork or modify the code
2. Test your changes
3. Share your improvements!

---

## 🎪 Credits

- Built with **Pygame-CE** (Community Edition)
- Inspired by classic arcade games
- Neon aesthetic design philosophy

---

## 📞 Support

Having issues? Check that:
- ✅ Python 3.10+ is installed
- ✅ pygame-ce is properly installed (`pip install pygame-ce`)
- ✅ All game files are in the correct directory
- ✅ Your system meets the graphics requirements

---

## 🎉 Have Fun!

Get ready to **DASH** through a neon wonderland! How many obstacles can you survive?

**Good luck, player! May your reflexes be sharp and your shield be strong!** 🎮⚡

---

*Last Updated: March 2026*
*Made with ❤️ and pygame-ce*
