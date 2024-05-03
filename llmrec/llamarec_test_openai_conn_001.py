import os
from langchain_openai import AzureChatOpenAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
load_dotenv()

llm = AzureChatOpenAI(
    openai_api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    azure_deployment=os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT_NAME"]
)

message = HumanMessage(
    content="Translate this sentence from English to French. I love programming."
)
print(f'Input: {message.content}')

print(f'Output: {llm.invoke([message]).content}')