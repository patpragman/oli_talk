import argparse
import tkinter as tk
import pyttsx3


def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def speak():
    text = text_area.get("1.0", tk.END)
    speak_text(text)


def on_entry_click(event):
    if text_area.get("1.0", tk.END).strip() == "Enter text here":
        text_area.delete("1.0", tk.END)
        text_area.insert("1.0", '')
        text_area.config(fg='black')


def on_focusout(event):
    if text_area.get("1.0", tk.END).strip() == '':
        text_area.insert("1.0", 'Enter text here')
        text_area.config(fg='grey')


def launch_gui():
    root = tk.Tk()
    root.title("Text-to-Speech")

    global text_area
    text_area = tk.Text(root, height=10, width=30, wrap=tk.WORD, fg='grey')
    text_area.insert("1.0", "Enter text here")
    text_area.bind("<FocusIn>", on_entry_click)
    text_area.bind("<FocusOut>", on_focusout)
    text_area.pack()

    speak_button = tk.Button(root, text="Talk", command=speak)
    speak_button.pack()

    root.mainloop()


def main():
    parser = argparse.ArgumentParser(description="Text-to-Speech application.")
    parser.add_argument("-gui", action="store_true", help="Launch the GUI version of the app.")
    parser.add_argument("-say", type=str, help="Text to speak in command line mode.")
    args = parser.parse_args()

    if args.gui:
        launch_gui()
    elif args.say:
        speak_text(args.say)


if __name__ == "__main__":
    main()
