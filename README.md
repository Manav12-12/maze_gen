# 🌀 Maze Generator using Randomized Prim's Algorithm  

This project implements a **random maze generator** using **Randomized Prim's Algorithm** in **Python with Pygame**. The algorithm progressively expands the maze by selecting random frontier cells and removing walls to connect them. The visualization updates in real-time, showing the maze being constructed dynamically.

---

## 📌 Features  
✔️ Generates **unique** and **fully connected** mazes each time  
✔️ Uses **Randomized Prim’s Algorithm** for natural maze structures  
✔️ **Live visualization** with smooth animations using Pygame  
✔️ **Dynamic coloring**:
   - **Current frontier cells** → Light Blue  
   - **Completed maze areas** → White  
✔️ Adjustable **grid size**, **cell size**, and **frame rate**  

---

## 🎯 How the Algorithm Works  

1️⃣ **Start with a random cell**  
2️⃣ **Add its unvisited neighbors to the frontier list**  
3️⃣ **Randomly select a frontier cell** and remove its wall to connect it to an adjacent visited cell  
4️⃣ **Expand the maze by adding its unvisited neighbors** to the frontier  
5️⃣ **Repeat until all cells are visited**  

The result is a **fully connected, randomized maze** with no isolated areas or loops.  

---

## 🛠️ Installation & Setup  

### **Prerequisites**  
- Python **3.8+**  
- Pygame library  

### **Installation Steps**  

1️⃣ **Install Pygame** (if not already installed)  
   ```bash
   pip install pygame
