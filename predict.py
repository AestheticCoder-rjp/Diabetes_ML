import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def make_predictions(data):
    st.title("Predictions")

    x = data.iloc[:,:8].values
    y = data.iloc[:,8].values
    x_tr, x_tt, y_tr, y_tt = train_test_split(x, y, test_size=0.2, random_state=0)
    model = RandomForestClassifier(n_estimators=500)
    model.fit(x_tr, y_tr)
    yp = model.predict(x_tt)
    acc = accuracy_score(yp, y_tt)
    st.success(f"Accuracy: {acc*100:.2f}%")

    st.markdown("### Please Enter your results here to check whether you are having diabetes or not.")
    name = st.text_input("Enter Your Name")
    
    st.write("Enter Your Details:")
    age = st.slider("Age", 0, 120, 0)
    preg = st.slider("Pregnancies", 0, 20, 0)
    glu = st.slider("Glucose", 0, 200, 0)
    bp = st.slider("Blood Pressure", 0, 130, 0)
    sthick = st.slider("Skin Thickness", 0, 100, 0)
    insulin = st.slider("Insulin", 0, 1000, 0)
    bmi = st.slider("BMI", 0.0, 70.0, 0.0)
    dpf = st.slider("Diabetes Pedigree Function", 0.0, 5.0, 0.0)
    
    input_data = [[preg, glu, bp, sthick, insulin, bmi, dpf, age]]
    if st.button("Predict"):
        prediction = model.predict(input_data)
        if prediction[0] == 0:
            st.success(f"{name}, You don't have Diabetes")
        else:
            st.error(f"{name}, You have Diabetes")