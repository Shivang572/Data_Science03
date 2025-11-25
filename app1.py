import streamlit as st
import pickle

pipe = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))

st.title("Laptop Predictor")
#brand
company = st.selectbox('Brand',df['Company'].unique())
#type of user
type = st.selectbox('Type',df['TypeName'].unique())
#Ram
ram = st.selectbox('RAM(in GB)',[2,4,6,8,12,16,24,32,64])

#weight
weight = st.number_input("Weight (in kg)")
#touchscreen
touchscreen = st.selectbox('TouchScreen',['Yes','No'])
#ips
ips = st.selectbox('IPS',['YES','NO'])
#screensize
screen_size = st.number_input('Screen Size')
#resolution
resolution = st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])
#cpu
cpu = st.selectbox('CPU',df['Cpu_Brand'].unique())
#hdd
hdd =   st.selectbox('HDD(In GB)',[0,128,256,512,1024,2048])
ssd =   st.selectbox('SSD(In GB)',[0,8,128,256,512,1024])

gpu = st.selectbox('GPU',df['Gpu_brand'].unique())

os = st.selectbox('OS',df['os'].unique())

if st.button('Predict Price'):
    pass