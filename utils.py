from fastapi import FastAPI, HTTPException, Query
import os
import openai
import logging 
import io
import requests
import markdown2
import PyPDF2
from langchain.chat_models import ChatOpenAI
from langchain.prompts import HumanMessagePromptTemplate, ChatPromptTemplate, SystemMessagePromptTemplate
import prompts

app = FastAPI(
    title="Notre API de génération de plans de cours",
    description="Une API pour générer des plans de cours à partir de PDF."
) 

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key=OPENAI_API_KEY

def validate_openai_token(token: str = Query(..., description="Token d'API OpenAI")):
    if token != OPENAI_API_KEY :
        raise HTTPException(status_code=401, detail="Non autorisé")
    
def extract_text_from_pdf(pdf_url: str):
    try:
        response=requests.get(pdf_url)
        file = io.BytesIO(response.content)
        reader = PyPDF2.PdfReader(file)
        pages = reader.pages
        extracted_text = "".join([page.extract_text() for page in pages])

        return extracted_text
    
    except Exception as e:
        logging.error(f"Erreur lors de l'extraction du texte du PDF : {str(e)}")
        raise HTTPException(status_code=500, detail=f"Échec de l'extraction du texte du PDF")
    
def translate_to_French(text_to_translate):
    # initialiser ChatGPT model
    chat = ChatOpenAI(temperature=0,model="gpt-3.5-turbo-0613")
    
    system_template = prompts.translate_template
    system_message_prompt_template = SystemMessagePromptTemplate.from_template(
        system_template)
    human_template = "{sample_text}"
    human_message_prompt_template = HumanMessagePromptTemplate.from_template(human_template)
    chat_prompt_template = ChatPromptTemplate.from_messages(
        [system_message_prompt_template, human_message_prompt_template])
    final_prompt = chat_prompt_template.format_prompt(output_language="French",
                            sample_text=text_to_translate).to_messages()
    
    # Générer l'output en appelant le ChatGPT model et en passant le prompt

    completion = chat(final_prompt)

    return completion.content

def to_markdown(text):

    markdown_plan = markdown2.markdown(text)

    return markdown_plan 

def is_pdf_relevant(text):

    chat = ChatOpenAI(temperature=0,model="gpt-3.5-turbo-0613")
    
    system_template = prompts.is_relevant_template
    
    system_message_prompt_template = SystemMessagePromptTemplate.from_template(
        system_template)
    
    chat_prompt_template = ChatPromptTemplate.from_messages(
        [system_message_prompt_template])
    
    final_prompt = chat_prompt_template.format_prompt(extracted_text=text).to_messages()

    # Générer l'output en appelant le ChatGPT model et en passant le prompt

    completion = chat(final_prompt)
    return completion.content

