import numpy as np
import pandas as pd
import streamlit as st
import time as t

# Title
st.title("Welcome to Numerology App")

# Header
st.header("Best Future Prediction Service")

# Sub header
st.subheader("Numerology")

# information details
st.info("Numerology is a  future prediction science mostly used in India and neighbouring contries.")

# Warning
st.warning("Numerology app provides generalised insights. For customized services, contact to our specialist")

# Error
st.error("Entered DOB is not in DD-MM-YYYY format, please correct the DOB as suggested")

# Success
st.success("Entred DOB is in correct format")

# Write
st.write("Enter your DOB in DD-MM-YYYY format")
#st.write(range(0,50))

# Markdown
st.markdown("### Predictions")

# Markdown with emoji
st.markdown(":moon:")

# Text
st.text("Prediction Message, which we are featching from df based on mulyank and bhagyank")

# Mathematical equation
st.latex('''a^2 +2ab +b^2''')

# Image
st.image("US States.png")

# Caption
st.caption("Image caption")

# Widgets

## Checkbox
st.checkbox("select items")

## Button
st.button("Save")

## Radio Button
st.radio("Select your gender",['Male','Female','Other'])

## Select box/ drop down
st.selectbox("Select the service",['Astrology','Numerology','Palmology'])

## Multi Select dropdown
st.multiselect("Select the prediction science based on coutry",['Indian','Chinese','Indo-Chinese'])

## Rating Slider
st.select_slider("Provide your feedback",["Bad","Good","Excellent","Outstanding"])

## Number Slider
st.slider("Rating on scale of 1 to 10",1,10)

## Numbper input, on clicking increases the number
st.number_input("pick a number:",1,10)

## Text input
st.text_input("Enter your mail id:")

## Date input
st.date_input("date")

## Time input
st.time_input("Time:")

## Text area to write more than one line
st.text_area("Enter your feedback here")

## Upload file
st.file_uploader("upload your file here")

## Color selector
st.color_picker("Color")

## Progress bar
st.progress(90)

## Spinner: for wait
# with st.spinner("wait for 5 seconds to process"):
#     t.sleep(2)


## Ballons
st.balloons()

## Side bar. Pin any element to side bar
st.sidebar.title("Numerology App")
st.sidebar.text_input("Enter your mail Id")
st.sidebar.text_input("Enter your password")
st.sidebar.button("Login")

### Data Visualization

## Bar chart
st.title("Bar Chart")
data = pd.DataFrame(np.random.randn(50,2),columns=['x','y'])
st.bar_chart(data)

## Line chart
st.title("Line Chart")
data = pd.DataFrame(np.random.randn(50,2),columns=['x','y'])
st.line_chart(data)

## Area chart
st.title("Area Chart")
data = pd.DataFrame(np.random.randn(50,2),columns=['x','y'])
st.area_chart(data)








# How to run stramlit: anaconda propt(enter this file adress), then write | streamlit run streamlit_app.py | This will open the browser
# Resource: https://www.youtube.com/watch?v=YzvMpvXyUfs