# import libraries
import streamlit as st

# give your app a name
st.title("Predictive Maintenance System")

# header
st.header(Smart Maintenance)
# paragraph info
st.write('This is a web created using streamlit for smart maintenance. The app is supposed to take in data informationand predict if an equipment preserved.')
#
st.subheader('Some info on the equipment data.')
#M1 Modelling part 
Url-'https://github.com/BeatriceMukuhi/tutorial/blob/main/equipment_anomaly_data.csv'
df- pd.read_csv(url).set_index('Unnamed:0') # remove unamed column 0

# Display sample data to the user
st.subheader(Sample Equipment Data)
st.dataframe(df.head(4))



