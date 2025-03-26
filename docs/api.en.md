# API Documentation

The Voice Clone API provides the following main functions: voice cloning, voice management, and speech synthesis.

## Basic Information

- **Base Path**: `/api/v1/voice`
- **Content Type**: `application/json`

## Authentication

The current version configures the API key through environment variables and does not require request-level authentication.

## Endpoint Overview

| Method | Path                    | Description           |
|--------|-------------------------|-----------------------|
| POST   | /voices                 | Create a voice clone  |
| GET    | /voices                 | Get voice list        |
| GET    | /voices/{voice_id}      | Get voice details     |
| PUT    | /voices/{voice_id}      | Update a voice        |
| DELETE | /voices/{voice_id}      | Delete a voice        |
| POST   | /synthesize             | Speech synthesis      |

## Detailed Specifications

### Create Voice Clone

Create a new cloned voice.

**Request**: 