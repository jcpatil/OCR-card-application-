import cv2
import json
import time
from paddleocr import PaddleOCR
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import pyttsx3  # For Text-to-Speech

# Initialize PaddleOCR
ocr = PaddleOCR(use_angle_cls=True, lang='en')

# Initialize TTS engine
tts_engine = pyttsx3.init()
tts_engine.setProperty("rate", 150)  # Adjust speaking speed
tts_engine.setProperty("volume", 1.0)  # Set volume level

# JSON file to store OCR results
json_file_name = "id_card_data.json"

# Load existing data if the JSON file exists
output_data = []
try:
    with open(json_file_name, "r") as json_file:
        output_data = json.load(json_file)
except FileNotFoundError:
    print(f"{json_file_name} not found. Creating a new file.")

# Webcam setup
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise RuntimeError("Failed to initialize the camera. Please check your webcam connection.")

# Initialize the GUI
root = tk.Tk()
root.title("VMukti Card Application")
root.geometry("900x600")
root.configure(bg="#f7f9fc")  # Light background

# Variable to display OCR results
ocr_result = tk.StringVar()
ocr_result.set("OCR results will appear here...")

# Function to play "Thank You" sound using TTS
def play_thank_you():
    tts_engine.say("Thank you!")
    tts_engine.runAndWait()

# Function to capture an image, perform OCR, and save to JSON
def capture_image():
    global output_data

    # Capture a frame
    ret, frame = cap.read()
    if not ret:
        ocr_result.set("Failed to capture image.")
        return

    # Perform OCR
    result = ocr.ocr(frame, cls=True)
    if result and result[0]:
        detected_text = "\n".join([line[1][0] for line in result[0]])
        ocr_result.set(f"Detected Text:\n{detected_text}")

        # Save image and append data
        timestamp = int(time.time())
        image_filename = f"captured_{timestamp}.png"
        cv2.imwrite(image_filename, frame)
        output_data.append({"timestamp": timestamp, "image_file": image_filename, "text": detected_text})

        # Auto-save to JSON
        with open(json_file_name, "w") as json_file:
            json.dump(output_data, json_file, indent=4)

        # Play acknowledgment sound
        play_thank_you()
    else:
        ocr_result.set("No text detected in the image.")
        play_thank_you()

# Function to retake an image and replace data in JSON
def retake_photo():
    global output_data

    # Capture a new frame
    ret, frame = cap.read()
    if not ret:
        ocr_result.set("Failed to retake image.")
        return

    # Perform OCR
    result = ocr.ocr(frame, cls=True)
    if result and result[0]:
        detected_text = "\n".join([line[1][0] for line in result[0]])
        ocr_result.set(f"Detected Text:\n{detected_text}")

        # Save image and replace data in JSON
        timestamp = int(time.time())
        image_filename = f"retaken_{timestamp}.png"
        cv2.imwrite(image_filename, frame)

        # Update JSON with only the latest data
        output_data = [{"timestamp": timestamp, "image_file": image_filename, "text": detected_text}]
        with open(json_file_name, "w") as json_file:
            json.dump(output_data, json_file, indent=4)

        # Play acknowledgment sound
        play_thank_you()
    else:
        ocr_result.set("No text detected in the image.")
        play_thank_you()

# Function to update the live video feed
def update_video_feed():
    ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)

        # Resize video feed to fit the video label dynamically
        label_width = video_label.winfo_width()
        label_height = video_label.winfo_height()
        img = img.resize((label_width, label_height), Image.Resampling.LANCZOS)

        img_tk = ImageTk.PhotoImage(img)
        video_label.config(image=img_tk)
        video_label.image = img_tk

    video_label.after(10, update_video_feed)

# Function to toggle full-screen mode
def toggle_screen():
    is_fullscreen = root.attributes('-fullscreen')
    root.attributes('-fullscreen', not is_fullscreen)

# Function to close the application
def close_application():
    cap.release()
    cv2.destroyAllWindows()
    root.destroy()

# Header
header = tk.Label(root, text="VMukti Card Application", font=("Helvetica", 24, "bold"), bg="#4a90e2", fg="white", pady=10)
header.pack(fill="x")

# Main Frame
main_frame = tk.Frame(root, bg="#f7f9fc", padx=10, pady=10)
main_frame.pack(fill="both", expand=True)

# Video Feed Frame
video_label = tk.Label(main_frame, bg="#d3d3d3", relief="solid")
video_label.place(relx=0.05, rely=0.1, relwidth=0.6, relheight=0.8)

# OCR Result Frame
ocr_result_frame = tk.LabelFrame(main_frame, text="OCR Result", bg="#f7f9fc", padx=10, pady=10, font=("Helvetica", 12, "bold"))
ocr_result_frame.place(relx=0.7, rely=0.1, relwidth=0.25, relheight=0.8)

result_label = tk.Label(ocr_result_frame, textvariable=ocr_result, bg="#ffffff", fg="#000000", font=("Arial", 12), wraplength=300, justify="left", relief="solid")
result_label.pack(fill="both", expand=True, padx=5, pady=5)

# Control Buttons Frame
button_frame = tk.Frame(root, bg="#f7f9fc", pady=10)
button_frame.pack()

# Capture Button
capture_button = tk.Button(button_frame, text="Capture Image", command=capture_image, bg="green", fg="white", font=("Helvetica", 14), padx=20, pady=10)
capture_button.grid(row=0, column=0, padx=10)

# Retake Button
retake_button = tk.Button(button_frame, text="Retake Photo", command=retake_photo, bg="blue", fg="white", font=("Helvetica", 14), padx=20, pady=10)
retake_button.grid(row=0, column=1, padx=10)

# Quit Button
quit_button = tk.Button(button_frame, text="Quit", command=close_application, bg="red", fg="white", font=("Helvetica", 14), padx=20, pady=10)
quit_button.grid(row=0, column=2, padx=10)

# Toggle Screen Button
fullscreen_button = tk.Button(button_frame, text="Toggle Screen", command=toggle_screen, bg="blue", fg="white", font=("Helvetica", 14), padx=20, pady=10)
fullscreen_button.grid(row=0, column=3, padx=10)

# Footer
footer = tk.Label(root, text="Powered by PaddleOCR", font=("Helvetica", 10, "italic"), bg="#f7f9fc", fg="#888888")
footer.pack(side="bottom", pady=5)

# Start the video feed and main GUI loop
update_video_feed()
root.mainloop()

