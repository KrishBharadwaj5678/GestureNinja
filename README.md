# 🥷 GestureNinja

**GestureNinja** is a computer vision based project that allows you to play **Fruit Ninja** game using real time index finger tracking. Harness the power of your webcam and slice fruits using hand gestures. 🍉

---

## ✨ Features

| Feature                         | Description                                                                      |
| ------------------------------- | -------------------------------------------------------------------------------- |
| ☝️ **Index Finger Tracking**    | Detects and tracks your index finger using webcam input                          |
| 🍊 **Gesture Based Control**    | No mouse or keyboard needed                                                      |
| ⚡ **Real Time Interaction**     | Low-latency tracking for smooth gameplay                                        |
| 🧠 **Hand Landmark Detection**  | Uses advanced hand tracking via MediaPipe                                       |
| 🖱️ **Mouse Emulation**         | Moves your system cursor based on finger position                                |
| 🎮 **Game Integration**         | Works with Fruit Ninja game                                                     |
| 🖥️ **Cross-Platform**          | Compatible with Windows, macOS, and Linux                                        |
| 💻 **Offline Support**          | Runs entirely offline after setup                                               |
| 🧩 **Modular Code Structure**   | Easy to extend for more gestures or games                                        |
| 👨‍💻 **Developer Friendly**    | Clean, well-documented code                                                         |

---

## 🧩 Tech Stack

| Technology        | Purpose                                                                 |
| ----------------- | ----------------------------------------------------------------------- |
| 🐍 **Python 3.x** | Core programming language                                              |
| 🎛️ **CVZone**    | Simplifies OpenCV + MediaPipe integrations with useful abstractions     |
| 🎥 **OpenCV**     | Video capture and image processing                                     |
| 🖐️ **MediaPipe** | Real time hand and finger tracking                                      |
| 🎛️ **PyAutoGUI** | Emulates mouse movements                                                |
| 🖱️ **mouse**     | Mouse control library for more precise input                            |
| 🧠 **NumPy**      | Efficient numerical operations and array handling                      |

---

## 🛠️ Installation

1. **Clone the repo**

```bash
git clone https://github.com/KrishBharadwaj5678/GestureNinja.git
cd GestureNinja
````

2. **Install dependencies**

Make sure you have Python 3.7 or later.

```bash
pip install -r requirements.txt
```

3. **Run the script**

```bash
python app.py
```

---

## 🎯 How It Works

GestureNinja uses your webcam to:

1. Detect your **hand landmarks** using [MediaPipe](https://google.github.io/mediapipe/)
2. Track the **tip of your index finger**
3. Move your system cursor based on finger position
4. Simulate mouse clicks/slices based on specific gestures or movements

---

## 📹 Demo

👉 *Coming Soon: GIF or YouTube link*

---

## 🤝 Contributing

Contributions are welcome! Feel free to open issues, submit PRs, or suggest improvements.

---
