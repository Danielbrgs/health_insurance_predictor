import pickle
import hashlib
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Insurance Prediction", page_icon="img/stethoscope.png")
st.sidebar.header('What if Prediction')
st.title("Insurance prediction")

st.markdown("Predict medical insurance based on the following features:")

# -- Parameters -- #

age = st.number_input(label='Age', value=18, min_value=18, max_value=120)
bmi = st.number_input(label='BMI', value=30.)
children = st.slider(label='Children', min_value=0, max_value=5)
smoker = st.selectbox(label='Smoker', options=['no','yes'])

# -- Model (safe loading with integrity check) -- #
# NOTE: For production, replace pickle with joblib or safetensors
# See: https://cwe.mitre.org/data/definitions/502.html

MODEL_PATH = 'models/model.pkl'
# Generate hash: python3 -c "import hashlib; print(hashlib.sha256(open('models/model.pkl','rb').read()).hexdigest())"
EXPECTED_HASH = None  # Set after generating

def safe_load_model(path, expected_hash=None):
    """Load pickle model with optional integrity verification."""
    import os
    if not os.path.exists(path):
        st.error(f"Model file not found: {path}")
        st.stop()
    
    with open(path, 'rb') as f:
        data = f.read()
    
    if expected_hash:
        actual = hashlib.sha256(data).hexdigest()
        if actual != expected_hash:
            st.error("⚠️ Model file integrity check failed!")
            st.stop()
    
    return pickle.loads(data)

model = safe_load_model(MODEL_PATH, EXPECTED_HASH)

def prediction():
    df_input = pd.DataFrame([{'age':age, 'bmi':bmi, 'children':children, 'smoker':smoker}])
    prediction = model.predict(df_input)[0]
    return prediction

# Predict
if st.button('Predict'):
    try:
        insurance = prediction()
        st.success(f'**Predicted insurance price:** ${insurance:,.2f}')
    except Exception as error:
        st.error(f"Couldn't predict the input data. The following error occurred: \n\n{error}")
