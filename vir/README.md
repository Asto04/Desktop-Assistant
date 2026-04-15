# 🖥️ Desktop Virtual Assistant

A lightweight **Desktop Virtual Assistant** built using Python that allows users to perform everyday tasks through simple text commands with voice feedback.

---

## 📌 Overview

This project is a GUI-based assistant designed to automate routine desktop operations such as opening websites, retrieving system time, and interacting with the user through text and speech.

It provides a simple and efficient alternative to heavy AI assistants by using offline libraries and modular architecture.

---

## 🚀 Features

* 🌐 Open websites like Google and YouTube
* 🎵 Play music (Gaana integration)
* 🕒 Get real-time system time
* 💬 Basic conversational responses
* 🔊 Voice feedback using text-to-speech
* 🖥️ User-friendly GUI with Tkinter

---

## 🛠️ Technologies Used

* **Programming Language:** Python
* **GUI Framework:** Tkinter
* **Libraries:**

  * pyttsx3 (Text-to-Speech)
  * webbrowser (Web automation)
  * datetime (Time handling)
  * Pillow (Image processing)

---

## 📂 Project Structure

```
Desktop-Assistant/
│── GUI.py          # User Interface
│── action.py       # Logic handling
│── speak.py        # Voice output
│── image/          # Images used in GUI
│── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```
git clone https://github.com/your-username/desktop-assistant.git
```

### 2. Navigate to project folder

```
cd desktop-assistant
```

### 3. Install dependencies

```
pip install pyttsx3 pillow
```

### 4. Run the project

```
python GUI.py
```

---

## 💡 How It Works

1. User enters a command in the GUI
2. Command is sent to `action.py`
3. Logic processes keywords (like "google", "time")
4. Task is executed (open browser / get time)
5. Response is displayed and spoken using `speak.py`

---

## 📊 Performance

* ⚡ Fast response time (no heavy processing)
* 💻 Low CPU and memory usage
* 🎯 Accurate for predefined commands

---

## ⚠️ Limitations

* Works only on predefined keywords
* No advanced Natural Language Processing (NLP)
* Requires internet for web-based tasks

---

## 🔮 Future Enhancements

* Add speech-to-text (voice commands)
* Integrate NLP for better understanding
* Add features like weather, email, and reminders
* Improve GUI design (dark mode, modern UI)

---

## 👨‍💻 Author

**Ashish Tamboli**
B.Tech CSE (3rd Year)
Jaipur Engineering College and Research Centre

---

## 📜 License

This project is for educational purposes and open for learning and improvements.

---

⭐ If you like this project, give it a star on GitHub!
