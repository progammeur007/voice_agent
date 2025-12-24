import pandas as pd
import logging
import os
from livekit.agents import llm
from tavily import TavilyClient

logger = logging.getLogger("voice-agent")

# Initialize Tavily client here
# Ensure TAVILY_API_KEY is in your .env
tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
@llm.function_tool(description="Search for Maharashtra government schemes using keywords like farmer, woman, or student.")
def search_schemes(keyword: str) -> str:
    """PRIMARY TOOL: Searches the local CSV database for matching government schemes."""
    print(f"\n🧠 [REASONING] User asked about '{keyword}'. Searching RAG (CSV)...")
    try:
        df = pd.read_csv("data/schemes.csv")
        # Fuzzy search to handle partial matches
        results = df[df.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)]

        if results.empty:
            print(f"⚠️  [RAG RESULT] No records found for '{keyword}'.")
            return f"No records found for '{keyword}' in the official CSV database."

        print(f"✅ [RAG RESULT] Found {len(results)} matches.")
        output = [f"Scheme: {r['scheme_name']}, Age: {r['min_age']}, Income: {r['income_limit']}" for _, r in results.iterrows()]
        return "\n".join(output)
    except Exception as e:
        return f"Database error: {e}"

@llm.function_tool(description="Search the web for the latest updates or news about Maharashtra schemes.")
def search_web(query: str) -> str:
    """SECONDARY TOOL: Use ONLY if CSV info is missing or user wants latest 2025 updates."""
    print(f"\n🌐 [REASONING] Expanding search to Web for: {query}")
    try:
        # Using the client initialized above
        search_result = tavily_client.search(query=query + " Maharashtra govt scheme 2025", search_depth="advanced")
        print(f"✅ [WEB RESULT] Live updates found.")
        return str(search_result['results'])
    except Exception as e:
        return f"Web search error: {e}"

@llm.function_tool(description="Check user eligibility for a scheme based on age and income.")
def check_eligibility(user_age: int, user_income: int, scheme_min_age: int, scheme_income_limit: int) -> str:
    """Performs eligibility validation using logic."""
    print(f"\n⚖️  [REASONING] Validating: Age {user_age}, Income {user_income}")
    reasons = []
    if user_age < scheme_min_age:
        reasons.append(f"Age {user_age} is below {scheme_min_age}.")
    if scheme_income_limit > 0 and user_income > scheme_income_limit:
        reasons.append(f"Income {user_income} exceeds {scheme_income_limit}.")
    
    return "User is ELIGIBLE." if not reasons else "Ineligible: " + " | ".join(reasons)