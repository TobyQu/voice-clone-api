# Voice Clone API

![License](https://img.shields.io/github/license/yourusername/voice-clone-api)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-green)

A voice cloning and synthesis API service based on FastAPI, providing a complete set of voice cloning and synthesis APIs with support for diverse audio configurations and extensible service providers.

**[中文文档](README.zh.md)** | [English](README.md)

## ✨ Features

- 🎙️ **Voice Cloning**: Create clone voices from audio samples
- 📋 **Voice Management**: Query, update, and delete cloned voices
- 🔊 **Speech Synthesis**: Convert text to speech using cloned voices
- 🔌 **Extensible Architecture**: Support for integrating various voice service providers
- 🎛️ **Rich Parameters**: Control audio format, sample rate, volume, speech rate, and pitch
- 📝 **Text Array Support**: Synthesize multiple text segments and automatically concatenate them

## 🛠️ Technical Architecture

This project adopts a modular design that easily supports multiple voice service providers:

- Service provider interfaces based on abstract base classes
- Factory pattern for creating service provider instances
- Decoupling of API endpoints and service implementations
- Each API function managed in a separate file
- High-performance async support with FastAPI

## 📚 Directory Structure

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