Text-to-Speech Application with Microphone Animation
This Python-based Text-to-Speech (TTS) application utilizes the tkinter library for a user-friendly graphical interface and pyttsx3 for speech synthesis. The app allows users to input text and convert it into speech with a simple click of a button. An engaging feature of this application is its animated microphone, which provides a visual cue while the speech is being generated.

Key Features:
User Interface: The app has a clean and intuitive layout that includes a text entry box for input and a button to initiate speech.
Text Input: Users can enter any text, which the application will read aloud, making it useful for various applications like language learning, accessibility, or entertainment.
Microphone Animation: A microphone icon on the canvas animates while the speech is playing, changing color to indicate when the TTS engine is active. This animation enhances user engagement and provides immediate feedback that the application is processing input.
Threading Support: The TTS function runs on a separate thread, ensuring that the application remains responsive during speech playback. Users can continue to input text or interact with the interface without delays.
Requirements:
Python: Ensure that you have Python installed on your machine.
Libraries: The application requires the tkinter and pyttsx3 libraries. Install pyttsx3 via pip if it’s not already installed.
Usage:
To use the application, simply run the provided script. Enter your desired text into the text box and click the "Speak" button. The application will read the text aloud while the microphone animation plays.

This TTS application is an excellent tool for anyone looking to convert text to speech easily while enjoying an interactive experience. It can be further enhanced with additional features such as voice selection, speed control, or saving the generated speech to an audio file.
