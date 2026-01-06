<div align="center">
<img width="415" height="347" alt="image" src="https://github.com/user-attachments/assets/ef5f09e7-ea69-4296-afdf-82242678d25a" />

<div align="center">

  # 👁️ Vivid
  
  ### **The NO-NONSENSE Pixel Pirate.**
  
  <p>
    <img src="https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" />
    <img src="https://img.shields.io/badge/Computer%20Vision-OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" />
    <img src="https://img.shields.io/badge/Automation-PyAutoGUI-green?style=for-the-badge" />
  </p>

  **A lightweight, zero-dependency screen recorder for creating silent demos, time-lapses, and automation logs.**

</div>

---

## ⚡ The Essence

**Vivid** strips away the complexity of audio processing to focus on one thing: reliable video capture. Whether you are debugging a script, recording a gaming clip, or logging server activity, Vivid creates high-compatibility video files without the bloat.

## ⭐ Features
* **🏎️ Fast & Light:** No heavy audio drivers or mixing libraries required.
* **⏱️ FPS Lock:** Includes a smart sync engine to ensure your video plays at normal speed (no "fast-forward" glitches).
* **📐 Auto-Resolution:** Automatically detects your monitor size—from 720p to 4K.
* **🛑 Safe Exit:** Saves your file cleanly even if you interrupt the recording.

---

## ⚙️ Configuration Guide

Because Vivid is video-only, your main controls are **Duration** and **FPS**.

### 1. Duration (How long?)
You can set a hard limit or let it run indefinitely.
* **Fixed Mode:** `DURATION = 10` (Stops automatically after 10 seconds).
* **Infinite Mode:** `DURATION = None` (Runs until you press 'q').

### 2. FPS (Frames Per Second)
The FPS determines how smooth the motion looks.
* **10-12 FPS (Recommended):** The sweet spot for Python. It captures readable text and mouse movements without overheating your CPU.
* **24-30 FPS:** Possible on powerful machines, but may cause the script to lag if the screen resolution is very high (4K).
* **60 FPS:** Not recommended for pure Python recorders (requires GPU acceleration tools).

### 3. File Formats & Codecs
Vivid supports the industry standards:

| Extension | Codec Tag | Description |
| :--- | :--- | :--- |
| **.mp4** | `mp4v` | **Best Balance.** Good quality, widely supported. |
| **.mp4** | `avc1` | **H.264 Standard.** High compression, very compatible. |
| **.avi** | `XVID` | **Most Robust.** Use this if MP4 fails. Slightly larger file size. |

---

## 🚀 Quick Start

1.  **Install Dependencies:**
    ```bash
    pip install opencv-python numpy pyautogui
    ```

2.  **Run Vivid:**
    ```bash
    python vivid.py
    ```

3.  **Control:**
    * A preview window will open showing what is being recorded.
    * Press **`q`** inside that window to save and quit.

---

<div align="center">
  <sub>"Vivid: Because your screen deserves to be seen, not just stared at." 📼</sub>
</div>
