from openai import OpenAI
import os

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

resp = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "你是AI Agent开发助手，回答简洁"},
        {"role": "user", "content": "简单说什么是AI Agent"}
    ],
    stream=False
)

answer = resp.choices[0].message.content
print("大模型回复：", answer)
