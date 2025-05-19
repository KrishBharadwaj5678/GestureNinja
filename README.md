# 🥷 GestureNinja

**GestureNinja** is a computer vision based project that allows you to play **Fruit Ninja** game using real-time index finger tracking. Harness the power of your webcam and slice fruits using hand gestures. 🍉

---

## ✨ Features

- ☝️ **Index Finger Tracking** using your webcam  
- 🍊 **Fruit Ninja Control** via gestures (mouse emulation)  
- ⚡ Real-time detection and interaction  
- 💻 Runs locally — no internet required after setup  
- 🐍 Built with Python + OpenCV + MediaPipe

---

## 🛠️ Installation

1. **Clone the repo**

```bash
git clone https://github.com/your-username/gestureninja.git
cd gestureninja
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

## 🧩 Tech Stack

* 🐍 Python 3.x
* 🎥 OpenCV
* 🖐️ MediaPipe (for hand/finger tracking)
* 🖱️ PyAutoGUI or pynput (for controlling the mouse)

---

## 🚀 Future Improvements

* Add support for other games
* Improve gesture accuracy and robustness
* Multi-finger gesture support
* Game-specific gesture mapping UI

---

## 🤝 Contributing

Contributions are welcome! Feel free to open issues, submit PRs, or suggest improvements.

---
