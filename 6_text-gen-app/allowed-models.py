import os
from openai import OpenAI
from openai import OpenAIError

client = OpenAI(
    api_key=os.environ["API_KEY"],
    base_url=f"{os.environ['OPENAI_API_BASE']}",
)
models = client.models.list()


models = client.models.list()

working_models = []
failed_models = []

for model in models.data:
    model_id = model.id

    print(f"Testing: {model_id}")

    try:
        response = client.responses.create(model=model_id, input="Say hello", max_output_tokens=30)

        print(f"✅ WORKING: {model_id}")
        working_models.append(model_id)

    except OpenAIError as e:
        print(f"❌ FAILED: {model_id}: {e}")
        failed_models.append(model_id)

print("\n========== RESULTS ==========")

print("\nWORKING MODELS:")
for model in working_models:
    print(model)

print("\nFAILED MODELS:")
for model in failed_models:
    print(model)
# prompt = "Complete the following: Once upon a time there was a"

# response = client.responses.create(
#     model="gpt-4",  # this is your model deployment name
#     input=prompt,
#     store=False,
# )
# print(response.output_text)


# WORKING MODELS:
# gpt-4-turbo-2024-04-09
# gpt-5.6-luna
# gpt-4-turbo
# gpt-4o-mini
# o4-mini
# gpt-4o
# gpt-5.4
# gpt-5.3-codex
# gpt-5.2
# gpt-3.5-turbo
# gpt-6-luna
# o3-mini
