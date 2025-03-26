# API Documentation

The Voice Clone API provides the following main functions: voice cloning, voice management, and speech synthesis.

## Basic Information

- **Base Path**: `/api/v1/voice`
- **Content Type**: `application/json`

## Authentication

The current version configures the API key through environment variables and does not require request-level authentication.

## Official Reference Documentation

This project is based on Alibaba Cloud's voice services. Detailed official documentation can be found at:

- [Alibaba Cloud Speech Synthesis and Speech Recognition Documentation](https://help.aliyun.com/zh/model-studio/developer-reference/speech-synthesis-and-speech-recognition/?spm=a2c4g.11186623.help-menu-2400256.d_3_3_7.12714308a2iXoG&scm=20140722.H_2868450._.OR_help-T_cn~zh-V_1)
- [CosyVoice Speech Synthesis API Documentation](https://help.aliyun.com/zh/model-studio/developer-reference/cosyvoice)

## Endpoint Overview

| Method | Path                     | Description         |
|--------|--------------------------|------------|
| POST   | /voices                  | Create voice clone |
| GET    | /voices                  | Get voice list   |
| GET    | /voices/{voice_id}       | Get voice details |
| PUT    | /voices/{voice_id}       | Update voice      |
| DELETE | /voices/{voice_id}       | Delete voice      |
| POST   | /synthesize              | Speech synthesis |

## Detailed Description

### Create Voice Clone

Create a new voice clone.

**Request**: 