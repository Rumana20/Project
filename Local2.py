# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 19:23:05 2021

@author: admin
"""
import streamlit as st
import pickle

#loading model
reco = pickle.load(open("rec_sys.pkl","rb"))


def main():
    st.title("Home")
    html_temp = """
    <div style="background-color:pink;padding:5px">
    <h2 styles="color:white;text-align:center;"> Find a Friend ML App </h2>
     <body>
    <div style=background-image: ('');>
    </body>
    </div>
     """
    st.markdown(html_temp,unsafe_allow_html=True)
    
if __name__=='__main__':
    main()   





name = st.text_input("Name","Type..")

age = st.number_input("Age",18,79)

gender = st.selectbox("gender", ["Female","Male"])

oreintation = st.selectbox("Orientation", ["Straight","Bisexual","Gay"])

status = st.selectbox("Status", ["Single","in a relationship","Unknown"])

education = st.selectbox("Education", ["college/university","Masters and above","other","Two-year college","High school","Med / Law school"])

ethnicity = st.selectbox("Ethnicity", ["White","Asian","Hispanic","African American","Mixed","Unknown","others"])

religion = st.selectbox("Religion", ["Agnosticism","Atheism","Christianity","Catholicism","Judaism","Buddhism","Islam","Hinduism","Unknown","others"])

smokes = st.selectbox("Smokes", ["Yes","No"])

drink = st.selectbox("Drink", ["Yes","No"])

body_type = st.selectbox("Body_Type", ["Fit","Average","Curvy","Thin","Overweight","Rather not say"])

diet = st.selectbox("Diet", ["Anything","Vegan","Vegetarian","Halal","Kosher","other"])

job = st.selectbox("Job", ["Office/Professional","Science/Tech","Business Management","Creative"])

speaks = st.text_input("Speaks \n Enter your 2nd preferred language","Type..")

sign = st.selectbox("Sign", ["Aries","Taurus","Gemini","Cancer","Leo","Virgo","Libra","Scorpion","Sagittarius","Capricorns","Aquarius","Pisces"])

offspring = st.selectbox("Offspring", ["Wants Kids","Does not want kids","Has kid","Unknown"])

drugs = st.selectbox("Drugs", ["Yes","No"])

height = st.number_input("Height \n (In inches)",30,100)

income = st.number_input("Income",0,100000)

pet = st.selectbox("Pet", ["Likes Cats and Dogs","Dislikes Cats and Dogs","Likes only cats","Likes only Dogs","Unknown"])

essay0 = st.text_input("essay0 \n My self summary","Type..")

essay1 = st.text_input("essay1  \n What I am doing with my life","Type..")

essay2 = st.text_input("essay2  \n I am really good at ","Type..")

essay3 = st.text_input("essay3 \n The first thing people usually notice about me","Type..")

essay4 = st.text_input("essay4  \n Favourite books, Movies, Show,Music, Food","Type..")

essay5 = st.text_input("essay4 \n The 6 things that I could never do without","Type..")

essay6 = st.text_input("essay6  \n I spend a lot of time thinking about","Type")

essay7 = st.text_input("essay7  \n On a typical Friday night I am","Type..")

essay8 = st.text_input("essay8  \n The most private thing I am willing to admit","Type..")

essay9 = st.text_input("essay9  \n You should message me if","Type..")
result =""
if st.button("Match Me"):
     result=reco(name,age,gender,oreintation,status,education,ethnicity,religion,smokes,drink,body_type,diet,job,speaks,sign,offspring,drugs,height,income,pet,essay0,essay1,essay2,essay3,essay4,essay5,essay6,essay7,essay8,essay9)
     st.success("Your recommended profiles are:{}".format(result))
   

      