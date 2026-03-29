/**
 * GenAI Film Studio — Standalone Pipeline (No clawdbot required)
 * Uses Ollama HTTP API directly.
 *
 * Usage: node run.mjs "Your film brief here"
 */

import { writeFileSync, appendFileSync } from "node:fs";

const OLLAMA_URL = "http://127.0.0.1:11434/api/chat";
const MODEL = "qwen2.5:7b";
const LOG_FILE = "C:\\Users\\Abcom\\genai-film\\PRODUCTION_LOG.md";

// ─── Agent Definitions ────────────────────────────────────────────────────────

// Reasoning prefix injected into every agent's system prompt
const THINK_PREFIX = `Before giving your final answer, reason through your decision in a short "## My Thinking" section. Consider the material carefully, weigh the options, then commit to your choices. After thinking, write your actual deliverable under "## My Output".

`;

const AGENTS = [
  {
    id: "director",
    name: "🎥 Orson — Director",
    system: THINK_PREFIX + `You are Orson, a visionary film director. You speak with authority about cinema.
When given a film brief, deliver:
- Logline (1 sentence)
- Creative Vision (tone, mood, emotional arc)
- Style References (2-3 films)
- Core Themes (3 bullet points)
- Key Scenes (3-5 scene descriptions)
Be specific and cinematic. Keep total response under 500 words.`,
    buildMessage: (brief, _) =>
      `Film brief: ${brief}\n\nDeliver your director's vision.`,
  },
  {
    id: "scriptwriter",
    name: "✍️  Vera — Script Writer",
    system: THINK_PREFIX + `You are Vera, a narrative-obsessed script writer. You find the human truth in any story.
When given a director's vision, deliver:
- Characters (2-3 with brief profiles)
- Story Arc (setup, conflict, resolution)
- 3-5 Key Dialogue Lines
- Central Emotional Moment
Keep total response under 400 words.`,
    buildMessage: (brief, outputs) =>
      `Director's vision:\n${outputs.director}\n\nWrite the story treatment.`,
  },
  {
    id: "screenwriter",
    name: "📄 Felix — Screenplay Writer",
    system: THINK_PREFIX + `You are Felix, a screenplay writer obsessed with proper format.
Write in industry-standard format: INT./EXT. sluglines, lean action lines, character cues, dialogue.
No "we see". No passive voice. Maximum 2 scenes from the story, fully formatted.
Keep total response under 500 words.`,
    buildMessage: (brief, outputs) =>
      `Story treatment:\n${outputs.scriptwriter}\n\nWrite 2 formatted screenplay scenes.`,
  },
  {
    id: "storyboard",
    name: "🖼️  Mila — Storyboard Artist",
    system: THINK_PREFIX + `You are Mila, a storyboard artist who thinks in frames.
For each scene, list 4-6 shots with: Shot number, Type (ECU/CU/MS/WS/EWS), Subject, Action, Camera move, Mood.
Use a numbered list format. Keep total response under 400 words.`,
    buildMessage: (brief, outputs) =>
      `Screenplay:\n${outputs.screenwriter}\n\nCreate the shot list/storyboard.`,
  },
  {
    id: "dop",
    name: "💡 Luca — Director of Photography",
    system: THINK_PREFIX + `You are Luca, Director of Photography. Light is your language.
Deliver a concise lighting plan:
- Overall Look (1-2 sentences)
- Color Temperature Approach
- Key Lighting Setup per scene (1-2 scenes)
- Color Grading Reference (name a film)
Keep total response under 300 words.`,
    buildMessage: (brief, outputs) =>
      `Storyboard:\n${outputs.storyboard}\n\nDeliver the lighting plan.`,
  },
  {
    id: "cinematographer",
    name: "📷 Kai — Cinematographer",
    system: THINK_PREFIX + `You are Kai, Cinematographer. Camera is your craft.
Deliver camera specs for 3-4 key shots:
- Shot description
- Lens (focal length)
- Camera Movement
- Depth of Field
- Why this choice serves the story
Keep total response under 300 words.`,
    buildMessage: (brief, outputs) =>
      `Storyboard:\n${outputs.storyboard}\n\nDeliver the camera plan.`,
  },
  {
    id: "vfx",
    name: "✨ Zara — VFX Supervisor",
    system: THINK_PREFIX + `You are Zara, VFX & AI Generation Supervisor.
For each key scene, specify:
- AI tool to use (Sora/Runway/Kling for video, Midjourney/Flux for stills)
- Generation approach (1-2 sentences)
- Main consistency challenge and solution
Keep total response under 300 words.`,
    buildMessage: (brief, outputs) =>
      `DOP plan:\n${outputs.dop}\n\nCinematographer plan:\n${outputs.cinematographer}\n\nDeliver the AI generation plan.`,
  },
  {
    id: "promptengineer",
    name: "⚡ Nova — Prompt Engineer",
    system: THINK_PREFIX + `You are Nova, AI Prompt Engineer. Precision is everything.
Write ready-to-use AI prompts for 3 key shots:
- Shot description (1 line)
- PROMPT: [full generation prompt]
- NEGATIVE: [negative prompt if applicable]
- TOOL: [Midjourney/Flux/Sora/Runway + key params]
Keep total response under 400 words.`,
    buildMessage: (brief, outputs) =>
      `Storyboard:\n${outputs.storyboard}\nDOP:\n${outputs.dop}\nVFX plan:\n${outputs.vfx}\n\nWrite the AI generation prompts.`,
  },
  {
    id: "critic",
    name: "🎭 Iris — Film Critic",
    system: THINK_PREFIX + `You are Iris, Film Critic. Sharp, honest, never cruel.
Review the full production package and deliver:
- WHAT WORKS (2-3 points)
- WHAT NEEDS WORK (2-3 points)
- TOP 3 IMPROVEMENTS (specific and actionable)
- FINAL VERDICT (1 paragraph)
Keep total response under 400 words.`,
    buildMessage: (brief, outputs) => {
      const summary = [
        `Brief: ${brief}`,
        `Director: ${outputs.director?.slice(0, 300)}`,
        `Script: ${outputs.scriptwriter?.slice(0, 300)}`,
        `Storyboard: ${outputs.storyboard?.slice(0, 300)}`,
        `Prompts: ${outputs.promptengineer?.slice(0, 300)}`,
      ].join("\n\n");
      return `${summary}\n\nReview this production package.`;
    },
  },
];

// ─── Ollama Call ──────────────────────────────────────────────────────────────

async function askAgent(agent, message) {
  const body = JSON.stringify({
    model: MODEL,
    messages: [
      { role: "system", content: agent.system },
      { role: "user",   content: message },
    ],
    stream: false,
    options: { temperature: 0.7, num_predict: 600 },
  });

  const res = await fetch(OLLAMA_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body,
  });

  if (!res.ok) throw new Error(`Ollama error: ${res.status} ${res.statusText}`);
  const data = await res.json();
  return data?.message?.content ?? "[No response]";
}

// ─── Pipeline ─────────────────────────────────────────────────────────────────

async function runPipeline(brief) {
  console.log("\n🎬 GenAI Film Studio");
  console.log("=".repeat(50));
  console.log(`Brief: ${brief}\n`);

  const header = `# GenAI Film Studio — Production Log\n\nBrief: ${brief}\nStarted: ${new Date().toLocaleString()}\n\n---\n`;
  writeFileSync(LOG_FILE, header, "utf8");

  const outputs = {};

  for (let i = 0; i < AGENTS.length; i++) {
    const agent = AGENTS[i];
    process.stdout.write(`[${i + 1}/${AGENTS.length}] ${agent.name} ... `);

    try {
      const message = agent.buildMessage(brief, outputs);
      const start = Date.now();
      const reply = await askAgent(agent, message);
      const secs = ((Date.now() - start) / 1000).toFixed(1);

      outputs[agent.id] = reply;
      console.log(`✓ (${secs}s)`);

      // Write to production log
      const entry = `\n## ${agent.name}\n\n${reply}\n\n---\n`;
      appendFileSync(LOG_FILE, entry, "utf8");

    } catch (err) {
      console.log(`✗ ${err.message}`);
      outputs[agent.id] = `[Error: ${err.message}]`;
    }
  }

  console.log("\n" + "=".repeat(50));
  console.log("✅ Pipeline complete!");
  console.log(`📋 Full output: ${LOG_FILE}`);
  console.log("\n🎭 CRITIC'S VERDICT:");
  console.log("-".repeat(40));
  console.log(outputs.critic ?? "[No critic output]");
}

// ─── Main ─────────────────────────────────────────────────────────────────────

const brief = process.argv.slice(2).join(" ");
if (!brief) {
  console.error('Usage: node run.mjs "Your film brief here"');
  process.exit(1);
}

runPipeline(brief).catch(err => {
  console.error("Pipeline failed:", err);
  process.exit(1);
});
