# Sonic-Sum AI

## Project Description
Sonic Sum is a revolutionary audio summarizer leveraging cutting-edge AI to transform spoken content into concise and engaging summaries. Whether you're dealing with podcast episodes, interviews, or any audio content, Sonic Sum is your intelligent companion, providing you with insightful summaries using advanced natural language processing techniques.

<!-- Overview -->
## Overview
Sonic Sum redefines the landscape of audio content by introducing an AI-driven summarization tool. Imagine having an assistant that listens to your audio files and extracts key insights, creating compelling summaries for your audience. Sonic Sum makes this a reality, offering a seamless solution for content creators, podcasters, and anyone dealing with spoken content.

### 1. Intelligent Summaries
Sonic Sum employs state-of-the-art natural language processing algorithms to generate intelligent and coherent summaries from your audio files. No more tedious manual transcriptions – Sonic Sum extracts the essence of your audio content, making it accessible and engaging.

### 2. Simplified Listening
Long audio files can be overwhelming. Sonic Sum simplifies the listening experience by providing concise summaries, enabling your audience to grasp the core message without investing significant time.

### 3. Topic Customization
Tailor your summaries based on the specific topics covered in your audio content. Sonic Sum understands the nuances of different subjects, allowing you to customize summaries for various niches and themes.

### 4. Enhance Accessibility
Make your audio content accessible to a wider audience. Sonic Sum creates bite-sized summaries that cater to diverse listener preferences, making your content more inclusive and engaging.

Sonic Sum is not just an audio summarizer; it's a transformative tool for content creators seeking to enhance the accessibility and impact of their spoken content. Experience the power of Sonic Sum and redefine the way you share audio content!

<!-- Use Cases -->
## Use Cases
Explore the versatility of Sonic Sum and discover how it can elevate various aspects of your audio content.

### 1. Podcast Precision
Craft concise summaries for your podcast episodes, allowing your audience to quickly grasp the key takeaways. Sonic Sum enhances the impact of your podcast content, attracting and retaining listeners.

### 2. Interview Insights
For interview-based content, Sonic Sum extracts key insights and highlights, enabling your audience to focus on the most valuable parts of the conversation.

### 3. Lecture Digest
Educators and speakers can use Sonic Sum to condense lengthy lectures into digestible summaries, ensuring that the educational content remains engaging and accessible.

### 4. Audiobook Previews
Create engaging previews for your audiobooks, giving potential listeners a taste of the content and encouraging them to explore further.

### 5. Content Accessibility
Improve accessibility for individuals with diverse preferences or limited time. Sonic Sum provides an alternative way to consume audio content, accommodating various lifestyles.


## Tech Stack
- **Langchain**: Langchain is used for natural language processing (NLP) tasks, including text extraction and understanding.
- **Streamlit**: Streamlit is the framework used for creating a user-friendly web interface for the chatbot.
- **Generative AI**: The project incorporates generative AI techniques to generate responses based on the content of the PDFs.
- **Python**: The project is primarily developed in Python.
- **Cohere**: The LLM used for all of text generation is done via Cohere.
- **Whisper**: The LLM used for all of video to text conversion.

## Deployed Link
[Live](https://sonic-sum.streamlit.app/)

<!-- Getting Started -->
## Getting Started

Get Sonic Sum up and running on your local machine by following these simple steps.

### Prerequisites

Ensure you have the following prerequisites installed on your machine:

- [Python](https://www.python.org/downloads/) (version 3.10 or higher)
- [pip](https://pip.pypa.io/en/stable/installation/) (Python package installer)

### Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/ShashankGupta10/Sonic-Sum.git
   cd Sonic-Sum

2. **Obtain API Keys:**
    - Sign in to Cohere and visit Cohere Dashboard to obtain your API key.
    - Sign in to OpenAI and visit API Dashboard to obtain your API key.

3. **Add API Key to Project:**
    - Create a .streamlit folder in the root directory of the project.
    - Add a secrets.toml file and include the following line:
    - COHERE_API_KEY = "your-api-key"
    - OPENAI_API_KEY = "your-api-key"

4. **Run the Application:**
    - Execute the following command:
    ```bash
    streamlit run app.py

### Demo

https://github.com/ShashankGupta10/Sonic-Sum/assets/117008526/de15e062-aa7e-491a-aacc-dd9883d8d224

