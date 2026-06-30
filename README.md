# Ultra-Fast Python Autoclicker

A minimalist, high-performance autoclicker built for Windows using pure Python. By leveraging `ctypes` to communicate directly with the Windows API (`user32.dll`), this script bypasses standard framework overhead and built-in safety delays, making it significantly faster than alternatives like `pyautogui`.

## 🚀 Features
* **Zero Dependencies:** No need for `pip install`. It runs out of the box on any standard Python installation.
* **Bare-Metal Speed:** Executes clicks directly through the OS for maximum performance.
* **Global Hotkeys:** Works instantly even when the console is minimized or running in the background.

## 🎮 Controls
* **`Z`** : Toggle Start / Stop
* **`T`** : Terminate / Quit the program

## 🛠️ Requirements
* **OS:** Windows (uses `user32.dll`)
* **Python:** 3.x

## 📦 How to Run
Simply clone the repository and run the script:
```bash
python autoclicker.py
