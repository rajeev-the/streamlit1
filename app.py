import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# Load dataset (replace 'your_dataset.csv' with your actual dataset)
df = pd.read_csv("C:/Users/sko98/Downloads/archive (1)/repository_data.csv")

# Set title for the app
st.title('Streamlit Dashboard: Data Visualization and Exploration')

# Display the dataset
st.subheader('Dataset Overview')
st.dataframe(df.head())

# Summary statistics
st.subheader('Summary Statistics')
st.write(df.describe())
st.divider()  

#pi-chart Display the dataset
languages = df["primary_language"].head(20) 

language_counts = Counter(languages)
labels = list(language_counts.keys())
sizes = list(language_counts.values())

# Create the pie chart
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Display the pie chart in the Streamlit app
st.title('Programming Language Frequency - Pie Chart')
st.pyplot(fig)
st.divider()  


#bar-graph Display the datasets  Watch
name  = df["name"].head(10) 
watch = df["watchers"].head(10)
# Create a matplotlib bar chart
plt.figure(figsize=(10, 6))
plt.bar(name, watch, color='blue')
plt.xlabel('Repository Name')
plt.ylabel('Forks Count')
plt.title('Top 10  watched Repositories ')
plt.xticks(rotation=45)
plt.tight_layout()

# Display the plot in Streamlit
st.title('Top 10  watched Repositories - Bar graph')
st.pyplot(plt)
st.divider()  



#bar-graph Display the datasets  forks_count
name  = df["name"].head(10) 
watch = df["forks_count"].head(10)
# Create a matplotlib bar chart
plt.figure(figsize=(10, 6))
plt.bar(name, watch, color='blue')
plt.xlabel('Repository Name')
plt.ylabel('Forks Count')
plt.title('Top 10  Repositories by forks count ')
plt.xticks(rotation=45)
plt.tight_layout()

# Display the plot in Streamlit
st.title('Top 10 Repositories for - forks count')
st.pyplot(plt)
st.divider()  


#pi-chart for licence in Repository:

languages = df["licence"].head(20) 

language_counts = Counter(languages)
labels = list(language_counts.keys())
sizes = list(language_counts.values())

# Create the pie chart
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Display the pie chart in the Streamlit app
st.title('Licence in Repository- Pie Chart')
st.pyplot(fig)
st.divider() 
  



#bar-graph Display the datasets  pull_requests
name  = df["name"].head(10) 
watch = df["pull_requests"].head(10)
# Create a matplotlib bar chart
plt.figure(figsize=(10, 6))
plt.bar(name, watch, color='blue')
plt.xlabel('Repository Name')
plt.ylabel('pull requests')
plt.title('Top 10  pull requests Repositories ')
plt.xticks(rotation=45)
plt.tight_layout()

# Display the plot in Streamlit
st.title('Top 10  pull Requests Repositories')
st.pyplot(plt)


