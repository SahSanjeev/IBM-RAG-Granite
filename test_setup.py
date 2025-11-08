import os
from dotenv import load_dotenv
from autogen.agentchat.contrib.retrieve_assistant_agent import AssistantAgent
from autogen.agentchat.contrib.retrieve_user_proxy_agent import RetrieveUserProxyAgent

# Load environment variables
load_dotenv()

def test_autogen_setup():
    print("Testing AutoGen setup with Ollama...")
    
    # Ollama configuration
    ollama_config = {
        "config_list": [
            {
                "model": os.getenv("OLLAMA_MODEL", "granite3.2:8b"),
                "api_base": os.getenv("OLLAMA_API_BASE", "http://localhost:11434"),
                "api_type": "ollama",
            }
        ],
    }

    try:
        # Initialize agents
        assistant = AssistantAgent(
            name="assistant",
            system_message="You are a helpful assistant. Reply 'TEST PASSED' if you receive this message.",
            llm_config=ollama_config,
        )

        print("✅ Assistant agent initialized successfully!")
        
        # Simple test message
        response = assistant.generate_reply(
            messages=[{"role": "user", "content": "Test message"}],
            sender=assistant
        )
        print(f"\n🤖 Assistant response: {response}")
        
    except Exception as e:
        print(f"❌ Error during test: {str(e)}")
        return False
    
    return True

if __name__ == "__main__":
    print("🚀 Starting AutoGen setup test...")
    if test_autogen_setup():
        print("\n🎉 Setup test completed successfully!")
    else:
        print("\n❌ Setup test failed. Please check the error messages above.")
