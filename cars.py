import streamlit as st
import pandas as pd

# Load the dataset
def load_data():
    data = pd.read_csv('Lab12/car_data.csv')
    return data

data = load_data()

car_name = st.sidebar.text_input('Car Name')

# b. Multiselect for choosing between Manual/Automatic
transmission_type = st.sidebar.multiselect('Transmission Type', ['Manual', 'Automatic'], default=['Manual', 'Automatic'])

# c. Slider for selling_price range
price_range = st.sidebar.slider('Selling Price Range', 0, 20, (0, 20))

# d. Slider for year range
year_range = st.sidebar.slider('Year Range', 2000, 2024, (2000, 2024))

# e. Submit button
if st.sidebar.button('Submit'):
    # Filter data based on selections
    filtered_data = data[data['Transmission'].isin(transmission_type) &
                         data['Selling_Price'].between(price_range[0], price_range[1]) &
                         data['Year'].between(year_range[0], year_range[1])]
    
    if car_name:
        filtered_data = filtered_data[filtered_data['Car_Name'].str.contains(car_name, case=False, na=False)]
    
    st.dataframe(filtered_data)
else:
    # If no filters are selected, show original data
    st.dataframe(data)