import os
import google.generativeai as genai
from langgraph.prebuilt import ToolNode
from langchain.tools import tool
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

@tool
def analyze_research_data(data: str) -> str:
    """Analyze research snippets to extract key themes, trends, and implications."""
    model = genai.GenerativeModel("gemini-2.5-flash")
    prompt = f"""Analyze the following research snippets. Produce:
- A bullet list of key themes
- Emerging trends
- Short 2-sentence implications

Data:
{data}
"""
    response = model.generate_content(prompt)
    return response.text.strip()

AnalysisAgent = ToolNode(tools=[analyze_research_data])
