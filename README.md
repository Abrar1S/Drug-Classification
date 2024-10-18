### This is a machine learning model deployment project using Flask and Docker. 
---

1. The purpose is to find the appropriate drug for a patient. The dataset can be found on Kaggle. To perform drug classification, age, sex, blood pressure, cholesterol, and sodium-to-potassium ratios have been considered as features. After taking the features, the random forest classifier algorithm is performed, and the achieved accuracy is 98%. 

2. Data and model versioning are key to deployment. By using the DVC tool, data and model versioning have been performed.

3. After that, the flask app shows the features as input and gives the predicted drug as output.
![drug_classification_app](https://github.com/user-attachments/assets/51357aae-434a-41a9-9125-021aa8ba89d1)


5. Finally, the whole project is being docarized and the docker container exists on the docker hub.

