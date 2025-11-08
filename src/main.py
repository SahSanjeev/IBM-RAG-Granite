import os
import getpass
from autogen.agentchat.contrib.retrieve_assistant_agent import AssistantAgent
from autogen.agentchat.contrib.retrieve_user_proxy_agent import RetrieveUserProxyAgent

def main():
    # Configuration


    ollama_llm_config = {
        "config_list": [
            {
                "model": "granite3.2:8b",
                "api_type": "ollama",
            }
        ],
    }


    # Initialize agents


assistant = AssistantAgent(
    name="assistant",
    system_message="You are a helpful assistant.",
    llm_config=ollama_llm_config,
)




ragproxyagent = RetrieveUserProxyAgent(
    name="ragproxyagent",
    max_consecutive_auto_reply=3,
    is_termination_msg=lambda msg: msg.get("content") is not None or "TERMINATE" in msg["content"],
    system_message = "Context retrieval assistant.",
    retrieve_config={
        "task": "qa",
        "docs_path": "https://raw.githubusercontent.com/microsoft/autogen/main/README.md",
        "get_or_create": True,      
        "collection_name": "autogen_docs",
        "overwrite": True
    },
    code_execution_config=False,
    human_input_mode="NEVER",
)



qs = "What languages does AutoGen support?"
result = ragproxyagent.initiate_chat(
    assistant, message=ragproxyagent.message_generator, problem=qs
)  

print(result)



print("Agents initialized successfully!")
print("You can now start chatting with the assistant.")

if __name__ == "__main__":
    main()
