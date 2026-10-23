from openai import OpenAI
import os

# 初始化客户端
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

# 【核心】消息历史列表，全程维护，所有对话内容都按顺序存在这里
# 每次调用大模型，都要把这个完整列表发过去，模型才能看懂上下文
messages = [
    # 开头放系统提示词，整个对话全程生效
    {"role": "system", "content": "你是一个简洁的AI助手，回答简短"}
]

# 循环3次，实现3轮连续对话
for i in range(3):
    # 接收用户在控制台输入的文字
    user_input = input("\n你：")

    # 把用户说的话，追加到消息历史末尾
    messages.append({"role": "user", "content": user_input})

    # 调用大模型，传入【完整的消息历史】，不是只传当前这一句
    resp = client.chat.completions.create(
        model="deepseek-chat",
        messages=messages,
        stream=False
    )

    # 取出AI的回答文本
    ai_reply = resp.choices[0].message.content
    print(f"AI：{ai_reply}")

    # 【关键】把AI的回答也追加到消息历史里
    # 下一轮对话时，连同历史一起发给模型，它就“记得”之前的内容了
    messages.append({"role": "assistant", "content": ai_reply})
