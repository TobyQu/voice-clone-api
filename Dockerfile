FROM python:3.10-slim

WORKDIR /app

# 复制项目文件
COPY requirements.txt .
COPY app/ ./app/

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 设置环境变量
ENV PORT=8000
ENV HOST=0.0.0.0

# 暴露端口
EXPOSE 8000

# 启动命令
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"] 