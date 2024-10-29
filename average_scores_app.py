# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# App title
st.title("Enhanced Average Scores of Students")

# Instructions for the user
st.write("Enter scores for each student below, and we'll calculate the average scores in each subject.")

# Step 1: Allow user input to create a sample dataset
num_students = st.number_input("Enter the number of students:", min_value=1, max_value=10, value=5)
student_data = {}

# Input names and scores for each student
for i in range(num_students):
    st.write(f"### Student {i+1}")
    name = st.text_input(f"Enter name for Student {i+1}:", f"Student {i+1}")
    math = st.number_input(f"Math score for {name}:", min_value=0, max_value=100, value=85)
    science = st.number_input(f"Science score for {name}:", min_value=0, max_value=100, value=90)
    english = st.number_input(f"English score for {name}:", min_value=0, max_value=100, value=88)
    student_data[name] = {'Math': math, 'Science': science, 'English': english}

# Convert to DataFrame
df = pd.DataFrame.from_dict(student_data, orient='index')

# Step 2: Calculate average score for each subject
average_scores = df.mean()

# Step 3: Display the DataFrame and calculated averages
st.write("### Student Scores")
st.dataframe(df)

st.write("### Average Scores")
st.write(average_scores)

# Step 4: Show additional statistics
st.write("### Summary Statistics")
st.write(f"**Highest Score in Math:** {df['Math'].max()}")
st.write(f"**Lowest Score in Math:** {df['Math'].min()}")
st.write(f"**Highest Score in Science:** {df['Science'].max()}")
st.write(f"**Lowest Score in Science:** {df['Science'].min()}")
st.write(f"**Highest Score in English:** {df['English'].max()}")
st.write(f"**Lowest Score in English:** {df['English'].min()}")

# Step 5: Plot the averages using matplotlib and display in Streamlit
fig, ax = plt.subplots()
average_scores.plot(kind='bar', ax=ax, color='skyblue')
ax.set_title('Average Scores in Each Subject')
ax.set_xlabel('Subject')
ax.set_ylabel('Average Score')

# Show the plot in Streamlit
st.pyplot(fig)