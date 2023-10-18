from fastapi import FastAPI, HTTPException,Depends
import logging 
import prompts
from utils import *

app = FastAPI(
    title="Notre API de génération de plans de cours",
    description="Une API pour générer des plans de cours à partir de PDF."
) 

@app.get("/course_plan")
async def generate_course_plan(pdf_url: str, token: str = Depends(validate_openai_token)):
    """
    Génère un plan de cours basé sur le contenu extrait d'un PDF.

    Args:
        pdf_url (str): L'URL du PDF en ligne.

    Returns:
        str: Le plan de cours généré au format Markdown.

    Raises:
        HTTPException: En cas d'erreur lors de l'extraction du PDF ou de l'appel à l'API OpenAI.
    """
    try:
        extracted_text = extract_text_from_pdf(pdf_url)

        #Si le pdf n'est pas pertinent on l'élimine
        if not is_pdf_relevant(extracted_text):
            raise HTTPException(status_code=400, detail="Contenu PDF non pertinent")
        
        #Définit le model ,on va opter pour le modèle gpt turbo 3.5-turbo-0613
        chat = ChatOpenAI(temperature=0,model="gpt-3.5-turbo-0613")

        #Séléctionne le prompt correspondant
        system_template = prompts.generate_educational_content

        #Crée un modèle de message système (SystemMessagePromptTemplate) à partir du modèle système (system_template) fourni.
        system_message_prompt_template = SystemMessagePromptTemplate.from_template(system_template)
    
       # Crée un modèle de message de chat (ChatPromptTemplate) à partir d'un modèle de message système.
        chat_prompt_template = ChatPromptTemplate.from_messages([system_message_prompt_template])

       # Formate le modèle de chat avec le contenu extrait du PDF.
        final_prompt = chat_prompt_template.format_prompt(content=extracted_text).to_messages()

       # Appelle le modèle de chat avec le prompt final.
        completion = chat(final_prompt)

        # Retourne la réponse en français sous forme de balisage Markdown.
        return to_markdown(translate_to_French(completion.content))

    except Exception as e:
        logging.error(f"Erreur lors de l'appel à l'API OpenAI : {str(e)}")
        raise HTTPException(status_code=500, detail="Erreur lors de l'appel à l'API OpenAI")
