import streamlit as st
import pandas as pd
import os

# Function to save data to Excel
def save_to_excel(data, file_name='customer_data.xlsx'):
    if not os.path.isfile(file_name):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)
    else:
        df = pd.DataFrame(data)
        df_existing = pd.read_excel(file_name)
        df_combined = pd.concat([df_existing, df], ignore_index=True)
        df_combined.to_excel(file_name, index=False)

# Function to showcase tour recommendations
def recommend_tours(destination):
    recommendations = {
    "Andhra Pradesh": ["Visakhapatnam", "Tirupati", "Vijayawada"],
    "Arunachal Pradesh": ["Tawang", "Ziro Valley", "Bomdila"],
    "Assam": ["Kaziranga National Park", "Majuli", "Guwahati"],
    "Bihar": ["Bodh Gaya", "Nalanda", "Patna"],
    "Chhattisgarh": ["Raipur", "Jagdalpur", "Bilaspur"],
    "Goa": ["Panaji", "Vasco da Gama", "Margao"],
    "Gujarat": ["Ahmedabad", "Surat", "Vadodara"],
    "Haryana": ["Gurgaon", "Faridabad", "Panchkula"],
    "Himachal Pradesh": ["Shimla", "Manali", "Dharamshala"],
    "Jharkhand": ["Ranchi", "Jamshedpur", "Dhanbad"],
    "Karnataka": ["Bangalore", "Mysore", "Mangalore"],
    "Kerala": ["Kochi", "Thiruvananthapuram", "Munnar"],
    "Madhya Pradesh": ["Bhopal", "Indore", "Gwalior"],
    "Maharashtra": ["Mumbai", "Pune", "Nagpur"],
    "Manipur": ["Imphal", "Churachandpur", "Ukhrul"],
    "Meghalaya": ["Shillong", "Cherrapunji", "Mawsynram"],
    "Mizoram": ["Aizawl", "Lunglei", "Champhai"],
    "Nagaland": ["Kohima", "Dimapur", "Mokokchung"],
    "Odisha": ["Bhubaneswar", "Puri", "Cuttack"],
    "Punjab": ["Amritsar", "Chandigarh", "Ludhiana"],
    "Rajasthan": ["Jaipur", "Udaipur", "Jodhpur"],
    "Sikkim": ["Gangtok", "Pelling", "Lachung"],
    "Tamil Nadu": ["Chennai", "Coimbatore", "Madurai"],
    "Telangana": ["Hyderabad", "Warangal", "Nizamabad"],
    "Tripura": ["Agartala", "Udaipur", "Dharmanagar"],
    "Uttar Pradesh": ["Agra", "Varanasi", "Lucknow"],
    "Uttarakhand": ["Dehradun", "Nainital", "Haridwar"],
    "West Bengal": ["Kolkata", "Darjeeling", "Siliguri"]
    }
    return recommendations.get(destination, ["No recommendations available"])

# Streamlit web app
st.title("Travel Booking Application")

st.header("Enter your information")
name = st.text_input("Name")
city = st.text_input("City")
address = st.text_area("Address")
mobile_number = st.text_input("Mobile Number")
destination = st.selectbox("Desired Travel Destination", ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
          "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka",
          "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram",
          "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu",
          "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"])
travel_days = st.number_input("Number of Days for Travel", min_value=6, max_value=30)

if st.button("Submit"):
    customer_data = {
        "Name": [name],
        "City": [city],
        "Address": [address],
        "Mobile Number": [mobile_number],
        "Desired Travel Destination": [destination]
    }
    save_to_excel(customer_data)
    st.success("Your information has been submitted!")

    st.header("Recommended Tours")
    tours = recommend_tours(destination)
    for tour in tours:
        st.write(tour)
