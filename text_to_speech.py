import tkinter as tk
import pyttsx3
import threading

class TextToSpeechApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text to Speech App")
        self.root.geometry("400x300")

        self.engine = pyttsx3.init()

        # Create a label
        self.label = tk.Label(self.root, text="Enter text below:", font=('Arial', 14))
        self.label.pack(pady=10)

        # Create a text entry widget
        self.text_entry = tk.Text(self.root, height=10, width=40, font=('Arial', 12))
        self.text_entry.pack(pady=10)

        # Create a speak button
        self.speak_button = tk.Button(self.root, text="Speak", command=self.speak_text, bg="#3C3D37", fg="white", font=('Arial', 12))
        self.speak_button.pack(pady=10)

        # Create a canvas for the microphone animation
        self.canvas = tk.Canvas(self.root, width=50, height=50, bg=self.root.cget("bg"), highlightthickness=0)
        self.canvas.pack(pady=20)
        self.microphone_icon = self.canvas.create_oval(10, 10, 40, 40, fill="gray")  # Microphone base
        self.microphone_top = self.canvas.create_rectangle(20, 0, 30, 10, fill="gray")  # Microphone top

        self.is_speaking = False  # Flag to check if speaking

    def speak_text(self):
        text = self.text_entry.get("1.0", tk.END).strip()  # Get text from the text widget
        if text:
            # Start speaking in a separate thread
            threading.Thread(target=self.start_speaking, args=(text,)).start()

    def start_speaking(self, text):
        self.is_speaking = True
        self.animate_microphone()  # Start the microphone animation
        self.engine.say(text)  # Use the TTS engine to say the text
        self.engine.runAndWait()  # Wait for the speech to finish
        self.is_speaking = False
        self.canvas.delete("all")  # Stop the animation

    def animate_microphone(self):
        # Animate the microphone while speaking
        if self.is_speaking:
            self.canvas.itemconfig(self.microphone_icon, fill="red")  # Change color to indicate speaking
            self.root.after(500, self.blink_microphone)

    def blink_microphone(self):
        if self.is_speaking:
            current_color = self.canvas.itemcget(self.microphone_icon, 'fill')
            new_color = "gray" if current_color == "red" else "red"
            self.canvas.itemconfig(self.microphone_icon, fill=new_color)  # Blink effect
            self.root.after(500, self.blink_microphone)

# Start the application
if __name__ == "__main__":
    root = tk.Tk()
    app = TextToSpeechApp(root)
    root.mainloop()
