import streamlit as st
from transformers import GPT2Tokenizer, GPT2LMHeadModel


model_name = "microsoft/Phi-3-mini-4k-instruct"
model = AutoModelForCausalLM.from_pretrained(model_name, load_in_8bit=True,trust_remote_code = True)
tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token=hf_token)


st.title("Script Generation App")
st.write("This app generates a script based on the topic you provide. Enter a topic and click 'Generate Script' to receive your generated script.")

# Get user input for the topic
topic = st.text_input("Enter a topic:", "Enter your topic here")

if st.button("Generate Script"):
    with st.spinner("Generating script..."):
        input_ids = tokenizer.encode(topic, return_tensors='pt')
        output = model.generate(input_ids, max_length=max_length)
        script = tokenizer.decode(output[0], skip_special_tokens=True)
        st.success("Generated Script:")
        st.write(script)

        
        st.download_button(
            label="Download Script",
            data=script,
            file_name="generated_script.txt",
            mime="text/plain"
        )
