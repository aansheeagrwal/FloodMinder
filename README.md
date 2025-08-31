# 🌊 FloodMinder

![FloodMinder Banner](assets/banner.png)

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-1.1-orange?logo=flask&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Build](https://img.shields.io/badge/Build-Passing-brightgreen)

**FloodMinder** is a web application that uses Machine Learning to predict floods based on weather data and historical disaster records. It aims to provide real-time insights and visualizations to help communities prepare and respond effectively.

---

## **🌐 Live Demo**
Currently under deployment. Link will be updated soon.

---
## ** Screenshots/Images
<img width="936" height="442" alt="contact page" src="https://github.com/user-attachments/assets/bf94697f-77b1-42d9-ae7f-b81ba47d5127" />

<img width="929" height="431" alt="Front page" src="https://github.com/user-attachments/assets/a4d78476-ec62-4857-bd1e-69fac4502730" />

<img width="941" height="426" alt="interactive heatmap anlysis image" src="https://github.com/user-attachments/assets/fe5a4cfa-101e-4679-b497-25249bc5c4fc" />

<img width="934" height="399" alt="Flood Prediction image" src="https://github.com/user-attachments/assets/14481584-fbff-4cb5-a548-847a63d84950" />

<img width="944" height="444" alt="plot damage analysis image" src="https://github.com/user-attachments/assets/6a6109d6-a209-4e09-a59d-92896b525378" />

<img width="936" height="428" alt="Flood image final" src="https://github.com/user-attachments/assets/057b429f-f7d7-4009-95c4-f56d84929b0b" />

<img width="944" height="433" alt="Plots page" src="https://github.com/user-attachments/assets/1f62c0d2-83b6-4014-99d9-2b214c13523e" />



<img width="950" height="440" alt="cover page" src="https://github.com/user-attachments/assets/360a34ba-1e10-4161-aa08-8a08f204168d" />

---

## **🌐 Demo Video**


https://github.com/user-attachments/assets/8f58a072-3ab8-4016-a7af-7eacea1b0d88


---

## **Features**

### 1. Flood Prediction
- Predict potential floods based on weather and historical data.
- Real-time predictions using ML models.
- Visual display of flood probability.

### 2. Earthquake Prediction
- Input seismic parameters to get earthquake likelihood.
- Instant results with probability scoring.

### 3. Hurricane Prediction
- Predict hurricane occurrence based on wind, pressure, and sea surface temperature.
- Shows prediction along with impact indicators.

### 4. Interactive Visualizations
- Bubble plots for flood probability, rainfall, and damage predictions.
- Heatmaps to analyze regions with high flood risk.
- Satellite imagery for precipitation patterns over time.

### 5. User-friendly Interface
- Simple forms to input environmental parameters.
- Results shown instantly in an easy-to-read format.
- Designed using Flask with responsive HTML templates.

---

## **Getting Started**

### Clone the repository
```bash
git clone https://github.com/<USERNAME>/FloodMinder.git
cd FloodMinder
```
---
### Setup virtual environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

```
### Install dependencies
```bash
pip install -r requirements.txt
```
### Run the app
```bash
python app.py
```
### Open your browser and go to:
```cpp
http://127.0.0.1:5000/
```
---
### 💡 Inspiration
Floods are frequent and devastating. In India alone, over 80% of the population (~1.08B) is at risk, causing billions of USD in economic losses annually. FloodMinder predicts floods in advance and visualizes potential impact effectively.

---
### 🛠 How We Built It
- Dataset: Scraped historical flood data + Visual Crossing weather API.

- ML Models: Random Forest, Logistic Regression, KNN tested; Random Forest chosen.

- Data Visualization: Scatter plots, heatmaps, bubble plots (Plotly), satellite images (matplotlib + cartopy).

- Front-End: Flask templates with HTML, CSS & JS integration.

---
### ⚡ Challenges
- Limited historical flood data

- Integrating interactive plots with Flask

- Managing dataset & pickle file inconsistencies
---
### 🏆 Accomplishments
- High-performing flood prediction model

- Interactive visualizations for flood impact & risk

- Learned web scraping, data preprocessing, and Plotly integration
---
### 🔮 Next Steps
- Expand coverage to cities worldwide.

- Develop an image classification model for flood detection from satellite imagery.

- Make predictions and visualizations more accessible for governments and citizens to enhance disaster preparedness.
---
### 🤝 Contributing
Contributions are welcome! 🎉

1. Fork the repo
2. Create a new branch (feature-xyz)
3. Commit changes
4. Open a Pull Request
---
### 📜 License

This project is licensed under the MIT License – see the LICENSE file for details.

---
### ⭐ Support
If you like this project, don’t forget to star the repo ⭐
It keeps me motivated to build more!

<p align="center">Made with ❤️ by <a href="https://github.com/aansheeagrwal">Anshi Goyal</a></p> ```


