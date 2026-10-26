# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
import os

# 创建app实例，uvicorn main:app 就是读取这里的app
app = FastAPI(title="AI Agent对话接口")

# 从环境变量读取密钥，不在代码里写死！
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

# 定义前端发过来的数据格式
class ChatRequest(BaseModel):
    user_msg: str
    session_id: str | None = None

# 健康检查接口，浏览器直接访问
@app.get("/")
def home():
    return {"msg": "服务已经跑起来啦 ✅"}

# AI对话接口
@app.post("/agent/chat")
def agent_chat(req: ChatRequest):
    result = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role":"system", "content":"你是简洁友好的AI助手"},
            {"role":"user", "content": req.user_msg}
        ],
        stream=False
    )
    return {
        "reply": result.choices[0].message.content,
        "session_id": req.session_id
    }
