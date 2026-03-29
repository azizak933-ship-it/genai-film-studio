# 🎬 GenAI Film Studio

A fully local AI-powered filmmaking pipeline with **32 specialized agents** across **9 production phases**, running entirely on your machine via [Ollama](https://ollama.ai).

## Features

- **32 AI Agents** — From Director to Colorist, each with unique expertise
- **Chat Mode** — Discuss ideas with your entire film crew simultaneously
- **@mention** — Tag specific agents like `@Orson` or `@Nova` for targeted advice
- **Pipeline Mode** — Run the full 9-agent production pipeline end-to-end
- **Custom GPTs** — Create your own specialized agents
- **Memory** — Learns your preferences across conversations
- **DeepSeek Operations Manager** — Cortex monitors everything and gives status updates
- **Projects** — Multiple parallel projects with persistent chat history
- **100% Local** — No cloud APIs needed, runs entirely on Ollama

## Agents

| Phase | Agents |
|-------|--------|
| 🟠 Orchestration | Max (Producer), Cortex (Ops Manager - DeepSeek) |
| 🟣 Pre-Production Story | Scout, Vera, Felix, Orson, Cast |
| 🟢 Visual Development | Arte, Pixel, Sage, Mila, Luca |
| 🔵 Cinematography | Kai, Lens |
| 🩷 Audio | Rex, Echo |
| 🟡 Prompt Engineering | Nova, Flux, Reel, Sonic |
| 🟠 AI Production | Frame, Motion, Lyra, Rex+, Zara |
| 🟢 Post-Production | Theo, Cut, Hue, Blend |
| 🔵 QA & Delivery | Align, Iris, Sub, Promo |

## Requirements

- [Node.js](https://nodejs.org) 18+
- [Ollama](https://ollama.ai) installed and running
- Models: `qwen2.5:7b` and `deepseek-r1:8b`

## Quick Start

```bash
# 1. Clone
git clone https://github.com/YOUR_USERNAME/genai-film-studio.git
cd genai-film-studio

# 2. Pull required models
ollama pull qwen2.5:7b
ollama pull deepseek-r1:8b

# 3. Start Ollama with parallel processing
# Windows:
set OLLAMA_NUM_PARALLEL=9 && ollama serve
# Mac/Linux:
OLLAMA_NUM_PARALLEL=9 ollama serve

# 4. Start the studio
npm start

# 5. Open
# http://localhost:3000
```

## Usage

### Chat Mode
Type a message and all active agents respond simultaneously with their professional perspective.

### @mention
Type `@` to see the agent list. Select an agent to direct your message to them specifically:
- `@Orson what lens would you use for this scene?`
- `@Nova @Flux generate prompts for the opening shot`

### Custom GPTs
Click "+ Create GPT" in the sidebar to build your own specialized agent with a custom system prompt.

### Pipeline Mode
Click "Run Pipeline" to execute the full 9-agent film production sequence with detailed thinking and output.

## Tech Stack

- **Runtime**: Node.js (vanilla, zero dependencies)
- **LLM**: Ollama (local)
- **Models**: qwen2.5:7b (agents), deepseek-r1:8b (operations)
- **Frontend**: Vanilla HTML/CSS/JS
- **Storage**: JSON files

## License

MIT
