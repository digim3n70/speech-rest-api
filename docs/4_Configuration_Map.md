# Chapter 4: Configuration Map for `HerikaServer/conf/conf.php`

This document serves as the definitive guide to the central configuration file for the HerikaServer application. All major services, feature flags, and AI model parameters are controlled from within `HerikaServer/conf/conf.php`.

---

## 4.1. Core Principle: Environment-Aware Endpoints

A critical detail of this configuration is the use of `127.0.0.1` (localhost) for all local service URLs (e.g., ChromaDB, Whisper, Kokoro). This implies that this PHP application **must** run from within the same network environment as the AI services, which in our case is the `DwemerAI4Skyrim2` WSL instance.

The Windows services (like KoboldCPP) must be referenced by the host machine's IP address.

---

## 4.2. Configuration Domains

The settings are grouped into the following logical domains.

### 4.2.1. Service Selection

These are the master switches that determine which implementation is used for core functions.

| Variable | Example Value | Controls |
| :--- | :--- | :--- |
| `$STTFUNCTION` | `"whisper"` | The active Speech-to-Text engine. |
| `$TTSFUNCTION` | `"kokoro"` | The active Text-to-Speech engine. |
| `$CONNECTORS` | `["koboldcpp"]` | The active Large Language Model (LLM) connector. This is an array, allowing for fallbacks. |

### 4.2.2. Service Endpoint Configuration

This table maps the configuration variables to the specific services we have been running and testing.

| Service | Configuration Variable | Example Value | Notes |
| :--- | :--- | :--- | :--- |
| **Local Whisper (STT)** | `$STT["LOCALWHISPER"]["URL"]` | `"http://127.0.0.1:3000/transcribe"` | Points to the `speech-rest-api` service. |
| **Kokoro (TTS)** | `$conf['kokoro_host']`, `$conf['kokoro_port']` | `"localhost"`, `"8881"` | Points to the Kokoro Docker container. |
| **ChromaDB (Memory)** | `$FEATURES["MEMORY_EMBEDDING"]["CHROMADB_URL"]` | `"http://127.0.0.1:8000"` | Points to the ChromaDB service. |
| **KoboldCPP (LLM)** | `$CONNECTOR["koboldcpp"]["url"]`| `"http://127.0.0.1:5001"` | **IMPORTANT:** This must be changed to the Windows Host IP (e.g., `http://192.168.1.100:5001`) for the WSL instance to connect to it. |

### 4.2.3. Feature Flags

These settings enable or disable major application subsystems.

| Feature | Configuration Variable | Behavior |
| :--- | :--- | :--- |
| **Long-Term Memory** | `$FEATURES["MEMORY_EMBEDDING"]["ENABLED"]` | `true` or `false`. Toggles the ChromaDB integration. |
| **Cost Monitoring** | `$FEATURES["COST_MONITOR"]["ENABLED"]` | `true` or `false`. Toggles the token/cost counter service. |

---

## 4.3. Standard Operational Procedures

### To Change the Active TTS Service:

1.  Set the `$TTSFUNCTION` variable to the desired service name (e.g., `"mimic3"`).
2.  Ensure the corresponding configuration block (e.g., `$TTS["MIMIC3"]`) has the correct URL, voice, and other parameters.
3.  Restart the HerikaServer application.

### To Switch from a Local LLM to an API-based one:

1.  Change the `$CONNECTORS` array to `["openai"]`.
2.  Ensure the `$CONNECTOR["openai"]["API_KEY"]` is set correctly.
3.  Restart the HerikaServer application.