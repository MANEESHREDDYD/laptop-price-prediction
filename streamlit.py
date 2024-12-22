import streamlit as st
import joblib
import requests

model = joblib.load('final_model_pipeline.joblib')
# Streamlit app title
st.title("Laptop Price Prediction")

# Sidebar instructions
st.sidebar.header("Input Features")

# Input fields for categorical and numerical features
brand_name = st.sidebar.selectbox("Brand Name", ["Lenovo", "Avita", "HP", "acer" ,"ASUS" ,"DELL" ,"RedmiBook", "realme" ,"Infinix",
 "MSI" ,"lenovo" ,"MICROSOFT" ,"Smartron", "LG" ,"Nokia" ,"APPLE", "Vaio", "Mi",
 "ALIENWARE", "iball", "SAMSUNG"])
model_name = st.sidebar.selectbox("Model Name", [
    "A6-9225", "Ideapad", "PURA", "APU", "Athlon", "Aspire", "ExpertBook", "Missing",
    "v15", "VivoBook", "EeeBook", "Nitro", "Cosmos", "x360", "IdeaPad", "Celeron",
    "15q", "250-G6", "Vostro", "15", "Pavilion", "Book", "Inspiron", "INBook",
    "ThinkPad", "Chromebook", "Commercial", "14s", "INSPIRON", "V15", "15s", "3000",
    "Notebook", "Vivo", "DA", "Insprion", "Travelmate", "14a", "Predator", "Spin",
    "Swift", "ROG", "XPS", "Omen", "Surface", "t.book", "Yoga", "Gram", "Spectre",
    "VivoBook14", "TUF", "Book(Slim)", "Pro", "PureBook", "ASUS", "Katana", "GF63",
    "Thinkbook", "Intel", "G15", "ZenBook", "Legion", "Modern", "ThinkBook",
    "Prestige", "Zenbook", "MacBook", "Sword", "Envy", "SE", "ConceptD", "HP", "DELL",
    "X390", "Thinpad", "Inpiron", "GAMING", "GS", "430", "Liber", "F17", "B50-70",
    "GE76", "GP65", "GP76", "250", "3511", "G3", "GS66", "X1", "GF65", "Stealth",
    "Zephyrus", "Summit", "OMEN", "Pulse", "WF65", "Creator", "Dual", "G7",
    "CompBook", "Pentium", "Extensa", "Asus", "Ryzen", "Bravo", "15-ec1105AX", "G5",
    "E", "AMD", "IDEAPAD", "Lenovo", "Alpha", "Delta", "Rog", "Galaxy", "Thinkpad"
])
processor_brand = st.sidebar.selectbox("Processor Brand", ["AMD", "Intel", "M1", "MediaTek", "Qualcomm"])
processor_name = st.sidebar.selectbox("Processor Name", [
    "A6-9225 Processor", "APU Dual", "Athlon Dual", "Core i3", "Core i5",
    "Celeron Dual", "Ryzen", "Ryzen 5", "Core", "Core i7", "Core i9", 
    "Core m3", "Dual Core", "Ever Screenpad", "GeForce GTX", "GeForce RTX", 
    "GEFORCE RTX", "Hexa Core", "M1", "Genuine Windows", "Pentium Quad", 
    "Pentium Silver", "Ryzen 3", "MediaTek Kompanio", "Quad", "Ryzen 7", 
    "Ryzen 9", "Snapdragon 7c"
])
processor_gnrtn = st.sidebar.selectbox("Processor Generation", [
    "10th", "Missing", "11th", "7th", "8th", "9th", "4th", "12th"])  # Min: 1, Max: 12
ram_gb = st.sidebar.selectbox("RAM (GB)", [
    "4 GB GB", "8 GB GB", "32 GB GB", "16 GB GB"
])
ram_type = st.sidebar.selectbox("RAM Type", [
    "DDR4", "LPDDR4X", "LPDDR4", "DDR5", "DDR3", "LPDDR3"
])
ssd = st.sidebar.selectbox("SSD (GB)", [
    "0 GB", "128 GB", "256 GB", "32 GB", "512 GB", "1024 GB", "2048 GB", "3072 GB"
])  # Min: 0, Max: 2048
hdd = st.sidebar.selectbox("HDD (GB)", [
    "1024 GB", "512 GB", "0 GB", "2048 GB"
])  # Min: 0, Max: 2000
weight = st.sidebar.selectbox("Weight", ["ThinNlight", "Casual", "Gaming"])  # Min: 1.0, Max: 5.0
display_size = st.sidebar.selectbox("Display Size (inches)", [
    "Missing", "14", "15.6", "14.96", "15", "14.1", "12.2", "13.3", "17.3", 
    "13", "16", "14.9", "16.1", "14.2", "16.2", "13.4"
])  # Min: 10.0, Max: 20.0

# Boolean fields
warranty = st.sidebar.selectbox("Warranty", [0, 1, 2, 3])
Touchscreen = st.sidebar.radio("Touchscreen", ["Yes", "No"])
msoffice = st.sidebar.radio("MS Office", ["Yes", "No"])
star_rating = st.sidebar.slider("Star Rating", 0.0, 5.0, 4.5)  # Min: 0.0, Max: 5.0
ratings = st.sidebar.number_input("Number of Ratings", min_value=0, max_value=10000, value=500)
reviews = st.sidebar.number_input("Number of Reviews", min_value=0, max_value=1000, value=100)
reactions = st.sidebar.number_input("Number of Reactions", min_value=0, max_value=10000, value=800)
warranty_importance = st.sidebar.selectbox("Warranty Importance", [0, 1, 2, 3])

# Prepare input payload for API request


print(input_data)

# API endpoint URL
api_url = "https://laptop-price-class.onrender.com/predict" 

# Make prediction when the user clicks the "Predict" button
if st.button("Get Prediction"):
    input_data = {
        "brand_name": brand_name,
        "model_name": model_name,
        "processor_brand": processor_brand,
        "processor_name": processor_name,
        "processor_gnrtn": processor_gnrtn,
        "ram_gb": ram_gb,
        "ram_type": ram_type,
        "ssd": ssd,
        "hdd": hdd,
        "weight": weight,
        "display_size": display_size,
        "warranty": warranty,
        "Touchscreen": Touchscreen,
        "msoffice": msoffice,
        "star_rating": star_rating,
        "ratings": ratings,
        "reviews": reviews,
        "reactions": reactions,
        "warranty_importance": warranty_importance,
    }
    try:
        # Send a POST request to the API
        response = requests.post(api_url, json=input_data)
        
        # Check if the request was successful
        if response.status_code == 200:
            prediction = response.json()  # Assuming the response returns a JSON with the prediction
            st.success(f"The predicted laptop price is: {prediction[0]}")
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
        st.error(f"An error occurred: {e}")