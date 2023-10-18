from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_generate_course_plan_success():
    response = client.get("/course_plan?pdf_url=https://pedagogie.ac-rennes.fr/sites/pedagogie.ac-rennes.fr/IMG/pdf/pdf_modifiable.pdf&openai_token=your_token")
    assert response.status_code == 200

def test_generate_course_plan_invalid_openai_token():
    response = client.get("/course_plan?pdf_url=https://pedagogie.ac-rennes.fr/sites/pedagogie.ac-rennes.fr&openai_token=invalid_token")
    assert response.status_code == 401

def test_generate_course_plan_invalid_pdf_url():
    response = client.get("/course_plan?pdf_url=https://pedagogie.fr/sites/pedagogie.fr/IMG/pdf/pdf_modifiable.pdf&openai_token=your_token")
    assert response.status_code == 400

def test_generate_course_plan_missing_pdf_url():
    response = client.get("/course_plan?openai_token=your_token")
    assert response.status_code == 422 

def test_generate_course_plan_markdown_format():
    response = client.get("/course_plan?pdf_url=https://pedagogie.fr/sites/pedagogie.fr/IMG/pdf/pdf_modifiable.pdf&openai_token=your_token")
    assert response.status_code == 200
    assert "<h1>" in response.text  
