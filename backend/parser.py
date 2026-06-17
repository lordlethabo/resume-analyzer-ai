from pypdf import PdfReader
import io


SKILLS = [
    "python",
    "sql",
    "azure",
    "aws",
    "oracle cloud",
    "oci",
    "docker",
    "terraform",
    "linux",
    "git",
    "github",
    "html",
    "css",
    "javascript",
    "fastapi",
    "api",
    "postgresql",
    "firebase",
    "vercel",
    "cloud",
    "devops",
]


def read_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return ""


def extract_pdf_text(file_content):
    pdf = PdfReader(io.BytesIO(file_content))
    text = ""

    for page in pdf.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def find_skills(text):
    text = text.lower()
    found_skills = []

    for skill in SKILLS:
        if skill in text:
            found_skills.append(skill)

    return found_skills
