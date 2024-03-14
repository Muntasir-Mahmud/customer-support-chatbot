from fastapi import FastAPI
from models.chatbot_query import ChatbotQueryInput, ChatbotQueryOutput
from utils.async_utils import async_retry

app = FastAPI(
    title="Customer Support Chatbot",
    description="Endpoints for a customer support chatbot",
)


@async_retry(max_retries=10, delay=1)
async def invoke_llm_with_retry(query: str):
    """
    Retry the agent if a tool fails to run. This can help when there
    are intermittent connection issues to external APIs.
    """
    pass
    # return await hospital_rag_agent_executor.ainvoke({"input": query})



@app.get("/")
async def get_status():
    return {"status": "running"}


@app.post("/chatbot")
async def query_chatbot(
    query: ChatbotQueryInput,
) -> ChatbotQueryOutput:
    query_response = await invoke_agent_with_retry(query.text)
    query_response["intermediate_steps"] = [
        str(s) for s in query_response["intermediate_steps"]
    ]

    return query_response
