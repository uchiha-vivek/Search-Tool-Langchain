from langchain.agents import create_react_agent, AgentExecutor
from llm.azure_openai import get_azure_openai_llm
from tools.search_tool import get_duckduckgo_tool
from prompts.react_prompt import get_react_prompt

def get_news_agent():
    llm = get_azure_openai_llm()
    search_tool = get_duckduckgo_tool()
    prompt = get_react_prompt()

    agent = create_react_agent(
        llm=llm,
        tools=[search_tool],
        prompt=prompt
    )

    agent_executor = AgentExecutor(
        agent=agent,
        tools=[search_tool],
        verbose=True
    )

    return agent_executor
