import webScraper
import tkinter as tk
from tkinter import filedialog, Text
import os

def main():
    root = tk.Tk()

    canvas = tk.Canvas(root, height=700, width=700, bg="#21312D")
    canvas.pack()
    
    frame=tk.Frame(root, bg="white")
    frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="#21312D")
    openFile.pack()

    runApps = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="#21312D")
    runApps.pack()

    root.mainloop()


if __name__ == "__main__":
    main()