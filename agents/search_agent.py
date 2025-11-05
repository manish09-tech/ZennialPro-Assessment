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
def search_research_data(query: str) -> str:
    """Fetch 5 recent research papers or summaries related to the given query."""
    model = genai.GenerativeModel("gemini-2.5-flash")
    prompt = f"List 5 recent research papers or concise summaries about: {query}"
    response = model.generate_content(prompt)
    return response.text.strip()

SearchAgent = ToolNode(tools=[search_research_data])
