import os
from openai import OpenAI

# env is set in github.  settings -> command pallet -> type ....>codespace: manage user secret
client = OpenAI(
    api_key=os.environ["API_KEY"],
    base_url=f"{os.environ['OPENAI_API_BASE']}",
)
model = model = "gpt-6-luna"
# Create your first prompt
text_prompt = " My foot hurts, what can be wrong?"

response = client.responses.create(
    model=model,
    input=[
        {"role": "system", "content": "I'm a doctor, specialist on surgery"},
        {"role": "user", "content": text_prompt},
    ],
    store=False,
)

print(response.output_text)
