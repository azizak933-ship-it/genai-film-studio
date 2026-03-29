# TOOLS.md - Producer Quick Reference

## sessions_spawn

Spawn a specialist agent sub-session. ALWAYS use this to delegate pipeline tasks.

### Correct Usage
```json
sessions_spawn({
  "task": "You are [AgentName]. Here is the project brief and your specific task: ...",
  "agentId": "director",
  "label": "director",
  "runTimeoutSeconds": 120
})
```

### Agent IDs
| Agent              | agentId           |
|--------------------|-------------------|
| Director           | director          |
| Script Writer      | scriptwriter      |
| Screenplay Writer  | screenwriter      |
| Storyboard Artist  | storyboard        |
| DOP                | dop               |
| Cinematographer    | cinematographer   |
| VFX Supervisor     | vfx-supervisor    |
| Prompt Engineer    | prompt-engineer   |
| Film Critic        | film-critic       |

### FORBIDDEN Parameters
- `thinking` — causes error with local models
- `sessionKey` — not needed when using agentId
- `model` — already configured per agent

## sessions_send

Send a message to an already-running session.

```json
sessions_send({
  "sessionKey": "agent:director:main",
  "message": "Here is the updated brief..."
})
```

Use `sessions_send` only if you need to follow up with an agent that's already running.
