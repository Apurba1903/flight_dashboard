import streamlit as st
import pandas as pd
from dbhelper import DB
import plotly.express as px


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
    
    
    
    # Pie Chart
    airline, frequency = db.fetch_airline_freq()
    
    st.subheader("Airline Frequency Distribution")
    
    fig_plotly = px.pie(
        values=frequency, 
        names=airline, 
        title=''
    )
    fig_plotly.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig_plotly)
    
    
    
    # Bar Chart
    city, frequency = db.busy_airport()
    
    st.subheader("Busiest Airport City")
    
    fig_plotly = px.bar(
        x=city, 
        y=frequency,
        labels={'x': 'Cities', 'y': 'Number of Flights'}
        
    )
    fig_plotly.update_traces(texttemplate='%{y}', textposition='outside')
    st.plotly_chart(fig_plotly)
    
    
    
    # Line Chart
    date, frequency = db.daily_frequency()
    
    st.subheader("Daily Flight History")
    
    fig_plotly = px.line(
        x=date, 
        y=frequency,
        labels={'x': 'Date', 'y': 'Number of Flights'}
        
    )
    fig_plotly.update_traces(texttemplate='%{y}', textposition='top center')
    st.plotly_chart(fig_plotly)
    
    
    
else:
    st.title('✈️ About The Project')

    st.markdown("""
    ## Flight Analytics Dashboard

    This application provides comprehensive flight data analysis and search functionality.

    ### 🎯 Features

    **Flight Search:**
    - Search flights between different cities
    - View detailed flight information including airline, route, departure time, duration, stops, and price
    - Filter results based on source and destination

    **Analytics Dashboard:**
    - Airline distribution analysis with interactive pie charts
    - Busiest airport cities visualization
    - Daily flight frequency trends
    - Real-time data insights

    ### 🛠️ Technology Stack
    - **Frontend:** Streamlit
    - **Database:** MySQL
    - **Visualization:** Plotly
    - **Backend:** Python

    ### 📊 Data Source
    The application uses flight data containing information about:
    - Airlines and routes
    - Departure times and duration
    - Pricing information
    - Airport locations
    - Historical flight patterns

    ### 🚀 How to Use
    1. **Check Flights:** Select source and destination cities to search for available flights
    2. **Analytics:** Explore various charts and insights about flight patterns
    3. **About:** Learn more about the project (you're here!)

    ---
    *Built with ❤️ using Python and Streamlit*
    """)
    
    
    
    
    
    
    