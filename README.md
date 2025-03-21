
<h1 align="center">Minecraft Death Location Finder</h1>

<p align="center">
   This script finds the last death location of a player in a Minecraft world.
   <br>
   It uses the provided Python script to read the NBT data of the Minecraft world.
   <br>
</p>

<p align="center">
  <img src="https://img.shields.io/github/v/release/Samxel/Minecraft-Death-Location-Finder" alt="GitHub release">
  <img src="https://img.shields.io/github/downloads/Samxel/Minecraft-Death-Location-Finder/total" alt="GitHub all releases">
  <img src="https://img.shields.io/github/issues/Samxel/Minecraft-Death-Location-Finder" alt="GitHub issues">
</p>

## Prerequisites

*   **Python 3.6+**
*   **The following Python packages:**
    *   `requests`
    *   `nbt` (PyNBT)

## Installation

This project uses a `requirements.txt` file to manage dependencies. This file lists all the necessary Python packages for the project.

1.  **Install Python:** If you don't have Python installed, download it from [python.org](https://www.python.org/downloads/) and install it. Make sure you add Python to your PATH.

2.  **Install Packages:** Open a command prompt or terminal, navigate to the directory where you saved the `requirements.txt` file (and your Python script), and run the following command:

    ```bash
    pip install -r requirements.txt
    ```

    This command will install all the packages listed in the `requirements.txt` file.

3.  **Download Script:** Download the Python file (`death_location_finder.py`) containing the script to find the death location.

## Usage

1.  **Run Script:** Open a command prompt or terminal and navigate to the directory where you saved the Python file. Then, run the script:

    ```bash
    python death_location_finder.py
    ```

2.  **Answer Prompts:** The script will ask you for the following information:

    *   **World Name:** Enter the name of the Minecraft World.
    *   **Player Name:** Enter the exact Minecraft username of the player.

3.  **View Results:** The script will output the dimension and coordinates (x, y, z) of the player's last death location.
