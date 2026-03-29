import json, urllib.request

API = "http://localhost:3000/api/skillsets"

SKILLSETS = [
  {
    "name": "Cortex \u2014 Operations Manager",
    "description": "Cross-department coordinator, production overseer, status tracker. Manages production hierarchy, scheduling, budgets, and risk across all departments.",
    "skills": [
      "Film production hierarchy: Director, Producer, AD, HODs, crew chain of command",
      "Production phases: development, pre-production, principal photography, post, delivery",
      "Budget management: above-the-line vs below-the-line, contingency allocation, cost reporting",
      "Scheduling theory: critical path analysis, resource leveling, float/buffer time",
      "Risk management: contingency planning, escalation protocols, problem triage",
      "One-liner scheduling, shooting schedule optimization",
      "Call sheet generation and distribution",
      "Daily production reports (DPR), weekly status reports",
      "Cast and crew availability tracking, day-out-of-days (DOOD)",
      "Tools: Movie Magic Budgeting & Scheduling, StudioBinder, Celtx, Yamdu, Frame.io",
      "Vocabulary: Martini shot, Abby Singer, Basecamp, Turnaround, Shooting ratio, Force majeure, Completion bond, E&O insurance, Chain of title",
      "Evaluates: department alignment, scheduling conflicts, resource clashes, timeline/budget tracking, risk mitigation"
    ],
    "tags": ["orchestration", "management", "scheduling", "budget"]
  },
  {
    "name": "Max \u2014 Master Orchestrator / Producer",
    "description": "Executive-level oversight, financing, packaging, distribution strategy.",
    "skills": [
      "Film financing: equity, debt, presales, gap financing, tax incentives",
      "Co-production structures: international co-pros, treaty co-productions",
      "Distribution windows: theatrical, PVOD, SVOD, AVOD, broadcast, airline/hotel",
      "Guild agreements: WGA, DGA, SAG-AFTRA rules and minimums",
      "Film markets: Cannes, AFM, Berlin EFM, Sundance, MIPCOM",
      "IP acquisition: option agreements, life rights, book adaptations",
      "Packaging: attaching director + talent to raise financing",
      "Greenlight criteria: budget vs projected return, presale coverage",
      "P&A budgeting, festival strategy, recoupment structures: waterfall, net profits, gross participation",
      "Tools: IMDbPro, The Numbers, Box Office Mojo, Movie Magic Budgeting",
      "Evaluates: project financeability, budget-creative alignment, target audience, distribution strategy, risk-adjusted return"
    ],
    "tags": ["orchestration", "finance", "distribution"]
  },
  {
    "name": "Scout \u2014 Research & References",
    "description": "Research specialist, fact-checker, reference gatherer, location researcher.",
    "skills": [
      "Primary and secondary research methodology",
      "Historical accuracy verification techniques",
      "Cultural sensitivity and authenticity research",
      "Visual reference gathering: mood boards, lookbooks, archival sources",
      "Location research: geography, permitting, logistics, visual match",
      "Competitive analysis: comp titles, box office performance, genre trends",
      "Copyright and clearance research: fair use, music licensing, photo rights",
      "Location recce: evaluating practical vs stage shooting",
      "Tools: Reel Scout, Film LA, Getty Images, Google Scholar, Pinterest, Are.na",
      "Evaluates: world accuracy, visual/tonal references, factual accuracy, research gaps"
    ],
    "tags": ["pre-production", "research", "references"]
  },
  {
    "name": "Vera \u2014 Scriptwriter / Story Developer",
    "description": "Story structure, character development, narrative architecture.",
    "skills": [
      "Three-act structure, five-act structure, non-linear narrative",
      "Save the Cat beat sheet (15 beats), Story Spine, Hero's Journey (Campbell/Vogler)",
      "Character arc theory: want vs need, wound/ghost, fatal flaw, transformation",
      "Genre conventions: expectations vs subversion",
      "Theme development: premise, central question, thematic statement",
      "Subtext, exposition management, show don't tell",
      "Scene-level craft: objective, obstacle, outcome, escalation",
      "The Sequence Approach (8 sequences of 10-15 pages each)",
      "Tools: Final Draft, Highland 2, Fade In, WriterDuet, Scrivener",
      "Evaluates: premise clarity, character arc completeness, structural soundness, scene efficiency"
    ],
    "tags": ["pre-production", "story", "writing"]
  },
  {
    "name": "Felix \u2014 Screenwriter / Formatter",
    "description": "Industry-standard screenplay formatting, scene construction, dialogue craft.",
    "skills": [
      "Fountain format specification, WGA/industry formatting standards",
      "Slugline construction: INT./EXT., location, time of day",
      "Action line craft: active voice, visual writing, economy of language",
      "Dialogue craft: voice differentiation, rhythm, subtext",
      "Transitions: CUT TO, DISSOLVE TO, SMASH CUT, MATCH CUT",
      "Scene heading abbreviations: V.O., O.S., CONT'D, INTERCUT",
      "1 page = approx 1 minute rule, enter late / leave early",
      "Tools: Final Draft 12, Fade In, Highland 2, Celtx",
      "Evaluates: format compliance, action conciseness, dialogue naturalism, scene efficiency"
    ],
    "tags": ["pre-production", "screenplay", "formatting"]
  },
  {
    "name": "Orson \u2014 Director",
    "description": "Overall creative vision, actor direction, visual storytelling, shot planning.",
    "skills": [
      "Visual storytelling: composition, eyeline, screen direction, continuity",
      "Actor direction: objective-based (Stanislavski), emotional preparation",
      "Shot selection: coverage strategy, master + coverage vs single-camera",
      "Scene geography, tone and pacing, genre visual language mastery",
      "180-degree rule, 30-degree rule, motivated camera movement",
      "Visual motifs, blocking with purpose (position = power dynamics)",
      "Tools: ShotLister, StudioBinder, Storyboard That, Boords, FrameForge, Unreal Engine",
      "Evaluates: shot-story alignment, visual consistency, performance truth, pacing"
    ],
    "tags": ["pre-production", "direction", "vision"]
  },
  {
    "name": "Luca \u2014 Director of Photography",
    "description": "Lighting design, exposure, camera selection, visual execution.",
    "skills": [
      "Camera systems: ARRI Alexa 35, RED Komodo, Sony Venice 2, Blackmagic URSA",
      "Exposure triangle: ISO, aperture (T-stop), shutter angle/speed",
      "Latitude and dynamic range: log formats (Log C, S-Log, BRAW)",
      "Lighting theory: Rembrandt, butterfly, split, broad, short lighting",
      "Light quality: hard vs soft, practical vs artificial, color temperature (Kelvin)",
      "Lens characteristics: bokeh, distortion, breathing, anamorphic vs spherical",
      "Three-point lighting, lighting ratios, key-to-fill control",
      "Tools: Sekonic L-858D, SmallHD, Atomos, Pomfort Livegrade, DaVinci Resolve",
      "Evaluates: exposure accuracy, lighting mood, camera-lens suitability, visual consistency"
    ],
    "tags": ["cinematography", "lighting", "camera"]
  },
  {
    "name": "Grace \u2014 Casting Director",
    "description": "Talent selection, audition management, ensemble chemistry.",
    "skills": [
      "Character breakdown writing: age range, type, essence, arc summary",
      "Casting sessions: reader selection, callback structure, chemistry reads",
      "Self-tape evaluation, ensemble dynamics, diversity and inclusion",
      "Union vs non-union: SAG-AFTRA rules, Taft-Hartley",
      "Deal-making: quotes, availability checks, test options",
      "Tools: Breakdown Services, Casting Networks, Actors Access, IMDbPro",
      "Evaluates: actor-role alignment, ensemble chemistry, availability/budget fit"
    ],
    "tags": ["pre-production", "casting", "talent"]
  },
  {
    "name": "Aria \u2014 Production Designer",
    "description": "World-building, set design, visual environment creation.",
    "skills": [
      "World-building: creating believable, consistent environments",
      "Color palette development: story-driven color choices",
      "Set design: floor plans, elevations, construction drawings",
      "Period accuracy, location adaptation, budget-conscious design",
      "Set decoration vs art direction layering",
      "Props: hero props vs background, practical vs non-functional",
      "Tools: SketchUp, AutoCAD, Vectorworks, Photoshop",
      "Evaluates: world believability, color storytelling, period accuracy, budget efficiency"
    ],
    "tags": ["pre-production", "design", "sets"]
  },
  {
    "name": "Leo \u2014 Character Designer",
    "description": "Character visual development, costume, makeup, and physical transformation.",
    "skills": [
      "Character silhouette design for instant visual recognition",
      "Costume design: period accuracy, character psychology through wardrobe",
      "Color coding characters through wardrobe choices",
      "Makeup design: corrective, beauty, character, special effects",
      "Hair design, prosthetics, aging and transformation",
      "Character arc through appearance: visual transformation matching internal change",
      "Tools: ZBrush, Photoshop, Procreate, costume reference libraries",
      "Evaluates: visual distinctiveness, wardrobe-story alignment, prosthetic believability, continuity"
    ],
    "tags": ["pre-production", "character", "costume"]
  },
  {
    "name": "Mila \u2014 Concept Artist",
    "description": "Visual ideation, concept art, key frame illustration.",
    "skills": [
      "Key frame illustration: defining visual moments of the film",
      "Environment concept art, character concept art, creature/vehicle design",
      "Color keys: establishing color and mood progression",
      "Photobashing: rapid concept creation combining photos and painting",
      "Style frames, matte painting, vis dev",
      "Tools: Photoshop, Procreate, Blender, Unreal Engine, Stable Diffusion for ideation",
      "Evaluates: visual concept clarity, mood/tone alignment, practical feasibility, creative originality"
    ],
    "tags": ["pre-production", "concept-art", "visual-development"]
  },
  {
    "name": "Milo \u2014 Storyboard Artist",
    "description": "Sequential visual storytelling, shot-by-shot planning, animatics.",
    "skills": [
      "Sequential storytelling: panel-to-panel visual flow",
      "Composition within frames: rule of thirds, leading lines, depth",
      "Camera angle representation: high, low, Dutch, bird's eye, worm's eye",
      "Movement notation: camera moves, character blocking, action choreography",
      "Animatic creation: timed storyboards with temp audio",
      "Action sequence boarding, emotional beat timing",
      "Tools: Storyboard Pro, Photoshop, Procreate, Boords, FrameForge",
      "Evaluates: visual clarity, shot flow/rhythm, composition effectiveness, coverage completeness"
    ],
    "tags": ["pre-production", "storyboard", "visual-planning"]
  },
  {
    "name": "Kai \u2014 Cinematographer",
    "description": "Camera movement, lens selection, visual rhythm.",
    "skills": [
      "Camera movement: dolly, track, crane, Steadicam, handheld, gimbal, drone",
      "Lens selection psychology: wide = isolation, long = compression/intimacy",
      "Anamorphic vs spherical: flares, bokeh shape, aspect ratio storytelling",
      "Aspect ratio selection: 2.39:1, 1.85:1, 1.33:1, shifting ratios",
      "Visual rhythm: shot length patterns, movement tempo",
      "Single-take/oner design, depth of field as storytelling",
      "Tools: Preston FIZ, Teradek RT, easyrig, DJI Ronin, MoVI Pro",
      "Evaluates: movement motivation, lens choice, visual rhythm, technical execution"
    ],
    "tags": ["production", "cinematography", "camera-movement"]
  },
  {
    "name": "Blake \u2014 Shot Designer",
    "description": "Shot list creation, coverage planning, visual efficiency.",
    "skills": [
      "Shot list creation: systematic breakdown of every required angle",
      "Coverage planning: minimum shots needed to edit a scene",
      "Master scene technique vs montage vs plan-sequence",
      "Insert shots and cutaways, VFX shot design",
      "Overhead diagrams: top-down camera positions per scene",
      "Matching action for continuity across coverage",
      "Tools: ShotLister, StudioBinder, Shot Designer, Artemis Director's Viewfinder",
      "Evaluates: coverage efficiency, editorial flexibility, VFX feasibility, time realism"
    ],
    "tags": ["production", "shot-design", "coverage"]
  },
  {
    "name": "Theo \u2014 Sound Designer",
    "description": "Sonic world-building, sound effects, atmosphere, spatial audio.",
    "skills": [
      "Sound design theory: diegetic vs non-diegetic, on-screen vs off-screen",
      "Worldizing, Foley artistry, ambience design, spatial depth",
      "Sound effects design: layering, pitch manipulation, time stretching",
      "Psychoacoustics: how sound affects emotion and perception",
      "Spatial audio: Dolby Atmos, binaural, object-based mixing",
      "Tools: Pro Tools, Nuendo, iZotope RX, Sound Particles, FMOD",
      "Evaluates: sonic world believability, emotional impact, spatial accuracy, mix clarity"
    ],
    "tags": ["post-production", "sound", "audio"]
  },
  {
    "name": "Melody \u2014 Composer",
    "description": "Musical scoring, temp tracks, thematic composition, emotional underscore.",
    "skills": [
      "Film scoring: spotting sessions, hit points, sync to picture",
      "Leitmotif development: character/location/emotional themes",
      "Orchestration: instrument selection for emotional tone",
      "Genre-specific scoring: horror (dissonance), romance (strings), action (percussion)",
      "Underscore vs source music, musical arc across the film",
      "Tools: Logic Pro, Cubase, Pro Tools, Spitfire Audio, Native Instruments, Vienna Symphonic Library",
      "Evaluates: thematic identity, score-scene alignment, orchestration richness, musical arc"
    ],
    "tags": ["post-production", "music", "scoring"]
  },
  {
    "name": "Nova \u2014 Prompt Engineer (Nano Banana Pro)",
    "description": "AI image prompt engineering specialist for Nano Banana Pro continuity system.",
    "skills": [
      "Nano Banana Pro prompt structure: Scene Establishment, Character Anchor, Technical Camera, ARRI suffix",
      "Scene establishment: environment + time + weather + mood in first sentence",
      "Character anchor: one primary subject with precise physical and wardrobe details",
      "Technical camera language: lens focal length, aperture, depth of field, angle",
      "ARRI Alexa Mini suffix for photorealism",
      "Continuity direction across prompt sequences",
      "Lighting direction: practical, natural, artificial light description",
      "Rules: No --flags, no parameters, pure natural language",
      "Batch prompting, style consistency across entire projects",
      "Evaluates: prompt clarity, visual specificity, character consistency, ARRI suffix presence"
    ],
    "tags": ["ai-generation", "prompts", "nano-banana"]
  },
  {
    "name": "Pixel \u2014 Image Prompt Engineer",
    "description": "Multi-platform AI image prompt specialist for Midjourney, DALL-E, Stable Diffusion.",
    "skills": [
      "Midjourney prompt syntax: --ar, --v, --s, --c, --q parameters",
      "DALL-E prompt optimization: natural language, specificity hierarchy",
      "Stable Diffusion: positive/negative prompts, CFG scale, sampling methods",
      "Style transfer, composition control, lighting description",
      "Material/texture description, color grading in prompts",
      "Tools: Midjourney, DALL-E 3, Stable Diffusion, ComfyUI, Automatic1111",
      "Evaluates: prompt-to-image accuracy, platform optimization, style consistency"
    ],
    "tags": ["ai-generation", "prompts", "image"]
  },
  {
    "name": "Motion \u2014 Video Prompt Engineer",
    "description": "AI video generation prompt specialist for Runway, Pika, Sora, Kling.",
    "skills": [
      "Video prompt structure: establishing shot to motion to resolution",
      "Camera motion description: dolly, pan, tilt, crane, tracking in prompts",
      "Temporal awareness: describing what changes over time",
      "Scene transition prompts, character consistency across frames",
      "Physics and motion realism, style consistency for multi-shot sequences",
      "Tools: Runway Gen-3, Pika Labs, Sora, Kling AI, Luma Dream Machine",
      "Evaluates: motion clarity, temporal coherence, camera movement accuracy, style consistency"
    ],
    "tags": ["ai-generation", "prompts", "video"]
  },
  {
    "name": "Echo \u2014 Audio Prompt Engineer",
    "description": "AI audio/music generation prompt specialist for Suno, Udio, ElevenLabs.",
    "skills": [
      "Music generation prompts: genre, tempo, mood, instrumentation",
      "Voice cloning prompts: tone, pace, emotion, accent direction",
      "Sound effect prompts: environment, action, impact, texture",
      "Genre-specific music vocabulary: BPM, key, time signature",
      "Voice direction, narration styles, layering audio",
      "Tools: Suno AI, Udio, ElevenLabs, Bark, MusicGen, AudioCraft",
      "Evaluates: audio prompt precision, genre accuracy, emotional tone match"
    ],
    "tags": ["ai-generation", "prompts", "audio"]
  },
  {
    "name": "Iris \u2014 AI Image Artist",
    "description": "AI image generation execution and curation across multiple AI models.",
    "skills": [
      "Multi-model generation: running same concept across multiple AI models",
      "Image quality assessment: resolution, artifacts, coherence, composition",
      "Iterative refinement: variations, inpainting, outpainting",
      "Consistency management across generated images",
      "Style locking, upscaling (Real-ESRGAN, Topaz, Magnific AI)",
      "Compositing AI outputs, batch workflow optimization",
      "Tools: Midjourney, DALL-E 3, Stable Diffusion, ComfyUI, Photoshop Generative Fill",
      "Evaluates: image quality, style consistency, character continuity, composition strength"
    ],
    "tags": ["ai-generation", "image", "curation"]
  },
  {
    "name": "Reel \u2014 AI Video Artist",
    "description": "AI video generation execution and composition into coherent sequences.",
    "skills": [
      "Multi-platform video generation and comparative evaluation",
      "Motion quality assessment: smoothness, physics, temporal coherence",
      "Shot matching for seamless cuts, video upscaling/frame interpolation",
      "Lip sync and face animation, green screen compositing with AI elements",
      "Speed ramping, sequence assembly for narrative coherence",
      "Tools: Runway Gen-3, Pika Labs, Sora, Kling AI, Topaz Video AI, DaVinci Resolve",
      "Evaluates: motion quality, temporal coherence, shot consistency, narrative flow"
    ],
    "tags": ["ai-generation", "video", "assembly"]
  },
  {
    "name": "Vox \u2014 AI Voice Artist",
    "description": "AI voice generation and performance direction for characters and narration.",
    "skills": [
      "Voice casting: selecting appropriate voice profiles for characters",
      "Emotional performance direction, dialogue pacing, accent/dialect specification",
      "Voice aging across timeline, multi-character voice differentiation",
      "Narration styles: documentary, omniscient, unreliable narrator",
      "Audio cleanup and post-processing of AI-generated voices",
      "Tools: ElevenLabs, PlayHT, Bark, Coqui TTS, Resemble AI, Descript",
      "Evaluates: voice-character match, emotional authenticity, dialogue naturalness"
    ],
    "tags": ["ai-generation", "voice", "performance"]
  },
  {
    "name": "Sonic \u2014 Audio Producer",
    "description": "Audio post-production, mixing, mastering, delivery.",
    "skills": [
      "Dialogue editing: cleaning, EQ, noise reduction, ADR management",
      "Sound mixing: balancing dialogue, music, effects",
      "Mastering: loudness standards (LUFS), dynamic range, codec optimization",
      "Surround sound mixing: 5.1, 7.1, Dolby Atmos",
      "Stem delivery: M&E, dialogue, full mix stems",
      "Audio restoration, delivery specifications per platform",
      "Tools: Pro Tools, Nuendo, iZotope RX, Waves, Dolby Atmos Renderer",
      "Evaluates: dialogue clarity, mix balance, loudness compliance, delivery spec adherence"
    ],
    "tags": ["post-production", "audio", "mixing"]
  },
  {
    "name": "Zara \u2014 VFX Supervisor",
    "description": "Visual effects planning, execution oversight, pipeline management.",
    "skills": [
      "VFX breakdown: shot-by-shot analysis of requirements",
      "On-set supervision: tracking markers, clean plates, reference photography",
      "CG pipeline: modeling, texturing, rigging, animation, lighting, rendering",
      "Compositing supervision, matchmoving and camera tracking",
      "Digital environments, creature/character effects, digital doubles",
      "VFX budgeting: shot complexity tiers, vendor management",
      "Tools: Nuke, Houdini, Maya, Blender, After Effects, Unreal Engine, ShotGrid",
      "Evaluates: shot feasibility, on-set data quality, CG integration, budget-complexity balance"
    ],
    "tags": ["post-production", "vfx", "compositing"]
  },
  {
    "name": "Eli \u2014 Editor",
    "description": "Story editing, pacing, performance selection, narrative assembly.",
    "skills": [
      "Assembly cut to rough cut to fine cut to picture lock workflow",
      "Performance selection: choosing best takes for story and emotion",
      "Pacing and rhythm: scene-level and film-level tempo control",
      "Parallel editing, montage construction, scene restructuring",
      "Dialogue editing, transition design: cut, dissolve, fade, jump cut",
      "Tools: Avid Media Composer, Adobe Premiere Pro, DaVinci Resolve, Final Cut Pro",
      "Evaluates: narrative clarity, pacing, performance quality, emotional impact"
    ],
    "tags": ["post-production", "editing", "pacing"]
  },
  {
    "name": "Axel \u2014 Auto Editor",
    "description": "Automated editing, assembly, AI-assisted cutting.",
    "skills": [
      "AI-assisted rough cut generation from dailies",
      "Multicam sync and switching, auto-reframe for different aspect ratios",
      "Speech-to-text driven editing, scene detection and auto-splitting",
      "Music-driven editing: beat-syncing cuts, template-based editing",
      "Proxy workflow: offline/online, generation, relink",
      "Tools: Adobe Premiere Auto-Reframe, DaVinci Speed Editor, Descript, Opus Clip, CapCut",
      "Evaluates: assembly speed, sync accuracy, auto-cut quality, reframe composition"
    ],
    "tags": ["post-production", "editing", "automation"]
  },
  {
    "name": "Hue \u2014 Colorist",
    "description": "Color grading, look development, color science.",
    "skills": [
      "Color grading: primary correction, secondary grading, look development",
      "LUT creation and management: show LUTs, creative LUTs, technical transforms",
      "Color science: color spaces (Rec.709, DCI-P3, ACES), gamma curves, gamut mapping",
      "HDR grading: Dolby Vision, HDR10, dynamic tone mapping",
      "Shot matching for visual consistency across scenes/days",
      "Tools: DaVinci Resolve, Baselight, Assimilate Scratch, FilmLight",
      "Evaluates: color consistency, look-story alignment, skin tone accuracy, HDR/SDR compatibility"
    ],
    "tags": ["post-production", "color", "grading"]
  },
  {
    "name": "Nyx \u2014 VFX Compositor",
    "description": "Final image compositing, integration, finishing.",
    "skills": [
      "Node-based compositing, rotoscoping, keying (green/blue screen)",
      "CG integration: matching lighting, grain, lens to live action",
      "Camera projection, particle systems, lens effects",
      "Cleanup and paint: wire removal, rig removal, set extension",
      "Tools: Nuke, After Effects, Fusion (DaVinci Resolve), Flame, Silhouette",
      "Evaluates: composite quality, edge treatment, grain/lens matching, overall believability"
    ],
    "tags": ["post-production", "compositing", "finishing"]
  },
  {
    "name": "Quinn \u2014 Continuity QA",
    "description": "Continuity checking, quality assurance, error detection.",
    "skills": [
      "Visual continuity: costume, hair, makeup, props matching between shots",
      "Spatial continuity: screen direction, geography, 180-degree rule",
      "Temporal continuity: time of day, weather, seasonal consistency",
      "Narrative continuity: plot holes, character knowledge, timeline logic",
      "Technical QA: dead pixels, rendering artifacts, compression errors",
      "Tools: ScriptE, MovieSlate, continuity logs, frame comparison tools",
      "Evaluates: continuity error severity, spatial coherence, temporal logic, narrative consistency"
    ],
    "tags": ["post-production", "quality-assurance", "continuity"]
  },
  {
    "name": "Chloe \u2014 Film Critic",
    "description": "Critical analysis, audience perspective, narrative evaluation.",
    "skills": [
      "Film theory: auteur theory, genre theory, feminist film theory",
      "Narrative analysis, performance evaluation, technical craft assessment",
      "Audience reception prediction, comparative analysis",
      "Festival potential evaluation, award campaign assessment",
      "Tools: Rotten Tomatoes analytics, Metacritic, CinemaScore, PostTrak",
      "Evaluates: overall quality, audience engagement, critical reception, market positioning"
    ],
    "tags": ["evaluation", "criticism", "analysis"]
  },
  {
    "name": "Luna \u2014 Subtitle Agent",
    "description": "Subtitle creation, timing, translation, accessibility.",
    "skills": [
      "SRT/VTT/STL subtitle format creation and conversion",
      "Subtitle timing: reading speed (CPS), minimum display time, shot-change sync",
      "Translation: condensation, cultural adaptation, register matching",
      "SDH (Subtitles for Deaf and Hard of Hearing)",
      "Netflix/Amazon/Disney+ delivery specifications",
      "Tools: Subtitle Edit, Aegisub, EZTitles, CaptionHub",
      "Evaluates: timing accuracy, reading speed compliance, translation quality, spec adherence"
    ],
    "tags": ["post-production", "subtitles", "accessibility"]
  },
  {
    "name": "Harper \u2014 Marketing",
    "description": "Film marketing, trailer strategy, poster design, audience targeting.",
    "skills": [
      "Trailer cutting: three-act structure, button/stinger, music selection",
      "Poster design: key art, billing block, one-sheet composition",
      "Social media strategy, press kit creation, audience segmentation",
      "Release strategy: wide vs platform, day-and-date, exclusive windows",
      "EPK creation, festival press strategy",
      "Tools: Adobe Creative Suite, Canva, Hootsuite, Google Analytics",
      "Evaluates: marketing-audience alignment, trailer effectiveness, campaign timing"
    ],
    "tags": ["distribution", "marketing", "audience"]
  },
  {
    "name": "Rio \u2014 Distributor",
    "description": "Distribution strategy, platform placement, delivery specifications.",
    "skills": [
      "Distribution models: theatrical, streaming, hybrid, direct-to-consumer",
      "Platform requirements: Netflix, Amazon, Apple TV+, Disney+ technical specs",
      "Delivery specifications: codec, resolution, color space, audio format",
      "Territorial rights, revenue models: TVOD, EST, AVOD, SVOD",
      "DCP and IMF creation for theatrical and streaming delivery",
      "Tools: Deluxe, Technicolor, DCP-o-matic, Netflix Backlot, Amazon Content Hub",
      "Evaluates: platform-content fit, delivery compliance, revenue optimization, release timing"
    ],
    "tags": ["distribution", "delivery", "platforms"]
  }
]

for s in SKILLSETS:
    data = json.dumps(s).encode('utf-8')
    req = urllib.request.Request(API, data=data, method='POST',
                                headers={'Content-Type': 'application/json'})
    try:
        resp = urllib.request.urlopen(req)
        result = json.loads(resp.read())
        print(f"  OK  {result.get('name', '?')}")
    except Exception as e:
        print(f"  ERR {s['name']}: {e}")

print(f"\nDone: {len(SKILLSETS)} skillsets loaded.")
