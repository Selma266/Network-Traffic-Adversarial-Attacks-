# Network Traffic Adversarial Attacks
### 📌 Project Overview

Network Intrusion Detection Systems (NIDS) based on machine learning have shown strong performance in detecting malicious network traffic. However, these models remain vulnerable to adversarial attacks, where carefully crafted perturbations are applied to input features in order to evade detection.

In this project, we investigate adversarial evasion attacks on Machine Learning-based Intrusion Detection Systems (ML-IDS). Specifically, we use:

--- FGSM (Fast Gradient Sign Method)
--- PGD (Projected Gradient Descent)

These attacks are typically designed for differentiable models (deep learning), but in this work they are extended to both Machine Learning (ML) and Deep Learning (DL) models applied to tabular network traffic data.

We focus on realistic attack scenarios, including: Black-box evasion attacks and Transfer-based attacks.


To further enforce realistic adversarial conditions, we integrate the TCGE (Tabular Constraint Guaranteed Evasion) algorithm. TCGE is specifically designed for tabular and constrained domains, ensuring that generated adversarial examples remain valid and realistic by respecting domain constraints (e.g., feature dependencies and logical relationships)

### 📌Models Implemented
Machine Learning Models: Logistic Regression, Random Forest, XGBoost, LightGBM.

Deep Learning Model: Multilayer Perceptron (MLP).

### 📌 Defense Mechanism
To improve robustness against adversarial attacks, we apply Adversarial Training.

### 📚 Reference
- The dataset used in this project is available at:
- Paper: Alhussien, N., Agrawal, G., & Al-Eroud, A. (2025). "Augmented Tabular Adversarial Evasion Attacks with Constraint Satisfaction Guarantees" International  Conference on Availability, Reliability and Security (ARES).
- Official implementation of the CGE/TCGE framework: [TCGE GitHub Repository](https://github.com/aucad/cge) 

