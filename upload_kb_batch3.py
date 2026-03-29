#!/usr/bin/env python3
"""Upload KB batch 3: Agents 21-27."""
import json, urllib.request

API = "http://localhost:3000/api/kb/upload"

def upload(agent_id, name, content):
    data = json.dumps({"agentId": agent_id, "name": name, "content": content}).encode()
    req = urllib.request.Request(API, data=data, headers={"Content-Type": "application/json"})
    try:
        resp = urllib.request.urlopen(req)
        result = json.loads(resp.read())
        print(f"  OK  {agent_id:25s} | {result.get('contentLength',0):>5} chars")
    except Exception as e:
        print(f"  ERR {agent_id}: {e}")

# 21. IRIS — AI Image Artist
upload("ai-image-artist", "World-Class AI Image Art Direction & Production",
"""# IRIS — ELITE AI IMAGE ART DIRECTION KNOWLEDGE BASE

## I. AI IMAGE ART DIRECTION

### The Art Director's Role in AI Production
Iris doesn't just generate images — she ART DIRECTS them. This means: defining the visual standard, maintaining consistency across all generated assets, ensuring every image serves the narrative, and knowing when AI output needs human refinement.

### Quality Standards
Every generated image must pass: (1) NARRATIVE TEST — does it tell the right story? (2) CONSISTENCY TEST — does it match established visual language? (3) TECHNICAL TEST — resolution, composition, no artifacts. (4) EMOTIONAL TEST — does it evoke the intended feeling?

## II. PRODUCTION IMAGE WORKFLOW

### Asset Categories
CONCEPT ART: Exploratory, multiple variations, mood and direction. 80% prompt, 20% refinement.
KEYFRAMES: Hero images defining the look. 50% generation, 50% post-production refinement.
STORYBOARD FRAMES: Quick, consistent, readable. Speed over polish.
CHARACTER PORTRAITS: Require consistency. LoRA training or strong reference image workflow.
ENVIRONMENT PAINTINGS: Atmosphere and scale. 3D base + AI generation + paintover.
PROPS & OBJECTS: Isolated items on neutral background. Multiple angles.
TEXTURE/MATERIAL STUDIES: Close-up surface detail for production design reference.

### The Iteration Pipeline
ROUND 1 — EXPLORATION: Generate 20-50 images with prompt variations. Cast wide net.
ROUND 2 — DIRECTION: Select top 5-10, refine prompts, adjust style/lighting/composition.
ROUND 3 — REFINEMENT: Inpaint problem areas, upscale, color correct.
ROUND 4 — FINALIZATION: Composite elements, add text/annotations, delivery format.

## III. STYLE CONSISTENCY

### Creating a Visual Bible
For every project, establish: COLOR PALETTE (hex codes), LIGHTING STYLE (direction, quality, color temperature), CAMERA LENS feel (focal length, depth of field), TEXTURE QUALITY (clean vs gritty vs painterly), ATMOSPHERE (haze, particles, weather).

Document these as reusable prompt blocks that prefix every generation.

### Cross-Image Consistency Techniques
STYLE REFERENCE: Use a "style anchor" image that defines the project look. Input as style reference in Midjourney (--sref) or IP-Adapter in SD/Flux.
COLOR GRADING: Apply consistent LUT/color grade to all outputs in Photoshop/Lightroom.
CHARACTER SHEETS: Maintain detailed reference sheets for every recurring character.
ENVIRONMENT KEYS: Master images of each location that all subsequent shots reference.

## IV. COMPOSITION MASTERY

### Classical Composition Rules
RULE OF THIRDS: Subject on intersections. Dynamic, balanced.
GOLDEN RATIO/SPIRAL: Natural, organic flow. Leading the eye.
SYMMETRY: Power, order, formality (Kubrick, Wes Anderson).
LEADING LINES: Guide eye to subject using architecture, roads, shadows.
FRAME WITHIN FRAME: Use doorways, windows, arches to create depth.
NEGATIVE SPACE: Empty space creates tension, isolation, elegance.

### Depth Creation
FOREGROUND ELEMENTS: Objects close to camera create depth layers.
ATMOSPHERIC HAZE: Distance = less contrast, shifted toward sky color.
OVERLAPPING FORMS: Objects partially obscuring others establish depth order.
SCALE CONTRAST: Large foreground + small background = immense depth feel.

## V. POST-PRODUCTION REFINEMENT

### Photoshop Workflow for AI Images
1. CROP/COMPOSE: Adjust framing, remove unwanted edges
2. FREQUENCY SEPARATION: Fix skin textures, smooth artifacts
3. DODGE & BURN: Add depth, sculpt light on faces/objects
4. COLOR GRADE: Curves, hue/saturation, selective color for mood
5. SHARPENING: Selective sharpening on focal points
6. GRAIN: Add subtle film grain for organic feel
7. EXPORT: Correct resolution and color space for delivery

### Common AI Artifacts to Fix
HANDS: Extra/missing fingers — inpaint or composite from reference
EYES: Asymmetry, wrong direction — careful clone/transform
TEXT: Garbled letters — remove and add real text
SYMMETRY: Faces too perfect/synthetic — add subtle asymmetry
EDGES: Hard borders between AI-generated regions — blend with soft brush

## VI. REFERENCES

Tools: Midjourney, DALL-E 3, Stable Diffusion/Flux (ComfyUI), Adobe Firefly, Photoshop (generative fill), Lightroom.
Upscaling: Magnific AI, Topaz Gigapixel, Real-ESRGAN.
Resources: ArtStation (reference), Behance, Pinterest (mood boards), Coolors (palette generation).""")

# 22. REEL — AI Video Artist
upload("ai-video-artist", "World-Class AI Video Art Direction & Production",
"""# REEL — ELITE AI VIDEO ART DIRECTION KNOWLEDGE BASE

## I. AI VIDEO PRODUCTION PIPELINE

### The Shot-by-Shot Approach
AI video is generated in SHORT CLIPS (4-10 seconds each). A full scene requires: (1) Pre-plan every shot with storyboard, (2) Generate each shot individually, (3) Edit shots together with transitions, (4) Add sound design and music, (5) Color grade for consistency.

### Shot Planning Document
For each shot: SHOT# | DURATION | CAMERA | SUBJECT | ACTION | PROMPT | REFERENCE_FRAME
This document is the shooting script for AI video production.

## II. ACHIEVING CINEMATIC QUALITY

### Camera Movement Prompting
For professional results, specify camera behavior precisely:
STABLE SHOTS: "locked-off camera," "tripod," "static frame" — reduces AI jitter
SMOOTH MOVEMENT: "slow cinematic dolly," "gentle crane up" — works best
COMPLEX MOVEMENT: "orbit shot," "tracking follow" — test extensively, may need multiple generations

### Lighting Consistency
Specify the SAME lighting in every prompt for a scene: "warm golden hour side lighting from the left, soft shadows, ambient fill" — copy this across all shots in the sequence.

### Film Grain & Texture
Add "35mm film grain," "cinematic color grading," "2.39:1 aspect ratio" to every prompt for consistent cinematic feel. Alternatively, add grain and letterboxing in post.

## III. NARRATIVE VIDEO CONSTRUCTION

### Scene Assembly Workflow
1. STORYBOARD: Draw/generate every shot in the scene
2. GENERATE: Create each shot as an AI video clip (2-3 attempts per shot for best result)
3. SELECT: Choose best take of each shot
4. ROUGH CUT: Assemble in NLE (Premiere, DaVinci, Final Cut)
5. TRIM: Cut each clip to exact needed duration
6. TRANSITIONS: Add cuts, dissolves, match cuts as designed
7. SOUND: Layer dialogue, SFX, ambience, music
8. COLOR: Grade for consistency across all clips
9. EXPORT: Final delivery format

### Continuity Between Clips
Use the LAST FRAME of the previous clip as the FIRST FRAME reference for the next clip. This maintains: character position, lighting, environment, mood.

### Handling Character Consistency
Method 1: LoRA-trained character model (best consistency, requires training)
Method 2: Reference image input (img2vid with character portrait)
Method 3: Consistent detailed description (same words in every prompt)
Method 4: Post-production face replacement (DeepFaceLab, careful ethical use)

## IV. VISUAL EFFECTS IN AI VIDEO

### Compositing AI Video
Layer multiple AI generations: background plate + character layer + foreground elements + atmospheric effects. Use green screen / masking in post.

### Speed Manipulation
SLOW MOTION: Generate at normal speed, apply AI frame interpolation (RIFE, Topaz Video AI, DaVinci Speed Warp). 24fps to 120fps+ for smooth slow-mo.
TIME-LAPSE: Generate with "time-lapse" in prompt, or composite multiple stills with morphing.
SPEED RAMP: Edit between normal and slow-motion sections for dramatic effect.

### Seamless Loops
Generate with matching first/last frames. Or: generate forward, reverse the clip, crossfade at midpoint. Useful for: environmental shots, ambient backgrounds, loading screens.

## V. EDITING AI VIDEO

### NLE Software
DAVINCI RESOLVE: Free, powerful color grading, Fusion VFX. Industry standard.
PREMIERE PRO: Adobe ecosystem integration, wide plugin support.
FINAL CUT PRO: Fast, Apple Silicon optimized, magnetic timeline.

### AI-Specific Editing Techniques
BEST TAKE SELECTION: Generate 3-5 versions of each shot, select best
FRANKENSTEINING: Combine best parts of different takes (composite in/out points)
STABILIZATION: AI video often has micro-jitter. Apply warp stabilizer.
UPSCALING: Most AI video generates at 720p-1080p. Upscale to 4K with Topaz Video AI.

## VI. ETHICAL CONSIDERATIONS

Always disclose AI-generated content in professional contexts. Never create deepfakes or non-consensual likeness usage. Respect IP: don't generate in copyrighted character likenesses without rights. Consider bias in AI models and actively diversify output.

## VII. REFERENCES

Platforms: Runway ML, Kling AI, Pika, Luma Dream Machine, Sora.
Post-Production: DaVinci Resolve, Topaz Video AI, After Effects.
Learning: Corridor Crew (YouTube — VFX + AI), Curious Refuge (AI filmmaking course).""")

# 23. VOX — AI Voice Artist
upload("ai-voice-artist", "World-Class AI Voice Production & Speech Synthesis",
"""# VOX — ELITE AI VOICE PRODUCTION KNOWLEDGE BASE

## I. VOICE SYNTHESIS TECHNOLOGY

### Text-to-Speech (TTS) Models
ELEVENLABS: Market leader. 29+ languages, voice cloning from 30 seconds of audio, emotion control, pacing control. Professional broadcast quality.
OPENAI TTS (Alloy/Echo/Fable/Onyx/Nova/Shimmer): Six preset voices, natural prosody, fast. Good for narration.
GOOGLE CLOUD TTS: WaveNet voices, SSML support, multi-language. Enterprise-grade.
MICROSOFT AZURE TTS: Neural voices, SSML, custom voice training. Integration with Azure ecosystem.
BARK (Suno): Open-source, emotional range, non-speech sounds (laughing, crying, music).
COQUI XTTS: Open-source, multilingual cloning, self-hostable.

### Voice Cloning
Ethical voice cloning requires: CONSENT from the voice owner, CLEAR USE CASE, ATTRIBUTION when appropriate.
Quality factors: clean recording (studio quality), 3+ minutes of speech, consistent microphone, no background noise, varied intonation.

## II. VOICE DIRECTION FOR AI

### Character Voice Design
Every character voice needs a VOICE BRIEF:
- AGE: Child (6-12), Teen (13-17), Young Adult (18-30), Middle (30-50), Mature (50-65), Elder (65+)
- GENDER: Male, Female, Non-binary, Androgynous
- PITCH: Bass, Baritone, Tenor, Alto, Mezzo-Soprano, Soprano
- TEXTURE: Smooth, Gravelly, Breathy, Nasal, Raspy, Crisp, Warm, Thin
- PACE: Deliberate/slow, Measured, Conversational, Quick, Rapid
- ACCENT: Specify precisely (not "British" but "London working-class Cockney" or "RP")
- EMOTIONAL DEFAULT: The character's baseline emotional state

### Directing AI Voice Performance
Since AI can't take direction like a human actor, you achieve performance through:
1. TEXT MANIPULATION: Add punctuation for pauses (... or —), CAPS for emphasis, stage directions in [brackets]
2. SSML TAGS: <break time="500ms"/>, <emphasis level="strong">, <prosody rate="slow">, <say-as interpret-as="exclamation">
3. EMOTIONAL PRESETS: Set mood parameter (if available): happy, sad, angry, fearful, surprised
4. MULTIPLE TAKES: Generate 3-5 versions, select best performance
5. MANUAL EDITING: Splice best sections from different takes

## III. DIALOGUE PRODUCTION

### Pre-Production
1. SCRIPT PREPARATION: Format dialogue with character names, stage directions, emotional notes
2. VOICE CASTING: Test multiple AI voices for each character. Select for: distinctiveness, appropriate quality, emotional range
3. PRONUNCIATION GUIDE: Mark unusual words, names, technical terms with phonetic guides

### Recording Workflow
1. Generate character voice for each line individually
2. Adjust pacing to match scene requirements
3. Listen for: naturalness, emotional accuracy, pronunciation, consistency
4. Re-generate problem lines with adjusted prompts
5. Export individual line files, named: [Scene]_[Character]_[Line#].wav

### Dialogue Editing
Clean each line: trim silence, normalize levels (-24 LUFS for dialogue), remove clicks/artifacts.
Assembly: Place lines on timeline with natural conversational gaps (200-800ms between speakers).
Room tone: Add consistent ambient/room tone underneath all dialogue for sonic cohesion.

## IV. NARRATION PRODUCTION

### Narration Styles
DOCUMENTARY: Warm, authoritative, measured pace, clear diction. Think David Attenborough or Morgan Freeman.
AUDIOBOOK: Engaging, varied pacing, character differentiation through subtle voice changes.
COMMERCIAL: Energetic, persuasive, clear call-to-action, upbeat.
MEDITATION/WELLNESS: Slow, gentle, low pitch, even breathing, calming.
CORPORATE: Professional, neutral, clear, moderate pace.

### Long-Form Narration Workflow
For content over 5 minutes: generate in paragraph-sized chunks (30-60 seconds each), maintaining consistent voice and pacing. Edit together with crossfades. Add subtle room ambience for naturalness.

## V. TECHNICAL STANDARDS

### Audio Quality
Sample Rate: 48kHz for video production, 44.1kHz for music/standalone audio.
Bit Depth: 24-bit for production, 16-bit for final delivery.
Format: WAV for production, MP3/AAC for web delivery.
Loudness: -24 LUFS for dialogue (broadcast), -16 LUFS for podcast, -14 LUFS for streaming music.

### Delivery Formats
STEM DELIVERY: Separate files for each character/narration track.
MIXED DELIVERY: Combined dialogue mix.
M&E (Music & Effects): International delivery format — all audio EXCEPT dialogue, for dubbing.

## VI. MULTILINGUAL PRODUCTION

### AI Dubbing
Generate translated dialogue in character-matched voices. Challenges: lip sync (AI lip sync tools: Wav2Lip, SadTalker), timing (translated text may be longer/shorter), cultural adaptation (not just translation but localization).

### Languages by AI Quality (2024-2026)
EXCELLENT: English, Spanish, French, German, Portuguese, Japanese, Korean, Chinese (Mandarin)
GOOD: Italian, Dutch, Polish, Hindi, Turkish, Arabic, Swedish, Norwegian
DEVELOPING: Thai, Vietnamese, Indonesian, Bengali, Swahili

## VII. REFERENCES

Platforms: ElevenLabs, OpenAI TTS API, Google Cloud TTS, Microsoft Azure TTS.
Audio Editing: Adobe Audition, Audacity (free), iZotope RX (restoration), Pro Tools.
Standards: EBU R128 (loudness), ITU-R BS.1770 (loudness measurement).""")

# 24. SONIC — Audio Producer
upload("audio-producer", "World-Class Audio Production & Music Supervision",
"""# SONIC — ELITE AUDIO PRODUCTION KNOWLEDGE BASE

## I. AUDIO PRODUCTION FOR FILM

### The Audio Producer's Role
The audio producer oversees ALL audio elements in the production: music (score + licensed tracks), dialogue (production + ADR), sound effects (SFX + Foley), and the final mix. They ensure sonic consistency, emotional alignment with picture, and technical delivery standards.

### The Audio Production Timeline
PRE-PRODUCTION: Spot sessions, music briefs, sound design concepts, temp music selection
PRODUCTION: On-set sound monitoring, wild track recording, production sound quality control
POST-PRODUCTION: Dialogue edit, ADR, SFX edit, Foley, music composition/licensing, pre-dubs, final mix
DELIVERY: Format masters (theatrical, streaming, broadcast, home video)

## II. MUSIC SUPERVISION

### Licensed Music
SYNC LICENSE: Permission from music publisher (songwriter's share). Covers the composition.
MASTER LICENSE: Permission from record label (recording owner). Covers the specific recording.
COSTS: Indie track in indie film: $5K-$25K total. Major artist in studio film: $100K-$500K+.
ALTERNATIVES: Production music libraries (Artlist, Epidemic Sound, MusicBed), original compositions, AI-generated music.

### Temp Music Strategy
Use temp tracks during editing to establish mood and pacing, but WARN the director about "temp love" — becoming too attached to temp tracks makes it hard to accept the original score.

### Music Spotting
Walk through the film with director and composer. For each music cue, document: TIMECODE START/END, EMOTIONAL INTENT, INSTRUMENTATION PREFERENCE, REFERENCE TRACKS, SYNC POINTS (specific moments music must hit).

## III. MIXING FUNDAMENTALS

### The Three Pillars of a Film Mix
DIALOGUE: Always king. Must be intelligible at all times. Level: -24 to -20 LUFS.
MUSIC: Supports emotion. Ducks under dialogue. Swells in music-only moments.
EFFECTS: Creates the world. Punctuates action. Background ambience is continuous.

### Frequency Allocation
SUB BASS (20-60 Hz): Rumble, LFE channel, impacts, explosions
BASS (60-250 Hz): Music bass, vehicle engines, weight
LOW-MID (250-500 Hz): Dialogue warmth, music body. CRITICAL — too much = muddy
MID (500-2K Hz): Dialogue clarity, music presence. The ear is most sensitive here.
UPPER-MID (2K-6K Hz): Dialogue intelligibility, presence, edge. Too much = harsh/fatiguing.
HIGH (6K-12K Hz): Brilliance, air, sibilance, detail
AIR (12K-20K Hz): Sparkle, openness, spatial cues

### Dynamic Range
THEATRICAL MIX: Wide dynamic range. Whispers to explosions. 20+ dB range.
HOME/STREAMING MIX: Compressed dynamic range. Dialogue must be heard over ambient noise. 12-15 dB range.
NEAR-FIELD MIX: For laptop/phone playback. Heavy compression. Dialogue above all. 8-10 dB range.

## IV. SPATIAL AUDIO

### Dolby Atmos for Film
Object-based audio: sounds are placed in 3D space (x, y, z coordinates) rather than assigned to fixed channels. Up to 128 audio objects + 7.1.4 bed.
ATMOS MIX WORKFLOW: Create bed mix (7.1.4 ambient), add objects for point sources (dialogue, specific SFX), pan objects in 3D space, render to delivery format.

### Surround Sound Principles
CENTER CHANNEL: Dialogue (always). Anchored to screen.
LEFT/RIGHT FRONT: Music, wide SFX, stereo imaging.
SURROUND L/R: Ambient, room tone, off-screen sound, immersion.
REAR SURROUNDS: Extended ambience, flyover effects.
LFE (.1): Subwoofer — explosions, rumble, musical bass extension.
HEIGHT (Atmos): Overhead sounds — rain, helicopter, spatial ambience.

## V. PRODUCTION SOUND

### Equipment Standards
RECORDER: Sound Devices Scorpio (32-track), 888 (8-track), MixPre-10 (budget).
BOOM MICS: Sennheiser MKH-416 (exterior, shotgun), MKH-50 (interior, hypercardioid), Schoeps CMC6/MK41.
WIRELESS: Lectrosonics (SMWB/SRc), Wisycom (MCR54), Sennheiser EW series. Lavalier: DPA 6060, Sanken COS-11, Countryman B6.
MONITORING: Comtek system for director/script supervisor IFB.

### On-Set Sound Best Practices
Room tone: Record 60 seconds of silence in every location. Essential for dialogue editing.
Wild lines: If a take had great performance but bad audio, record the line immediately after with same energy.
Sound reports: Document every take with: track assignments, notes on quality, circle takes.

## VI. MASTERING & DELIVERY

### Delivery Specifications
THEATRICAL: Dolby Atmos (7.1.4 objects), 7.1, 5.1, stereo fold-down. 48kHz/24-bit.
NETFLIX: Dolby Atmos master + 5.1 near-field + stereo. -27 LKFS dialogue norm.
AMAZON: Dolby Atmos or 5.1. -24 LKFS.
BROADCAST: Stereo or 5.1. -24 LKFS (US), -23 LUFS (EU).
STREAMING (general): Loudness normalized to -14 to -16 LUFS.

## VII. AI AUDIO IN PRODUCTION

### Where AI Audio Fits
TEMP MUSIC: AI-generated temp tracks during editing (replace with real score/licensed tracks)
AMBIENT BEDS: AI-generated background ambiences and room tones
SOUND EFFECTS: AI SFX for unique, hard-to-record sounds
SCRATCH DIALOGUE: AI voices for pre-visualization before casting
TRANSLATION: AI-generated dubbed dialogue for international pre-sales

## VIII. REFERENCES

Books: "Sound Design" (Sonnenschein), "The Sound Effects Bible" (Viers), "Audio Post Production for Television and Film" (Wyatt/Amyes).
Organizations: CAS (Cinema Audio Society), MPSE (Motion Picture Sound Editors), AES (Audio Engineering Society).
Tools: Pro Tools (Avid), Nuendo (Steinberg), DaVinci Resolve Fairlight, Logic Pro, iZotope RX.""")

# 25. ZARA — VFX Supervisor
upload("vfx-supervisor", "World-Class Visual Effects Supervision & Pipeline",
"""# ZARA — ELITE VFX SUPERVISION KNOWLEDGE BASE

## I. THE VFX SUPERVISOR'S ROLE

### On-Set Responsibilities
The VFX Supervisor is the bridge between production and post. On set: (1) Ensure proper data capture for VFX shots (tracking markers, clean plates, HDRIs, reference photography, grey/chrome ball lighting reference). (2) Advise director on what's achievable. (3) Monitor shots that will require VFX. (4) Supervise blue/green screen work. (5) Document everything.

### The VFX Pipeline Overview
PREVIS (Pre-visualization): Low-res 3D animation of complex sequences before shooting. Establishes camera, timing, blocking.
TECHVIS (Technical Visualization): Engineering specs for practical builds, rigging, camera rigs based on previs.
ON-SET VFX: Supervision, data acquisition, reference capture.
POSTVIS (Post-visualization): Quick VFX composites during editorial to show intent.
PRODUCTION: The full VFX pipeline — asset build, animation, simulation, lighting, rendering, compositing.
FINAL: Delivery of finished VFX shots to editorial for conform.

## II. VFX TECHNIQUES

### Computer Generated Imagery (CGI)
MODELING: 3D asset creation. Maya, Blender, ZBrush (sculpting), Houdini (procedural).
TEXTURING: Surface appearance. Substance 3D Painter/Designer, Mari (high-end), UV mapping.
RIGGING: Skeleton + controls for animation. Auto-rigging (Mixamo), custom rigs for complex characters.
ANIMATION: Keyframe (hand-animated), Motion Capture (MoCap — Vicon, OptiTrack, Rokoko), Performance Capture (face + body — Dynamixyz, Faceware, iPhone ARKit).
SIMULATION (FX): Physics-based effects — fire, water, smoke, cloth, destruction. Houdini (industry standard), Embergen (real-time fire/smoke), Phoenix FD (3DS Max).
LIGHTING: Match CG lighting to plate photography. HDRI capture on set is essential. PBR (Physically Based Rendering) ensures realistic light interaction.
RENDERING: Arnold (Autodesk), RenderMan (Pixar), V-Ray (Chaos), Redshift (GPU), Cycles (Blender). Render farms: AWS Deadline, Google Cloud Batch, Conductor.

### Compositing
The art of combining multiple image elements into a single seamless frame.
KEYING: Extracting subjects from blue/green screen. Keylight, Primatte, IBK.
ROTOSCOPING: Frame-by-frame masking of elements without green screen. Silhouette, Mocha Pro.
TRACKING: 3D camera tracking (matchmoving) to place CG objects in live-action plates. PFTrack, SynthEyes, 3DEqualizer.
COLOR MATCHING: Ensuring CG elements match the color, contrast, and grain of the plate.
INTEGRATION: Adding shadows, reflections, interactive lighting, atmospheric effects to sell the composite.

### Matte Painting
Digital painting extended backgrounds, environments, and set extensions. Traditionally Photoshop, now increasingly 3D environments (Unreal Engine, Blender) + 2D paint-over.

## III. ON-SET DATA ACQUISITION

### Essential VFX Data
HDRI (High Dynamic Range Image): Chrome and grey ball photography at each VFX setup. Captures full lighting environment for CG rendering.
LIDAR SCAN: 3D scan of set/location for accurate CG integration. FARO, Leica scanners.
TRACKING MARKERS: Physical markers on green screens and set pieces for 3D tracking. Tennis balls, tracking dots.
CLEAN PLATES: Identical shot without actors/action for background reconstruction.
REFERENCE PHOTOGRAPHY: Texture references, color charts (X-Rite ColorChecker), measurements.
WITNESS CAMERAS: Additional cameras capturing VFX action from multiple angles for reference.

## IV. VFX BUDGETING

### Shot Complexity Tiers
SIMPLE (e.g., wire removal, sky replacement): $2K-$10K per shot
MEDIUM (e.g., set extension, CG prop, screen replacement): $10K-$50K per shot
COMPLEX (e.g., full CG character, destruction sim, crowd duplication): $50K-$200K per shot
HERO (e.g., full CG environment, creature close-up, massive battle): $200K-$1M+ per shot

### VFX Vendor Management
RFP (Request for Proposal): Send shot breakdowns to multiple vendors. Include: reference, complexity assessment, schedule, delivery specs.
BID COMPARISON: Evaluate on: price, quality (reel), schedule feasibility, capacity, communication.
MILESTONE DELIVERY: Asset approval > Layout > Animation > Lighting > Comp > Final.
SHOT STATUS: Track per-shot progress — NOT STARTED > IN PROGRESS > INTERNAL REVIEW > CLIENT REVIEW > APPROVED > FINAL.

## V. AI IN VFX

### AI-Powered VFX Tools
ROTOSCOPING: AI roto (Runway, Davinci Neural Engine, Rotobot) dramatically speeds up roto work.
UPSCALING: AI upscaling (Topaz, Real-ESRGAN) for resolution enhancement.
DENOISING: AI denoising in renders (NVIDIA OptiX, Intel OIDN) cuts render time 50-80%.
FACE REPLACEMENT: Deepfake technology for de-aging, face replacement (ethical use cases: de-aging actors, recreating deceased performers with estate permission).
BACKGROUND GENERATION: AI-generated environments as matte painting bases.
MOTION CAPTURE: AI-based markerless MoCap (Move.ai, Plask, DeepMotion).

## VI. INDUSTRY TOOLS

3D: Maya (Autodesk), Houdini (SideFX), Blender, Cinema 4D, 3DS Max.
Compositing: Nuke (Foundry — industry standard), After Effects (Adobe), Fusion (Blackmagic, free with DaVinci).
Tracking: PFTrack, SynthEyes, 3DEqualizer.
Pipeline: ShotGrid (Autodesk), ftrack, Kitsu (open-source).
Review: Frame.io, SyncSketch, Frankie (DaVinci), cineSync.
Real-time: Unreal Engine 5, Unity HDRP.

## VII. LEGENDARY VFX

STAR WARS (1977): ILM founded. Miniatures, motion control, optical compositing.
JURASSIC PARK (1993): First photorealistic CG creatures + practical animatronics.
THE MATRIX (1999): Bullet time. Virtual cinematography.
LORD OF THE RINGS (2001-2003): Massive (crowd simulation), Gollum (performance capture), miniatures at epic scale.
AVATAR (2009): Performance capture revolution, virtual production, stereoscopic 3D.
GRAVITY (2013): "Lightbox" — LED-lit environments for realistic space lighting on actors.
THE MANDALORIAN (2019): StageCraft LED Volume — real-time VFX on set.
AVATAR: THE WAY OF WATER (2022): Underwater performance capture, HFR, next-gen facial capture.

## VIII. REFERENCES

Books: "The VES Handbook of Visual Effects" (Okun/Zwerman), "Digital Compositing for Film and Video" (Steve Wright), "The Art and Science of Digital Compositing" (Brinkmann).
Organizations: VES (Visual Effects Society), BAFTA VFX.
Studios: ILM, Weta FX, DNEG, Framestore, MPC, Digital Domain, Sony Imageworks.""")

# 26. ELI — Editor
upload("editor", "World-Class Film Editing & Post-Production",
"""# ELI — ELITE FILM EDITING KNOWLEDGE BASE

## I. EDITING PHILOSOPHY

### The Invisible Art
The best editing is invisible. The audience should be emotionally carried through the story without ever thinking about cuts. Walter Murch's "Rule of Six" — priorities when making a cut:
1. EMOTION (51%): Does the cut feel right emotionally?
2. STORY (23%): Does it advance the story?
3. RHYTHM (10%): Does it occur at the right rhythmic moment?
4. EYE-TRACE (7%): Does it follow where the audience is looking?
5. TWO-DIMENSIONAL SCREEN (5%): Does the new composition work?
6. THREE-DIMENSIONAL SPACE (4%): Does it maintain spatial continuity?

Murch's insight: if you have to sacrifice something, sacrifice from the bottom up. Emotion is ALWAYS king.

## II. THE EDITING WORKFLOW

### Assembly Cut
The first pass: every scene in script order, using the best take of each setup. Usually 2-3x the final runtime. No finesse — just story structure. The editor often does this while production is still shooting.

### Rough Cut
Tighten assembly. Make scene-level decisions: what stays, what's trimmed, what's reordered. Performance selects refined. Temp music and temp sound effects added. Usually 30-50% longer than final.

### Fine Cut
Frame-level precision. Every cut optimized. Performance perfected. Rhythm established. Temp audio refined. This is where the craft lives.

### Picture Lock
The FINAL edit. No more changes to picture (or only minor adjustments). All subsequent work (VFX, sound, color, music) is done to the locked picture. Changing picture after lock is expensive — new VFX renders, new sound edits, new music sync.

## III. CUTTING TECHNIQUE

### Types of Cuts
HARD CUT: Direct cut from one shot to another. Standard, clean.
J-CUT: Audio from next scene starts before picture cuts. Creates anticipation. Common in dialogue scenes.
L-CUT: Audio from current scene continues after picture cuts to next. Creates continuity.
MATCH CUT: Visual similarity links two shots. 2001: bone to satellite. Lawrence of Arabia: match to sunrise.
JUMP CUT: Intentional discontinuity within same shot. Time passing, agitation, modern style.
SMASH CUT: Abrupt cut between dramatically different scenes. Comedy or shock.
CROSS-CUT/INTERCUT: Alternating between two or more simultaneous storylines.
MONTAGE: Compressed time passage through a series of shots with music.
FADE IN/OUT: Gradual appearance/disappearance. Scene or act transitions.
DISSOLVE: Overlapping fade-out and fade-in. Time passage, dream, memory.

### Cutting on Action
Cut during movement — the eye follows the action and doesn't notice the edit. A hand reaching for a door in medium shot, cut to close-up of hand grabbing handle mid-reach. The motion masks the cut.

### The Kuleshov Effect
The same shot of a face takes on different meanings based on what's cut next to it. Face + food = hunger. Face + dead child = grief. Face + attractive person = desire. THIS IS THE FUNDAMENTAL POWER OF EDITING — meaning is created by juxtaposition, not by individual shots.

## IV. PACING & RHYTHM

### Scene-Level Pacing
Short scenes = urgency, energy (action, thriller climax)
Long scenes = depth, tension, intimacy (drama, character development)
Alternating short/long = dynamic rhythm, prevents fatigue

### Cut-Level Pacing
Fast cutting (< 2 seconds per shot): Chaos, action, confusion, energy
Medium cutting (2-5 seconds): Conversational, comfortable, standard
Slow cutting (5-15+ seconds): Contemplation, tension building, art-house
Hold after the scene "ends": Creates discomfort, forces audience to think

### Music as Pacing Tool
Cut on the beat: Creates energy, musicality, satisfaction
Cut off the beat: Creates tension, unease, sophistication
Letting music drive the edit: Montages, emotional swells, transitions

## V. EDITING SOFTWARE

### Industry Standard NLEs
AVID MEDIA COMPOSER: Hollywood's standard for decades. Bin system, collaborative editing, robust media management. Used by: nearly all major studio features and broadcast TV.
DAVINCI RESOLVE: Free + Studio ($295). Color grading + editing + VFX + audio in one app. Rapidly gaining market share. Used by: indie films, streaming content, YouTube.
PREMIERE PRO: Adobe ecosystem integration. Strong for hybrid video/graphics workflows.
FINAL CUT PRO: Apple Silicon optimized. Fast, intuitive. Strong in doc/indie.

### Collaborative Editing
Avid's shared storage + bin locking allows multiple editors on same project simultaneously. NEXIS shared storage. Essential for episodic TV where multiple episodes cut simultaneously.

## VI. LEGENDARY EDITORS

WALTER MURCH: Apocalypse Now, The English Patient, The Conversation. Wrote "In the Blink of an Eye" — the most important book on editing theory.
THELMA SCHOONMAKER: Scorsese's editor for 50+ years. Raging Bull, Goodfellas, The Departed. Energy and rhythm master.
MICHAEL KAHN: Spielberg's editor for 40+ years. Schindler's List, Saving Private Ryan, Raiders.
SALLY MENKE: Tarantino's editor through Kill Bill. Defined the rhythmic, music-driven Tarantino style.
LEE SMITH: Nolan's editor. Interstellar, Dunkirk, Inception. Master of cross-cutting timelines.
MARGARET SIXEL: Mad Max: Fury Road (Oscar winner). Turned chaos into clarity through editing.

## VII. REFERENCES

Books: "In the Blink of an Eye" (Walter Murch), "The Technique of Film and Video Editing" (Ken Dancyger), "Cut by Cut" (Gael Chandler), "When the Shooting Stops... the Cutting Begins" (Ralph Rosenblum).
Organizations: ACE (American Cinema Editors). ACE Eddie Awards.
Education: EditFest, editors' panels at NAB/IBC.""")

# 27. AXEL — Auto Editor
upload("auto-editor", "World-Class Automated Editing & AI-Assisted Post-Production",
"""# AXEL — ELITE AUTOMATED EDITING KNOWLEDGE BASE

## I. AUTOMATED EDITING PRINCIPLES

### What AI Editing Can Do
1. ASSEMBLY: Auto-sync multi-camera footage using audio waveforms. Auto-select best takes using face detection, audio quality, and sharpness metrics.
2. ROUGH CUT: AI-driven scene assembly based on script matching (speech-to-text aligned with screenplay).
3. SELECTION: Auto-highlight best performances using facial expression analysis, vocal energy, and gestures.
4. PACING: Algorithmically adjust cut timing based on music tempo, dialogue rhythm, and genre conventions.
5. COLOR MATCHING: Auto-match shots within a scene for consistency.
6. AUDIO LEVELING: Automatic dialogue normalization and noise reduction.

### What AI Editing Cannot Replace
Creative decision-making, emotional intuition, narrative restructuring, performance nuance detection, comedic timing, the "aha" moment of a perfect match cut. AI assists the editor — it doesn't replace them.

## II. AUTOMATED EDITING TECHNIQUES

### Multi-Cam Sync
Audio waveform matching: Align all cameras using production audio. Software: PluralEyes (Red Giant), DaVinci Resolve auto-sync, Premiere multi-cam.
Timecode sync: If all cameras share timecode (jam-synced on set), alignment is automatic and frame-accurate.

### Script-Based Assembly
1. Run speech-to-text on all production audio
2. Match transcription to screenplay text
3. Identify which take covers which lines
4. Auto-assemble based on: best audio quality, preferred take notes, director's circle takes
5. Insert coverage based on shot type metadata (wide, medium, close-up)

### AI-Assisted Selection
FACIAL ANALYSIS: Detect when actors blink during lines (unusable), look off-camera (distraction), or break character.
AUDIO ANALYSIS: Flag takes with background noise, mic bumps, airplane flyovers, or crew talking.
SHARPNESS ANALYSIS: Auto-detect soft focus, camera shakes, or rack focus errors.
METADATA DRIVEN: Use script supervisor notes and circle takes to prioritize.

## III. EDITING WORKFLOW AUTOMATION

### Template-Based Editing
For recurring formats (interviews, vlogs, corporate), create EDITING TEMPLATES:
- Beat patterns (intro, A-roll, B-roll, lower thirds, outro)
- Auto-generated lower thirds from metadata
- Music auto-placement and ducking
- Standard color grade application
- Auto-export to multiple formats

### Batch Processing
TRANSCODE: Batch convert all footage to editing-friendly codec (ProRes Proxy/LT).
PROXY WORKFLOW: Auto-generate low-res proxies for editing, relink to full-res for finishing.
RENDER: Batch render multiple delivery formats from single timeline.
SUBTITLE BURN-IN: Auto-apply subtitles and render multiple language versions.

## IV. AI TOOLS FOR EDITING

### Commercial AI Editing Tools
DAVINCI RESOLVE AI: AI-based scene cut detection, facial recognition, magic mask, voice isolation, speed warp, super scale.
PREMIERE AUTO REFRAME: AI-powered aspect ratio adaptation (16:9 to 9:16 for social).
RUNWAY: AI-powered green screen (Remove Background), inpainting, super-slow motion.
DESCRIPT: Text-based video editing — edit the transcript, video follows.
OPUS CLIP: AI-powered clip extraction for social media from long-form content.
TOPAZ VIDEO AI: Upscaling, deinterlacing, frame interpolation, stabilization.

### Open-Source AI Tools
WHISPER (OpenAI): Speech-to-text for transcription and subtitle generation.
RIFE: AI frame interpolation for smooth slow-motion.
REAL-ESRGAN: Image/video upscaling.
DEMUCS (Meta): Audio source separation (vocals, drums, bass, other).
PYANNOTE: Speaker diarization (who speaks when).

## V. DELIVERY AUTOMATION

### Multi-Platform Output
From a single master timeline, auto-export:
THEATRICAL: DCP (Digital Cinema Package), ProRes 4444 XQ, 24fps
STREAMING: H.264/H.265 at multiple bitrates, HDR and SDR versions
BROADCAST: XDCAM HD, ProRes 422, closed captions embedded
SOCIAL: 9:16 vertical (TikTok/Reels/Shorts), 1:1 square, 16:9 landscape
WEB: H.264 at 1080p, optimized for streaming

### Quality Control
Automated QC tools check: black frame detection, audio silence detection, loudness compliance, color gamut legality, safe area, closed caption timing, file naming conventions.

## VI. REFERENCES

Software: DaVinci Resolve, Premiere Pro, Avid, Final Cut Pro, Descript, Frame.io.
AI Tools: Topaz Video AI, Runway ML, Whisper, RIFE, Real-ESRGAN.
Education: Ripple Training, MZed (post-production courses).""")

print("\n=== Batch 3 complete (agents 21-27) ===")
