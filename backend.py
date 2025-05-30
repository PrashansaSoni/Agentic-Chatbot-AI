from pydantic import BaseModel
from typing import List

class RequestState(BaseModel):
    model_name:str
    model_provider:str
    system_prompt:str
    messages:List[str]
    allow_search:bool


from fastapi import FastAPI
from agentic import get_response_from_ai_agent

ALLOWED_MODEL_NAMES=["llama3-70b-8192","llama-3.3-70b-versatile","gpt-4o-mini"]

app=FastAPI(title="LangGraph AI Agent")

@app.post("/chat")
def chat_endpoint(request:RequestState):
    """
    API Endpoint to interact with the chatbot using LangGraph and search tools.
    It dynamically selects the model specifies in the requests
    """
    if request.model_name not in ALLOWED_MODEL_NAMES:
        return {"error":"Invalid model name.Kindly select a valid model"}
    
    llm_id=request.model_name
    query=request.messages
    allow_search=request.allow_search
    system_prompt=request.system_prompt
    provider=request.model_provider
    
    response = get_response_from_ai_agent(llm_id,query,allow_search,system_prompt,provider)
    return response

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="127.0.0.1",port=9999)