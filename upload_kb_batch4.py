#!/usr/bin/env python3
"""Upload KB batch 4: Agents 28-34 (final batch)."""
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

# 28. HUE — Colorist
upload("colorist", "World-Class Color Grading & Digital Intermediate",
"""# HUE — ELITE COLOR GRADING KNOWLEDGE BASE

## I. COLOR GRADING PHILOSOPHY

### The Colorist's Power
Color grading is the FINAL creative pass on a film. It determines the audience's emotional experience more than almost any other post-production process. A warm grade makes a scene feel nostalgic; a cold grade makes it feel clinical; a desaturated grade feels bleak; a saturated grade feels vibrant. The colorist completes the director and DP's vision.

### Color as Storytelling
Different acts/sequences should have distinct palettes. A film might progress: warm (safety) > neutral (journey) > cold (danger) > warm again (resolution). This COLOR ARC mirrors the story arc.

## II. COLOR SCIENCE FUNDAMENTALS

### Color Spaces
REC.709: Standard HD color space. sRGB equivalent. Most consumer displays.
DCI-P3: Digital cinema standard. 25% wider gamut than Rec.709. Theater projectors.
REC.2020: Ultra-wide gamut for HDR/UHD. Future-proof but few displays cover it fully.
ACES (Academy Color Encoding System): Scene-referred, device-independent. The universal interchange standard for professional pipelines.

### Log vs Linear
LOG: Camera records in logarithmic curve, capturing maximum dynamic range. Looks flat/grey on screen. Must be transformed for viewing. Each camera has its own log curve: ARRI LogC3/LogC4, Sony S-Log3, RED Log3G10, Canon C-Log3, Panasonic V-Log.
LINEAR: What the sensor actually captures. Used internally in compositing. NOT for grading.
DISPLAY: The final transform to screen. Rec.709 gamma 2.4, PQ (Perceptual Quantizer for HDR), HLG.

### LUTs (Look-Up Tables)
TECHNICAL LUT: Converts log footage to display color space. Mathematical transform.
CREATIVE LUT: Applies a "look" — teal and orange, bleach bypass, vintage, noir. Starting point, not final grade.
SHOW LUT: On-set preview LUT so director/DP see approximate final look during shooting. Created in pre-production by colorist or DIT.

## III. THE GRADING WORKFLOW

### DI (Digital Intermediate) Pipeline
1. CONFORM: Import editorial timeline (AAF/XML from Avid/Premiere) and relink to full-resolution camera files
2. PRIMARY GRADE: Overall exposure, white balance, and contrast for each shot. Get the "normal" right.
3. SHOT MATCHING: Ensure consecutive shots in a scene have consistent color, exposure, and contrast
4. SECONDARY GRADE: Targeted corrections — windows/masks on specific areas (sky, skin, background)
5. CREATIVE GRADE: Apply the director-approved look. This is where the artistry lives.
6. POWER WINDOWS: Track moving subjects. Brighten faces, darken backgrounds, create vignettes.
7. HDR TRIM: If delivering HDR, create separate HDR pass (brighter highlights, wider gamut).
8. DELIVERABLES: Render final files in all required formats.

### Primary Corrections
LIFT/GAMMA/GAIN: Shadows/midtones/highlights — the three fundamental controls. Adjust luminance and color independently in each range.
OFFSET: Global shift of all tonal values. Useful for overall exposure correction.
CONTRAST: S-curve in luma channel. Increases difference between lights and darks.
SATURATION: Global color intensity. Subtle changes have big impact.
COLOR TEMPERATURE: Warm (orange shift) or cool (blue shift) overall.

### Secondary Corrections
QUALIFIER: Select specific colors/luminance ranges to adjust. "Make just the sky bluer" or "warm just the skin tones."
POWER WINDOWS: Geometric masks (circle, rectangle, gradient, custom) to isolate areas. Track to follow movement.
CURVES: Per-channel (R, G, B) curves for precise color manipulation. Hue vs Hue, Hue vs Sat, Hue vs Lum for surgical adjustments.
SKIN TONE LINE: On a vectorscope, all healthy skin tones (regardless of ethnicity) fall along a specific angle (~123 degrees, the "I" line). Correcting skin toward this line produces natural, appealing results.

## IV. ICONIC FILM LOOKS

### Teal and Orange (Blockbuster Standard)
Push shadows toward teal/cyan, push highlights toward orange/amber. Creates complementary color contrast. Flattering to skin tones (which are naturally warm). Used in: Transformers, Mad Max, most modern blockbusters.

### Bleach Bypass / Skip Bleach
Desaturated, high contrast, silver-grey highlights. Originally a photochemical process. Digital recreation: reduce saturation 30-50%, increase contrast, add silver/grey to highlights. Used in: Saving Private Ryan, Seven, Minority Report.

### Day for Night
Shooting in daylight but grading to look like night. Technique: heavy blue shift, crush blacks, add vignette, reduce exposure 2-3 stops, desaturate highlights. Tricky to make convincing.

### Noir Look
High contrast, deep blacks, single hard light source, limited color palette (near-monochrome with selective color), heavy shadows, venetian blind patterns.

### Vintage/Period Look
Faded blacks (raised shadows), warm highlights, reduced saturation, green/yellow tint in midtones, halation on highlights, grain overlay. Mimics aged film stock.

## V. HDR GRADING

### HDR Standards
DOLBY VISION: Dynamic metadata, up to 10,000 nits. Gold standard. Per-scene optimization.
HDR10: Static metadata, up to 1,000 nits. Open standard. Most common.
HDR10+: Samsung's dynamic metadata format. Growing adoption.
HLG: Hybrid Log-Gamma. Broadcast standard. Compatible with SDR displays.

### HDR Grading Approach
Grade SDR first (Rec.709), then create HDR pass by: expanding highlight detail, widening color gamut, adjusting specular highlights for HDR "pop." Key: faces should look similar between SDR and HDR. Don't make everything brighter — use the expanded range for SELECTIVE brightness (sun, fire, neon, metal reflections).

## VI. SOFTWARE

### Industry Standard
DAVINCI RESOLVE (Blackmagic): The dominant grading platform. Free version is remarkably powerful. Studio version ($295) adds HDR tools, film grain, neural engine. Used by: 90%+ of professional colorists.
BASELIGHT (FilmLight): Premium grading system. Highest quality, dedicated hardware. Used by: top-tier facilities.

### Supporting Tools
Color management: ACES, DaVinci color management (DaVinci YRGB vs DaVinci Wide Gamut).
Scopes: Waveform (exposure), Vectorscope (color), Histogram (distribution), CIE chromaticity.
Monitoring: FSI DM250 (reference monitor), Sony BVM-HX310 (HDR reference), Flanders Scientific.

## VII. LEGENDARY COLORISTS

STEFAN SONNENFELD (Company 3): Star Wars sequels, Transformers, Man of Steel. Defined modern blockbuster color.
PETER DOYLE: Lord of the Rings trilogy, Harry Potter. Pioneer of digital grading for fantasy.
GREG FISHER: Parasite, Moonlight. Subtle, emotionally precise grading.
JOE WALKER: Collaborated with colorists on Denis Villeneuve films (Blade Runner 2049, Dune).

## VIII. REFERENCES

Books: "Color Correction Handbook" (Alexis Van Hurkman — THE bible), "Color Correction Look Book" (Van Hurkman), "The Art and Technique of Digital Color Correction" (Steve Hullfish).
Education: Mixing Light (mixinglight.com — best online resource), Lowepost, fxphd.
Organizations: CSI (Colorist Society International).""")

# 29. NYX — VFX Compositor
upload("vfx-compositor", "World-Class VFX Compositing & Visual Integration",
"""# NYX — ELITE VFX COMPOSITING KNOWLEDGE BASE

## I. COMPOSITING FUNDAMENTALS

### What is Compositing?
Compositing is the art of combining multiple visual elements into a single seamless image that looks like it was captured by one camera in one take. It is the LAST stage of the VFX pipeline — where everything comes together.

### The Compositing Mantra
"If you can see it, it's bad compositing." The audience should never detect where the real footage ends and the CG/painted elements begin. Seamless integration requires matching: COLOR, CONTRAST, GRAIN, FOCUS, MOTION BLUR, LENS DISTORTION, and ATMOSPHERIC EFFECTS.

## II. CORE COMPOSITING OPERATIONS

### Keying (Green/Blue Screen Extraction)
Algorithms: Keylight (industry standard, After Effects/Nuke), IBK (Image-Based Keyer, Nuke), Primatte.
BEST PRACTICES: Even lighting on screen (no hotspots/shadows), sufficient distance between subject and screen (minimize spill), complementary clothing (no green on green screen), proper exposure (screen should be ~1 stop above mid-grey).
SPILL SUPPRESSION: Remove colored contamination from green/blue screen reflecting onto subject. Use despill nodes, hue shift, or replace spill with complementary color.
EDGE TREATMENT: The matte edge is where composites fail or succeed. Core matte (solid interior), edge matte (semi-transparent fringe). Use: edge blur, edge erode/dilate, mini/channel blur for natural edges.

### Rotoscoping
Frame-by-frame masking of elements without a clean screen. THE most time-consuming VFX task.
TECHNIQUES: Bezier splines following subject contours. Articulated roto (separate shapes for each body part). Motion blur roto (match directional blur at edges).
AI ROTO: Machine learning tools (Runway, Nuke CopyCat, DaVinci Neural Engine) dramatically speed up roto. Still require human cleanup for quality.
MOCHA PRO: Planar tracking for roto. Track a surface, mask follows. Dramatically faster than point-by-point roto.

### Tracking
2D TRACKING: Lock a point in the image across frames. For stabilization, match-move, corner pin.
PLANAR TRACKING: Track a flat surface (Mocha). For screen replacement, sign replacement, surface projections.
3D CAMERA TRACKING: Reconstruct the camera's 3D movement from 2D footage. Essential for placing CG objects in live-action. Tools: PFTrack, SynthEyes, 3DEqualizer, Nuke's CameraTracker.
OBJECT TRACKING: Track a moving object's position and rotation. For attaching CG elements to practical objects.

### Color Matching
The CG element must match the live-action plate's: WHITE BALANCE, CONTRAST RATIO, SATURATION LEVEL, BLACK LEVEL, HIGHLIGHT ROLLOFF, COLOR CAST.
Use: color curves, hue/saturation, grade node matched to plate's colorimetry. Sample plate colors and match CG to them.

## III. INTEGRATION TECHNIQUES

### Atmosphere & Depth
Add ATMOSPHERIC PERSPECTIVE to CG elements: slight desaturation, contrast reduction, and color shift toward ambient color with distance. Add haze, fog, or dust between layers.

### Light Interaction
CG objects must cast shadows, create reflections, and emit/block light on the plate. CONTACT SHADOWS are critical — objects touching surfaces need soft, diffused shadows at the contact point.

### Grain Matching
Plate footage has camera grain/noise. CG elements are perfectly clean. Adding matched grain to CG elements is ESSENTIAL for integration. Analyze plate grain: size, intensity, color, animation. Apply matching grain to CG layer.

### Lens Effects
Match the plate's lens characteristics on CG: DISTORTION (barrel/pincushion), CHROMATIC ABERRATION (color fringing at edges), VIGNETTE (darkened corners), LENS BREATHING (slight zoom during focus pulls), BOKEH shape (hexagonal, circular).

### Motion Blur
CG motion blur must match the plate's shutter angle. 180-degree shutter (standard) creates moderate motion blur. Render CG with matching motion blur or add it in comp.

## IV. NODE-BASED COMPOSITING (NUKE)

### Why Node-Based?
Layer-based (After Effects): Stack of layers, applied top to bottom. Intuitive for simple comps.
Node-based (Nuke, Fusion): Network of connected processing nodes. VASTLY superior for complex comps: non-destructive, re-usable, branchable, readable.

### Essential Nuke Nodes
MERGE: Combine two images (over, plus, multiply, screen, difference)
COLOR CORRECT: Lift/gamma/gain with masks
GRADE: Multiply, offset, black/white point
ROTO: Create animated masks
TRACKER: 2D and 3D tracking
KEYER: Chroma keying
BLUR/DEFOCUS: Selective focus effects
TRANSFORM: Position, scale, rotation
CORNERPIN: Four-point perspective transform
SCANLINE RENDER: 3D rendering within Nuke
DEEP compositing: Volume-based compositing for accurate CG integration

## V. ADVANCED TECHNIQUES

### Deep Compositing
Instead of flat 2D images, deep compositing stores depth information PER PIXEL. CG elements can correctly intersect with other CG elements and plates without manual masking. Industry standard for complex CG-heavy films.

### Multi-Pass Compositing
CG renders are delivered as separate passes: BEAUTY (combined), DIFFUSE, SPECULAR, REFLECTION, REFRACTION, SHADOW, AMBIENT OCCLUSION, EMISSION. Compositors adjust each pass independently for maximum control.

### Stereo Compositing (3D Films)
All compositing done twice — left eye and right eye. Depth must be consistent. Rotoscoping must be matched. Conversion from 2D to stereo 3D is a specialized discipline.

## VI. SOFTWARE

NUKE (Foundry): Industry standard for film VFX. Node-based. NukeX adds camera tracking, particle system.
AFTER EFFECTS (Adobe): Motion graphics standard. Layer-based. Strong plugin ecosystem.
FUSION (Blackmagic): Free with DaVinci Resolve. Node-based. Growing adoption.
FLAME (Autodesk): Premium online finishing + compositing. High-end commercials.
SILHOUETTE (Boris FX): Specialized roto and paint tool.

## VII. REFERENCES

Books: "The Art and Science of Digital Compositing" (Ron Brinkmann — THE bible), "Digital Compositing for Film and Video" (Steve Wright), "Nuke 101" (Ron Ganbar).
Education: fxphd, Gnomon Workshop, FXGUIDE.
Community: Nukepedia (free tools/gizmos), comp-fu, fxguide.com.""")

# 30. QUINN — Continuity/QA
upload("continuity-qa", "World-Class Continuity & Quality Assurance for Film",
"""# QUINN — ELITE CONTINUITY & QA KNOWLEDGE BASE

## I. CONTINUITY FUNDAMENTALS

### What Continuity Covers
VISUAL CONTINUITY: Props, wardrobe, hair, makeup, set dressing remain consistent between shots and scenes.
TEMPORAL CONTINUITY: Time of day, weather, seasons, clocks, calendars, character aging are consistent.
SPATIAL CONTINUITY: Geography, screen direction, character positions, eyelines are consistent.
NARRATIVE CONTINUITY: Plot points, character knowledge, established rules of the world are consistent.
AUDIO CONTINUITY: Ambient sound, music, dialogue tone match across cuts.

### The Script Supervisor's Bible
The script supervisor (continuity supervisor) maintains THE MASTER RECORD of everything shot: which takes were printed/circled, exact dialogue as spoken (not as scripted), timing of each scene, screen direction, prop placement, wardrobe notes, actor blocking, and editor's notes.

## II. VISUAL CONTINUITY CHECKLIST

### Between Takes (Same Scene)
WARDROBE: Collar position, button status, jacket open/closed, sleeves rolled/unrolled, tie loosened/tight, jewelry placement, watch hand, glasses on/off.
HAIR: Parting, strand placement, clips/bands, wet/dry, wind-blown direction.
MAKEUP: Sweat, tears, blood, bruising level, lipstick, beard shadow.
PROPS: Hand props — which hand holds what, drink level in glass, cigarette length, food amount on plate, pen in hand, phone position, bag strap shoulder.
SET: Door open/closed, lights on/off, curtains, papers on desk, computer screen content, background extras.
BODY POSITION: Hand placement, leg crossing, head tilt, lean direction at CUT point.

### Between Scenes (Story Continuity)
WARDROBE PROGRESSION: Does the character's outfit match the timeline? Same day = same clothes.
INJURY TRACKING: Cuts, bruises, bandages must evolve logically — fresh > healing > scarred.
PROP TRACKING: Items acquired, lost, or destroyed in previous scenes.
EMOTIONAL STATE: Character's emotional arc must be consistent with what just happened narratively.
TIME OF DAY: Interior/exterior matching, sun position, shadow direction.

## III. SCREEN DIRECTION

### The 180-Degree Rule
When two characters face each other, the camera stays on one side of the imaginary line between them. Character A looks screen-left, Character B looks screen-right — ALWAYS, until the axis is intentionally crossed.

### Travel Direction
If a character travels left-to-right, maintain that direction in all shots of that journey. Reversal suggests returning. Neutral (directly toward/away from camera) is safe.

### Eyeline Matching
When characters look at each other across cuts, their eyelines must match in height and direction. Looking up in shot A means the other character should be shown from slightly above in shot B.

## IV. QUALITY ASSURANCE FRAMEWORK

### QA Checklist for AI-Generated Content
1. PROMPT FIDELITY: Does the output match the creative brief?
2. TECHNICAL QUALITY: Resolution, artifact-free, proper format?
3. CHARACTER CONSISTENCY: Do characters look the same across all outputs?
4. STYLE CONSISTENCY: Is the visual/audio style consistent across the project?
5. NARRATIVE ALIGNMENT: Does this piece serve the story correctly?
6. FACTUAL ACCURACY: Are there any factual errors in text/dialogue?
7. CULTURAL SENSITIVITY: Any unintended stereotypes or offensive content?
8. LEGAL CLEARANCE: Any recognizable faces, brands, copyrighted material?
9. ACCESSIBILITY: Subtitles accurate, audio described, color-blind friendly?
10. DELIVERABLE SPEC: Correct format, resolution, frame rate, color space?

### Error Severity Levels
CRITICAL: Breaks the story or creates legal/ethical issue. MUST fix before delivery.
MAJOR: Noticeable to general audience. Should fix.
MINOR: Only noticed by professionals. Fix if time/budget allows.
COSMETIC: Nitpick level. Fix in next pass or ignore.

## V. CONTINUITY TOOLS

### Script Supervisor Software
ScriptE: Digital script supervision. Auto-sync with sound, generates facing pages and reports.
MovieSlate: iPad-based digital slate + script supervision.
Scriptation: PDF annotation for script supervisors.

### QA Documentation
CONTINUITY REPORT: Per-scene document with photos, measurements, timestamps.
EDITOR'S DAILY LOG: Which takes to use, performance notes, technical issues.
FACING PAGES: Script on left, shooting notes on right. The editorial bible.
WRAP REPORT: Summary of day's work, variances from schedule, continuity flags.

### Photo Documentation
Polaroids/digital photos of EVERY setup from camera position. Wardrobe photos front/back. Prop photos with measurement reference. Set photos wide and detail.

## VI. COMMON CONTINUITY ERRORS IN FAMOUS FILMS

These happen even in major productions:
- Starbucks cup in Game of Thrones (set dressing)
- Changing bruise locations in Fight Club (makeup)
- Disappearing/reappearing background extras (blocking)
- Modern cars in period films (set dressing)
- Crew reflections in glass/metal surfaces (staging)

The lesson: VIGILANCE at every level. Multiple eyes on every shot.

## VII. REFERENCES

Books: "Script Supervising and Film Continuity" (Pat P. Miller — THE bible), "The Continuity Supervisor" (Avril Rowlands).
Resources: MovieMistakes.com (educational examples of what to avoid).
Organizations: Local 871 (Script Supervisors/Coordinators), BECTU (UK).""")

# 31. CHLOE — Film Critic
upload("film-critic", "World-Class Film Criticism & Analysis",
"""# CHLOE — ELITE FILM CRITICISM KNOWLEDGE BASE

## I. FILM CRITICISM PHILOSOPHY

### The Critic's Purpose
A film critic does three things: (1) EVALUATE — is this film successful at what it's trying to do? (2) CONTEXTUALIZE — where does it fit in cinema history, the genre, the director's body of work? (3) ILLUMINATE — reveal layers the audience might have missed, deepen appreciation.

A good review is NOT a thumbs up/down. It's a CONVERSATION about the film that enriches the reader's understanding whether they agree or not.

## II. CRITICAL FRAMEWORKS

### Formalist Analysis
Focus on FORM: cinematography, editing, sound design, production design, music, visual effects. How do the technical elements create meaning? A long take creates tension. A jump cut creates disorientation. A desaturated palette creates melancholy. This is the "how" of filmmaking.

### Narrative Analysis
Focus on STORY: structure (three-act, five-act, nonlinear), character development, theme, conflict, resolution, subtext. Does the story earn its ending? Are character arcs complete? Is the theme coherent?

### Auteur Analysis
Focus on the DIRECTOR as author. How does this film relate to their body of work? Recurring themes, visual motifs, thematic obsessions, evolution of style. Kubrick's symmetry and control anxiety. Spielberg's broken families and wonder. Nolan's time manipulation and identity.

### Genre Analysis
Evaluate against GENRE CONVENTIONS: Does it fulfill, subvert, or transcend genre expectations? A horror film that isn't scary has failed. A comedy that isn't funny has failed. But a horror film that's also a sharp social commentary (Get Out) has transcended its genre.

### Cultural/Political Analysis
What does the film say about SOCIETY? Representation, power dynamics, class, race, gender. What ideologies does it reinforce or challenge? This is not about whether the film has a "correct" message — it's about being honest about what the film says.

### Emotional/Experiential Analysis
How does the film make you FEEL? The visceral, subjective experience. Sometimes the most honest criticism acknowledges personal response: "I cried." "I was bored." "I was terrified." This is valid criticism when combined with analysis of WHY.

## III. THE REVIEW STRUCTURE

### Professional Review Format
HOOK: Opening line/paragraph that captures the essence of the film or the review's argument. Must make the reader want to continue.
SYNOPSIS: Brief, spoiler-free plot summary. Max 2-3 sentences. Enough context for the reader.
THESIS: Your central argument about the film. What makes it work or fail?
ANALYSIS: 3-5 paragraphs examining specific elements with evidence (scenes, shots, performances).
PERFORMANCES: Evaluate acting — specifics, not generalities. "Driver's Hamlet is a study in controlled grief" not "the acting is good."
TECHNICAL: Cinematography, editing, score, design — how they serve (or undermine) the story.
CONTEXT: How does this relate to the genre, the director's work, current culture?
VERDICT: Final assessment. Not just good/bad but WHO should see this and WHY.

### Rating Systems
STAR SYSTEM: 0-4 or 0-5 stars. Simple, universal. (Ebert's thumbs up/down was even simpler.)
LETTER GRADE: A+ through F. Granular, familiar.
NUMERICAL: 0-10 or 0-100. Most granular, feels false precision.
NO RATING: Some critics refuse to reduce art to numbers. The review IS the evaluation.

## IV. CRITICAL VOCABULARY

### Praise
"Masterfully crafted," "luminous performance," "devastating emotional truth," "virtuosic direction," "transcendent," "economy of storytelling," "visually ravishing," "propulsive," "haunting," "assured filmmaking."

### Criticism
"Overwritten," "emotionally inert," "visually pedestrian," "tonally inconsistent," "derivative," "on-the-nose," "self-indulgent," "bloated," "undercooked," "dramatically inert," "narratively confused."

### Neutral/Analytical
"Deliberately paced" (not slow), "stylized" (not unrealistic), "demanding" (not boring), "economical" (not thin), "restrained" (not flat), "ambitious" (not messy).

## V. ESSENTIAL FILM THEORY

### Key Movements
FRENCH NEW WAVE (1950s-60s): Godard, Truffaut, Varda. Jump cuts, location shooting, self-reflexivity.
ITALIAN NEOREALISM (1940s-50s): Rossellini, De Sica. Non-actors, real locations, social reality.
GERMAN EXPRESSIONISM (1920s): Murnau, Lang, Wiene. Distorted sets, extreme shadows, psychological horror.
SOVIET MONTAGE (1920s): Eisenstein, Vertov. Editing as meaning-creation. The Kuleshov effect.
HOLLYWOOD NEW WAVE (1967-1980): Scorsese, Coppola, Altman, Spielberg. Personal vision within studio system.
DOGME 95 (1995): Von Trier, Vinterberg. No artificial lighting, handheld only, location sound only.

### Essential Theorists
ANDRE BAZIN: Realism, deep focus, the long take. Founded Cahiers du Cinema.
SERGEI EISENSTEIN: Montage theory — meaning created through collision of images.
LAURA MULVEY: "Visual Pleasure and Narrative Cinema" — the male gaze, feminist film theory.
DAVID BORDWELL: Neoformalism — how films create meaning through form and style.

## VI. REFERENCES

Essential Criticism: Roger Ebert (Chicago Sun-Times), Pauline Kael (The New Yorker), Andrew Sarris ("The American Cinema"), A.O. Scott (New York Times), Manohla Dargis (NYT), David Ehrlich (IndieWire).
Books: "The Great Movies" (Ebert), "Sculpting in Time" (Tarkovsky), "Hitchcock/Truffaut," "5001 Nights at the Movies" (Kael), "Film Art: An Introduction" (Bordwell/Thompson).
Publications: Sight & Sound (BFI), Cahiers du Cinema, Film Comment, Cineaste, Little White Lies.""")

# 32. LUNA — Subtitles
upload("subtitle-agent", "World-Class Subtitling & Localization",
"""# LUNA — ELITE SUBTITLING & LOCALIZATION KNOWLEDGE BASE

## I. SUBTITLE STANDARDS

### Timing Rules (Netflix/BBC/Industry Standard)
MINIMUM DURATION: 5/6 of a second (~833ms). No subtitle should appear for less.
MAXIMUM DURATION: 7 seconds. Longer subtitles get split.
GAP BETWEEN SUBTITLES: Minimum 2 frames (~83ms at 24fps). Allows the brain to register the change.
SYNC: Subtitles should appear within 0-500ms of speech onset. Must disappear when speech ends (not before).
SCENE CHANGES: Subtitles should not span a hard cut. End before the cut, restart after.

### Character Limits
ONE LINE: Maximum 42 characters (Netflix standard), 37 characters (BBC).
TWO LINES: Maximum 2 lines per subtitle. Never 3.
READING SPEED: 17 characters per second (adult), 13 characters per second (children's content).

### Line Breaking Rules
Break at natural linguistic boundaries:
GOOD: "I went to the store / and bought some milk" (clause break)
BAD: "I went to the / store and bought some milk" (mid-phrase break)
Keep articles with their nouns: "the" belongs with what follows.
Keep prepositions with their objects.
Never break a proper name across lines.
Bottom line should be longer than top line (pyramid shape preferred).

## II. SUBTITLE TYPES

### Open Captions (Burned-In)
Permanently embedded in the video. Cannot be turned off. Used for: forced narrative subtitles (foreign language within English film), festival screenings, social media.

### Closed Captions (CC)
Separate text track. Can be toggled on/off. Includes: all dialogue, speaker identification, sound effects descriptions [THUNDER RUMBLES], music descriptions [SOFT PIANO PLAYING]. Required for accessibility (ADA compliance).

### SDH (Subtitles for the Deaf and Hard of Hearing)
Like closed captions but in subtitle format. Include: speaker identification when not obvious, sound effects in brackets, music lyrics when narratively relevant.

### Forced Narrative
Subtitles that appear for: foreign language dialogue within an otherwise English film, on-screen text (signs, letters, screens), and alien/fantasy languages. Always on, even with subtitles "off."

## III. TRANSLATION FOR SUBTITLES

### Subtitle Translation Is NOT Literary Translation
Subtitles must be CONDENSED. Spoken language is redundant — subtitles remove redundancy while preserving meaning. A 12-word spoken sentence might become 8 words in subtitles. The constraint: reading speed + screen space.

### Translation Principles
ACCURACY: Preserve meaning, tone, and intent.
CONCISENESS: Eliminate filler, reduce to essential information.
NATURALNESS: Read like natural written language in the target language.
REGISTER: Match the formality level (slang stays slang, formal stays formal).
CULTURAL ADAPTATION: Localize jokes, idioms, references. "Hit a home run" might become "scored a goal" for non-US audiences.

### Challenging Translation Scenarios
PUNS/WORDPLAY: Often impossible to translate directly. Find an equivalent pun in target language, or translate the meaning and sacrifice the wordplay.
CULTURAL REFERENCES: Localize when possible. Some references need footnote subtitles (rare).
SUNG LYRICS: Translate for meaning, not rhyme. Indicate [SINGING] in SDH.
OVERLAPPING DIALOGUE: Prioritize the narratively important speaker. Indicate second speaker with dashes.

## IV. TECHNICAL SPECIFICATIONS

### File Formats
SRT (SubRip): Simple text + timing. Most universal. Used by YouTube, most platforms.
VTT (WebVTT): Web standard. Supports styling. HTML5 video.
ASS/SSA: Advanced styling, positioning, effects. Used by anime community.
TTML/IMSC: XML-based. Netflix, Amazon, broadcast standard. Supports regions, timing, styling.
STL (EBU): European broadcast standard.
SCC: Closed caption format for US broadcast.

### Positioning
Default: Bottom center of screen. White text on semi-transparent black background.
FORCED REPOSITIONING: When subtitles cover important on-screen text or action. Move to top.
SPEAKER POSITIONING: In some formats, position subtitles near the speaker (used in some European markets).

## V. AI-ASSISTED SUBTITLING

### Speech-to-Text (Transcription)
WHISPER (OpenAI): Best open-source speech recognition. Multilingual. Word-level timestamps.
GOOGLE CLOUD SPEECH: Commercial, high accuracy, streaming capable.
AMAZON TRANSCRIBE: AWS ecosystem, automatic punctuation.
Rev.com/Otter.ai: Commercial services, human review option.

### Machine Translation for Subtitles
Use MT as FIRST DRAFT only. Always human review. MT struggles with: context-dependent meaning, character voice consistency, cultural adaptation, subtitle-specific constraints (length, timing).

### AI Subtitle Workflow
1. Auto-transcribe with Whisper or equivalent
2. Time-code alignment (auto or manual adjustment)
3. Line breaking and reading speed compliance (automated)
4. Human review: accuracy, timing, line breaks, style
5. Translation (if needed): MT first draft, human post-edit
6. QC: spotting check against picture, technical compliance
7. Delivery: convert to required format(s)

## VI. REFERENCES

Standards: Netflix Timed Text Style Guide (public), BBC Subtitle Guidelines, W3C TTML/IMSC spec.
Books: "Audiovisual Translation: Subtitling" (Diaz Cintas & Remael — THE textbook), "Subtitling" (Georgakopoulou & Bywood).
Software: Subtitle Edit (free), Aegisub (free, advanced), EZTitles (professional), FAB Subtitler (broadcast).
Organizations: ATAA (Audiovisual Translators Association), MESA (Media & Entertainment Services Alliance).""")

# 33. HARPER — Marketing
upload("marketing", "World-Class Film Marketing & Campaign Strategy",
"""# HARPER — ELITE FILM MARKETING KNOWLEDGE BASE

## I. FILM MARKETING STRATEGY

### The Marketing Funnel for Film
AWARENESS: "This movie exists" — teaser trailer, first-look images, social media announcement
INTEREST: "This looks good" — full trailer, behind-the-scenes, cast interviews, press junket
DESIRE: "I want to see this" — reviews, festival buzz, fan events, exclusive clips
ACTION: "I'm buying a ticket/subscribing" — release date push, pre-sale, platform availability

### Campaign Timeline (Theatrical Release)
18-12 MONTHS: Announce film, first-look image. Trade press coverage.
9-6 MONTHS: Teaser trailer (60-90 seconds). Social media campaign launches.
6-3 MONTHS: Full trailer (2-2.5 minutes). Poster campaign. Press junket.
3-1 MONTHS: TV spots (15-30 seconds). Influencer screenings. Festival premiere.
2-1 WEEKS: Embargo lifts (reviews published). Final push. Premiere event.
OPENING WEEKEND: Social media blitz, audience reactions, real-time marketing.
POST-RELEASE: Word-of-mouth management, "still in theaters" push, awards campaign (if applicable).

## II. KEY MARKETING ASSETS

### Trailer Strategy
TEASER (60-90s): Mood, world, maybe one character moment. NO plot. Create intrigue.
THEATRICAL TRAILER (2:00-2:30): Three-act structure in miniature: setup > escalation > climax. Show the promise of the premise. End with a button (joke, shocking moment, title card).
TV SPOT (15-30s): Single selling point. One emotional beat. Clear call to action.
DIGITAL/SOCIAL (6-60s): Platform-specific. Vertical for TikTok/Reels, square for feeds, landscape for YouTube.

### Poster Campaign
ONE-SHEET: The single poster that defines the film. Must communicate: genre, tone, star power, title.
CHARACTER POSTERS: Individual posters for ensemble casts. Comic-Con and fan engagement.
TEASER POSTER: Minimal, intriguing. Often before trailer drops. Creates mystery.
INTERNATIONAL VARIATIONS: Different markets may need different visual emphasis (action > drama in some territories, different star power by region).

### Key Art Principles
COMPOSITION: Central subject, clear focal point, readable at thumbnail size (critical for streaming).
TYPOGRAPHY: Title treatment = brand identity. Must be legible at small sizes.
COLOR: Genre coding — blue/teal (sci-fi), red/orange (action), soft pastels (romance), dark/desaturated (horror).
STAR FACES: Above-title talent faces sell tickets. Face size correlates with star power.

## III. DIGITAL & SOCIAL MARKETING

### Platform Strategy
YOUTUBE: Trailers, behind-the-scenes, cast interviews. SEO-optimized titles.
INSTAGRAM: Stills, poster reveals, behind-the-scenes Stories, Reels for short-form.
TIKTOK: Trend-riding, meme-format, creator partnerships, sound trends, challenges.
X/TWITTER: Real-time conversation, premiere live-tweeting, fan engagement.
FACEBOOK: Event promotion, older demographic targeting, community groups.
REDDIT: AMA with talent, targeted subreddit engagement (careful — Reddit detects marketing).

### Influencer & Creator Marketing
Partner with relevant creators (film critics, entertainment TikTokers, genre-specific channels). Provide exclusive access: early screenings, on-set visits, talent interviews. Let creators make authentic content — do NOT script them.

### SEO & SEM
Optimize for search: official website, IMDb page, social profiles all consistent.
Paid search: Protect the title (bid on own title + competitors).
Display/programmatic: Retarget trailer viewers with release date messaging.

## IV. AUDIENCE RESEARCH

### Test Screenings
RECRUITED SCREENING: Invite target demographic. Post-screening questionnaire: "Excellent," "Very Good," "Good," "Fair," "Poor." "Definitely recommend" vs "Probably recommend." Top-two-box score is the metric.
FOCUS GROUPS: 10-15 audience members discuss the film in depth. Moderator-led. Qualitative insights.

### Tracking Surveys
2-3 weeks before release: AWARENESS (have you heard of this film?), INTEREST (are you interested in seeing it?), FIRST CHOICE (is this your #1 film to see this weekend?), DEFINITE INTEREST (will you definitely see it?). Track weekly to measure campaign effectiveness.

## V. P&A (PRINTS & ADVERTISING) BUDGET

### Budget Allocation (Typical Theatrical)
MEDIA BUY: 60-70% (TV, digital, outdoor, print, radio)
CREATIVE PRODUCTION: 10-15% (trailers, posters, social content, website)
PR & EVENTS: 5-10% (premieres, press junket, festival, talent travel)
RESEARCH: 5% (tracking, testing, analytics)
CONTINGENCY: 5-10%

### Budget by Film Tier
MICRO-INDIE (<$1M budget): $50K-$500K P&A. Grassroots, social, festival.
INDIE ($1M-$15M): $2M-$10M P&A. Limited theatrical + platform release.
MID-BUDGET ($15M-$80M): $20M-$50M P&A. Targeted theatrical + streaming.
TENTPOLE ($80M+): $100M-$200M+ P&A. Global theatrical blitz.

## VI. AWARDS CAMPAIGN

### Oscar Campaign Strategy
FESTIVAL LAUNCH: Venice, Telluride, or Toronto premiere (September).
GUILD SCREENINGS: SAG, DGA, PGA, ASC, ACE — guild members vote for nominations.
FOR YOUR CONSIDERATION (FYC): Trade ads in Variety, THR. Screener distribution.
Q&A SCREENINGS: Director and talent present film and take questions.
GRASSROOTS: House parties, intimate screenings, personal outreach to Academy members.
TIMELINE: Sep-Nov (festival buzz) > Dec (critics' awards, Golden Globes noms) > Jan (Globes, guild awards, Oscar noms) > Feb-Mar (Oscar ceremony).

## VII. REFERENCES

Books: "The Big Picture" (Gabler), "Sleepless in Hollywood" (Obst), "Marketing to Moviegoers" (Marich).
Publications: Variety, Deadline, THR (marketing coverage), The Wrap.
Tools: Tableau (data viz), Hootsuite/Sprout Social (social management), Google Analytics, Comscore.""")

# 34. RIO — Distribution
upload("distributor", "World-Class Film Distribution & Revenue Strategy",
"""# RIO — ELITE FILM DISTRIBUTION KNOWLEDGE BASE

## I. DISTRIBUTION LANDSCAPE

### Distribution Models
THEATRICAL: Wide release (3,000+ screens), limited release (500-2,000), platform release (4-50 screens expanding based on performance), day-and-date (theatrical + digital simultaneously).
STREAMING/SVOD: Netflix, Amazon Prime, Apple TV+, Disney+, Max, Hulu, Paramount+. License fee or original production deal.
TVOD/EST (Transactional): Rental ($5.99-$19.99) or purchase ($14.99-$24.99) on Apple TV, Google Play, Amazon, Vudu.
FREE/AVOD: Tubi, Pluto TV, Freevee, YouTube. Ad-supported. Lower revenue per view.
BROADCAST/CABLE: Network TV, cable channels. License fees for windows.

### The Distribution Deal
MINIMUM GUARANTEE (MG): Upfront payment from distributor to producer. Based on estimated revenue.
DISTRIBUTION FEE: Percentage of gross revenue taken by distributor (typically 25-35% theatrical, 15-25% home entertainment, 30-40% international).
P&A COMMITMENT: Marketing budget the distributor commits to spend.
EXPENSES CAP: Maximum distribution expenses before they're borne by the distributor.
TERM: How long the distributor controls the rights (typically 10-25 years, sometimes "in perpetuity").
TERRITORY: Which geographic markets are covered (domestic, international, worldwide).

## II. REVENUE WINDOWS

### Traditional Windowing (2020s Evolution)
1. THEATRICAL: 45-90 day exclusive window (shortened from 120 days pre-COVID)
2. PREMIUM VOD (PVOD): $19.99 rental, 17-45 days post-theatrical
3. EST (Electronic Sell-Through): Digital purchase, ~90 days post-theatrical
4. SVOD (Subscription Streaming): 6-9 months post-theatrical
5. FREE VOD/AVOD: 12-18 months post-theatrical
6. PAY TV: 18-24 months
7. FREE TV/BROADCAST: 24-36 months

### Revenue Split by Window (Typical Studio Film)
Theatrical: 40-50% of total revenue
Home Entertainment (digital + physical): 25-30%
TV licensing: 10-15%
Ancillary (merchandise, theme parks, music): 5-15%

## III. INTERNATIONAL DISTRIBUTION

### Territory Sales
Films are sold territory-by-territory at film markets: CANNES (May — Marche du Film), AFM (November — American Film Market), EFM (February — European Film Market/Berlin), TIFF (September), FILMART (March — Hong Kong/Asia focus).

### Key International Territories (Revenue Ranking)
1. China (unpredictable — censorship, quota system, revenue repatriation issues)
2. United Kingdom / Ireland
3. Japan (unique market — anime dominant, Hollywood titles need strong marketing)
4. Germany
5. France (strong local film industry, cultural preferences)
6. South Korea (rapidly growing, sophisticated audience)
7. Australia
8. Brazil / Mexico (growing Latin American markets)
9. India (massive market, very price-sensitive, Bollywood dominant)
10. Middle East (growing, cultural content considerations)

### International Deal Structures
ALL-RIGHTS DEAL: One distributor handles all media in a territory.
OUTPUT DEAL: Distributor takes all films from a studio/label for a territory over a multi-year period.
REVENUE SHARE: Split of gross receipts rather than flat MG.

## IV. DIGITAL DISTRIBUTION

### Platform Economics
NETFLIX: License fee ($5M-$250M+ depending on profile). No backend for producers. They own viewership data.
AMAZON PRIME: License or first-look/overall deals. Some backend tied to viewership.
APPLE TV+: Premium license fees, quality-focused catalog. Strong marketing support.
YOUTUBE: Revenue share on ad views. Self-distribution possible. Low barrier.
VIMEO OTT: White-label streaming platform. Filmmakers keep 90% of revenue.

### Self-Distribution
DIRECT TO CONSUMER (D2C): Your own website + payment processor. Keep ~90% after payment fees. Need to drive your own traffic. Works for: niche audiences, established brands, educational content.
AGGREGATORS: Platforms like Filmhub, Distribber (defunct), Quiver that place your film on multiple platforms. Take 15-20% commission.

## V. THEATRICAL DISTRIBUTION SPECIFICS

### Booking
FOUR-WALL: Rent the theater yourself ($2K-$10K/week). You keep box office. High risk.
STANDARD BOOKING: Theater takes 40-50% of box office (sliding scale — studio gets more in early weeks, theater gets more later).
BLIND BIDDING: Banned in most states. Theaters bid on films without seeing them.

### DCP (Digital Cinema Package)
Standard delivery format for theatrical exhibition. ENCRYPTED (KDM keys sent to each theater).
Specs: 2K (2048x1080) or 4K (4096x2160), JPEG2000 codec, 24fps or 48fps HFR, Dolby Atmos/7.1/5.1 audio.

### Box Office Analytics
OPENING WEEKEND: The crucial metric. Determines screen count for week 2.
LEGS: Total gross / Opening weekend. Good legs = 3x+. Great legs = 5x+.
FRIDAY-TO-SATURDAY: Measures walkup audience vs pre-sold. Good sign if Saturday > Friday.
WEEKDAY HOLDS: Monday-Thursday performance indicates staying power.

## VI. DELIVERY REQUIREMENTS

### Standard Deliverables Package
Picture: DCP (theatrical), ProRes/DNxHR master (digital), HDR master (streaming)
Audio: 7.1/5.1/Stereo stems, M&E (Music & Effects for international dubbing)
Subtitles: Multiple languages in TTML/SRT/VTT
Metadata: Title, synopsis, cast/crew, ratings, poster art, stills, trailer
Legal: Chain of title, E&O insurance, music cue sheet, copyright registration
Marketing: Poster art (various sizes), stills (min 20), EPK (Electronic Press Kit)

## VII. REFERENCES

Books: "The Movie Business Book" (Jason Squire — THE distribution bible), "Selling Your Film" (Broderick), "Think Outside the Box Office" (Jon Reiss).
Markets: Cannes Marche du Film, AFM, EFM, TIFF Industry, Ventana Sur (Latin America).
Data: Box Office Mojo, The Numbers, Comscore, Luminate.
Organizations: IFTA (Independent Film & Television Alliance), NATO (National Association of Theatre Owners), AMPAS (Academy — for awards-track distribution).""")

print("\n=== Batch 4 complete (agents 28-34) — ALL AGENTS DONE ===")
