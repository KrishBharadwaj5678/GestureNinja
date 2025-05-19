# 🥷 GestureNinja

**GestureNinja** is a computer vision based project that allows you to play **Fruit Ninja** game using real time index finger tracking. Harness the power of your webcam and slice fruits using hand gestures. 🍉🍎

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
| 🎛️ **CVZone**    | Simplifies OpenCV + MediaPipe                                           |
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

```bash
pip install -r requirements.txt
```

3. **Run the script**

```bash
python app.py
```

---

## 🎯 How It Works

1. 📸 Detect your **hand landmarks** using MediaPipe.
2. ☝️ Track the **tip of your index finger** to control the mouse position.
3. 🤙 **Show your pinky finger** to simulate a *mouse hold* (useful for slicing).
4. 🖱️ Move your system cursor in real time based on your finger’s position.
5. 🔁 Continuously respond to your gestures for smooth interaction.

---

## 🤝 Contributing

Contributions are welcome! Feel free to open issues, submit PRs, or suggest improvements.

---
