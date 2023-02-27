## Folder Structure

spam_detection_flask
 ┣ webapp                      # the folder containing frontend design and supporting flies
 ┃ ┣ model_webapp_dir          # the folder keeps the model file
 ┃ ┃ ┗ model.joblib 
 ┃ ┣ static                    # it usually keeps css, js, images files  
 ┃ ┃ ┣ css
 ┃ ┃ ┃ ┗ main.css
 ┃ ┃ ┗ sctipt
 ┃ ┃ ┃ ┗ index.js
 ┃ ┗ templates                # it usually has html files 
 ┃ ┃ ┣ 404.html
 ┃ ┃ ┣ base.html
 ┃ ┃ ┗ index.html
 ┗ app.py                      # the main backend logic