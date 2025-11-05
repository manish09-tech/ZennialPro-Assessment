from agents.analysis_agent import analyze_research_data

sample_data = """
    Recent AI models like GPT-5 and Gemini 2.5 are focusing on multimodal understanding.
    Advances in federated learning are improving data privacy in healthcare.
    Reinforcement learning applications are expanding into robotics and process automation.
    """
result = analyze_research_data.invoke({"data": sample_data})
print("=== Research Analysis ===\n")
print(result)
