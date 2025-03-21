import streamlit as st 
import pandas

st.title('Hello World')
st.header('Hello World')
st.subheader('This is a simple Streamlit app.')
st.text('This is a simple Streamlit app.')
st.markdown('**This is a simple Streamlit app.**')
st.checkbox('I agree')
st.slider('Slide me', min_value=0, max_value=10)
st.text_input('Enter some text')

if st.button('Say Hello'):
    st.write('Why hello there')


data = {
   'name' : ['John', 'Anna', 'Peter', 'Linda'],
   " age" : [23, 34, 45, 56],
   "city" : ['New York', 'Paris', 'Berlin', 'London']
}

df = pandas.DataFrame(data)

city = st.selectbox('Select a city', df['city'])
selected_city = df[df['city'] == city]
st.write(f"Data for {city} is:")
st.write(selected_city)

