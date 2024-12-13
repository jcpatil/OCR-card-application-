# OCR-card-application-
Perfect for automating text extraction tasks and enhancing document digitization workflows.


# OCR Card Application

This is a Python-based graphical user interface (GUI) application for Optical Character Recognition (OCR) using PaddleOCR. The application can capture images from a webcam, extract text from the images, and save the results in JSON format along with the captured image. It also includes functionality to retake photos, perform live video feed updates, and interact using Text-to-Speech (TTS) for acknowledgment.

---

## Repository Name

**VMukti-OCR-Card-Application**

---

## Features

1. **Real-Time OCR:** Captures images from a webcam and extracts text using PaddleOCR.
2. **Text-to-Speech (TTS):** Provides audio feedback after capturing an image.
3. **JSON Storage:** Saves extracted text and image data in a JSON file for future use.
4. **Interactive GUI:** Built using `tkinter` for an intuitive user interface.
5. **Live Video Feed:** Displays a live video feed from the webcam.
6. **Full-Screen Toggle:** Allows toggling between full-screen and windowed mode.

---

## Prerequisites

Before running the application, ensure you have the following installed on your system:

1. **Python 3.7 or higher**
2. Required Python libraries (install using the command below):

```bash
pip install paddleocr==2.6.0.1 opencv-python-headless pillow pyttsx3
```

---

## How to Run

1. Clone the repository to your local system:

```bash
git clone <repository_url>
cd VMukti-OCR-Card-Application
```

2. Run the application:

```bash
python <script_name>.py
```

3. Once the application starts, the GUI will open, and you can:
   - View the live video feed.
   - Click "Capture Image" to capture an image, perform OCR, and save the results.
   - Click "Retake Photo" to overwrite the previously captured data with a new image and OCR results.
   - View extracted text in the "OCR Result" section.

4. Exit the application by clicking the "Quit" button.

---

## Files

- **`<script_name>.py`**: Main Python script.
- **`id_card_data.json`**: JSON file storing captured data (created automatically if it doesn't exist).

---

## How to Use

1. **Live Video Feed:** The application displays a live feed from your webcam.
2. **Capture an Image:**
   - Press "Capture Image" to take a snapshot and extract text.
   - The OCR results will be displayed in the "OCR Result" section.
3. **Retake Photo:** Press "Retake Photo" to replace the last captured image and text in the JSON file.
4. **Full-Screen Mode:** Press "Toggle Screen" to switch between full-screen and windowed mode.

---

## Additional Notes

- Ensure your webcam is properly connected and functional.
- The extracted text and associated image data are saved in `id_card_data.json`. You can view or modify this file as needed.
- This application uses PaddleOCR for text extraction, which supports multiple languages. Modify the `lang` parameter in the script to use other languages if necessary.

---

## Contributing

Feel free to fork the repository, make changes, and create a pull request. Suggestions and contributions are always welcome.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Acknowledgments

- [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR): For the OCR engine.
- [OpenCV](https://opencv.org/): For video capture.
- [tkinter](https://docs.python.org/3/library/tkinter.html): For GUI development.
- [pyttsx3](https://pyttsx3.readthedocs.io/): For Text-to-Speech functionality.
