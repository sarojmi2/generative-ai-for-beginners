##----------------------------------------------------------------------------
## “a zero-shot, role-based prompt template with a required response format”
##-----------------------------------------------------------------------------

from openai import OpenAI
import os

# configure Azure OpenAI service client
client = OpenAI(
    api_key=os.environ["API_KEY"],
    base_url=f"{os.environ['OPENAI_API_BASE']}",
)

# add your completion code
question = input("Ask your questions on python language to your study buddy: ")
prompt = f"""
You are an expert on the python language.

Whenever certain questions are asked, you need to provide response in below format.

- Concept
- Example code showing the concept implementation
- explanation of the example and how the concept is done for the user to understand better.

Provide answer for the question: {question}
"""
# make a request using the Responses API
response = client.responses.create(model="gpt-6-luna", input=prompt, store=False)

# print response
print(response.output_text)
