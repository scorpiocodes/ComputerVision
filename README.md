# Computer Vision Projects

This repository encompasses three distinct computer vision projects, each demonstrating various techniques and applications in the field:

1. **Face Detection**
2. **Facial Emotion Recognition**
3. **MNIST Digit Classification with PyTorch**

## 1. Face Detection

The Face Detection project focuses on identifying human faces within images. It employs the Haar Cascade Classifier from the OpenCV library, a widely used method for object detection.

### Features

- Detects faces in static images.
- Utilizes pre-trained Haar Cascade models for face detection.

### Requirements

- Python 3.x
- OpenCV

### Usage

1. Navigate to the `Face Detection` directory.
2. Run the script:

   ```bash
   python face_detection.py
   ```

3. The script will process the input image and display it with detected faces highlighted.

## 2. Facial Emotion Recognition

This project aims to recognize human emotions from facial expressions in images. It leverages deep learning models trained on labeled datasets to classify emotions such as happiness, sadness, anger, and surprise.

### Features

- Classifies emotions from facial expressions.
- Employs convolutional neural networks (CNNs) for image classification.

### Requirements

- Python 3.x
- TensorFlow or PyTorch
- OpenCV

### Usage

1. Navigate to the `Facial Emotions` directory.
2. Ensure the pre-trained model is available or train the model using the provided dataset.
3. Run the script:

   ```bash
   python emotion_recognition.py
   ```

4. The script will analyze the input image and output the detected emotion.

## 3. MNIST Digit Classification with PyTorch

This project involves building a neural network to classify handwritten digits from the MNIST dataset using PyTorch. The MNIST dataset is a benchmark in machine learning for image processing tasks.

### Features

- Trains a neural network to classify digits (0-9).
- Evaluates model performance on test data.

### Requirements

- Python 3.x
- PyTorch
- Torchvision

### Usage

1. Navigate to the `MNIST PyTorch` directory.
2. Run the training script:

   ```bash
   python train.py
   ```

3. After training, evaluate the model:

   ```bash
   python evaluate.py
   ```

4. The scripts will display the model's accuracy and other performance metrics.

---

*Note: Ensure you have Python 3.x installed on your machine before setting up the projects.* 
