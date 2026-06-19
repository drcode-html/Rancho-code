from google import genai

client = genai.Client(api_key="Removed for safety concerns")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Tell me a fun fact about space"
)

print(response.text)