# OIBSIP_Task3
# 🤖 Voice Assistant - Full Audio GUI (Python)

A modern **Tkinter-based Voice Assistant** with full audio responses using `pyttsx3`.  
This assistant reads **every response aloud**, shows timestamps, and supports quick command buttons.

---

## 🚀 Features

- 🔊 Text-to-Speech (Reads ALL responses)
- 💬 Full conversation history with timestamps
- ⌨️ Type commands or click quick-action buttons
- 🎨 Modern dark-themed GUI
- 🎵 Open music folder or YouTube
- 🌐 Open browser (Google)
- 📝 Open Notepad
- ⏰ Tell current time
- 📅 Tell current date
- 😂 Tell programming jokes
- 🔄 Repeat last response
- 🗑️ Clear chat history

---

## 🛠️ Technologies Used

- Python 3
- Tkinter (GUI)
- ttk Styling
- pyttsx3 (Text-to-Speech)
- threading
- datetime
- webbrowser
- os
- random

---

## 📂 Project Structure

```
Voice-Assistant/
│
├── voice_assistant.py
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/Voice-Assistant.git
cd Voice-Assistant
```

### 2️⃣ Install Required Library

```bash
pip install pyttsx3
```

*(Tkinter comes pre-installed with Python)*

### 3️⃣ Run the Application

```bash
python voice_assistant.py
```

---

## 🎮 Available Commands

You can either type commands or click buttons.

### 💬 Text Commands

- `time` → Tells current time  
- `date` → Tells today's date  
- `joke` → Tells a programming joke  
- `notepad` → Opens Notepad  
- `browser` / `google` → Opens Google  
- `music` → Opens music folder  
- `hello` → Greeting  
- `bye` / `exit` → Close assistant  

---

## 🎨 Interface Overview

- Left Panel → Colorful Quick Action Buttons  
- Right Panel → Full Chat History (with timestamps)  
- Input Field → Type and press Enter or Click SPEAK  
- Audio → Every assistant message is spoken aloud  

---

## 🔮 Future Improvements

- Speech Recognition (Voice Input)
- Weather integration
- AI chatbot integration (GPT API)
- System control commands
- Cross-platform music detection

---

## 👩‍💻 Author

Deekshitha

---

## 📜 License

This project is licensed under the MIT License.
