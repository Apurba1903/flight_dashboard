import streamlit as st
import pandas as pd
from dbhelper import DB

db = DB()

st.sidebar.title('Flights Analytics')

user_option = st.sidebar.selectbox('Menu', ['Select One', 'Check Flights', 'Analytics'])

if user_option == 'Check Flights':
    st.title('Check Flights')
    
    col1,col2 = st.columns(2)
    city = db.fetch_city_names()
    
    with col1:
        source = st.selectbox('Source', sorted(city))
        
    with col2:
        destination = st.selectbox('Destination', sorted(city))
    
    if st.button('Search'):
        if source and destination:  # Check if both cities are selected
            if source != destination:  # Prevent same source and destination
                results = db.fetch_all_flights(source, destination)
                if results:
                    df = pd.DataFrame(results, columns=[
                        'Airline', 'Route', 'Departure Time', 
                        'Duration', 'Total Stops', 'Price'
                    ])
                    st.dataframe(df)
                    st.success(f"Found {len(results)} flights from {source} to {destination}")
                else:
                    st.warning(f"No flights found from {source} to {destination}")
            else:
                st.error("Source and destination cannot be the same!")
        else:
            st.error("Please select both source and destination cities")
    
    
elif user_option == 'Analytics':
    st.title('Analytics')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
else:
    st.title('About The Project')
    # Add project information here