# 🌧️ Rainfall Prediction System

This project is a machine learning-based **Rainfall Prediction System** developed using a **Random Forest Classifier**. It predicts whether rainfall will occur based on key meteorological features such as pressure, dew point, humidity, cloud cover, sunshine, wind direction, and wind speed.



## 📌 Objective

To build a classification model that predicts **Rain** or **No Rain** using historical weather data.



## 🧪 Features Used

| Feature         | Description                      |
|----------------|----------------------------------|
| `pressure`      | Atmospheric pressure (hPa)       |
| `dewpoint`      | Dew point temperature (°C)       |
| `humidity`      | Relative humidity (%)            |
| `cloud`         | Cloud cover level (in %)         |
| `sunshine`      | Sunshine duration (hours)        |
| `winddirection` | Wind direction (degrees)         |
| `windspeed`     | Wind speed (km/h)                |

> 🔸 The feature `day` was excluded as it is not relevant to the classification task.



## ⚙️ Technologies Used

- **Python**
- **Jupyter Notebook**
- **Pandas, NumPy**
- **Matplotlib, Seaborn**
- **Scikit-learn (RandomForestClassifier, GridSearchCV)**
- **Pickle** for model serialization



## 🧹 Data Preprocessing

- Cleaned column names
- Dropped highly correlated features (maxtemp, temperature, mintemp) to prevent multicollinearity
- Removed irrelevant features (like day)
- Downsampled the majority class using sklearn.utils.resample() to balance the dataset
- Applied train-test split
- Tuned hyperparameters using **GridSearchCV**



## 🎯 Model Details

- **Model:** Random Forest Classifier
- **Training:** Trained on weather data to classify rainfall (1) or no rainfall (0)
- **Evaluation Metrics:** Accuracy, Confusion Matrix, Classification Report
- **Model Exported:** Final model saved as `rainfall_model.pkl`



## 📥 Sample Inputs

### `sample_input1.txt` ✅ (Expected: Rainfall)
### `sample_input2.txt` ✅ (Expected: No Rainfall)

## Clone this repository:

git clone https://github.com/Ushosipal/rainfall_prediction.git
cd rainfall-prediction-system


1015.9, 19.9, 95, 81, 0.0, 40.0, 13.7

