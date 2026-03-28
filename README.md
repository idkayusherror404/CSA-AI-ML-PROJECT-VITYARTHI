# 🧠 AI/ML Algorithm Playground

**Course:** CSA2001 — Fundamentals of AI and ML  
**Institution:** VIT Bhopal  
**Language:** C++ (Backend) + HTML/CSS/JS (Frontend)

A full-stack web application demonstrating core AI and ML algorithms from the CSA2001 course curriculum, implemented in C++ with a modern interactive frontend.

---

## 🚀 Features

| Module | Algorithm | Description |
|--------|-----------|-------------|
| Module 2 | **MiniMax + Alpha-Beta Pruning** | Unbeatable Tic-Tac-Toe AI |
| Module 2 | **A\* / BFS / Greedy Search** | Visual grid pathfinding |
| Module 4 | **Linear Regression (OLS)** | Least squares line fitting |
| Module 4 | **K-Means Clustering** | K-Means++ initialization |
| Module 4 | **Naive Bayes Classifier** | Text sentiment analysis |

---

## 📁 Project Structure

```
ai-ml-playground/
├── backend/
│   ├── main.cpp          ← C++ HTTP server (all algorithms)
│   ├── httplib.h         ← Download this (see setup)
│   └── json.hpp          ← Download this (see setup)
├── frontend/
│   └── index.html        ← Single-page web app
├── README.md
├── description.txt
└── .gitignore
```

---

## ⚙️ Setup & Run

### Step 1 — Download Dependencies

Download these two header files into the `backend/` folder:

```bash
# Option A: Using curl
curl -o backend/httplib.h https://raw.githubusercontent.com/yhirose/cpp-httplib/master/httplib.h
curl -o backend/json.hpp https://raw.githubusercontent.com/nlohmann/json/develop/single_include/nlohmann/json.hpp

# Option B: Manual download
# 1. Go to https://github.com/yhirose/cpp-httplib → httplib.h → Raw → Save As
# 2. Go to https://github.com/nlohmann/json → single_include/nlohmann/json.hpp → Raw → Save As
```

### Step 2 — Compile the Backend

```bash
cd backend
g++ -std=c++17 -O2 -pthread main.cpp -o server
```

**Windows (MinGW):**
```bash
g++ -std=c++17 -O2 -lws2_32 main.cpp -o server.exe
```

### Step 3 — Run the Backend

```bash
./server          # Linux/Mac
server.exe        # Windows
```

You should see:
```
╔══════════════════════════════════════╗
║  AI/ML Algorithm Playground Backend  ║
║  Running at http://localhost:8080     ║
╚══════════════════════════════════════╝
```

### Step 4 — Open the Frontend

Simply open `frontend/index.html` in your browser (double-click it).

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/health` | Server status |
| POST | `/api/tictactoe` | Get AI's next move |
| POST | `/api/search` | Run A*/BFS/Greedy pathfinding |
| POST | `/api/regression` | Fit linear regression model |
| POST | `/api/kmeans` | Cluster data points |
| POST | `/api/sentiment` | Classify text sentiment |

### Example API Calls

**Tic-Tac-Toe:**
```json
POST /api/tictactoe
{ "board": [1,0,0, 0,-1,0, 0,0,0] }
→ { "move": 2, "status": "ongoing" }
```

**A\* Search:**
```json
POST /api/search
{ "grid": [[0,0,1],[0,0,0],[1,0,0]], "start": [0,0], "end": [2,2], "algorithm": "astar" }
→ { "path": [[0,0],[1,0],[1,1],[1,2],[2,2]], "found": true, "cost": 4 }
```

**Linear Regression:**
```json
POST /api/regression
{ "x": [1,2,3,4,5], "y": [2.1,4.0,5.9,8.1,10.0] }
→ { "slope": 1.99, "intercept": 0.1, "r2": 0.999, "equation": "y = 1.99x + 0.10" }
```

---

## 📚 Algorithm Details

### MiniMax + Alpha-Beta Pruning
- **Concept:** Game tree search where AI minimizes score, human maximizes
- **Alpha-Beta:** Prunes branches that cannot affect the final decision
- **Complexity:** O(b^d) worst case, O(b^(d/2)) with alpha-beta
- **Result:** Optimal play — AI never loses

### A* Search
- **Heuristic:** Manhattan distance `h(n) = |x1-x2| + |y1-y2|`
- **Cost function:** `f(n) = g(n) + h(n)`
- **BFS mode:** h=0 (explores uniformly, guaranteed shortest path)
- **Greedy mode:** g=0 (only uses heuristic, fast but suboptimal)

### Linear Regression (OLS)
- **Formula:** `slope = (nΣxy - ΣxΣy) / (nΣx² - (Σx)²)`
- **R² Score:** Proportion of variance explained by the model
- **Residuals:** Shown as vertical lines on the scatter plot

### K-Means Clustering
- **Initialization:** K-Means++ (smart centroid initialization)
- **Update:** Iterative assignment + centroid recomputation (Lloyd's)
- **Inertia:** Within-cluster sum of squared distances (lower = better)

### Naive Bayes
- **Formula:** `P(class|words) ∝ P(words|class) × P(class)`
- **Smoothing:** Laplace smoothing to avoid zero probability
- **Classes:** Positive, Negative, Neutral

---

## 🛠 Requirements

- **GCC** 7+ or **Clang** 5+ (with C++17 support)
- **Modern browser** (Chrome, Firefox, Edge)
- **Internet** (for Google Fonts in frontend)

---

## 👤 Author

VIT Bhopal — CSA2001 Project  
Fundamentals of AI and ML
