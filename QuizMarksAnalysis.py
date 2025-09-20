import pandas as pd 
import numpy as np
import streamlit as st

data = pd.read_csv('quiz_1_mark_list_full.csv')
print(data)

st.title("Quiz Marks Analysis")

st.write("This application is made to analyze quiz marks data.")

st.subheader("Dataset")
st.dataframe(data)

# Let us find the average, median and modal marks.
quiz_marks = pd.to_numeric(data['QUIZ 1'], errors='coerce').dropna()
st.subheader("Statistical Analysis")
st.write("Average Marks: ", np.mean(quiz_marks))
st.write("Median Marks: ", np.median(quiz_marks))
st.write("Mode Marks: ", quiz_marks.mode()[0])

# Let us visualize the marks via histogram.

st.subheader("Marks Distribution")
st.bar_chart(quiz_marks.value_counts().sort_index())
st.line_chart(quiz_marks.value_counts().sort_index())
st.area_chart(quiz_marks.value_counts().sort_index())

# creating a percentile calculator

st.subheader("Percentile Calculator")
marks = st.number_input("Enter the marks to find the percentile: ", min_value  = 0, max_value = 20, step= 2)
if st.button("Calculate Percentile"):
    percentile = (quiz_marks < marks).sum() / len(data) * 100
    st.write(f"The percentile for marks {marks} is {percentile:.2f}%")
    st.balloons()

