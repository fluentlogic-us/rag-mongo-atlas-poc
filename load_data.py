import os

# Set the MongoDB URI, DB, Collection Names
mongodb_uri = os.getenv("MONGODB_URI")
llm_api_key = os.getenv("LLM_API_KEY")
if mongodb_uri is None or llm_api_key is None:
    raise ValueError("Please set the MONGODB_URI and LLM_API_KEY environment variables.")




