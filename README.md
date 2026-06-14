# Diabetes Prediction using Artificial Neural Networks (ANN)

## Overview

This project implements a machine learning model using Artificial Neural Networks (ANN) to predict the likelihood of diabetes in patients. The model is trained on historical patient data and uses various health indicators to make accurate predictions.

## Project Description

Diabetes is a chronic disease affecting millions of people worldwide. Early detection and prediction can help in timely intervention and better disease management. This project leverages the power of deep learning with neural networks to build a predictive model that can assist healthcare professionals in identifying patients at risk of diabetes.

## Features

- **Data-Driven Approach**: Uses comprehensive patient health data for model training
- **Deep Learning Model**: Implements Artificial Neural Networks for accurate predictions
- **Easy-to-Use Interface**: Simple implementation for quick predictions
- **Model Evaluation**: Includes comprehensive metrics for model performance assessment
- **Jupyter Notebooks**: Interactive notebooks for exploration and understanding

## Repository Structure

```
DiabetesPredictionusing-ANN/
├── README.md
├── notebooks/              # Jupyter notebooks for analysis and modeling
│   └── *.ipynb            # Main analysis and model training notebooks
├── data/                  # Dataset files
├── models/                # Trained model files
└── src/                   # Python source code
```

## Technologies & Libraries

- **Python 3.x**
- **TensorFlow / Keras** - Deep learning framework
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computing
- **Scikit-learn** - Machine learning utilities
- **Matplotlib & Seaborn** - Data visualization
- **Jupyter Notebook** - Interactive development environment

## Dataset

The project uses a diabetes dataset containing various health metrics and indicators:

- Age
- Gender
- Blood Glucose Level
- Blood Pressure
- BMI (Body Mass Index)
- Insulin Level
- Diabetes Pedigree Function
- Pregnancies
- And other relevant health indicators

## Model Architecture

The ANN model consists of:

- **Input Layer**: Features from patient health data
- **Hidden Layers**: Multiple layers with activation functions (ReLU/Sigmoid)
- **Output Layer**: Binary classification (Diabetic / Non-Diabetic)
- **Optimization**: Adam optimizer with binary crossentropy loss function

## How to Use

### Prerequisites

```bash
pip install pandas numpy tensorflow keras scikit-learn matplotlib seaborn jupyter
```

### Running the Project

1. **Clone the repository**
   ```bash
   git clone https://github.com/adithyap15122005/DiabetesPredictionusing-ANN.git
   cd DiabetesPredictionusing-ANN
   ```

2. **Start Jupyter Notebook**
   ```bash
   jupyter notebook
   ```

3. **Open and run the notebooks**
   - Navigate to the notebook files and execute the cells sequentially
   - Follow the step-by-step analysis and model training process

4. **Make Predictions**
   - Use the trained model to predict diabetes risk for new patient data
   - Input patient health metrics and get predictions

## Results

- **Model Accuracy**: Evaluated on test dataset
- **Precision & Recall**: Metrics for model performance
- **ROC-AUC Score**: Measure of model's discriminative ability
- **Confusion Matrix**: Breakdown of correct and incorrect predictions

## Model Performance Metrics

The model is evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC Score
- Confusion Matrix

## Installation

```bash
# Clone the repository
git clone https://github.com/adithyap15122005/DiabetesPredictionusing-ANN.git

# Install dependencies
cd DiabetesPredictionusing-ANN
pip install -r requirements.txt
```

## Contributing

Contributions are welcome! Feel free to:

- Report bugs or issues
- Suggest improvements or new features
- Submit pull requests with enhancements
- Improve documentation

## Future Enhancements

- [ ] Web interface for easy predictions
- [ ] Real-time prediction API
- [ ] Additional features from medical datasets
- [ ] Model deployment to cloud platforms
- [ ] Comparison with other ML algorithms
- [ ] Mobile application integration

## License

This project is open source and available under the MIT License.

## Contact

For questions or inquiries about this project, please reach out to the repository owner:

- **GitHub**: [adithyap15122005](https://github.com/adithyap15122005)

## Disclaimer

This project is for educational and research purposes only. It is not intended to replace professional medical diagnosis. Always consult with healthcare professionals for actual medical decisions.

## References

- [TensorFlow Documentation](https://www.tensorflow.org/)
- [Scikit-learn Documentation](https://scikit-learn.org/)
- [Diabetes Prediction Research Papers](https://scholar.google.com/)

---

**Last Updated**: June 2026

Feel free to star ⭐ this repository if you find it helpful!
