#%%
import streamlit as st
from pymongo import MongoClient
from streamlit.type_util import data_frame_to_bytes
import pandas as pd
from pandas import DataFrame

db_username = st.secrets["myusr"]
db_pwd= st.secrets["mypwd"]

st.write(db_username)
st.write(db_pwd)

client = MongoClient("mongodb+srv://db_username:db_pwd@cluster0.vkduz.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.get_database("test")
users = db.get_collection("users")

#THIS WORKS BELOW
# data = db.users.count_documents({'username':'Gina', 'password':'GinaPHP1'})  #registers a 1 if correct info and a 0 if not
# print(data)
#THIS WORKS ABOVE

#%%
def login_user(username, password):
    data = db.users.count_documents({'username':username, 'password':password})
    # data = db.users.find({"username":username, "password":password})
    return data



def app_page():
    st.title("App Page")
    st.subheader("This is the app page")
    st.write("This is a simple app that allows you to login and view the data in the database")


def main():

    st.sidebar.title("Login")

    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")

    if st.sidebar.button("Login"):
        res = login_user(username, password)
        if res == 1:
            st.sidebar.success("Login successful")
            app_page()
        else:
            st.sidebar.error("username or password is incorrect, please try again")

if __name__ == '__main__':
    main()