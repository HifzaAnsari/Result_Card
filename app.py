import streamlit as st
import urllib.parse

st.set_page_config(

    page_title= "TechCart",
    page_icon="🖥️",
    layout="wide"



)

st.title("🖥️ TechCart")
st.title("Smat Products. Simple Shopping.")

menu = st.radio("Menu",
               ["Home","Products","Categories","About","Contact"],
               horizontal=True)






st.divider()

if menu == "Home":
    st.header("Welcom To My TechCart")
    st.write("Discover useful technology products at affortable prices")

    st.divider()
    st.header("My Shop Here")
    col1 , col2, col3 = st.columns(3)

    with col1:
        st.subheader("Quality Product")
        st.write("We offer reliable and useful products.")

    with col2:
        st.subheader("Affordable Prices")
        st.write("Get Products at resonable prices")
    
    with col3:
        st.subheader("Easy Odering")
        st.write("Order Your Favorite Product")

    

elif menu == "Products":
    st.header('Our Products')
    st.write("Our Products will Show here")

    st.divider()
    col1,col2,col3 = st.columns(3)

    with col1:
        st.image("mouse.png", use_container_width=True)
        st.subheader("Premium And Affordable Mouse")
        st.write("100% Quality")
        st.write("Rs : 1699")
        st.button ("Order Now!",key="mouse")

    with col2:
        st.image("key.png", use_container_width=True)
        st.subheader("Premium And Affordable Easy to use")
        st.write("100% Quality")
        st.write("Rs : 9999")
        st.button ("Shop Now!",key="key")

        message = ''' Hellow, I am intrested in odering:
        Product : HP Laptop 
        Price : 100000
        Please provider more details
        '''
        whatsapp_url = (
            f"https://wa.me/{"03136934566"}?text = " + urllib.qoute(message)


        )



    with col3:
        st.image("ear.png" , use_container_width=True)
        st.subheader("Premium And Affordable Easy to use")
        st.write("100% Quality")
        st.write("Rs : 999")
        st.button ("Shop Now!",key="ear")



elif menu =="Categories":
    st.header("Products Categories")
    st.write("Our Product Categories Will Appear Here")
elif menu =="About":
    st.header("About US")
    st.write("We Are Selling Our Products In All Over The World!")
elif menu=="Contact":
    st.header("Contact Info")
    st.write("Contact : Email:infotechcart@gmail.com")
    st.write("Contact Number : 03136934566")

