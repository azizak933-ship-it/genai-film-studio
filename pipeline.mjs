/**
 * GenAI Film Studio — Pipeline Orchestrator
 *
 * Usage: node pipeline.mjs "Your film brief here"
 *
 * Calls each specialist agent in sequence via the clawdbot gateway.
 * No model tool-calling required — this script handles all orchestration.
 */

import { randomUUID } from "node:crypto";
import { appendFileSync, writeFileSync, existsSync } from "node:fs";
import { callGateway } from "file:///C:/Users/Abcom/AppData/Roaming/npm/node_modules/clawdbot/dist/gateway/call.js";

const TIMEOUT_MS = 8 * 60 * 1000; // 8 minutes per agent
const LOG_FILE = "C:\\Users\\Abcom\\genai-film\\PRODUCTION_LOG.md";

const PIPELINE = [
  { id: "director",       name: "🎥 Orson (Director)",         session: "agent:director:main" },
  { id: "scriptwriter",   name: "✍️  Vera (Script Writer)",     session: "agent:scriptwriter:main" },
  { id: "screenwriter",   name: "📄 Felix (Screenplay Writer)", session: "agent:screenwriter:main" },
  { id: "storyboard",     name: "🖼️  Mila (Storyboard Artist)", session: "agent:storyboard:main" },
  { id: "dop",            name: "💡 Luca (DOP)",                session: "agent:dop:main" },
  { id: "cinematographer",name: "📷 Kai (Cinematographer)",     session: "agent:cinematographer:main" },
  { id: "vfx-supervisor", name: "✨ Zara (VFX Supervisor)",     session: "agent:vfx-supervisor:main" },
  { id: "prompt-engineer",name: "⚡ Nova (Prompt Engineer)",    session: "agent:prompt-engineer:main" },
  { id: "film-critic",    name: "🎭 Iris (Film Critic)",        session: "agent:film-critic:main" },
];

async function sendToAgent(sessionKey, message) {
  const idem = randomUUID();

  console.log(`  → Sending to ${sessionKey}...`);

  // Send message to agent session
  const response = await callGateway({
    method: "agent",
    params: {
      message,
      sessionKey,
      idempotencyKey: idem,
      deliver: false,
      channel: "webchat",
    },
    timeoutMs: 15_000,
  });

  const runId = response?.runId ?? idem;
  console.log(`  → Run started: ${runId}`);

  // Wait for completion
  const wait = await callGateway({
    method: "agent.wait",
    params: { runId, timeoutMs: TIMEOUT_MS },
    timeoutMs: TIMEOUT_MS + 5000,
  });

  if (wait?.status === "timeout") throw new Error(`Agent timed out after ${TIMEOUT_MS / 1000}s`);
  if (wait?.status === "error") throw new Error(`Agent error: ${wait?.error}`);

  // Get the response from chat history
  const history = await callGateway({
    method: "chat.history",
    params: { sessionKey, limit: 5 },
    timeoutMs: 10_000,
  });

  const messages = history?.messages ?? [];
  // Find last assistant message
  for (let i = messages.length - 1; i >= 0; i--) {
    const msg = messages[i];
    if (msg?.role === "assistant") {
      const content = msg.content;
      if (typeof content === "string") return content;
      if (Array.isArray(content)) {
        const text = content.filter(c => c?.type === "text").map(c => c.text).join("\n");
        if (text) return text;
      }
    }
  }
  return "[No response received]";
}

function logEntry(agentName, received, delivered) {
  const timestamp = new Date().toLocaleString();
  const entry = `\n### ${agentName} — ${timestamp}\n**Received:** ${received.slice(0, 100)}...\n**Delivered:** ${delivered.slice(0, 200)}...\n---\n`;
  appendFileSync(LOG_FILE, entry, "utf8");
}

async function runPipeline(brief) {
  console.log("\n🎬 GenAI Film Studio — Pipeline Starting");
  console.log("=".repeat(50));
  console.log(`Brief: ${brief}\n`);

  // Reset log for this run
  const header = `# GenAI Film Studio — Production Log\n\nBrief: ${brief}\nStarted: ${new Date().toLocaleString()}\n\n---\n`;
  writeFileSync(LOG_FILE, header, "utf8");

  const outputs = {};
  let previousOutput = brief;

  for (const agent of PIPELINE) {
    console.log(`\n[${PIPELINE.indexOf(agent) + 1}/${PIPELINE.length}] ${agent.name}`);

    try {
      // Build context message based on pipeline position
      let message;
      const idx = PIPELINE.indexOf(agent);

      if (idx === 0) {
        // Director gets the raw brief
        message = `DIRECTOR BRIEF: ${brief}\n\nGive me: creative vision, tone, themes, key scenes, shot style.`;
      } else if (idx <= 3) {
        // Story/visual chain: each agent gets previous output
        const prevAgent = PIPELINE[idx - 1];
        message = `From ${prevAgent.name}:\n\n${previousOutput}\n\n---\nNow do your job based on the above.`;
      } else if (idx === 4 || idx === 5) {
        // DOP and Cinematographer both get storyboard output
        const storyboardOut = outputs["storyboard"] ?? previousOutput;
        message = `STORYBOARD:\n\n${storyboardOut}\n\n---\nNow do your job based on the above.`;
      } else {
        // VFX, Prompt, Critic get a summary of key outputs (keep context short for speed)
        const storyboardOut = outputs["storyboard"] ?? "";
        const dopOut = outputs["dop"] ?? "";
        const cineOut = outputs["cinematographer"] ?? "";
        const screenOut = outputs["screenwriter"] ?? "";
        const summary = [
          storyboardOut && `## Storyboard\n${storyboardOut.slice(0, 800)}`,
          dopOut && `## DOP\n${dopOut.slice(0, 500)}`,
          cineOut && `## Cinematographer\n${cineOut.slice(0, 500)}`,
          screenOut && `## Screenplay\n${screenOut.slice(0, 600)}`,
        ].filter(Boolean).join("\n\n");
        message = `PRODUCTION CONTEXT:\n\n${summary}\n\n---\nNow do your job based on the above. Be concise.`;
      }

      const reply = await sendToAgent(agent.session, message);
      outputs[agent.id] = reply;
      previousOutput = reply;

      logEntry(agent.name, message, reply);
      console.log(`  ✓ Done (${reply.length} chars)`);

    } catch (err) {
      console.error(`  ✗ Error: ${err.message}`);
      outputs[agent.id] = `[Error: ${err.message}]`;
      logEntry(agent.name, "error", err.message);
    }
  }

  console.log("\n" + "=".repeat(50));
  console.log("✅ Pipeline complete!");
  console.log(`📋 Full log: ${LOG_FILE}`);
  console.log("\n🎭 FILM CRITIC FINAL VERDICT:");
  console.log("-".repeat(40));
  console.log(outputs["film-critic"] ?? "[No critic output]");
}

// Main
const brief = process.argv.slice(2).join(" ");
if (!brief) {
  console.error("Usage: node pipeline.mjs \"Your film brief here\"");
  process.exit(1);
}

runPipeline(brief).catch(err => {
  console.error("Pipeline failed:", err.message);
  process.exit(1);
});
