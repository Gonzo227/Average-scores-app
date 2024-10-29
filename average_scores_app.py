# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# App title
st.title("Average Scores of Students")

# Step 1: Create a sample dataset
data = {
    'Student': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Math': [85, 78, 92, 88, 76],
    'Science': [91, 82, 85, 79, 88],
    'English': [78, 84, 89, 85, 80]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Step 2: Calculate average score for each subject
average_scores = df[['Math', 'Science', 'English']].mean()

# Display the DataFrame and calculated averages in Streamlit
st.write("### Student Scores")
st.dataframe(df)

st.write("### Average Scores")
st.write(average_scores)

# Step 3: Plot the averages using matplotlib and display in Streamlit
fig, ax = plt.subplots()
average_scores.plot(kind='bar', ax=ax)
ax.set_title('Average Scores in Each Subject')
ax.set_xlabel('Subject')
ax.set_ylabel('Average Score')

# Show the plot in Streamlit
st.pyplot(fig)