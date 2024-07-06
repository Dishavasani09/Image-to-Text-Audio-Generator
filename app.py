import streamlit as st
import pathlib
import textwrap
import google.generativeai as genai
from IPython.display import Markdown
from gtts import gTTS
from IPython.display import Audio
import PIL.Image
import os

# Function to convert text to Markdown format
def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# Streamlit app layout
def main():
    st.title("Gemini 1.0 Pro Vision - Image Analysis and Text Generation")
    
    # File uploader for images
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png"])

    if uploaded_file is not None:
        # Display the uploaded image
        st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
        
        # Load the image for processing
        img = PIL.Image.open(uploaded_file)
        
        # Generate content using the Gemini model
        response = model.generate_content(img)
        
        # Convert the generated text to Markdown format for display
        generated_text = response.text
        
        # Display the generated text
        st.write("Generated Text:")
        st.write(generated_text)
        
        # Convert generated text to speech
        tts = gTTS(response.text)
        tts.save('output.mp3')
        st.audio('output.mp3', format='audio/mp3', start_time=0)
        
if __name__ == "__main__":
    # Configure Google API key
    fetcheed_api_key = os.getenv("API_KEY")
    genai.configure(api_key = fetcheed_api_key)
    
    # List available models
    # for m in genai.list_models():
    #     if 'generateContent' in m.supported_generation_methods:
    #         st.write("Model Name:", m.name)
    
    # Load the Gemini model
    model = genai.GenerativeModel('gemini-1.0-pro-vision-latest')
    
    # Run the Streamlit app
    main()





# from dotenv import load_dotenv
# import streamlit as st
# import os
# import google.generativeai as ggi
# import pathlib
# import textwrap
# import google.generativeai as genai
# from IPython.display import display
# from IPython.display import Markdown

# load_dotenv(".env")

# fetcheed_api_key = os.getenv("API_KEY")
# ggi.configure(api_key = fetcheed_api_key)

# model = ggi.GenerativeModel("gemini-1.0-pro-vision-latest") 
# chat = model.start_chat()

# def LLM_Response(question):
#     response = chat.send_message(question,stream=True)
#     return response

# st.title("Gemini 1.5 Pro Vision Integration Demo")

# # Upload image file
# uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "png"])

# # st.title("Chat Application using Gemini Pro")

# # user_quest = st.text_input("Ask a question:")
# # btn = st.button("Ask")

# # if btn and user_quest:
# #     result = LLM_Response(user_quest)
# #     st.subheader("Response : ")
# #     for word in result:
# #         st.text(word.text)