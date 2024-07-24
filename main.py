# Code generated by ChatGPT


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

# Load the data
file_path = '202406_202406_연령별인구현황_월간.csv'
data = pd.read_csv(file_path, encoding='cp949')

# Preprocess the data
age_columns = [f'2024년06월_계_{i}세' for i in range(0, 100)] + ['2024년06월_계_100세 이상']
data = data[['행정구역'] + age_columns]
data.columns = ['Region'] + list(range(100))
# Calculate middle school population (ages 12 to 14)
data['MiddleSchool'] = data[12] + data[13] + data[14]

# Streamlit app
st.title('Middle School Population Proportion by Region')

# Select region
regions = data['Region'].unique()
selected_region = st.selectbox('Select a region:', regions)

# Filter data for the selected region
region_data = data[data['Region'] == selected_region]

if not region_data.empty:
    total_population = region_data[range(101)].sum(axis=1).values[0]
    middle_school_population = region_data['MiddleSchool'].values[0]
    other_population = total_population - middle_school_population

    # Pie chart
    labels = ['Middle School Students (Ages 12-14)', 'Other Population']
    sizes = [middle_school_population, other_population]
    colors = ['#ff9999','#66b3ff']
    explode = (0.1, 0)  # explode the middle school slice

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.pyplot(fig1)
else:
    st.write("No data available for the selected region.")
