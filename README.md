# IoT Intrusion Detection using CNN-LSTM

## 📌 Overview
This project presents an improved intrusion detection system for IoT networks using deep learning. The proposed model enhances a baseline CNN approach by integrating LSTM layers, enabling the system to capture both spatial and temporal features of network traffic.

The system is designed to detect multiple types of cyber-attacks in IoT environments, improving both accuracy and real-world applicability.

---

## 🚀 Key Improvements
Compared to the baseline model, the following improvements were implemented:

- ✅ Dataset integration (multiple CSV files combined)
- ✅ Multi-class classification (Benign, DDoS, DoS, Recon)
- ✅ CNN-LSTM hybrid model (spatial + temporal learning)
- ✅ Data preprocessing and normalization
- ✅ Real-time prediction simulation

---

## 🧠 Model Architecture
The model consists of:

- 1D Convolutional layers (feature extraction)
- MaxPooling layers
- LSTM layer (temporal dependency learning)
- Fully connected (Dense) layers
- Softmax output layer

---

## 📊 Results
The proposed model achieved:

- **Accuracy:** ~97%
- **Precision:** ~97%
- **Recall:** ~97%
- **F1-Score:** ~96%

### Key Observations:
- Excellent performance on **DDoS** and **DoS** attacks
- Slightly lower performance on **Recon** class (due to similarity with normal traffic)

---

## 📈 Visualizations
The project includes:

- Accuracy comparison (CNN vs CNN-LSTM)
- Confusion Matrix
- Training & Validation Accuracy Graph

---

## 📂 Project Structure
├── src/
│ ├── main.py
│ ├── model.py
│ ├── data_loader.py
│ ├── combine.py
│
├── requirements.txt
├── README.md
├── .gitignore


---

## 📥 Dataset

Due to size limitations, the dataset is not included in this repository.

📎 Download it from:
👉 **[Paste Your Google Drive Link Here]**

After downloading:
1. Extract the ZIP file
2. Place the `data/` folder in the project root directory
project-folder/
│
├── data/
├── src/


---

## ⚙️ Installation

Install required dependencies:

```bash
pip install -r requirements.txt


Class Config Options:
2 → Binary classification
6 → Multi-class (recommended)
19 → Fine-grained classification


🧪 Technologies Used
Python
TensorFlow / Keras
Scikit-learn
Pandas / NumPy
📄 Research Contribution

This work is based on and improves upon:

"Securing Healthcare with Deep Learning: A CNN-Based Model for Medical IoT Threat Detection"
📍 19th Iranian Conference on Intelligent Systems (ICIS), 2024, pp. 168–173

Enhancements include:

Addition of LSTM layer
Multi-class classification
Improved preprocessing pipeline
🔮 Future Work
Improve detection of minority classes (e.g., Recon)
Apply class balancing techniques (SMOTE)
Explore attention mechanisms and transformers
Real-time deployment in live network environments
Advanced hyperparameter tuning
👥 Authors
Mohammad Tariq Ikhlas
Pohanyar Khowaja Khil
Malak Muhammad Mueed

SEECS, NUST, Pakistan
