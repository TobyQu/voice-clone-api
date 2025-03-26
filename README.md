# 声音复刻 API

基于 FastAPI 的声音复刻服务，支持声音克隆、管理和语音合成。

## 功能特点

- 声音复刻（创建克隆声音）
- 声音列表查询
- 获取声音详情
- 更新声音
- 删除声音
- 语音合成（支持丰富的参数配置）

## 架构设计

该项目采用模块化设计，可轻松支持多种声音服务提供者：

- 基于抽象基类实现提供者接口
- 使用工厂模式创建服务提供者实例
- API 端点与服务实现解耦
- 每个 API 功能使用独立的文件管理

## 安装与配置

### 环境要求

- Python 3.8+
- pip 或 conda

### 使用 conda 创建环境

```bash
# 创建环境
conda create -n voice-clone-api python=3.10

# 激活环境
conda activate voice-clone-api

# 安装依赖
pip install -r requirements.txt
```

### 配置环境变量

创建 `.env` 文件： 