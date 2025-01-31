import joblib
import numpy as np
import pandas as pd
import streamlit as st


model = joblib.load('gbr_pred_salary_dev_v2.joblib')
onehot_encoder = joblib.load('onehot_encoder.joblib')

st.title('Salary 💵 Prediction in 2022 With GBR Model')
st.write("""### We need some information to predict the salary""")


countries = [
    "United States of America", "Iran, Islamic Republic of...", "India",
    "United Kingdom of Great Britain and Northern Ireland", "Germany",
    "Canada", "Brazil", "France", "Spain", "Australia", "Netherlands",
    "Poland", "Italy", "Russian Federation", "Sweden", "Switzerland",
    "Israel", "Austria", "Portugal", "Denmark", "Turkey", "Belgium",
    "Norway", "Finland", "Greece", "Czech Republic", "New Zealand",
    "Mexico", "South Africa", "Pakistan"
]

education_levels = [
    "Less than a Bachelors", "Bachelor’s degree", "Master’s degree"
]


country = st.selectbox("Country", countries)
education = st.selectbox("Education Level", education_levels)
expericence = st.slider("Years of Experience", 0, 50, 3)


X_new = pd.DataFrame([[country, education, expericence]], columns=["Country", "EdLevel", "YearsCodePro"])
X_new_encoded = onehot_encoder.transform(X_new[["Country", "EdLevel"]]).toarray()


X_final = np.hstack([X_new_encoded, np.array([[expericence]])])


if st.button("Calculate Salary"):
    salary = model.predict(X_final)
    st.subheader(f"The estimated salary is ${salary[0]:.2f} 🤑")
