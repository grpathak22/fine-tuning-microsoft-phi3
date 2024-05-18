import streamlit as st
st.title("Script Generation App")
st.write("Enter a topic and receive a generated script.")
# Get user input for the topic
topic = st.text_input("Enter a topic:", "Enter your topic here")
#topic = "American Air Force"
input_ids = tokenizer.encode(topic, return_tensors='pt')

if st.button("Generate Script"):
    output = model.generate(input_ids, max_length=512)
    script = tokenizer.decode(output[0], skip_special_tokens=True) 
    st.write("Generated Script:")
    st.write(script)