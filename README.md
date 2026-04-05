# 🚗 Autonomous Vehicle Brake Control System (Fuzzy Logic)

<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Fuzzy%20Logic-8A2BE2?style=for-the-badge&logo=magic&logoColor=white" alt="Fuzzy Logic" />
</p>

## 📌 About the Project
This repository contains an application study demonstrating an **Autonomous Vehicle Brake Control System** powered by Fuzzy Logic. The system evaluates real-time environmental factors to determine the optimal braking pressure, ensuring safety and ride comfort.

This project was developed to model human-like decision-making processes in autonomous driving scenarios using mathematical fuzzy sets and rules, moving away from rigid binary constraints.

## ⚙️ Features
* **Mamdani Fuzzy Inference System:** Implements logical rules to mimic human driving intuition.
* **Input Variables:** Evaluates dynamic environmental inputs such as `Speed` (Hız) and `Distance` (Mesafe).
* **Output Variable:** Calculates the precise and safe `Brake Pressure` (Fren Basıncı).
* **Visualization:** Graphical representations of membership functions and the defuzzification process.

---

## 📈 Visualizations

Here are the fuzzy set representations for our system's inputs and outputs:

### 1. Speed (Hız) Input
<img width="640" height="480" alt="hiz" src="https://github.com/user-attachments/assets/8a5e75d2-5e29-4f57-9123-c017d557ba6b" />


### 2. Distance (Mesafe) Input
<img width="640" height="480" alt="mesafe" src="https://github.com/user-attachments/assets/6d9c0fa3-1f89-40be-a352-e4595527e83a" />

### 3. Brake Pressure (Fren Basıncı) Output
<img width="640" height="480" alt="fren" src="https://github.com/user-attachments/assets/2eee9542-9f9c-4635-8307-38bca4294558" />

---

## 🛠️ Technologies & Libraries
* **Python 3.x**
* **NumPy & SciPy:** For numerical operations, mathematical modeling, and scientific computing.
* **NetworkX:** For structural analysis and modeling.
* **Matplotlib:** For visualizing the fuzzy sets and output graphs.

## 🚀 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/OmerFarukAY/fuzzyLogicProject.git](https://github.com/OmerFarukAY/fuzzyLogicProject.git)
   cd fuzzyLogicProject

2. **Install the required dependencies:**
   ```bash
   pip install scipy networkx matplotlib numpy scikit-fuzzy

3. **Run the application:**
   ```bash
   python otonomFrenleme.py
   
