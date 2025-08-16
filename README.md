# 🌲 Forest Cover Type Prediction using Random Forest

This project predicts **forest cover type** based on cartographic variables such as elevation, slope, aspect, hydrology distances, and hillshade values.  
The model is built using **Random Forest Classifier**, evaluated with multiple metrics, and deployed as an interactive **Streamlit web application**.

---

## 📌 Project Overview

1. **Data Preprocessing**
   - Loaded and explored the **Forest Cover Type dataset**.
   - Handled features like:
     - Elevation
     - Aspect
     - Slope
     - Horizontal & Vertical Distance to Hydrology
     - Horizontal Distance to Roadways
     - Hillshade (9am, Noon, 3pm)
   - Target variable: **Cover_Type** (7 different forest types).

2. **Model Building**
   - Used **Random Forest Classifier** from scikit-learn.
   - Trained the model on preprocessed dataset.
   - Evaluated with:
     - Accuracy
     - Confusion Matrix
     - Classification Report
     - Visual comparison of predictions vs. actual values.

3. **Visualization**
   - Plotted a **confusion matrix heatmap**.
   - Plotted side-by-side **prediction vs actual cover type comparison**.

4. **Deployment**
   - Exported the trained Random Forest model with **pickle**.
   - Built a **Streamlit app** where:
     - Users input environmental features.
     - The app predicts the **forest type**.
     - Shows a **real-life image of the predicted forest type** for better visualization.

---

## 🎥 Video Demonstration

👉 [Click here to watch the video demo](https://drive.google.com/file/d/1FpZhtV8xSPw30c5ID_uyEC1RQ-qZRLal/view?usp=sharing)  

*(Replace `YOUR_VIDEO_LINK_HERE` with your YouTube / Google Drive / GitHub link to the video.)*

---

## 📊 Results

- Achieved strong prediction performance with Random Forest.
- Model generalized well on unseen test data.
- Interactive web app provides both predictions and a visual forest type representation.
