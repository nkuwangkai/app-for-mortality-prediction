import pandas as pd
import numpy as np
import xgboost
from xgboost.sklearn import XGBClassifier
import streamlit as st

df = pd.read_csv("https://raw.githubusercontent.com/nkuwangkai/app-for-mortality-prediction/main/data4.csv",thousands=',')
X = df[["label", "Race", "Norepinephrine","Dopamine", "Phenylephrine", "Vasopressin","Vent", "Intubated", "MC","HepF"]]
X = X.replace(["Yes", "No"], [1, 0])
X = X.replace(["white", "black","others"], [1,2,3])						
Y = df[["label"]]
Y = Y.replace(["death", "live"], [1, 0])	


clf = XGBClassifier(objective='binary:logistic',
              booster='gbtree',
              colsample_bytree=0.558759,
              gamma=0.1477409,
              learning_rate=0.08694605,
              max_delta_step=8,
              max_depth=3,
              min_child_weight=37,
              n_estimators=92,
              subsample=0.6428299)

clf.fit(X,Y)

# Title
st.header("Machine learning app for in-hospital mortality prediction")

Age = st.number_input("Age (years)") 
Temperature = st.number_input("Temperature (℃)")
RespiratoryRate = st.number_input("RespiratoryRate (breaths per minute)")
HeartRate = st.number_input("HeartRate (beats per minute)")
SBP = st.number_input("SBP (mmHg)")
AG = st.number_input("AG")
BUN = st.number_input("BUN (mg/dL)")
MCHC = st.number_input("MCHC (g/L)")
MCV = st.number_input("MCV (fL)")
RDW = st.number_input("RDW")
WBC = st.number_input("WBC (×109/L)")

Race = st.selectbox("Race (white=1,black=2,others=3)", ("1", "2","3"))
Norepinephrine = st.selectbox("Norepinephrine (No=0,Yes=1)", ("0","1"))
Dopamine = st.selectbox("Dopamine (No=0,Yes=1)", ("0","1"))
Phenylephrine = st.selectbox("Phenylephrine (No=0,Yes=1)", ("0","1"))
Vasopressin = st.selectbox("Vasopressin (No=0,Yes=1)", ("0","1"))
Vent = st.selectbox("Vent (No=0,Yes=1)", ("0","1"))
Intubated = st.selectbox("Intubated (No=0,Yes=1)", ("0","1"))
MC = st.selectbox("MC (No=0,Yes=1)", ("0","1"))
HepF = st.selectbox("HepF (No=0,Yes=1)", ("0","1"))
                                               
                                                        
Age	Temperature	RespiratoryRate	HeartRate	SBP

# If button is pressed
if st.button("Predict"):

    # Store inputs into dataframe
    X = pd.DataFrame([[Age, Temperature, RespiratoryRate, HeartRate, SBP, AG, BUN, MCHC, MCV, RDW, WBC, Race,
                       Norepinephrine, Dopamine, Phenylephrine, Vasopressin, Vent, Intubated, MC, HepF]],
                     columns=["Age", "Temperature", "RespiratoryRate", "HeartRate", "SBP", "AG", "BUN", "MCHC", "MCV",
                              "RDW", "WBC", "Race", "Norepinephrine", "Dopamine", "Phenylephrine", "Vasopressin",
                              "Vent", "Intubated", "MC", "HepF"])
    X = X.replace(["Yes", "No"], [1, 0])
    X = X.replace(["white", "black","others"], [1,2,3])						
    Y = Y.replace(["death", "live"], [1, 0])
                                                        
    # Get prediction
    prediction = clf.predict(X)[0]
    prectionProbability = clf.predict_proba(X)

    # Output prediction
    st.text(f"in-hospital survive/mortality probability {prectionProbability}")
    st.text(f"in-hospital mortality prediction {prediction}")
