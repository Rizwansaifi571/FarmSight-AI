
# 🌾 **FarmSigh-AI** 🌾

**FarmSigh-AI** is an advanced AI-based agricultural crop production prediction and analysis system designed to provide insights from historical crop production data. With a robust data pipeline and machine learning models, **FarmSigh-AI** helps predict crop yields and make data-driven decisions for agricultural planning. This project leverages data science and machine learning techniques for optimizing agricultural productivity.

### 📊 **Sample Data Overview:**
The dataset contains crop production data across different states and districts in India. Here's a glimpse of the data structure:

| State            | District       | Crop            | Crop_Year | Season     | Area   | Production | Yield |
|------------------|----------------|-----------------|-----------|------------|--------|------------|-------|
| Jharkhand        | RAMGARH        | Potato          | 2013      | Winter     | 1361.0 | 7544.0     | 5.54  |
| Jammu and Kashmir| REASI          | Moong (Green Gram) | 2015    | Kharif     | 13.0   | 9.0        | 0.7   |
| Haryana          | GURGAON        | Sweet Potato    | 2009      | Whole Year | 39.0   | 800.0      | 20.51 |
| Uttar Pradesh    | JALAUN         | Sannhamp        | 2010      | Kharif     | 9.0    | 3.0        | 0.33  |
| Tamil Nadu       | MADURAI        | Sugarcane       | 2006      | Whole Year | 6006.0 | 656204.0   | 109.26|
| ...              | ...            | ...             | ...       | ...        | ...    | ...        | ...   |

---

### 🚀 **Project Steps:**

1. **Setup the Environment**  
   - Created the `setup.py` for environment setup and dependency management.

2. **Template Structure**  
   - Built a basic `template.py` to handle the overall project logic and structure.

3. **Logging and Custom Exception Handling**  
   - Implemented a custom logging and exception handling system for better error tracking and debugging.

4. **Data Ingestion**  
   - Moved the data to a SQL database for efficient management and performed data ingestion for analysis.

5. **Data Transformation & Preprocessing**  
   - Processed the raw data and saved the transformed preprocessing pipeline in a `.pkl` file (`preprocessor.pkl`).

6. **Exploratory Data Analysis (EDA) & Model Training**  
   - Conducted EDA to understand trends, relationships, and outliers in the data.
   - Trained machine learning models for predicting crop yield based on historical data using Jupyter Notebooks.

7. **Prediction Pipeline**  
   - Created a prediction pipeline to generate real-time yield predictions based on input crop data.

8. **Web Application**  
   - Developed a web app using Flask to deploy the machine learning model and prediction pipeline for user interactions.

---

### 🌱 **Features**:

- **Data Visualization**: Detailed EDA charts to understand crop yield trends.
- **Prediction**: Predict crop yield for given states, districts, and crops.
- **Web Interface**: Easy-to-use web interface for making predictions.
- **Custom Logging**: Keep track of errors and logs for efficient debugging.

---

### 🧑‍💻 **Technologies Used**:

- **Python**  
- **Flask** for Web Development  
- **pandas**, **numpy**, **matplotlib**, **seaborn** for Data Science  
- **scikit-learn** for Machine Learning  
- **SQL** for Data Management  
- **Pickle** for saving preprocessor model

---

### ⚡ **How to Use**:

1. Clone the repository:
   ```bash
   git clone https://github.com/Rizwansaifi571/FarmSigh-AI
   ```
2. Navigate to the project directory:
   ```bash
   cd FarmSigh-AI
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Flask app:
   ```bash
   python app.py
   ```
   The app will be available at `http://localhost:5000`.

---

### 📂 **Folder Structure**:

```bash
FarmSigh-AI/
│
├── app.py               # Main entry point for the web app
├── setup.py             # Setup script for environment
├── template.py          # Template structure for project logic
├── data/
│   ├── raw_data.csv     # Sample data file
│   └── transformed_data/ # Transformed data for analysis
├── notebooks/
│   └── model_training.ipynb  # Jupyter notebook for EDA & model training
├── logs/                # Logs and exceptions
└── models/
    ├── preprocessor.pkl  # Preprocessing model
    └── trained_model.pkl # Trained machine learning model
```

---

### 📈 **Future Improvements**:

- Integrating more data sources for better accuracy.
- Add an option for users to upload their crop data for predictions.
- Implement additional machine learning models for yield prediction comparison.

---

### 📞 **Contact**:

For any queries or contributions, feel free to reach out!  
**GitHub**: [Rizwansaifi571](https://github.com/Rizwansaifi571)  
**Email**: rizwansaifi2614@gmail.com

---

🌾 **FarmSigh-AI** is the future of smart farming, empowering farmers to make data-driven decisions for higher yields! 🌾

--- 
