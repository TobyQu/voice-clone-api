# 声音复刻 API

![许可证](https://img.shields.io/github/license/yourusername/voice-clone-api)
![Python 版本](https://img.shields.io/badge/python-3.8%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-green)

基于 FastAPI 的声音复刻服务，提供一套完整的声音克隆与合成 API，支持多样化的音频配置和服务提供者扩展。

**[中文文档](README.zh.md)** | [English](README.md)

## ✨ 功能特点

- 🎙️ **声音复刻**：通过音频样本创建克隆声音
- 📋 **声音管理**：查询、更新和删除已克隆的声音
- 🔊 **语音合成**：将文本转换为使用克隆声音的语音
- 🔌 **可扩展架构**：支持集成多种声音服务提供者
- 🎛️ **丰富参数**：控制音频格式、采样率、音量、语速和语调
- 📝 **文本数组支持**：合成多段文本并自动拼接

## 🛠️ 技术架构

该项目采用模块化设计，可轻松支持多种声音服务提供者：

- 基于抽象基类实现服务提供者接口
- 使用工厂模式创建服务提供者实例
- API 端点与服务实现解耦
- 每个 API 功能使用独立文件管理
- FastAPI 提供高性能异步支持

## 📚 目录结构 