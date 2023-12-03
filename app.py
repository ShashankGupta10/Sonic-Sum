import streamlit as st
from langchain.document_loaders.blob_loaders.youtube_audio import YoutubeAudioLoader
from langchain.document_loaders.generic import GenericLoader
from langchain.document_loaders.parsers import OpenAIWhisperParser
from langchain.memory import ConversationBufferMemory
from langchain.llms.cohere import Cohere
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import whisper
import os

memory = ConversationBufferMemory()

def summarize(text):
    prompt = PromptTemplate(
        input_variables=["transcript"],
        template="The following will be a transcript for an audio file. Your task is to summarize it in as short as possible while also keeping the meaning of the audio file intact. The transcript is: {transcript}"
    )
    llm = Cohere(temperature=0.7, cohere_api_key=st.secrets["COHERE_API_KEY"])
    chain = LLMChain(llm=llm, prompt=prompt, memory=memory)
    summary = chain.run(text)
    return summary


st.title("Audio Summarizer 🦜🔗")
youtube = st.text_input("Enter the YouTube video URLs (comma-separated)")
st.subheader("OR")
local = st.file_uploader("Upload local audio file", type=["mp3", "wav"])
save_dir = "./audio"

if youtube:
    urls = youtube.split(",")
    loader = GenericLoader(YoutubeAudioLoader(urls=urls, save_dir=save_dir),
                           OpenAIWhisperParser(api_key=st.secrets["OPENAI_API_KEY"]))
    docs = loader.load()
    text = docs[0].page_content
    st.write(summarize(text))
    youtube_file_path = docs[0].metadata["source"]
    print(youtube_file_path)
    os.remove(youtube_file_path)

if local:
    # Save the uploaded file temporarily to disk
    file_path = os.path.join(save_dir, local.name)
    with open(file_path, "wb") as f:
        f.write(local.getvalue())

    # Transcribe using whisper
    model = whisper.load_model("base", device="cpu")
    result = model.transcribe(file_path, fp16=False)
    transcribed_text = result["text"]
    st.write(summarize(transcribed_text))
    os.remove(file_path)

if memory.buffer:
    st.info(memory.buffer)
