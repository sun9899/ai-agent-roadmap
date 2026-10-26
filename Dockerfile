# Dockerfile
# 基础镜像，python3.9精简版
FROM hub-mirror.c.163.com/library/python:3.9-slim

# 设置容器内工作目录
WORKDIR /app

# 先复制依赖文件，利用docker缓存
COPY requirements.txt .

# 安装依赖，不缓存减少镜像大小
RUN pip install --no-cache-dir -r requirements.txt

# 把当前目录所有代码复制进容器
COPY . .

# 对外暴露8000端口（只是声明，不代表自动打开）
EXPOSE 8000

# 启动命令，0.0.0.0很关键，不然外部访问不到
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
