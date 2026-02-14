import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import datetime
import webbrowser
import os
import random
import pyttsx3
import threading


class VoiceAssistantGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("🤖 Voice Assistant - FULL AUDIO")
        self.root.geometry("850x750")
        self.root.configure(bg='#1e1e2e')

        self.engine = None
        self.setup_audio()
        self.create_widgets()
        self.welcome()

    def setup_audio(self):
        try:
            self.engine = pyttsx3.init()
            self.engine.setProperty('rate', 165)
            self.engine.setProperty('volume', 0.9)
            print("✅ Audio engine ready - WILL READ ALL OUTPUTS")
        except:
            print("⚠️ No audio - text mode only")
            self.engine = None

    def speak(self, text, read_aloud=True):
        """Enhanced speak - reads EVERYTHING by default"""
        print(f"🤖: {text}")

        # Always add to chat AND speak
        if read_aloud:
            self.add_message("🤖", text)

        if self.engine:
            try:
                def speak_thread():
                    self.engine.say(text)
                    self.engine.runAndWait()

                threading.Thread(target=speak_thread, daemon=True).start()
            except:
                pass

    def create_widgets(self):
        style = ttk.Style()
        style.theme_use('clam')

        # HEADER
        header = tk.Frame(self.root, bg='#0f3460', height=90)
        header.pack(fill='x', pady=(0, 25))
        header.pack_propagate(False)

        tk.Label(header, text="🤖  VOICE ASSISTANT - FULL AUDIO",
                 font=('Arial', 22, 'bold'), bg='#0f3460', fg='#00d4ff').pack(expand=True)

        tk.Label(header, text="🔊 Reads EVERY response + timestamps | Click buttons or type!",
                 font=('Arial', 11), bg='#0f3460', fg='#66d9ef').pack(pady=(0, 10))

        main_frame = tk.Frame(self.root, bg='#1e1e2e')
        main_frame.pack(fill='both', expand=True, padx=25)

        # LEFT PANEL - BIG AUDIO BUTTONS
        left_panel = tk.Frame(main_frame, bg='#2a2a3e', width=280, relief='ridge', bd=2)
        left_panel.pack(side='left', fill='y', padx=(0, 20))
        left_panel.pack_propagate(False)

        self.status_label = tk.Label(left_panel, text="🔊 READY - Click or type commands!",
                                     font=('Arial', 13, 'bold'), bg='#2a2a3e', fg='#00ff88')
        self.status_label.pack(pady=20, padx=20)

        btn_frame = tk.Frame(left_panel, bg='#2a2a3e')
        btn_frame.pack(pady=20, padx=20, fill='both', expand=True)

        buttons = [
            ("⏰ TELL TIME", self.quick_time, '#ff6b35'),
            ("📅 TELL DATE", self.quick_date, '#4ecdc4'),
            ("😂 TELL JOKE", self.quick_joke, '#f9ca24'),
            ("📝 OPEN NOTEPAD", self.open_notepad, '#6c5ce7'),
            ("🌐 OPEN BROWSER", self.open_browser, '#00d4ff'),
            ("🎵 OPEN MUSIC", self.open_music, '#ff9ff3')
        ]

        for text, command, color in buttons:
            btn = tk.Button(btn_frame, text=text, bg=color, fg='white',
                            font=('Arial', 11, 'bold'), command=lambda c=command: self.button_speak(c),
                            relief='flat', pady=12, height=2)
            btn.pack(fill='x', pady=6)

        # RIGHT CHAT - FULL HISTORY
        chat_frame = tk.Frame(main_frame, bg='#2a2a3e', relief='ridge', bd=2)
        chat_frame.pack(side='right', fill='both', expand=True)

        tk.Label(chat_frame, text="💬 FULL CONVERSATION (All read aloud)",
                 font=('Arial', 16, 'bold'), bg='#2a2a3e', fg='#00d4ff').pack(pady=20)

        self.chat_display = scrolledtext.ScrolledText(chat_frame, state='disabled',
                                                      font=('Consolas', 11), height=20,
                                                      bg='#1e1e2e', fg='#e0e0e0',
                                                      insertbackground='#00d4ff')
        self.chat_display.pack(padx=25, pady=(0, 25), fill='both', expand=True)

        # INPUT - FIXED (No height parameter)
        input_frame = tk.Frame(chat_frame, bg='#2a2a3e')
        input_frame.pack(fill='x', padx=25, pady=(0, 25))

        self.command_entry = tk.Entry(input_frame, font=('Arial', 14),
                                      bg='#3a3a5a', fg='white', relief='flat',
                                      insertbackground='#00d4ff')
        self.command_entry.pack(side='left', fill='both', expand=True, padx=(0, 15), ipady=12)
        self.command_entry.bind('<Return>', self.execute_command)

        tk.Button(input_frame, text="🔊 SPEAK", bg='#00d4ff', fg='#1e1e2e',
                  font=('Arial', 12, 'bold'), command=self.execute_command,
                  relief='flat', padx=25, pady=12).pack(side='right')

        # EXTRA CONTROLS
        control_frame = tk.Frame(chat_frame, bg='#2a2a3e')
        control_frame.pack(pady=10)

        tk.Button(control_frame, text="🗑️ CLEAR CHAT", bg='#e74c3c', fg='white',
                  font=('Arial', 11, 'bold'), command=self.clear_chat).pack(side='left', padx=10)

        tk.Button(control_frame, text="🔄 REPEAT LAST", bg='#f39c12', fg='white',
                  font=('Arial', 11, 'bold'), command=self.repeat_last).pack(side='left', padx=10)

    def button_speak(self, command_func):
        """Wrapper for buttons - speaks confirmation"""
        command_func()
        self.speak("Command executed!")

    def welcome(self):
        self.speak("Welcome Deekshitha! Your AI assistant is ready. Click colorful buttons or type commands!")

    def add_message(self, speaker, text):
        """ALWAYS adds to chat display"""
        self.chat_display.config(state='normal')
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        self.chat_display.insert(tk.END, f"[{timestamp}] {speaker}: {text}\n\n")
        self.chat_display.config(state='disabled')
        self.chat_display.see(tk.END)

    def execute_command(self, event=None):
        command = self.command_entry.get().strip()
        if not command:
            return

        # SPEAK USER COMMAND + ADD TO CHAT
        self.speak(f"You said: {command}", read_aloud=False)
        self.add_message("👤", command)
        self.command_entry.delete(0, tk.END)

        command_lower = command.lower()

        # PROCESS COMMANDS
        if any(word in command_lower for word in ["time", "clock"]):
            self.tell_time()
        elif any(word in command_lower for word in ["date", "today", "day"]):
            self.tell_date()
        elif any(word in command_lower for word in ["joke", "funny"]):
            self.tell_joke()
        elif any(word in command_lower for word in ["notepad", "notes"]):
            self.open_notepad()
        elif any(word in command_lower for word in ["browser", "google", "internet", "web"]):
            self.open_browser()
        elif any(word in command_lower for word in ["music", "song", "player"]):
            self.open_music()
        elif any(word in command_lower for word in ["hello", "hi", "hey"]):
            self.speak("Hello! How can I help you today from Bengaluru?")
        elif any(word in command_lower for word in ["bye", "exit", "quit", "stop"]):
            self.speak("Goodbye! Happy coding from your Python assistant!")
            self.root.after(2500, self.root.quit)
        else:
            self.speak("I understand! Try: time, date, joke, notepad, browser, music, hello, or goodbye")

    def quick_time(self):
        self.speak("Getting current time...")
        now = datetime.datetime.now()
        time_str = now.strftime("%I:%M %p")
        self.speak(f"Right now it is {time_str}")

    def quick_date(self):
        self.speak("Checking today's date...")
        now = datetime.datetime.now()
        date_str = now.strftime("%A, %B %d, %Y")
        self.speak(f"Today is {date_str}")

    def quick_joke(self):
        self.speak("Here's a programmer joke for you...")
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "Why was the JavaScript developer sad? He didn't know how to null his feelings!",
            "Python programmers love geometry because they love circles of trust!"
        ]
        joke = random.choice(jokes)
        self.speak(joke)

    def tell_time(self):
        now = datetime.datetime.now()
        time_str = now.strftime("%I:%M %p")
        self.speak(f"The current time is {time_str}")

    def tell_date(self):
        now = datetime.datetime.now()
        date_str = now.strftime("%A, %B %d, %Y")
        self.speak(f"Today is {date_str}")

    def tell_joke(self):
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
            "Why was the JavaScript developer sad? He didn't know how to null his feelings! 😢",
            "Python programmers love geometry because they love circles of trust! 🔄"
        ]
        joke = random.choice(jokes)
        self.speak(joke)

    def open_notepad(self):
        try:
            os.system("notepad")
            self.speak("Opening Notepad right now!")
        except:
            self.speak("Notepad is not available on this system")

    def open_browser(self):
        webbrowser.open("https://www.google.com")
        self.speak("Opening Google browser for you!")

    def open_music(self):
        try:
            os.system("explorer.exe /select,music")
            self.speak("Opening your music folder!")
        except:
            webbrowser.open("https://www.youtube.com")
            self.speak("Opening YouTube music for you!")

    def clear_chat(self):
        self.chat_display.config(state='normal')
        self.chat_display.delete(1.0, tk.END)
        self.chat_display.config(state='disabled')
        self.speak("Chat history cleared!")

    def repeat_last(self):
        content = self.chat_display.get("end-2l", "end-1l")
        if content.strip():
            self.speak("Repeating last message...")
            self.speak(content.strip())

    def run(self):
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def on_closing(self):
        self.speak("Shutting down voice assistant. Goodbye from Bengaluru!")
        self.root.destroy()


if __name__ == "__main__":
    app = VoiceAssistantGUI()
    app.run()
