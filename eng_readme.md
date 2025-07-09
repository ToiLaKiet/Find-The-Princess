# 🤴 Finding the Path to Save the Princess (The Suitor's Challenge)

A course project that applies the **BFS (Breadth-First Search)** algorithm to find the shortest path on a grid-based map. The application is built using Python and features a visual interface powered by Streamlit.

**Student:**
- **Full Name:** `Võ Anh Kiệt`
- **Student ID:** `23520825`
- **Class:** `CS112.P22`
---
[**Click here to visit the demo website**](https://find-the-princess-cs112.streamlit.app/)

[**Click here to watch the demo video**](https://drive.google.com/file/d/1xE3Mq9miBi245dtxoUufTmEX6o4S3g1Z/view?usp=sharing)

---

## 📜 Journey Overview

- [🎯 Problem Objective](#problem-objective)
- [💡 Idea and Solution](#idea-and-solution)
- [📌 Sample Test Cases](#sample-test-cases)
- [🕹️ Additional Features](#additional-features)
- [⚠️ Limitations](#limitations)
- [📂 Directory Structure](#directory-structure)
- [⚙️ Installation and Usage Guide](#installation-and-usage-guide)
- [🛠️ Technology Stack](#technology-stack)
- [📬 Contact Information](#contact-information)

## Problem Objective

The problem requires finding the **shortest path** for a knight on an `m x n` grid map to reach the palace and save the princess.

1.  **Map:** A rectangular grid of size `m x n`, with traversable cells (`0`) and non-traversable obstacle cells (`1`).
2.  **Movement:** The knight can move from one cell to any of its 8 adjacent cells (horizontally, vertically, and diagonally). Each move costs **1 unit of time**.
3.  **Coordinate System:** The bottom-left corner of the map has the coordinates `(0, 0)`.
4.  **Goal:** Calculate the minimum time (number of steps) required to travel from the knight's position to the palace. If no path exists, return `-1`.

---

## Idea and Solution

To solve the shortest path problem on an unweighted graph (or a graph with uniform edge weights), the **Breadth-First Search (BFS)** algorithm is the optimal choice.

### How BFS Works:
1.  **Initialization:**
    *   Start from the source node (the knight's position).
    *   Use a `queue` to store cells to be visited.
    *   Use a 2D `check` array to mark visited cells, preventing revisits and infinite loops.
    *   Use a 2D `mark` array to store the coordinates of the preceding cell (the "parent" of the current cell), which helps in backtracking the path.

2.  **Traversal Process:**
    *   Dequeue the first cell from the queue.
    *   Check if this cell is the princess's location. If yes, backtrack using the `mark` array to find the path and terminate. If not, continue.
    *   Iterate through all adjacent cells (8 directions) of the current cell.
    *   For each neighboring cell:
        *   Check if it is within the map's boundaries.
        *   Check if it is an obstacle (`1`) or has already been visited (`check`).
        *   If the neighbor is valid, mark it as visited (`check`), store the current cell's coordinates in the `mark` array for the neighbor, and enqueue it.
    *   Repeat this process until the queue is empty or the princess is found.

3.  **Result:**
    *   If the loop finishes without finding the destination, it means no path exists. Return `-1`.
    *   Otherwise, return an array containing the coordinates of the path from the knight's position to the princess.

### Note on the Coordinate System:
The problem specifies coordinates `(x, y)` with `(0, 0)` at the bottom-left corner. When working with 2D arrays in C++ (or other languages), the index `[0][0]` is typically at the top-left corner. Therefore, a coordinate transformation is needed:
`map_array[m - 1 - y][x]` corresponds to the coordinate `(x, y)`.

---

## Sample Test Cases
[🧪 Link to Sample Test Cases](https://github.com/ToiLaKiet/Find-The-Princess/tree/master/test)

## Additional Features
- **Random Map Generation**: You can create a new map with custom dimensions and randomly distributed obstacles.

## Limitations
- While the random generation feature is functional, continuous re-rendering of components can currently lead to errors, requiring a page reload.

## Directory Structure

The project structure is organized for easy management and compilation.

```
.
├── src/
│   ├── app.py            # Streamlit app interface file
│   └── utils.py          # File containing the BFS algorithm logic
├── assets/
│   └── logo-uit.png      # Logo, favicon
├── test/                 # Directory containing test case files
│   ├── Test Case 1
        ├── input.txt
│   └── Test Case 2  
        ├── input.txt 
├── .gitignore
├── readme.md             # This usage guide file    
├── requirements.txt      # File containing necessary libraries
```

---

## Installation and Usage Guide

To run this program on your local machine, follow these steps.

### Requirements
- Python 3.x (version 3.9+ is recommended).

### Steps

#### 1. Clone the Repository
First, clone this repository to your computer and navigate into the project directory.
```bash
git clone https://github.com/ToiLaKiet/Find-The-Princess.git
cd Find-The-Princess
```

#### 2. Create and Activate a Virtual Environment
Using a virtual environment is good practice to manage project dependencies independently and avoid conflicts with other projects.

**Option A: Using `venv` (Python's built-in tool, recommended)**
```bash
# Create a virtual environment named "venv"
python3 -m venv venv

# Activate the newly created environment
# On macOS or Linux:
source venv/bin/activate

# On Windows (Command Prompt/PowerShell):
venv\Scripts\activate
```

**Option B: Using `Conda` (If you have Anaconda or Miniconda installed)**
```bash
# Create a new environment named "princess_app" with Python 3.9
conda create --name princess_app python=3.9 -y

# Activate the environment
conda activate princess_app
```
After activation, you will see the environment's name (`(venv)` or `(princess_app)`) at the beginning of your command prompt.

#### 3. Install Required Libraries
With the virtual environment activated, run the following command to install all required libraries from the `requirements.txt` file.
```bash
pip install -r requirements.txt
```

#### 4. Run the Streamlit Application
Now, you are ready to run the application!
```bash
streamlit run src/app.py
```
After executing this command, a new tab should automatically open in your web browser with the application's interface, typically at **http://localhost:8501**.

#### 5. Stop the Application
To stop the application, return to the running terminal window and press `Ctrl + C`.

---

## Technology Stack

- **Language:** Python
- **Framework:** Streamlit

---

## Contact Information

- 📧 **Email:** `[toilakiet.dev@gmail.com]`
- 🐛 **Bug Reports:** For any suggestions or bug reports, please open a new issue at the repository's [GitHub Issues](https://github.com/ToiLaKiet/Find-The-Princess/issues).
