import streamlit as st

# st.title("Welcome to wscube tech")
# st.header("python")
# st.subheader("java")
# st.markdown("I love Python")
# st.code("""for i in range(1,5,1):
#               print("hello")
#         """)
name = st.text_input("Enter your name : ")
fname = st.text_input("Enter your father name : ")
adr = st.text_area("Enter your Address : ")
classdata = st.selectbox("Enter Your Class : ", (1,2,3,4,5,6))

button = st.button("Done")
if button :
    st.markdown(f"""
    Name : {name}
    Father Name : {fname}
    address : {adr}
    class : {classdata}""")
