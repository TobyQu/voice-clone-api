# Voice Clone API

![License](https://img.shields.io/github/license/tobyqu/voice-clone-api)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-green)

A modular voice cloning API service built with FastAPI. Supports CosyVoice voice replication, customizable audio parameters, and extensible architecture for multiple service providers.

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