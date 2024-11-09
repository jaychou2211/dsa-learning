FROM python:3.11-slim

WORKDIR /dsa-learning

# 安裝基本開發工具
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

# 安裝常用的演算法相關套件
RUN pip install --no-cache-dir -r requirements.txt || true