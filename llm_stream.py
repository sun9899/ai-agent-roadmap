from openai import OpenAI
import os

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

stream = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "你是一个幽默的助手"},
        {"role": "user", "content": "讲一个很短的程序员笑话"}
    ],
    stream=True  # 开启流式输出
)

# 逐块打印，模拟打字效果
for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="")
