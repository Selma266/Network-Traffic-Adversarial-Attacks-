# Network Traffic Adversarial Attacks
### 📌 Project Overview

Network Intrusion Detection Systems (NIDS) based on machine learning have shown strong performance in detecting malicious network traffic. However, these models remain vulnerable to adversarial attacks, where carefully crafted perturbations are applied to input features in order to evade detection.

In this project, we investigate adversarial evasion attacks on Machine Learning-based Intrusion Detection Systems (ML-IDS). Specifically, we use:  FGSM (Fast Gradient Sign Method) and PGD (Projected Gradient Descent)

These attacks are typically designed for differentiable models (deep learning), but in this work they are extended to both Machine Learning (ML) and Deep Learning (DL) models applied to tabular network traffic data.

We focus on realistic attack scenarios, including: Black-box evasion attacks and Transfer-based attacks.


To further enforce realistic adversarial conditions, we integrate the** TCGE (Tabular Constraint Guaranteed Evasion) algorithm **. TCGE is specifically designed for tabular and constrained domains, ensuring that generated adversarial examples remain valid and realistic by respecting domain constraints (e.g., feature dependencies and logical relationships)

### 📌Models Implemented
Machine Learning Models: Logistic Regression, Random Forest, XGBoost, LightGBM.

Deep Learning Model: Multilayer Perceptron (MLP).

### 📌 Defense Mechanism
To improve robustness against adversarial attacks, we apply Adversarial Training.

### 📊 Experimental Scenarios
To comprehensively evaluate the robustness of the proposed models, we design five experimental scenarios, each reflecting a different security setting:

🔹 S1: Baseline Performance

In this scenario, models are trained and tested on clean (non-adversarial) network traffic data. This serves as a reference to compare the performance of different models under normal conditions.

🔹 S2: Adversarial Attack Evaluation

Here, trained models are directly exposed to adversarial examples generated using: FGSM and PGD. This scenario evaluates the vulnerability of each model to adversarial evasion attacks.

🔹 S3: Adversarial Training on Seen Attacks

Models are trained and tested on the same type of adversarial attack: 

Train on FGSM → Test on FGSM
Train on PGD → Test on PGD

This scenario measures how well models can defend against attacks they have already seen during training.

🔹 S4: Cross-Attack Generalization

Models are trained on one type of attack and tested on another:

Train on FGSM → Test on PGD
Train on PGD → Test on FGSM

This evaluates the model’s ability to generalize defenses across different attack types.

🔹 S5: Mixed Adversarial Training

Models are trained on a combination of clean and adversarial data (FGSM + PGD), and then evaluated on clean test data.

This scenario assesses whether adversarial training improves robustness without degrading performance on normal traffic.

### These scenarios are designed to simulate realistic deployment conditions and evaluate both robustness and generalization capabilities of ML-IDS models.

### 📚 Reference
- The dataset used in this project is available at:
- Paper: Alhussien, N., Agrawal, G., & Al-Eroud, A. (2025). "Augmented Tabular Adversarial Evasion Attacks with Constraint Satisfaction Guarantees" International  Conference on Availability, Reliability and Security (ARES).
- Official implementation of the CGE/TCGE framework: [TCGE GitHub Repository](https://github.com/aucad/cge) 

