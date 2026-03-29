"""
Generate GenAI Film Studio - Agent Skillset Database PDF
Professional dark-themed reference document with 33 agent entries.
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import HexColor, white, Color
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph
from reportlab.lib.enums import TA_LEFT, TA_CENTER
import textwrap

OUTPUT_PATH = r"C:\Users\Abcom\genai-film\Agent_Skillset_Database.pdf"

# Colors
BG_DARK = HexColor("#1a1a2e")
BG_CARD = HexColor("#16213e")
BG_SECTION = HexColor("#0f3460")
TEXT_WHITE = white
TEXT_LIGHT = HexColor("#e0e0e0")
TEXT_DIM = HexColor("#a0a0b0")
ACCENT_GOLD = HexColor("#e2b714")

# Phase accent colors
PHASE_COLORS = {
    "Orchestration": HexColor("#4fc3f7"),       # Light blue
    "Pre-Production Story": HexColor("#66bb6a"), # Green
    "Pre-Production Visual": HexColor("#81c784"),# Light green
    "Production": HexColor("#ffb74d"),           # Orange
    "Post-Production": HexColor("#ce93d8"),      # Purple
    "AI Generation": HexColor("#ef5350"),        # Red
    "VFX": HexColor("#ff7043"),                  # Deep orange
    "Quality": HexColor("#4dd0e1"),              # Cyan
    "Distribution": HexColor("#aed581"),         # Lime
}

W, H = letter  # 612 x 792

# ── Agent Data ──────────────────────────────────────────────────────────

agents = [
    # PHASE 1: ORCHESTRATION
    {
        "num": 1, "name": "Cortex", "role": "Operations Manager",
        "phase": "Orchestration",
        "domain": "Cross-department coordination, production hierarchy, scheduling (critical path method, resource leveling), budget management (above/below the line, contingency reserves), risk management and mitigation strategies.",
        "tools": "Movie Magic Scheduling, StudioBinder, Celtx, Frame.io",
        "techniques": "Critical path scheduling, resource leveling, cross-department workflow synchronization, risk assessment matrices, budget tracking and variance analysis.",
        "vocab": "Martini shot, Abby Singer, DOOD (Day Out of Days), Force majeure, Completion bond, Call sheet, Basecamp, Hot cost.",
        "eval": "Department alignment accuracy, scheduling conflict resolution, budget tracking precision, risk mitigation effectiveness."
    },
    {
        "num": 2, "name": "Max", "role": "Master Orchestrator / Producer",
        "phase": "Orchestration",
        "domain": "Executive oversight, film financing (equity, debt, presale models), co-productions, distribution windows (theatrical, PVOD, SVOD, AVOD), guild agreements (WGA, DGA, SAG-AFTRA), film markets (Cannes, AFM, EFM).",
        "tools": "IMDbPro, The Numbers, Box Office Mojo, Entertainment Partners",
        "techniques": "Financing structuring, distribution windowing strategy, guild negotiation, market analysis, risk-adjusted return modeling, greenlight analysis.",
        "vocab": "Greenlight, Pay-or-play, Backend participation, Negative pickup, Gap financing, Waterfall, First dollar gross, Minimum guarantee.",
        "eval": "Financeability assessment, budget-creative alignment, distribution strategy viability, risk-adjusted return projections."
    },
    # PHASE 2: PRE-PRODUCTION — STORY
    {
        "num": 3, "name": "Scout", "role": "Research & References",
        "phase": "Pre-Production Story",
        "domain": "Primary and secondary research methodology, historical accuracy verification, cultural sensitivity review, visual reference curation, location research, comp title analysis, copyright clearance procedures.",
        "tools": "Reel Scout, Film LA, Getty Images, Google Scholar, Pinterest, Library of Congress archives",
        "techniques": "Deep research methodology, visual reference board creation, historical cross-referencing, cultural consultation frameworks, location scouting analysis, comparative title analysis.",
        "vocab": "Recce, Tech scout, Lookbook, Mood board, Visual bible, Reference package, Clearing rights, Public domain.",
        "eval": "World accuracy and authenticity, reference quality and relevance, factual accuracy, cultural sensitivity compliance."
    },
    {
        "num": 4, "name": "Vera", "role": "Scriptwriter",
        "phase": "Pre-Production Story",
        "domain": "Three-act and five-act structure, Save the Cat (15 beats), Hero's Journey (12 stages), character arc theory (want vs need, wound/ghost, fatal flaw), genre conventions, theme development, subtext layering.",
        "tools": "Final Draft, Scrivener, WriterDuet, Save the Cat software",
        "techniques": "Beat sheet construction, character arc mapping, theme weaving, scene-by-scene outlining, dialogue subtext layering, genre convention analysis.",
        "vocab": "Inciting incident, Midpoint, Dark night of the soul, MacGuffin, Throughline, B-story, All Is Lost, Break into Two.",
        "eval": "Premise clarity, character arc completeness, structural soundness, scene efficiency, thematic coherence."
    },
    {
        "num": 5, "name": "Felix", "role": "Screenwriter",
        "phase": "Pre-Production Story",
        "domain": "Fountain markup format, WGA formatting standards (Courier 12pt), slugline conventions (INT./EXT.), action line craft, dialogue voice differentiation, transitions (CUT TO, MATCH CUT, SMASH CUT), dual dialogue formatting.",
        "tools": "Final Draft 12, Fade In, Highland 2, WriterSolo",
        "techniques": "Visual writing in action lines, dialogue voice differentiation, white space management, spec vs shooting script formatting, revision color coding.",
        "vocab": "Slugline, Parenthetical, V.O. (Voice Over), O.S. (Off Screen), CONT'D, Spec script, Shooting script, Locked pages, Blue revision.",
        "eval": "Format compliance with industry standards, visual writing quality, dialogue naturalism, scene efficiency."
    },
    # PHASE 3: PRE-PRODUCTION — VISUAL
    {
        "num": 6, "name": "Orson", "role": "Director",
        "phase": "Pre-Production Visual",
        "domain": "Visual storytelling (composition, eyeline, continuity systems), actor direction (Stanislavski method, Meisner technique), shot selection, scene geography, 180-degree rule, 30-degree rule, motivated camera movement, visual motifs, blocking choreography.",
        "tools": "ShotLister, StudioBinder, FrameForge Previz, Unreal Engine (virtual production)",
        "techniques": "Shot-reverse-shot coverage, blocking diagrams, visual motif development, actor direction techniques, scene geography mapping, motivated camera movement design.",
        "vocab": "Coverage, Master shot, Mise-en-scene, Eyeline match, J-cut, L-cut, Blocking, Marks, Cheat (framing), Fourth wall.",
        "eval": "Shot-story alignment, visual consistency across scenes, performance truth and authenticity."
    },
    {
        "num": 7, "name": "Luca", "role": "Director of Photography",
        "phase": "Pre-Production Visual",
        "domain": "Camera systems (ARRI Alexa 35, RED Komodo, Sony Venice 2), exposure triangle, dynamic range and log formats, lighting theory (Rembrandt, butterfly, split, loop), color temperature (Kelvin scale), lens characteristics (bokeh, anamorphic vs spherical distortion).",
        "tools": "Sekonic L-858D light meter, SmallHD monitors, Pomfort Livegrade, Lightcraft Previzion",
        "techniques": "Three-point lighting setups, exposure control via waveform/histogram, log/RAW workflow design, lens testing, color temperature mixing, lighting plot creation.",
        "vocab": "T-stop, ND filter, C-stand, Flag, Fresnel, HMI, Book light, Neg fill, Chimera, Kino Flo, Grip, Gaffer.",
        "eval": "Exposure accuracy, lighting mood alignment with story, visual consistency across setups."
    },
    {
        "num": 8, "name": "Grace", "role": "Casting Director",
        "phase": "Pre-Production Visual",
        "domain": "Character breakdown creation, casting session management, self-tape evaluation criteria, ensemble dynamics assessment, SAG-AFTRA rules and tiers, diversity casting initiatives, deal-making and negotiation.",
        "tools": "Breakdown Services, Casting Networks, Actors Access, Eco Cast",
        "techniques": "Character breakdown writing, audition evaluation, chemistry read facilitation, ensemble balancing, deal structuring, talent availability coordination.",
        "vocab": "Sides, Callback, Chemistry read, Test option, Day player, Scale, Favored nations, First refusal, Avail check, Pinned.",
        "eval": "Actor-role alignment, ensemble chemistry, budget fit, diversity representation."
    },
    {
        "num": 9, "name": "Aria", "role": "Production Designer",
        "phase": "Pre-Production Visual",
        "domain": "Environment design, color palette development for narrative, set design (floor plans, elevations, cross-sections), period accuracy research, location adaptation, budget-conscious design solutions, props management and sourcing.",
        "tools": "SketchUp, AutoCAD, Vectorworks, Adobe Photoshop, Unreal Engine",
        "techniques": "Color palette storytelling, set construction planning, forced perspective design, location modification plans, prop breakdown management, scenic painting.",
        "vocab": "Practical (working prop/light), Hero prop, Set dressing, Wild wall, Forced perspective, Cyc wall, Swing gang, Striking (removing).",
        "eval": "World believability, color storytelling effectiveness, period accuracy, budget efficiency."
    },
    {
        "num": 10, "name": "Leo", "role": "Character Designer",
        "phase": "Pre-Production Visual",
        "domain": "Character silhouette design, costume design and construction, color coding characters for visual storytelling, makeup design (corrective, beauty, SFX), hair design, prosthetics application, aging and transformation techniques.",
        "tools": "ZBrush, Adobe Photoshop, Procreate, CLO 3D",
        "techniques": "Silhouette-first character design, costume color scripting, makeup continuity tracking, prosthetics lifecycle planning, aging progression design, wardrobe multiples management.",
        "vocab": "Breakdown (distressing costumes), Continuity photos, Hero costume, Multiples, Bald cap, Appliance, Life cast, Color script.",
        "eval": "Visual distinctiveness of characters, wardrobe-story alignment, makeup/hair continuity."
    },
    {
        "num": 11, "name": "Mila", "role": "Concept Artist",
        "phase": "Pre-Production Visual",
        "domain": "Key frame illustration, environment concept art, character concept art, color keys for sequences, photobashing techniques, style frames, matte painting, visual development pipelines.",
        "tools": "Adobe Photoshop, Procreate, Blender (3D base), Unreal Engine (virtual scouts)",
        "techniques": "Photobashing for rapid iteration, color key sequences, key frame storytelling, environment mood studies, character turnaround sheets, style guide creation.",
        "vocab": "Key frame, Color key, Photobash, Matte painting, Vis dev (visual development), Turnaround sheet, Callout sheet, Ortho view.",
        "eval": "Concept clarity, mood alignment with script, production feasibility, originality."
    },
    {
        "num": 12, "name": "Milo", "role": "Storyboard Artist",
        "phase": "Pre-Production Visual",
        "domain": "Sequential storytelling in panels, composition principles (rule of thirds, leading lines, depth), camera angle representation, movement notation systems, animatic creation, action sequence boarding.",
        "tools": "Toon Boom Storyboard Pro, Procreate, Boords, FrameForge 3D",
        "techniques": "Panel-to-panel flow design, camera movement notation, action line continuity, animatic timing, beat board creation, overhead staging diagrams.",
        "vocab": "Panel, Beat board, Animatic, Pre-viz, Action line, Staging, Thumbnail, Rough board, Clean board, Leica reel.",
        "eval": "Visual clarity per panel, shot flow and transitions, composition quality, coverage completeness."
    },
    # PHASE 4: PRODUCTION
    {
        "num": 13, "name": "Kai", "role": "Cinematographer",
        "phase": "Production",
        "domain": "Camera movement systems (dolly, track, crane, Steadicam, handheld, gimbal, drone), lens psychology (wide = isolation, long = compression), anamorphic vs spherical characteristics, aspect ratio selection, visual rhythm, oner design, depth of field storytelling.",
        "tools": "Preston FIZ system, Teradek RT, DJI Ronin 4D, Freefly MoVI, Technocrane",
        "techniques": "Motivated camera movement design, lens-driven emotional storytelling, oner choreography, aspect ratio justification, visual rhythm pacing, depth of field manipulation.",
        "vocab": "Dolly in/out, Push-in, Whip pan, Tracking shot, Oner, Stitched oner, Texas switch, Cowboy shot, Dutch angle.",
        "eval": "Movement motivation clarity, lens choice appropriateness, visual rhythm effectiveness."
    },
    {
        "num": 14, "name": "Blake", "role": "Shot Designer",
        "phase": "Production",
        "domain": "Shot list creation, minimum coverage planning, master scene technique vs montage approach, insert shot selection, VFX shot design, overhead diagrams, matching action across setups.",
        "tools": "ShotLister, StudioBinder Shot Lists, Artemis Director's Viewfinder app",
        "techniques": "Coverage planning matrices, setup optimization, overhead blocking diagrams, VFX plate planning, editorial pre-visualization, matching action design.",
        "vocab": "Setup, Reset, Turnaround, Clean single, Dirty single, Two-shot, OTS (Over-the-shoulder), POV, ECU, CU, MS, WS, XWS.",
        "eval": "Coverage efficiency, editorial flexibility provided, VFX shot feasibility."
    },
    # PHASE 5: POST-PRODUCTION
    {
        "num": 15, "name": "Theo", "role": "Sound Designer",
        "phase": "Post-Production",
        "domain": "Diegetic vs non-diegetic sound theory, worldizing techniques, Foley artistry, ambience design and layering, sound effects creation and editing, psychoacoustics, spatial audio (Dolby Atmos), sound perspective matching.",
        "tools": "Pro Tools Ultimate, Steinberg Nuendo, iZotope RX 11, Sound Particles, Krotos",
        "techniques": "Foley recording and editing, ambience bed construction, sound effects layering, worldizing (re-recording through spaces), psychoacoustic manipulation, Atmos object-based mixing.",
        "vocab": "Room tone, Wild sound, Foley, Walla, Sweetener, Atmos bed, Hard effects, BG (background), Futz (filtered audio).",
        "eval": "Sonic believability, emotional impact of sound design, spatial accuracy in mix."
    },
    {
        "num": 16, "name": "Melody", "role": "Composer",
        "phase": "Post-Production",
        "domain": "Film scoring methodology (spotting sessions, hit points), leitmotif development, orchestration for film, genre-specific scoring conventions, underscore vs source music, musical arc across the film.",
        "tools": "Logic Pro X, Steinberg Cubase, Spitfire Audio libraries, Vienna Symphonic Library, Kontakt",
        "techniques": "Spotting session analysis, leitmotif composition and variation, orchestration for emotional impact, tempo mapping to picture, source music integration, musical arc design.",
        "vocab": "Cue, Spotting session, Stinger, Underscore, Leitmotif, Ostinato, Diegetic source, Temp track, Streamers and punches.",
        "eval": "Thematic identity strength, score-scene alignment, orchestration richness and variety."
    },
    # PHASE 6: AI GENERATION
    {
        "num": 17, "name": "Nova", "role": "Prompt Engineer (Nano Banana Pro)",
        "phase": "AI Generation",
        "domain": "Nano Banana Pro prompt structure: Scene Establishment, Character Anchor, Technical Camera Direction, ARRI Alexa suffix. Continuity direction for character/environment consistency, lighting direction integration. Rules: No --flags, no parameters, pure natural language only.",
        "tools": "Nano Banana Pro pipeline, ARRI look library, custom prompt templates",
        "techniques": "Scene establishment framing, character anchoring for consistency, technical camera language integration, ARRI suffix application, continuity chain management across shots.",
        "vocab": "Scene establishment, Character anchor, ARRI suffix, Continuity chain, Prompt chaining, Natural language direction, Shot-to-shot consistency.",
        "eval": "Prompt clarity, visual specificity, character consistency across generations, proper ARRI suffix usage."
    },
    {
        "num": 18, "name": "Pixel", "role": "Image Prompt Engineer",
        "phase": "AI Generation",
        "domain": "Multi-platform prompt engineering: Midjourney syntax (--ar, --v, --s, --c), DALL-E prompt optimization, Stable Diffusion (positive/negative prompts, CFG scale), style transfer techniques, composition control, lighting and material description.",
        "tools": "Midjourney, DALL-E 3, ComfyUI, Automatic1111, InvokeAI",
        "techniques": "Platform-specific prompt optimization, negative prompt engineering, style reference chaining, composition keywords, lighting description vocabulary, iterative refinement workflows.",
        "vocab": "--ar (aspect ratio), --v (version), --s (stylize), CFG scale, Negative prompt, ControlNet, LoRA, Seed, Img2img, Inpainting.",
        "eval": "Prompt-to-output accuracy, platform optimization, style consistency across batches."
    },
    {
        "num": 19, "name": "Motion", "role": "Video Prompt Engineer",
        "phase": "AI Generation",
        "domain": "Video prompt structure for AI generation, camera motion description language, temporal awareness in prompts, scene transition specification, character consistency across frames, motion quality direction.",
        "tools": "Runway Gen-3 Alpha, Pika Labs 1.0, Sora, Kling AI, Luma Dream Machine",
        "techniques": "Camera motion prompting, temporal continuity direction, scene transition specification, character consistency anchoring, motion quality keywords, duration and pacing control.",
        "vocab": "Temporal coherence, Camera motion keywords, Scene transition, Frame interpolation, Motion consistency, Keyframe anchoring.",
        "eval": "Motion clarity in output, temporal coherence, style consistency across generated clips."
    },
    {
        "num": 20, "name": "Echo", "role": "Audio Prompt Engineer",
        "phase": "AI Generation",
        "domain": "Music generation prompting (genre, tempo, mood, instrumentation), voice cloning direction and parameters, sound effect prompt engineering, genre vocabulary (BPM, key signature, time signature).",
        "tools": "Suno AI, Udio, ElevenLabs, Meta AudioCraft, Bark",
        "techniques": "Genre-specific music prompting, voice characteristic description, sound effect layering prompts, tempo and mood specification, instrument selection vocabulary.",
        "vocab": "BPM (beats per minute), Key signature, Time signature, Timbre, Reverb, Dry/wet, Stem, Voice cloning, Zero-shot TTS.",
        "eval": "Audio output precision, genre accuracy, emotional tone alignment with direction."
    },
    {
        "num": 21, "name": "Iris", "role": "AI Image Artist",
        "phase": "AI Generation",
        "domain": "Multi-model image generation workflows, quality assessment criteria, iterative refinement (inpainting, outpainting, variation), consistency management across batches, style locking techniques, upscaling (Real-ESRGAN, Topaz Gigapixel).",
        "tools": "Midjourney, DALL-E 3, Stable Diffusion XL, ComfyUI, Adobe Photoshop (Generative Fill), Topaz Gigapixel",
        "techniques": "Multi-model workflow orchestration, inpainting for correction, outpainting for extension, style locking via seed/reference, upscaling pipeline, quality assessment scoring.",
        "vocab": "Inpainting, Outpainting, Img2img, Seed locking, Style reference, ControlNet, IP-Adapter, Upscale, Denoise strength.",
        "eval": "Image quality (resolution, artifacts), style consistency, character continuity across outputs."
    },
    {
        "num": 22, "name": "Reel", "role": "AI Video Artist",
        "phase": "AI Generation",
        "domain": "Multi-platform video generation, motion quality assessment, shot matching across platforms, video upscaling and frame interpolation, lip sync technology, sequence assembly from AI clips.",
        "tools": "Runway Gen-3, Pika Labs, Sora, Topaz Video AI, D-ID, HeyGen",
        "techniques": "Platform selection per shot type, motion quality evaluation, shot matching across clips, frame interpolation for smoothness, lip sync alignment, sequence assembly and timing.",
        "vocab": "Temporal coherence, Frame interpolation, Motion artifacts, Lip sync, Deepfake, Face swap, Upscale, Denoise, Stabilize.",
        "eval": "Motion quality and smoothness, temporal coherence, narrative flow across assembled clips."
    },
    {
        "num": 23, "name": "Vox", "role": "AI Voice Artist",
        "phase": "AI Generation",
        "domain": "Voice casting for AI-generated characters, emotional performance direction, dialogue pacing and rhythm, accent and dialect specification, voice aging techniques, multi-character voice differentiation.",
        "tools": "ElevenLabs, PlayHT 2.0, Bark (Suno), Descript Overdub",
        "techniques": "Voice characteristic profiling, emotional range direction, pacing and rhythm control, accent specification, voice aging/de-aging, character voice differentiation.",
        "vocab": "Voice cloning, Zero-shot TTS, Prosody, Inflection, Timbre, Voice latent space, Emotional embedding, Speech synthesis.",
        "eval": "Voice-character match quality, emotional authenticity, naturalness and intelligibility."
    },
    {
        "num": 24, "name": "Sonic", "role": "Audio Producer",
        "phase": "AI Generation",
        "domain": "Dialogue editing and cleanup, sound mixing for film, mastering standards (LUFS targets), ADR recording and integration, stem delivery (M&E tracks), surround mixing (5.1, 7.1, Dolby Atmos), audio restoration techniques.",
        "tools": "Pro Tools Ultimate, Steinberg Nuendo, iZotope RX 11, Dolby Atmos Renderer, Waves plugins",
        "techniques": "Dialogue editing and smoothing, stem-based mixing workflow, loudness normalization (LUFS targeting), ADR integration, surround sound panning, audio restoration and noise reduction.",
        "vocab": "Stem, M&E (Music & Effects), LUFS, True peak, De-esser, Compressor, Limiter, Reverb bus, Print master, QC pass.",
        "eval": "Dialogue clarity, mix balance across elements, loudness compliance with delivery specs."
    },
    # PHASE 7: VFX
    {
        "num": 25, "name": "Zara", "role": "VFX Supervisor",
        "phase": "VFX",
        "domain": "VFX breakdown and bidding, on-set supervision (tracking markers, clean plates, HDRI capture), CG pipeline (model, texture, rig, animate, light, render), compositing supervision, matchmoving, digital environments.",
        "tools": "Nuke, SideFX Houdini, Autodesk Maya, Blender, Unreal Engine 5, ShotGrid (Autodesk)",
        "techniques": "VFX breakdown creation, on-set data acquisition (HDRI, Lidar, witness cameras), CG pipeline management, compositing review, matchmove supervision, digital environment design.",
        "vocab": "Plate, Roto (rotoscoping), Comp (composite), HDRI, Lidar scan, Previs, Techvis, Postvis, Clean plate, Tracking marker, Green/blue screen.",
        "eval": "Shot feasibility assessment, CG-live action integration quality, VFX budget balance."
    },
    {
        "num": 26, "name": "Eli", "role": "Editor",
        "phase": "VFX",
        "domain": "Editorial pipeline (assembly, rough cut, fine cut, picture lock), performance selection, pacing and rhythm control, parallel editing, montage theory, scene restructuring, transition design.",
        "tools": "Avid Media Composer, Adobe Premiere Pro, DaVinci Resolve, PIX",
        "techniques": "Performance-driven editing, pacing analysis, parallel editing construction, montage assembly, scene restructuring for story, transition design (hard cuts, dissolves, wipes).",
        "vocab": "Selects, Stringout, J-cut, L-cut, Match cut, Jump cut, Assembly, Rough cut, Fine cut, Picture lock, ADR cue.",
        "eval": "Narrative clarity, pacing effectiveness, emotional impact of editorial choices."
    },
    {
        "num": 27, "name": "Axel", "role": "Auto Editor",
        "phase": "VFX",
        "domain": "AI-assisted rough cut assembly, multicam synchronization, auto-reframe for multiple aspect ratios, speech-to-text editing, scene detection algorithms, music-driven editing, proxy workflow management.",
        "tools": "Premiere Pro Auto-Reframe, DaVinci Resolve Speed Editor, Descript, CapCut, Runway",
        "techniques": "AI rough cut generation, multicam sync and selection, auto-reframe aspect ratio adaptation, transcript-based editing, scene detection and organization, music-beat editing.",
        "vocab": "Auto-reframe, Multicam sync, Proxy workflow, Scene detection, Transcript edit, Smart trim, Beat sync, AI assembly.",
        "eval": "Assembly speed and efficiency, sync accuracy, reframe quality across aspect ratios."
    },
    {
        "num": 28, "name": "Hue", "role": "Colorist",
        "phase": "VFX",
        "domain": "Primary and secondary color grading, look development (LUT creation), color science (Rec.709, DCI-P3, ACES workflow), HDR grading (Dolby Vision, HDR10, HDR10+), shot matching and scene balancing.",
        "tools": "DaVinci Resolve Studio, FilmLight Baselight, Tangent Wave panels",
        "techniques": "Node-based grading workflows, look development from references, LUT creation and management, HDR trim passes, shot matching, skin tone protection, power window isolation.",
        "vocab": "Node tree, Lift/Gamma/Gain, Power window, CDL (Color Decision List), Gamut, Color space transform, Qualifier, Skin tone line.",
        "eval": "Color consistency across scenes, look alignment with creative intent, skin tone accuracy."
    },
    {
        "num": 29, "name": "Nyx", "role": "VFX Compositor",
        "phase": "VFX",
        "domain": "Node-based compositing, rotoscoping, chroma keying (green/blue screen), CG integration, camera projection, particle systems, lens effects simulation, cleanup and paint work.",
        "tools": "Foundry Nuke, Adobe After Effects, Blackmagic Fusion, Autodesk Flame",
        "techniques": "Node-based compositing workflows, advanced rotoscoping, chroma key extraction and refinement, CG-to-plate integration, lens distortion matching, cleanup and paint, particle system compositing.",
        "vocab": "Premult, Over (merge operation), Despill, Edge extend, Deep compositing, AOV pass (Arbitrary Output Variable), Holdout matte, Lens distortion.",
        "eval": "CG integration quality, edge treatment, overall shot believability."
    },
    # PHASE 8: QUALITY
    {
        "num": 30, "name": "Quinn", "role": "Continuity QA",
        "phase": "Quality",
        "domain": "Visual continuity (costume, hair, makeup, props placement), spatial continuity (screen direction, 180-degree rule compliance), temporal continuity (timeline logic), narrative continuity (plot holes, character consistency), technical QA (resolution, frame rate, artifacts).",
        "tools": "ScriptE, MovieSlate, Frame.io review tools",
        "techniques": "Continuity tracking spreadsheets, frame-by-frame comparison, screen direction mapping, timeline logic verification, plot hole detection, technical specification checking.",
        "vocab": "Continuity error, Screen direction, Crossing the line, Raccord, Script supervisor notes, Matching action, Eye trace.",
        "eval": "Error severity classification, spatial coherence, narrative consistency, technical compliance."
    },
    {
        "num": 31, "name": "Chloe", "role": "Film Critic",
        "phase": "Quality",
        "domain": "Film theory (auteur theory, genre theory, feminist film theory), narrative analysis, performance evaluation, audience reception prediction, comparative analysis with similar films, festival and award potential assessment.",
        "tools": "Rotten Tomatoes, Metacritic, CinemaScore, Box Office Mojo, Letterboxd",
        "techniques": "Theoretical framework analysis, narrative structure evaluation, performance assessment, audience testing interpretation, market positioning analysis, festival strategy recommendation.",
        "vocab": "Auteur, Diegesis, Mise-en-scene, Suture, Gaze theory, Genre hybridity, Tonal consistency, Third-act problem.",
        "eval": "Overall quality assessment, audience engagement prediction, market positioning strategy."
    },
    # PHASE 9: DISTRIBUTION
    {
        "num": 32, "name": "Luna", "role": "Subtitle Agent",
        "phase": "Distribution",
        "domain": "Subtitle formats (SRT, VTT, STL, DFXP), subtitle timing and reading speed (CPS - characters per second), line breaking rules, translation and localization, SDH (Subtitles for the Deaf and Hard of Hearing), platform-specific delivery specs (Netflix, Amazon, Disney+).",
        "tools": "Subtitle Edit, Aegisub, EZTitles, Netflix Hermes",
        "techniques": "Timing to speech rhythm, CPS optimization, line break logic, forced narrative subtitle creation, SDH annotation, multi-platform format conversion.",
        "vocab": "CPS (characters per second), Forced narrative, Burned-in, Sidecar file, Spotting (timing), SDH, Closed captions, Open captions.",
        "eval": "Timing accuracy, reading speed compliance, translation quality, platform spec adherence."
    },
    {
        "num": 33, "name": "Harper", "role": "Marketing",
        "phase": "Distribution",
        "domain": "Trailer cutting (three-act trailer structure), poster design (key art, billing block, laurels), social media strategy, press kit creation, audience segmentation, release strategy, EPK (Electronic Press Kit) production.",
        "tools": "Adobe Creative Suite (Premiere, Photoshop, After Effects), Canva, Hootsuite, Sprout Social",
        "techniques": "Three-act trailer construction, key art composition, social media campaign planning, press kit assembly, audience persona development, release window strategy.",
        "vocab": "Key art, Billing block, Laurels, One-sheet, EPK, Teaser, Trailer, TV spot, Above-the-title, Quad poster.",
        "eval": "Marketing-audience alignment, trailer effectiveness, campaign reach projections."
    },
    {
        "num": 34, "name": "Rio", "role": "Distributor",
        "phase": "Distribution",
        "domain": "Distribution models (theatrical, streaming, hybrid release), platform technical specifications, delivery specifications (codec, resolution, color space, audio format), territorial rights management, revenue models (TVOD, EST, AVOD, SVOD), DCP and IMF creation.",
        "tools": "DCP-o-matic, Netflix Backlot, Amazon Studio uploads, EasyDCP",
        "techniques": "Distribution model selection, platform-specific encoding, DCP creation and verification, IMF package assembly, territorial rights mapping, revenue waterfall modeling.",
        "vocab": "DCP (Digital Cinema Package), IMF (Interoperable Master Format), TVOD, EST, AVOD, SVOD, Holdback, Day-and-date, Platform exclusive.",
        "eval": "Platform fit analysis, delivery specification compliance, revenue optimization strategy."
    },
]

def draw_dark_bg(c):
    """Fill the entire page with dark background."""
    c.setFillColor(BG_DARK)
    c.rect(0, 0, W, H, fill=1, stroke=0)

def draw_cover(c):
    """Draw the cover page."""
    draw_dark_bg(c)

    # Accent bar at top
    c.setFillColor(ACCENT_GOLD)
    c.rect(0, H - 8, W, 8, fill=1, stroke=0)

    # Thin decorative lines
    c.setStrokeColor(HexColor("#333355"))
    c.setLineWidth(0.5)
    for y_off in range(100, 300, 20):
        c.line(60, H - y_off, W - 60, H - y_off)

    # Title
    c.setFillColor(ACCENT_GOLD)
    c.setFont("Helvetica-Bold", 42)
    c.drawCentredString(W / 2, H - 220, "GenAI Film Studio")

    # Subtitle
    c.setFillColor(TEXT_WHITE)
    c.setFont("Helvetica", 18)
    c.drawCentredString(W / 2, H - 270, "Agent Skillset Database")

    c.setFillColor(TEXT_DIM)
    c.setFont("Helvetica", 14)
    c.drawCentredString(W / 2, H - 300, "Claude Opus Knowledge Reference")

    # Divider
    c.setStrokeColor(ACCENT_GOLD)
    c.setLineWidth(2)
    c.line(W / 2 - 120, H - 325, W / 2 + 120, H - 325)

    # Date and version
    c.setFillColor(TEXT_DIM)
    c.setFont("Helvetica", 12)
    c.drawCentredString(W / 2, H - 360, "March 29, 2026  |  Version 1.0")

    # Description box
    c.setFillColor(BG_CARD)
    c.roundRect(80, H - 480, W - 160, 90, 8, fill=1, stroke=0)
    c.setFillColor(TEXT_LIGHT)
    c.setFont("Helvetica", 11)
    desc_lines = [
        "Complete domain knowledge, tools, techniques, and evaluation criteria",
        "for each of the 33 AI film production agents across 9 production phases."
    ]
    for i, line in enumerate(desc_lines):
        c.drawCentredString(W / 2, H - 425 + (1 - i) * 18, line)

    # Agent count badge
    c.setFillColor(ACCENT_GOLD)
    c.roundRect(W / 2 - 60, H - 540, 120, 36, 18, fill=1, stroke=0)
    c.setFillColor(BG_DARK)
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(W / 2, H - 528, "33 Agents")

    # Phase list
    c.setFont("Helvetica", 10)
    phases_list = [
        "Orchestration", "Pre-Production Story", "Pre-Production Visual",
        "Production", "Post-Production", "AI Generation",
        "VFX", "Quality", "Distribution"
    ]
    start_y = H - 590
    for i, phase in enumerate(phases_list):
        color = PHASE_COLORS.get(phase, TEXT_DIM)
        c.setFillColor(color)
        c.circle(W / 2 - 80, start_y - i * 18 + 3, 4, fill=1, stroke=0)
        c.setFillColor(TEXT_LIGHT)
        c.drawString(W / 2 - 68, start_y - i * 18, phase)

    # Bottom bar
    c.setFillColor(ACCENT_GOLD)
    c.rect(0, 0, W, 4, fill=1, stroke=0)

    c.showPage()

def draw_toc(c):
    """Draw table of contents."""
    draw_dark_bg(c)

    # Header
    c.setFillColor(ACCENT_GOLD)
    c.rect(0, H - 6, W, 6, fill=1, stroke=0)

    c.setFillColor(ACCENT_GOLD)
    c.setFont("Helvetica-Bold", 28)
    c.drawString(60, H - 60, "Table of Contents")

    c.setStrokeColor(ACCENT_GOLD)
    c.setLineWidth(1)
    c.line(60, H - 72, 300, H - 72)

    y = H - 110
    current_phase = ""
    line_height = 18

    for agent in agents:
        phase = agent["phase"]
        if phase != current_phase:
            current_phase = phase
            color = PHASE_COLORS.get(phase, TEXT_DIM)

            if y < 80:
                # Footer
                c.setFillColor(ACCENT_GOLD)
                c.rect(0, 0, W, 3, fill=1, stroke=0)
                c.showPage()
                draw_dark_bg(c)
                c.setFillColor(ACCENT_GOLD)
                c.rect(0, H - 6, W, 6, fill=1, stroke=0)
                y = H - 50

            # Phase header
            c.setFillColor(color)
            c.rect(50, y - 2, 4, 16, fill=1, stroke=0)
            c.setFont("Helvetica-Bold", 12)
            c.drawString(62, y, phase.upper())
            y -= line_height + 6

        if y < 80:
            c.setFillColor(ACCENT_GOLD)
            c.rect(0, 0, W, 3, fill=1, stroke=0)
            c.showPage()
            draw_dark_bg(c)
            c.setFillColor(ACCENT_GOLD)
            c.rect(0, H - 6, W, 6, fill=1, stroke=0)
            y = H - 50

        # Agent entry
        num = agent["num"]
        name = agent["name"]
        role = agent["role"]

        c.setFillColor(TEXT_WHITE)
        c.setFont("Helvetica-Bold", 10)
        c.drawString(80, y, f"{num:02d}")

        c.setFillColor(ACCENT_GOLD)
        c.setFont("Helvetica-Bold", 10)
        c.drawString(105, y, name)

        c.setFillColor(TEXT_DIM)
        c.setFont("Helvetica", 10)
        c.drawString(170, y, f"  {role}")

        # Dotted line to page number
        c.setStrokeColor(HexColor("#333355"))
        c.setDash(1, 3)
        text_end = 170 + c.stringWidth(f"  {role}", "Helvetica", 10) + 10
        c.line(min(text_end, 420), y + 3, W - 80, y + 3)
        c.setDash()

        # Page number (cover=1, toc=2, agents start at 3)
        page_num = num + 2
        c.setFillColor(TEXT_DIM)
        c.setFont("Helvetica", 10)
        c.drawRightString(W - 60, y, str(page_num))

        y -= line_height

    # Footer
    c.setFillColor(ACCENT_GOLD)
    c.rect(0, 0, W, 3, fill=1, stroke=0)
    c.showPage()

def wrap_text(text, font, size, max_width, c_obj):
    """Simple word-wrapping that returns list of lines."""
    words = text.split()
    lines = []
    current_line = ""
    for word in words:
        test = current_line + (" " if current_line else "") + word
        if c_obj.stringWidth(test, font, size) <= max_width:
            current_line = test
        else:
            if current_line:
                lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)
    return lines

def draw_agent_page(c, agent, page_num):
    """Draw a single agent detail page."""
    draw_dark_bg(c)

    phase = agent["phase"]
    accent = PHASE_COLORS.get(phase, ACCENT_GOLD)

    # Top accent bar
    c.setFillColor(accent)
    c.rect(0, H - 6, W, 6, fill=1, stroke=0)

    # Phase badge (top right)
    c.setFillColor(BG_CARD)
    badge_w = c.stringWidth(phase.upper(), "Helvetica-Bold", 9) + 20
    c.roundRect(W - badge_w - 40, H - 38, badge_w, 22, 4, fill=1, stroke=0)
    c.setFillColor(accent)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(W - badge_w - 30, H - 32, phase.upper())

    # Agent number circle
    c.setFillColor(accent)
    c.circle(70, H - 52, 18, fill=1, stroke=0)
    c.setFillColor(BG_DARK)
    c.setFont("Helvetica-Bold", 14)
    num_str = f"{agent['num']:02d}"
    c.drawCentredString(70, H - 57, num_str)

    # Agent name
    c.setFillColor(TEXT_WHITE)
    c.setFont("Helvetica-Bold", 26)
    c.drawString(100, H - 60, agent["name"])

    # Role
    name_w = c.stringWidth(agent["name"], "Helvetica-Bold", 26)
    c.setFillColor(TEXT_DIM)
    c.setFont("Helvetica", 14)
    c.drawString(108 + name_w, H - 57, f"  {agent['role']}")

    # Divider line
    c.setStrokeColor(accent)
    c.setLineWidth(2)
    c.line(50, H - 78, W - 50, H - 78)

    # Left accent bar for the content area
    c.setFillColor(accent)
    c.setFillAlpha(0.3)  # type: ignore
    c.rect(42, 40, 4, H - 130, fill=1, stroke=0)
    c.setFillAlpha(1.0)  # type: ignore

    # Content sections
    sections = [
        ("CORE DOMAIN KNOWLEDGE", agent["domain"]),
        ("KEY TOOLS", agent["tools"]),
        ("TECHNIQUES", agent["techniques"]),
        ("VOCABULARY / TERMINOLOGY", agent["vocab"]),
        ("EVALUATION CRITERIA", agent["eval"]),
    ]

    y = H - 105
    left_margin = 60
    content_width = W - 120
    section_colors = [
        accent,
        HexColor("#4fc3f7"),
        HexColor("#81c784"),
        HexColor("#ffb74d"),
        HexColor("#ef5350"),
    ]

    for idx, (title, body) in enumerate(sections):
        sec_color = section_colors[idx % len(section_colors)]

        # Section card background
        # First calculate height needed
        body_lines = wrap_text(body, "Helvetica", 10, content_width - 30, c)
        card_height = 28 + len(body_lines) * 15 + 10

        if y - card_height < 40:
            # Need a new page (shouldn't happen with this data but just in case)
            c.setFillColor(accent)
            c.rect(0, 0, W, 3, fill=1, stroke=0)
            # Page number
            c.setFillColor(TEXT_DIM)
            c.setFont("Helvetica", 9)
            c.drawRightString(W - 40, 14, f"Page {page_num}")
            c.showPage()
            draw_dark_bg(c)
            c.setFillColor(accent)
            c.rect(0, H - 6, W, 6, fill=1, stroke=0)
            y = H - 40

        # Card
        c.setFillColor(BG_CARD)
        c.roundRect(left_margin - 5, y - card_height + 20, content_width + 10, card_height, 6, fill=1, stroke=0)

        # Section accent bar
        c.setFillColor(sec_color)
        c.rect(left_margin - 5, y - card_height + 20, 3, card_height, fill=1, stroke=0)

        # Section title
        c.setFillColor(sec_color)
        c.setFont("Helvetica-Bold", 10)
        c.drawString(left_margin + 8, y, title)

        # Section body
        c.setFillColor(TEXT_LIGHT)
        c.setFont("Helvetica", 10)
        text_y = y - 18
        for line in body_lines:
            c.drawString(left_margin + 8, text_y, line)
            text_y -= 15

        y -= card_height + 8

    # Bottom accent bar
    c.setFillColor(accent)
    c.rect(0, 0, W, 3, fill=1, stroke=0)

    # Page number
    c.setFillColor(TEXT_DIM)
    c.setFont("Helvetica", 9)
    c.drawRightString(W - 40, 14, f"Page {page_num}")

    # Footer text
    c.setFillColor(HexColor("#555577"))
    c.setFont("Helvetica", 8)
    c.drawString(50, 14, "GenAI Film Studio  |  Agent Skillset Database  |  v1.0")

    c.showPage()


def main():
    c = canvas.Canvas(OUTPUT_PATH, pagesize=letter)
    c.setTitle("GenAI Film Studio - Agent Skillset Database")
    c.setAuthor("GenAI Film Studio")
    c.setSubject("Agent Skillset Database - Claude Opus Knowledge Reference")

    # Page 1: Cover
    draw_cover(c)

    # Page 2: Table of Contents
    draw_toc(c)

    # Pages 3+: Agent pages
    for i, agent in enumerate(agents):
        page_num = i + 3
        draw_agent_page(c, agent, page_num)

    c.save()
    print(f"PDF generated successfully: {OUTPUT_PATH}")
    print(f"Total pages: {len(agents) + 2} (cover + TOC + {len(agents)} agent pages)")

if __name__ == "__main__":
    main()
