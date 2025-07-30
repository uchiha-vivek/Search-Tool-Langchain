from langchain import hub

def get_react_prompt():
    return hub.pull("hwchase17/react")
