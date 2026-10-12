import os
from openai import OpenAI

# env is set in github.  settings -> command pallet -> type ....>codespace: manage user secret
client = OpenAI(
    api_key=os.environ["API_KEY"],
    base_url=f"{os.environ['OPENAI_API_BASE']}",
)
model = "gpt-6-luna"
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model=model,  # this is your model deployment name
    input=prompt,
    store=False,
)
print(response.output_text)
