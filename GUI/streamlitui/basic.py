import streamlit as st
import pandas as pd
import time

# Set page configuration for a wider layout and better appearance
st.set_page_config(page_title="My Dashboard", layout="wide")

# Title and headers
st.title("My Dashboard")
st.header("I am learning Streamlit")
st.subheader("I am loving it!")

# Normal text
st.write("This is normal text")

# Markdown for favorite languages
st.markdown("""
### My Favorite Languages
- Python
- Java
- C++
""")

# Code block
st.code("""
def test(arr: list):
    return len(arr)
""", language="python")

# LaTeX equation
st.latex(r"x^2 + y^2 = 0")

# DataFrame
df = pd.DataFrame({
    'name': ['Akshay', 'Karan', 'Rohit'],
    'marks': [70, 80, 90],
    'package': [40, 70, 90]
})

# Sidebar for interactivity
st.sidebar.title("Sidebar")
st.sidebar.markdown("Filter the DataFrame")
min_marks = st.sidebar.slider("Minimum Marks", min_value=0, max_value=100, value=0)
filtered_df = df[df['marks'] >= min_marks]

# Display filtered DataFrame
st.dataframe(filtered_df, use_container_width=True)

# Metric
st.metric('Revenue', 'Rs 3L', '3%')

# JSON data
st.json({
    'name': ['Akshay', 'Karan', 'Rohit'],
    'marks': [70, 80, 90],
    'package': [40, 70, 90]
})

# Image with error handling
try:
    st.image('img.jpg', caption="Sample Image", use_column_width=True)
except FileNotFoundError:
    st.error("Image 'img.jpg' not found. Please upload the correct file.")

# Columns for videos
col1, col2 = st.columns(2)
with col1:
    try:
        st.video('Video-510.mp4')
    except FileNotFoundError:
        st.error("Video 'Video-510.mp4' not found in col1.")
with col2:
    try:
        st.video('Video-510.mp4')
    except FileNotFoundError:
        st.error("Video 'Video-510.mp4' not found in col2.")

# Message types
st.success("This is a success message!")
st.error("This is an error message!")
st.warning("This is a warning message!")
st.info("This is an info message!")
st.write("This is a basic message using st.write!")

# Progress bar
st.write("Simulating a task with a progress bar...")
progress_bar = st.progress(0)
try:
    for i in range(100):
        time.sleep(0.05)  # Simulate work
        progress_bar.progress(i + 1)
    st.success("Task completed successfully!")
except Exception as e:
    st.error(f"An error occurred: {e}")
