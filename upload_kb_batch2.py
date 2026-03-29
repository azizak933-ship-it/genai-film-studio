#!/usr/bin/env python3
"""Upload KB batch 2: Agents 11-20."""
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

# 11. MILA — Concept Artist
upload("concept-artist", "World-Class Concept Art & Visual Development",
"""# MILA — ELITE CONCEPT ART KNOWLEDGE BASE

## I. CONCEPT ART FUNDAMENTALS

### What Concept Art IS
Concept art is VISUAL PROBLEM-SOLVING. It's not illustration — it's ideation. The concept artist explores possibilities, iterates rapidly, and communicates ideas that don't yet exist. Speed and clarity over polish.

### The Concept Art Pipeline
1. BRIEF ANALYSIS: Understand story context, mood, technical constraints, target audience
2. RESEARCH/REFERENCE: Gather real-world references — architecture, nature, machines, cultures, textures
3. THUMBNAIL EXPLORATION: 20-100 tiny sketches (1-2 inch). Pure silhouette and composition. Speed over detail.
4. SELECTED DEVELOPMENT: 5-10 thumbnails developed to rough sketch level
5. DIRECTOR REVIEW: Present options, discuss direction, receive feedback
6. REFINED CONCEPT: Full resolution painting of approved direction
7. CALLOUT SHEET: Annotations explaining materials, colors, scale, functionality
8. KEYFRAME: Final presentation-quality painting showing the concept in context

### Keyframe Illustration
The most important deliverable. A keyframe is a single image that captures the FEELING of a scene — lighting, mood, scale, atmosphere, character placement. It's the frame the director points to and says "make the movie look like THIS."

## II. ENVIRONMENT DESIGN

### World-Building Hierarchy
MACRO: Planet/world type, climate, geography, civilization level
REGIONAL: Biome, culture, architecture style, economic status
LOCAL: Specific location, time of day, weather, activity
MICRO: Surface detail, wear patterns, personal touches, storytelling objects

### Depth & Atmosphere
Use ATMOSPHERIC PERSPECTIVE: Objects lose contrast, shift toward sky color, and lose detail with distance. Three value planes: foreground (dark, detailed), midground (medium, some detail), background (light, minimal detail).

### Scale Indicators
Include human figures, vehicles, trees, or known objects to communicate scale. A 50-foot robot means nothing without a person next to it.

## III. CREATURE DESIGN (Terryl Whitlatch Method)

### Anatomical Plausibility
Even fantastical creatures need believable anatomy. Start with REAL animal anatomy as foundation:
- Skeletal structure determines silhouette and movement
- Muscle groups determine surface form and locomotion
- Skin/hide/scales/fur determined by environment
Hybrid creatures: combine no more than 2-3 real animal bases. More becomes incoherent.

### Creature Design Checklist
Locomotion (how does it move?), Diet (predator/herbivore/omnivore — determines teeth, eyes, build), Environment (arctic/desert/aquatic — determines surface), Intelligence (tool use, social behavior), Threat display (how does it intimidate?), Vulnerability (what weakness makes it interesting?).

## IV. HARD SURFACE & PROP DESIGN

### Functional Believability
Even sci-fi technology should suggest function. Where does fuel go? Where does exhaust vent? How does the pilot see? Where are structural supports? Form follows function, then add style.

### Design Language
A world's technology should share a DESIGN LANGUAGE — consistent shapes, materials, proportions across all objects. Star Wars: gritty, angular, industrial. Star Trek: sleek, curved, clean. Alien: bio-mechanical, organic-industrial hybrid.

## V. DIGITAL PAINTING TECHNIQUES

### The 3-Step Block-In
1. VALUE FIRST: Grey-scale composition. Big shapes. Squint to check readability. This is 80% of the painting.
2. COLOR OVERLAY: Add hue on top of values. Use color modes (Soft Light, Overlay, Color) to maintain value structure.
3. DETAIL PASS: Render only focal areas. Leave periphery loose. Guide the eye.

### Photo-Bashing
Using photographic elements composited and painted over to achieve photorealistic results quickly. Workflow: (1) 3D block-out or rough sketch as base, (2) composite photo elements for materials/textures, (3) paint over for cohesion, (4) add atmospheric effects, (5) color grade.

### 3D to 2D Pipeline
Block scene in Blender/SketchUp for accurate perspective and lighting. Render multiple passes (ambient occlusion, normals, depth). Paint over in Photoshop. This hybrid approach is now INDUSTRY STANDARD for environment concept art.

## VI. AI-ASSISTED CONCEPT ART

### AI as Ideation Tool
Use Midjourney/DALL-E/Stable Diffusion/Flux for rapid ideation — generate 50+ variations in minutes, then sketch over favorites. AI excels at unexpected combinations and mood exploration.

### ControlNet for Precision
Depth maps: maintain spatial structure while generating new surface details.
Canny edges: preserve linework while generating variations.
OpenPose: consistent character poses across style variations.
Inpainting: selectively regenerate portions while keeping what works.

### The Human Advantage
AI can't solve specific design problems, maintain world-internal consistency, or make intentional storytelling choices. The concept artist's role shifts from pure rendering to CREATIVE DIRECTION — choosing, combining, refining, and ensuring narrative coherence.

## VII. SOFTWARE

Photoshop (industry standard), Procreate (iPad, rapid sketching), Blender (3D blocking), KeyShot (quick rendering), ZBrush (sculpting), Clip Studio Paint, Corel Painter.

## VIII. LEGENDARY CONCEPT ARTISTS

RALPH McQUARRIE: Star Wars. Defined an entire universe's visual language. Gold standard.
SYD MEAD: Blade Runner, Tron, Aliens. "Visual futurist." Industrial design meets cinema.
JOHN HOWE & ALAN LEE: Lord of the Rings. Tolkien's world made real. Decades of Middle-earth painting.
FENG ZHU: FZD School of Design founder. Master educator. Entertainment design methodology.
CRAIG MULLINS (Sparth): Pioneer of digital painting. Painterly approach to concept art.
JAMA JURABAEV: Marvel, Industrial Light & Magic. Modern photo-bash master.
DYLAN COLE (Avatar): Pandora's environments. Digital matte painting evolved into concept art.

## IX. REFERENCES

Books: "Imaginative Realism" (James Gurney), "Color and Light" (Gurney), "How to Draw" (Scott Robertson), "How to Render" (Robertson), "The Skillful Huntsman," "Nuthin' But Mech" series.
Schools: FZD School of Design, Gnomon Workshop, CGMA, Schoolism, Brainstorm School, Art Center College of Design.
Portfolios: ArtStation (primary), DeviantArt, Behance.""")

# 12. MILO — Storyboard Artist
upload("storyboard-artist", "World-Class Storyboarding & Visual Sequencing",
"""# MILO — ELITE STORYBOARD ARTIST KNOWLEDGE BASE

## I. STORYBOARD FUNDAMENTALS

### Purpose
Storyboards are the BLUEPRINT for how a film will be shot. They translate the script into a visual sequence of shots, establishing: camera angle, composition, character staging, camera movement, shot transitions, and emotional pacing. They save enormous time and money on set by pre-solving visual problems.

### Types of Storyboards
PRODUCTION STORYBOARDS: Detailed frames for every shot in the film. Standard for features.
PITCH BOARDS: High-polish presentation boards to sell a concept. Common in advertising and animation.
THUMBNAIL BOARDS: Tiny rapid sketches for the director to explore coverage ideas.
ANIMATICS: Storyboard frames edited together with timing and temp audio. Pre-visualization in 2D.

## II. VISUAL STORYTELLING LANGUAGE

### Shot Composition
RULE OF THIRDS: Place subjects on intersection points. Creates dynamic, balanced compositions.
LEADING LINES: Use architecture, roads, shadows to guide the eye to the subject.
FRAMING: Use doorways, windows, arches to create frames within frames.
DEPTH: Foreground, midground, background layers create dimensional compositions.
HEADROOM & LOOK ROOM: Give space above heads (headroom) and in front of where characters look (look room/nose room).

### Camera Angles in Boards
BIRD'S EYE / OVERHEAD: God's perspective, vulnerability, geography
EYE LEVEL: Neutral, relatable
LOW ANGLE (WORM'S EYE): Power, heroism, intimidation
HIGH ANGLE: Submission, weakness, surveillance
DUTCH/CANTED: Unease, chaos, psychological imbalance
OVER-THE-SHOULDER (OTS): Connection, conversation, POV proximity
POV: Subjective, immersive, identification

### Indicating Camera Movement
PAN: Curved arrow left/right along frame bottom
TILT: Vertical arrow along frame side
DOLLY/TRACK: Arrow with "wheels" or parallel lines showing direction
ZOOM: Converging/diverging lines from frame center
CRANE: Diagonal arrow with arc showing up/down movement
PUSH IN / PULL OUT: Arrow toward or away from subject
HANDHELD: Wavy line indicating shakiness

## III. STORYBOARD TECHNIQUE

### Drawing for Storyboards
Speed > polish. Boards must communicate CLEARLY, not be beautiful. Use construction lines for perspective, simple figures for staging, value (light/dark) for mood. A skilled storyboard artist produces 30-75 frames per day.

### The Three Essential Skills
1. PERSPECTIVE: One, two, and three-point perspective fluency. Ability to draw any space from any angle.
2. FIGURE DRAWING: Pose, gesture, and proportion. Characters must ACT in the frames — body language tells the story.
3. CINEMATOGRAPHIC THINKING: Understanding which shot serves the story moment. Not just drawing what you see, but drawing what the CAMERA sees.

### Frame Annotations
Below each frame: SCENE/SHOT NUMBER, DIALOGUE excerpt, ACTION description, CAMERA MOVEMENT notes, SFX notes, DURATION estimate.

## IV. SHOT DESIGN PRINCIPLES

### Coverage Planning
MASTER SHOT: Wide establishing shot of entire scene geography. The safety net.
MEDIUM SHOTS: Standard conversation coverage.
CLOSE-UPS: For emotional beats, reactions, important details.
INSERTS: Extreme close-ups of objects, hands, screens, documents.
The SHOT/REVERSE-SHOT pattern for dialogue. Cut on action for movement scenes.

### Continuity in Boards
SCREEN DIRECTION: If a character moves left-to-right in one shot, maintain that direction in subsequent shots (unless crossing the axis intentionally).
EYELINE MATCHING: Characters looking at each other must have consistent eyelines across cuts.
180-DEGREE RULE: Establish and maintain the axis of action. Show line-crossing explicitly if intentional.

## V. ACTION SEQUENCE BOARDING

### The Geography Principle
The audience must ALWAYS understand where characters are in relation to each other and the environment. Establish geography with wide shots before going into close action.

### Cause and Effect
Every action shot must clearly show: WHO is doing WHAT to WHOM. Wide for geography, medium for action, close for impact/reaction. The Russo Brothers (MCU) methodology: every punch has a setup, execution, and reaction.

### Timing in Boards
For action sequences, boards need more frames per second of screen time. An explosion that lasts 3 seconds might need 8-12 boards to communicate the full choreography: anticipation, event, shockwave, reaction.

## VI. ANIMATION STORYBOARDING

### Key Differences from Live-Action
Animation boards are more detailed because there is NO LOCATION to reference — the board IS the location. Every background is designed. Character acting is specified in boards since there's no actor improvising. Boards include timing notes and may be used directly as animatic bases.

### Story Reel / Leica Reel
In animation, storyboards are edited into a full-length story reel with temporary dialogue and music. The entire film is "watchable" in board form before any animation begins. This is where story problems are solved.

## VII. DIGITAL STORYBOARDING

### Software
Storyboard Pro (Toon Boom): Industry standard for animation and live-action. Timeline integration, camera movement simulation.
Photoshop: Traditional approach, frame-by-frame.
Procreate: iPad-based, fast sketching.
FrameForge: 3D pre-visualization, camera lens simulation.
ShotPro: iPad app with 3D blocking and virtual camera.
Boords: Web-based collaborative storyboarding.

## VIII. LEGENDARY STORYBOARD ARTISTS

HAROLD MICHELSON: Storyboarded The Graduate, The Birds, Spaceballs. Pioneer of modern production storyboarding.
SAUL BASS: Title designer who storyboarded Psycho's shower scene and Spartacus battle for Kubrick.
JOE JOHNSTON: Storyboarded Star Wars original trilogy before becoming director (Jurassic Park III, Captain America).
GABRIEL HARDMAN: Interstellar, The Dark Knight Rises. Published comic artist bringing graphic novel quality to boards.
PREVIZ COMPANIES: The Third Floor (leading pre-vis studio), Halon Entertainment, Proof Inc.

## IX. REFERENCES

Books: "Prepare to Board!" (Nancy Beiman), "Professional Storyboarding" (Sergio Paez & Anson Jew), "Directing the Story" (Francis Glebas), "Setting Up Your Shots" (Jeremy Vineyard), "Framed Ink" (Marcos Mateu-Mestre).
Film study: Watch with sound off to see how visual storytelling works without dialogue.""")

# 13. KAI — Cinematographer
upload("cinematographer", "World-Class Cinematography Execution & Shot Craft",
"""# KAI — ELITE CINEMATOGRAPHY EXECUTION KNOWLEDGE BASE

## I. ON-SET CINEMATOGRAPHY WORKFLOW

### Pre-Production Prep
1. SCRIPT BREAKDOWN: Note every lighting change, time of day, mood shift, practical light source
2. LOCATION TECH SCOUT: Walk every location with director, gaffer, key grip. Note sun path, power access, rigging points, ceiling height, windows
3. SHOT LIST: Collaborate with director. Every shot numbered with: lens, movement, lighting notes
4. LOOK BOOK: Visual reference document. Film stills, photographs, paintings that define the look
5. CAMERA/LENS TESTS: Test camera, lenses, filtration, film stocks on actors. Project in theater.
6. LUT DEVELOPMENT: Work with DIT/colorist to create show LUT for on-set monitoring

### The Shooting Day
CALL TIME: Arrive before crew. Walk set with gaffer, discuss lighting plan.
PRE-LIGHT: Gaffer and electricians set lights per plan. Key grip sets flags, frames, diffusion.
REHEARSAL: Block scene with actors and director. Cinematographer calls out shots.
TWEAKING: Adjust lights for actor positions. Set final iris/ND.
SHOOTING: Operate or supervise operator. Monitor exposure via waveform. Communicate with 1st AC (focus puller).
CHECKING: Review selects on calibrated monitor with DIT. Verify color, exposure, sharpness.

## II. EXPOSURE MASTERY

### The Exposure Triangle
ISO: Sensor sensitivity. Higher ISO = more noise/grain. Dual native ISO cameras (Sony VENICE: 500/2500) provide two clean sensitivity points.
APERTURE (T-Stop): Controls depth of field AND exposure. T2.0 = shallow DOF, lots of light. T5.6 = deeper DOF, less light. T-stops (transmission) are more accurate than F-stops (focal ratio) for cinema lenses.
SHUTTER ANGLE: 180 degrees = standard motion blur (1/48 at 24fps). 90 degrees = sharper, more staccato (Saving Private Ryan). 360 degrees = dreamy, more blur. 45 degrees = hyper-sharp (Gladiator battle).

### Exposure Tools
WAVEFORM MONITOR: Shows luminance values. Keep skin tones at 40-60 IRE (Rec.709). Avoid clipping highlights (100 IRE) or crushing blacks (0 IRE).
FALSE COLOR: Color-coded exposure overlay. Red = overexposed, yellow = hot, green = proper skin tone, blue = underexposed.
LIGHT METER: Incident (measures light falling ON subject) vs reflected (measures light bouncing OFF subject). Incident is more reliable for faces.
SPOT METER: Measures reflectance of specific areas. Key for high-contrast situations.

### Exposing for Post
ETTR (Expose To The Right): In LOG/RAW, overexpose slightly to maximize signal-to-noise ratio in shadows. But NEVER clip highlights — clipped data cannot be recovered.

## III. ADVANCED LIGHTING EXECUTION

### Lighting Ratios
KEY-TO-FILL RATIO: 2:1 = low contrast, flattering. 4:1 = dramatic, dimensional. 8:1 = noir, extreme. Measured with incident meter at subject position.

### Motivating Light Sources
Every light in frame should appear to come from a logical source: window, lamp, TV screen, fire, moonlight. Even when you add lights the audience can't see, they should FEEL motivated by a visible source.

### Day Interior Lighting
1. Establish window source (HMI or LED daylight through diffusion)
2. Add negative fill on opposite side for contrast
3. Soft ambient fill if needed (bounced light off ceiling or walls)
4. Practical lamps for depth and motivated sources
5. Edge/backlight from secondary window or practical

### Night Interior Lighting
1. Establish practical motivation (lamps, TV, moonlight through windows)
2. Build from darkness — start with all lights off, add one at a time
3. Use tungsten-balanced sources for warm practicals
4. Blue-gelled moonlight through windows (1/4 CTB or daylight LED at low intensity)
5. Embrace shadows — night scenes should feel dark

### Day Exterior Lighting
Challenge: the sun is unmotivable and changes constantly.
OVERCAST: Nature's softbox. Even, beautiful light. Limited hours.
DIRECT SUN: Hard shadows. Use: large silk/diffusion overhead, reflectors for fill, negative fill for contrast.
MAGIC HOUR: 20-30 minutes of golden/warm light at sunrise/sunset. Shoot fast, have multiple cameras.
BACKLIT: Sun behind subject creates rim light. Fill from front with bounce or HMI.

## IV. LENS FILTRATION

ND (Neutral Density): Reduces exposure without changing aperture. IRND for digital (cuts IR pollution). Variable ND for run-and-gun.
DIFFUSION: Pro-Mist (halation on highlights), Glimmerglass (subtle softening), Classic Soft (strong diffusion). Reduces digital "sharpness" for filmic quality.
POLARIZER: Cuts reflections on glass/water, deepens sky. Loses 1.5 stops.
DIOPTER: Close-focus attachment. Split diopter creates two focal planes simultaneously (De Palma's signature).

## V. ESSENTIAL REFERENCES

ASC (American Society of Cinematographers): ASC Manual, American Cinematographer magazine.
Books: "Cinematography" (Blain Brown), "Painting with Light" (Alton), "Set Lighting Technician's Handbook" (Box).
Online: Cooke Optics TV (lens education), Wandering DP (lighting tutorials), Cinematography Database (interviews).""")

# 14. BLAKE — Shot Designer
upload("shot-designer", "World-Class Shot Design & Visual Planning",
"""# BLAKE — ELITE SHOT DESIGN KNOWLEDGE BASE

## I. SHOT DESIGN PHILOSOPHY

### Every Shot is a Sentence
A shot is the smallest unit of visual storytelling. It must convey: WHO (subject), WHERE (environment), WHAT (action), and HOW (emotionally — through angle, movement, lens). Unnecessary shots dilute impact.

### The Shot as Emotional Vehicle
SHOT SIZE controls intimacy: Wide = context, Medium = engagement, Close = intimacy/intensity.
ANGLE controls power: Low = powerful, High = diminished, Eye-level = neutral.
LENS controls psychology: Wide = isolation/distortion, Normal = naturalism, Long = compression/surveillance.
MOVEMENT controls energy: Static = contemplation, Slow dolly = deepening, Fast track = urgency, Handheld = chaos.

## II. SHOT TYPES ENCYCLOPEDIA

### Static Shots
EXTREME WIDE (EWS): Landscape, tiny figure in vast space. Establishes world, isolation.
WIDE/FULL (WS): Full body, environment context. Geography, blocking.
MEDIUM WIDE (MWS): Knees up. Action + environment balance.
MEDIUM (MS): Waist up. Standard conversational framing.
MEDIUM CLOSE-UP (MCU): Chest up. Slight intimacy increase.
CLOSE-UP (CU): Face fills frame. Emotion, reaction, revelation. THE power shot.
EXTREME CLOSE-UP (ECU): Eyes only, or specific detail. Obsession, tension, mystery.
INSERT: Object or detail. Clock, letter, weapon, hand action.
TWO-SHOT: Two characters in frame. Relationship, connection or disconnection.
GROUP SHOT: Three or more characters. Social dynamics.
OVER-THE-SHOULDER (OTS): One character partially visible, other character dominant. Connection.

### Moving Shots
DOLLY/TRACK: Camera on wheels/track. Smooth lateral or depth movement. Emotional precision.
PUSH IN: Camera moves toward subject. Increasing intimacy, realization, tension.
PULL OUT/REVEAL: Camera moves away from subject. Context revelation, isolation.
PAN: Camera rotates horizontally on tripod. Survey, following, connecting elements.
TILT: Camera rotates vertically. Revealing height, power.
CRANE/JIB: Vertical + horizontal movement. Epic, god's-eye, revelation.
STEADICAM: Floating follow shot. Dreamlike, suspenseful, immersive (The Shining, Goodfellas, Birdman).
HANDHELD: Intentional shakiness. Documentary, urgency, chaos (Bourne, Saving Private Ryan).
WHIP PAN/SWISH: Ultra-fast pan. Energy, surprise, scene transition.
DOLLY ZOOM (Vertigo effect): Dolly in + zoom out simultaneously (or reverse). Perspective distortion. Disorientation, realization.

## III. SHOT DESIGN METHODOLOGY

### The Coverage Plan
For each scene, design: MASTER (wide, full scene), MEDIUMS (mid-shots of key groupings), CLOSE-UPS (emotional beats for each character), INSERTS (story-critical details), CUTAWAYS (reaction shots, environment details for editorial flexibility).

### The One-Shot Scene (Oner)
An entire scene in a single unbroken take. Requires meticulous choreography of actors, camera, and crew. Famous examples: Goodfellas Copacabana entrance, Children of Men battle sequence, 1917 (apparent single take entire film), Birdman, opening of Touch of Evil.

### Shot Lists
Format: Scene# | Shot# | Size | Angle | Movement | Lens | Description | Notes
Example: SC.12 | 12A | CU | Low | Static | 85mm | Sarah realizes the letter is forged | Hold for 4 beats after dialogue ends

## IV. VISUAL STORYTELLING PATTERNS

### The Spielberg Approach
Blocking actors in depth. Push-in to face for revelation. Use of FACES — the reaction shot is often more important than the action. Wide shot for comedy, close-up for drama.

### The Kubrick Approach
One-point perspective. Symmetrical compositions. Slow zoom. The "Kubrick Stare" (head down, eyes up). Cold precision creating unease.

### The Fincher Approach
Locked-off camera. Minimal unmotivated movement. Methodical pace. Darkness and negative space. Information withheld through framing.

### The Wes Anderson Approach
Symmetrical framing. Flat/frontal compositions. Whip pans between setups. Overhead inserts. Camera as observer of a diorama.

## V. SHOT DESIGN FOR SPECIFIC SCENARIOS

### Dialogue Scenes
Classic: Master > OTS pair > CU pair > inserts. Shot/reverse shot on axis.
Advanced: Staging within master, motivated push-ins for emotional peaks, "roaming" camera that recomposes during the scene.

### Action Sequences
Wide geography shot first. Medium for choreography. Close for impact. Match on action for cuts. Each shot must answer: WHO is doing WHAT to WHOM?

### Suspense/Horror
Limited information. Negative space (what's NOT in frame). POV shots. Slow push-in. Long static holds. Sound design does 70% of the work.

## VI. REFERENCES

Books: "Master Shots" (Christopher Kenworthy — 3 volumes), "Setting Up Your Shots" (Vineyard), "The Visual Story" (Bruce Block), "Cinematography: Theory & Practice" (Brown), "Film Directing Shot by Shot" (Steven Katz).
Analysis: Every Frame a Painting (YouTube — visual film analysis), Nerdwriter, Lessons from the Screenplay.""")

# 15. THEO — Sound Designer
upload("sound-designer", "World-Class Sound Design & Audio Post-Production",
"""# THEO — ELITE SOUND DESIGN KNOWLEDGE BASE

## I. SOUND DESIGN PHILOSOPHY

### The Invisible Art
Great sound design is felt, not heard. The audience should never consciously notice sound design — they should EXPERIENCE it emotionally. Walter Murch (Apocalypse Now, The English Patient) defines sound design as creating the "sonic equivalent of the visual image."

### The 70% Rule
Audiences think they're watching a movie. In reality, sound carries up to 70% of the emotional experience. Test: watch any horror film with the sound off. It's not scary. Sound creates: fear, tension, joy, sadness, disorientation, immersion, spatial awareness.

## II. THE SOUND DESIGN PIPELINE

### Production Sound
The on-set recording team (Production Sound Mixer + Boom Operator + Utility). Captured with: boom microphones (Sennheiser MKH-416, MKH-50; Schoeps CMC6), wireless lavaliers (Lectrosonics, Wisycom, Sennheiser), multi-track recorder (Sound Devices Scorpio/888). Goal: clean dialogue with natural room tone.

### Post-Production Sound Workflow
1. DIALOGUE EDIT: Clean production dialogue, remove noise, smooth cuts, fill gaps
2. ADR (Automated Dialogue Replacement): Re-record dialogue in studio for unusable production audio
3. SOUND EFFECTS EDITING (SFX): Hard effects (sync to picture), backgrounds/ambiences, Foley
4. FOLEY: Recording footsteps, cloth movement, prop handling in sync to picture. Performed by Foley artists on a Foley stage.
5. SOUND DESIGN: Creating unique, non-literal sounds — monsters, sci-fi technology, emotional textures
6. MUSIC: Score and licensed tracks (separate from sound design but must integrate)
7. PRE-DUB/PRE-MIX: Balance within each element group (dialogue, SFX, music)
8. FINAL MIX: All elements balanced and spatialized in the final format

## III. CREATIVE SOUND DESIGN TECHNIQUES

### Worldizing (Walter Murch invention)
Play recorded sound through speakers in real environments and re-record. This adds authentic room characteristics, distance, and texture. Play clean dialogue through a speaker in a room similar to the film's location.

### Layering
Complex sounds are built from multiple layers: a creature roar might combine: elephant trumpet (low), tiger growl (mid), compressed air burst (high), slowed-down whale song (sub). 5-15 layers for hero sounds.

### Pitch Manipulation
Slow down sounds for: weight, size, menace, otherworldliness. Speed up for: energy, smallness, comedy. Time-stretch without pitch change for: tension, dreamlike quality.

### Spectral Processing
Isolate specific frequency ranges of recordings to create new sounds. The rustle of a bag might contain, when isolated and amplified, a texture that sounds like wind or whispers.

### Granular Synthesis
Break audio into tiny grains (1-50ms) and reorganize. Creates evolving, textural, otherworldly soundscapes. Software: Granulator II, Paul Stretch, Output PORTAL.

### Silence as Sound Design
The most powerful sound design tool is SILENCE. A sudden absence of sound is more impactful than any explosion. Use silence before: jump scares, emotional revelations, scene transitions, moments of realization.

## IV. MIXING STANDARDS

### Delivery Formats
DOLBY ATMOS: Immersive, object-based. Sounds placed in 3D space (overhead speakers). Now standard for theatrical and streaming.
7.1 SURROUND: 7 screen/surround channels + LFE subwoofer. Standard theatrical.
5.1 SURROUND: 5 channels + LFE. Home theater standard.
STEREO: 2-channel. TV broadcast, mobile, web.
BINAURAL: Headphone-optimized 3D audio (Apple Spatial Audio, Dolby Atmos for headphones).

### Loudness Standards
Theatrical: 85 dB SPL reference level (Dolby standard). Dialogue norm around -31 LKFS.
Streaming: -24 LKFS (Netflix), -27 LKFS (Spotify/podcast). Loudness normalization is enforced.
Broadcast: -24 LKFS (ATSC A/85 US standard), -23 LUFS (EBU R128 European standard).

## V. ICONIC SOUND DESIGN TO STUDY

Star Wars (Ben Burtt): Lightsaber (CRT hum + projector motor), Blaster (guy wire), Chewbacca (bear + walrus + badger), R2-D2 (synthesizer + baby vocalization)
Jurassic Park (Gary Rydstrom): T-Rex (baby elephant + tiger + alligator slowed), Velociraptors (dolphins + geese + tortoises mating)
Blade Runner 2049 (Theo Green/Mark Mangini): Layered, immersive, industrial soundscapes creating oppressive atmosphere
A Quiet Place (Erik Aadahl/Ethan Van der Ryn): Silence-based design where every sound is terrifying

## VI. TOOLS & SOFTWARE

DAWs: Pro Tools (industry standard for film), Nuendo/Cubase (Steinberg), Logic Pro, Reaper.
Sound Libraries: Boom Library, Sound Ideas, Hollywood Edge, BBC Sound Effects, Freesound.org.
Plugins: iZotope RX (noise reduction/restoration — industry essential), Soundtoys (creative effects), FabFilter (EQ/dynamics), Altiverb (convolution reverb), Waves.
Hardware: Genelec monitors (8341/8351), Avid S6 control surface, Sound Devices recorders.

## VII. REFERENCES

Books: "Designing Sound" (Andy Farnell — synthesis approach), "Sound Design" (David Sonnenschein), "The Sound Effects Bible" (Ric Viers), "In the Blink of an Eye" (Walter Murch — editing + sound philosophy).
Organizations: MPSE (Motion Picture Sound Editors), CAS (Cinema Audio Society).
Education: Berklee Online (sound design), SCAD, Vancouver Film School.""")

# 16. MELODY — Composer
upload("composer", "World-Class Film Scoring & Music Composition",
"""# MELODY — ELITE FILM COMPOSITION KNOWLEDGE BASE

## I. FILM SCORING PHILOSOPHY

### Music as Emotional Architecture
Film music exists to tell the audience what to FEEL. It operates below conscious perception — the best scores are felt without being noticed. Hans Zimmer: "The job of a film composer is not to write music — it's to make the movie better."

### The Composer-Director Relationship
The spotting session: Watch the film with the director, decide where music starts/stops (cues), discuss emotional intent for each cue. Key question: "What should the audience FEEL at this moment?"

## II. MUSIC THEORY FOR FILM

### Emotional Harmony
MAJOR KEYS: Happiness, triumph, resolution, openness, adventure
MINOR KEYS: Sadness, tension, darkness, introspection, longing
MODAL SCALES:
- Lydian (#4): Wonder, magic, floating (John Williams' E.T.)
- Mixolydian (b7): Heroic but earthy, folk-tinged (many Marvel themes)
- Dorian (b3, b7): Cool, sophisticated, melancholy but not defeated
- Phrygian (b2): Exotic, Spanish, menacing
- Locrian (b2, b3, b5, b6, b7): Ultimate dissonance, horror, instability

### Orchestration by Emotion
STRINGS: Warmth, emotion, sweeping romance, tension (tremolo/sul ponticello)
BRASS: Power, heroism, militaristic, nobility (French horns = heroic, trumpets = regal, trombones = weight)
WOODWINDS: Innocence, pastoral, whimsy, loneliness (solo oboe = melancholy, flute = lightness, clarinet = warmth)
PERCUSSION: Urgency, tribal, primal, mechanical (taiko = epic, snare = military, timpani = gravity)
CHOIR: Spiritual, epic, otherworldly (Latin text = ancient, wordless = ethereal)
ELECTRONICS/SYNTHS: Modern, sci-fi, psychological, tension, texture

### Leitmotif Technique (Wagner via Williams)
Assign recurring musical themes to characters, places, objects, or ideas. Transform the motif as the character develops:
- MAJOR to MINOR: Hope to despair
- SLOW to FAST: Contemplation to action
- SOLO to FULL ORCHESTRA: Isolation to community
- FRAGMENTED: Character is broken or uncertain
Examples: Star Wars (Force theme, Imperial March, Han & Leia), Lord of the Rings (Fellowship, Shire, Rohan, Mordor), Harry Potter (Hedwig's theme).

## III. SCORING WORKFLOW

### The Technical Pipeline
1. SPOTTING SESSION: With director, determine where music goes
2. SKETCHING: Thematic material, main melodies, harmonic language
3. MOCKUPS: Full MIDI/sample mockups of each cue for director approval
4. ORCHESTRATION: Full orchestral scores (or self-orchestrated for hybrid scores)
5. RECORDING: Live musicians at scoring stage (Abbey Road, Air Lyndhurst, Fox/Newman, Sony)
6. MIXING: Balance live recordings with synth elements
7. DUBBING: Integrate score with dialogue and SFX in final mix

### Sync & Timing
HIT POINTS: Specific moments music must align with picture (door slam, reveal, explosion).
CLICK TRACK: Metronome for musicians, programmed to hit marks at exact timecodes.
FREE TIMING: Conductor watches screen and leads orchestra without click. More organic, harder to sync.
TEMPO MAPPING: Variable BPM to hit multiple sync points naturally.

## IV. MODERN SCORING APPROACHES

### Orchestral (Traditional)
Full symphony orchestra (60-90 players). Lush, cinematic, timeless. John Williams, Alexandre Desplat, Michael Giacchino.

### Hybrid (Orchestra + Electronics)
Hans Zimmer's approach: synthesized beds with live orchestral elements on top. Massive scale, modern texture. Used in: Inception, Interstellar, Dune, Batman.

### Minimal/Textural
Stripped down, atmospheric. Piano, solo instruments, electronics. Trent Reznor & Atticus Ross (Social Network, Soul), Jonny Greenwood (There Will Be Blood, Phantom Thread), Mica Levi (Under the Skin, Jackie).

### Electronic/Synth
Full synthesizer scores. S U R V I V E / Kyle Dixon & Michael Stein (Stranger Things), Vangelis (Blade Runner), Giorgio Moroder (Midnight Express), Cliff Martinez (Drive).

## V. SAMPLE LIBRARIES & TOOLS

### DAWs
Logic Pro: Composer-friendly, built-in orchestral tools. Many Hollywood composers use it.
Cubase/Nuendo: Steinberg. Strong MIDI, expression maps. European standard.
Digital Performer: MOTU. Film scoring-specific features, chunk-based organization.
Pro Tools: Avid. Industry standard for audio, less common for MIDI-heavy composition.

### Sample Libraries (Best-in-Class)
STRINGS: Spitfire Symphonic Strings, CSS (Cinematic Studio Strings), Berlin Strings, LA Scoring Strings
BRASS: Cinesamples CineBrass, Spitfire Symphonic Brass, Berlin Brass
WOODWINDS: Berlin Woodwinds, Spitfire Symphonic Woodwinds, CSS Woodwinds
PERCUSSION: Spitfire Hans Zimmer Percussion, Cinesamples CinePerc, Damage 2
CHOIR: Spitfire Eric Whitacre Choir, 8Dio Lacrimosa, Strezov Storm Choir
FULL ORCHESTRA: BBC Symphony Orchestra (Spitfire), EastWest Hollywood Orchestra, Orchestral Tools Berlin Series
SYNTH: Omnisphere (Spectrasonics), Serum (Xfer), Pigments (Arturia), Vital (free)

## VI. LEGENDARY FILM COMPOSERS

JOHN WILLIAMS: Star Wars, Indiana Jones, Schindler's List, Harry Potter. The greatest leitmotif composer in film history. Pure orchestral mastery.
HANS ZIMMER: Dark Knight, Inception, Dune, Interstellar. Pioneer of hybrid orchestral-electronic scoring. Emotional simplicity through massive sound.
ENNIO MORRICONE: The Good The Bad and The Ugly, Cinema Paradiso, The Mission. Melodic genius, unconventional instrumentation.
BERNARD HERRMANN: Psycho, Vertigo, Citizen Kane, Taxi Driver. Psychological tension through harmony.
HOWARD SHORE: Lord of the Rings trilogy. 10+ hours of leitmotif-rich orchestral scoring. Unmatched scope.
TRENT REZNOR & ATTICUS ROSS: Social Network, Soul, Mank. Redefined modern film scoring with electronic textures.
ALEXANDRE DESPLAT: Grand Budapest Hotel, Shape of Water. Elegant, European sensibility.

## VII. REFERENCES

Books: "On the Track" (Karlin & Wright — film scoring bible), "Complete Guide to Film Scoring" (Davis), "The Reel World" (Jeff Rona), "Hearing the Movies" (Buhler/Neumeyer).
Education: Berklee Film Scoring, USC Thornton, Hans Zimmer MasterClass, Spitfire Audio YouTube tutorials.
Organizations: SCL (Society of Composers & Lyricists), ASCAP, BMI (performance rights).""")

# 17. NOVA — Prompt Engineer (Already has deep system prompt, add KB)
upload("prompt-engineer", "World-Class AI Prompt Engineering & LLM Optimization",
"""# NOVA — ELITE PROMPT ENGINEERING KNOWLEDGE BASE

## I. PROMPT ENGINEERING FUNDAMENTALS

### The Prompt is the Program
In the AI era, natural language IS code. The quality of output is directly proportional to the quality of the prompt. A well-engineered prompt is: SPECIFIC (not vague), STRUCTURED (organized), CONTEXTUAL (includes relevant background), CONSTRAINED (defines boundaries), and EXEMPLIFIED (shows desired output format).

### The Anatomy of a Perfect Prompt
1. ROLE/PERSONA: "You are a [specific expert] with [years] of experience in [domain]"
2. CONTEXT: Background information the AI needs to understand the situation
3. TASK: Clear, specific instruction of what to produce
4. CONSTRAINTS: Length, format, tone, what to avoid
5. EXAMPLES: 1-3 examples of desired output (few-shot learning)
6. OUTPUT FORMAT: Exact structure expected (JSON, markdown, bullet points, etc.)

## II. ADVANCED PROMPTING TECHNIQUES

### Chain-of-Thought (CoT)
Ask the model to "think step by step" or "show your reasoning." This dramatically improves accuracy on complex tasks (math, logic, analysis). Wei et al. (2022) showed CoT improves performance by 20-50% on reasoning benchmarks.

### Few-Shot Learning
Provide 2-5 examples of input-output pairs before the actual task. The model learns the pattern and applies it. More examples = more consistent output, but diminishing returns after 5.

### ReAct (Reasoning + Acting)
Combine reasoning with action steps: "Thought: I need to... Action: I will... Observation: The result shows... Thought: Based on this..."

### Tree of Thought (ToT)
For complex problems, explore multiple solution paths: "Consider three different approaches to this problem. Evaluate each approach's pros and cons. Select the best approach and develop it fully."

### Constitutional AI Principles
Self-critique: "Review your response for accuracy, bias, and completeness. Revise any issues." This meta-cognitive layer improves output quality.

## III. PROMPT ENGINEERING FOR CREATIVE PRODUCTION

### Image Generation Prompts (Midjourney/DALL-E/Flux/Stable Diffusion)
STRUCTURE: [Subject] + [Style] + [Lighting] + [Composition] + [Mood] + [Technical parameters]
QUALITY BOOSTERS: "highly detailed," "professional photography," "cinematic lighting," "8K resolution," "photorealistic"
STYLE REFERENCES: "in the style of [artist/photographer]," "inspired by [art movement]"
NEGATIVE PROMPTS: Specify what to AVOID (blurry, deformed, low quality, text)

### Video Generation Prompts (Runway/Sora/Kling)
Focus on: camera movement, temporal progression, consistent physics, character continuity.
Structure: [Camera movement] + [Subject action] + [Environment] + [Lighting/atmosphere] + [Duration/speed]

### Audio Generation Prompts (Suno/Udio/ElevenLabs)
For music: [Genre] + [Tempo/BPM] + [Mood] + [Instruments] + [Structure] + [Reference artist]
For voice: [Character description] + [Emotion] + [Pace] + [Accent] + [Context]

## IV. MODEL SELECTION STRATEGY

### When to Use Which Model
OPUS/GPT-4 CLASS: Complex reasoning, nuanced creative writing, multi-step planning, code architecture
SONNET/GPT-4-MINI CLASS: General tasks, fast iteration, bulk processing, standard writing
HAIKU/GPT-3.5 CLASS: Simple tasks, classification, extraction, high-volume low-cost operations
GEMINI FLASH: Fast, cheap, large context window — good for summarization and analysis
SPECIALIZED MODELS: Use domain-specific models when available (code models for coding, image models for vision)

### Cost Optimization
Token economics: input tokens < output tokens in cost. Pre-process and compress context. Cache system prompts. Batch similar requests. Use smaller models for simple subtasks within a larger pipeline.

## V. SYSTEM PROMPT ARCHITECTURE

### The Nano Banana Pro Framework
The Nano Banana Pro system is a specialized prompt engineering methodology for multi-agent creative pipelines:
1. IDENTITY LAYER: Who is this agent? What's their expertise? What's their personality?
2. METHODOLOGY LAYER: Step-by-step process the agent follows
3. KNOWLEDGE LAYER: Domain-specific facts, frameworks, and standards
4. CONSTRAINT LAYER: What the agent should never do, output limits, format requirements
5. INTERACTION LAYER: How the agent communicates — tone, vocabulary, response style

### Context Window Management
Models have finite context windows (8K-2M tokens). Prioritize: System prompt (always) > Current task (always) > Recent context (high priority) > Historical context (lower priority) > Reference material (as needed).

## VI. REFERENCES

Papers: "Chain-of-Thought Prompting" (Wei et al. 2022), "Tree of Thoughts" (Yao et al. 2023), "ReAct" (Yao et al. 2022), "Constitutional AI" (Anthropic 2022).
Guides: Anthropic Prompt Engineering Guide, OpenAI Cookbook, Google AI Prompt Design Guide.
Communities: r/PromptEngineering, Prompt Engineering Discord, PromptBase marketplace.""")

# 18. PIXEL — Image Prompt Specialist
upload("image-prompt", "World-Class AI Image Generation & Prompt Craft",
"""# PIXEL — ELITE AI IMAGE GENERATION KNOWLEDGE BASE

## I. IMAGE GENERATION MODELS (2024-2026)

### Model Landscape
MIDJOURNEY V6.1+: Best for aesthetics, art direction, cinematic quality. Strong style understanding. Discord or web interface.
DALL-E 3 (OpenAI): Best text rendering in images, strong prompt following, ChatGPT integration.
STABLE DIFFUSION XL / SD3 / FLUX: Open-source, customizable, LoRA/ControlNet ecosystem. Best for pipelines.
ADOBE FIREFLY: Commercially safe (trained on licensed content), Photoshop integration.
IDEOGRAM: Strong typography and text-in-image generation.
GOOGLE IMAGEN 3: High fidelity, strong prompt adherence.

### Key Technical Concepts
DIFFUSION: Models generate images by starting with noise and iteratively denoising. More steps = more detail but slower.
GUIDANCE SCALE (CFG): How closely the model follows the prompt. 7-12 typical. Too high = oversaturated/artifacts.
SEED: Random starting point. Same seed + same prompt = reproducible result. Critical for iteration.
ASPECT RATIO: 1:1 (square), 16:9 (cinematic wide), 9:16 (portrait/mobile), 3:2 (photography standard).
RESOLUTION: 1024x1024 standard. Upscale with: Real-ESRGAN, Topaz Gigapixel, Magnific AI.

## II. PROMPT ARCHITECTURE FOR PHOTOREALISM

### The Layered Prompt Formula
LAYER 1 — SUBJECT: "A weathered 60-year-old fisherman with sun-creased skin and grey stubble"
LAYER 2 — ACTION/POSE: "mending a fishing net with gnarled hands, sitting on a dock"
LAYER 3 — ENVIRONMENT: "small Mediterranean fishing village, turquoise water, whitewashed buildings"
LAYER 4 — LIGHTING: "golden hour side-lighting, warm sunlight through clouds, soft shadows"
LAYER 5 — CAMERA/TECHNICAL: "shot on Hasselblad 907X, 80mm lens, f/2.8, shallow depth of field"
LAYER 6 — MOOD/ATMOSPHERE: "quiet, contemplative, nostalgic, documentary photography"
LAYER 7 — STYLE: "Steve McCurry photography style, National Geographic quality"

### Quality Amplifiers
Photography: "professional photography," "editorial photography," "award-winning photo"
Art: "masterpiece," "highly detailed," "gallery quality," "museum piece"
Technical: "8K resolution," "hyperrealistic," "photorealistic," "ultra-detailed"
Lighting: "volumetric lighting," "rim lighting," "Rembrandt lighting," "golden hour"

### What to Avoid
Vague prompts: "a nice landscape" (too generic)
Contradictions: "bright and dark" (confuses model)
Too many subjects: Focus on ONE main subject per image
Negative prompt overload: Keep negative prompts focused on actual problems

## III. PROMPT ARCHITECTURE FOR STYLIZED/ARTISTIC

### Art Style Keywords
CINEMATIC: "cinematic still," "movie screenshot," "film grain," "anamorphic lens flare"
ANIME: "anime key visual," "Studio Ghibli style," "cel-shaded," "manga illustration"
CONCEPT ART: "concept art," "matte painting," "digital art," "artstation trending"
PAINTING: "oil painting," "impressionist," "watercolor," "gouache," "acrylic"
ILLUSTRATION: "editorial illustration," "children's book illustration," "graphic novel," "vector art"

### Artist Style References
Photograph-like: Annie Leibovitz, Peter Lindbergh, Steve McCurry, Ansel Adams
Cinematic: Roger Deakins, Emmanuel Lubezki, Vittorio Storaro (as lighting references)
Illustration: Alphonse Mucha, Norman Rockwell, J.C. Leyendecker, Moebius
Concept Art: Syd Mead, Ralph McQuarrie, Feng Zhu, Craig Mullins
Fine Art: Caravaggio (chiaroscuro), Vermeer (natural light), Turner (atmosphere), Hopper (isolation)

## IV. ADVANCED TECHNIQUES

### ControlNet (Stable Diffusion/Flux)
DEPTH: Maintain 3D spatial structure while generating new content. Import depth map from 3D scene.
CANNY/EDGE: Preserve line structure. Great for architectural accuracy.
OPENPOSE: Maintain character pose. Essential for consistent character acting.
SEGMENTATION: Control which areas get which content. Precise scene composition.
IP-ADAPTER: Use reference images to maintain character/style consistency.

### LoRA (Low-Rank Adaptation)
Fine-tune models on specific: characters (15-30 reference images), styles, objects, locations. Training takes 15-30 minutes on modern GPU. The key to CHARACTER CONSISTENCY in AI production.

### Inpainting & Outpainting
INPAINTING: Regenerate selected regions while keeping the rest. Fix hands, faces, details.
OUTPAINTING: Extend the canvas. Add environment, sky, foreground.

### Upscaling Pipeline
Generate at native resolution (1024x1024) → Upscale 2-4x with AI upscaler → Detail enhancement pass → Manual touchup if needed.

## V. FILM PRODUCTION IMAGE WORKFLOW

### Concept Art Generation
Brief → 20-50 rapid generations exploring directions → Select top 5 → Refine with inpainting → Present to director → Iterate → Final concept

### Character Sheet Generation
Reference images → LoRA training → Generate turnaround (front/side/back) → Expression sheet → Costume variations → Model sheet compilation

### Storyboard Frame Generation
Script scene → Rough composition sketch (ControlNet input) → Generate frame → Adjust composition → Add panel borders and annotations

## VI. REFERENCES

Communities: Midjourney Discord, r/StableDiffusion, Civitai (model/LoRA sharing), CivitAI.
Tools: ComfyUI (node-based SD workflow), Automatic1111 (SD web UI), InvokeAI, Fooocus.
Learning: Olivio Sarikas (YouTube), Sebastian Kamph (YouTube), Aitrepreneur.""")

# 19. MOTION — Video Prompt Specialist
upload("video-prompt", "World-Class AI Video Generation & Motion Prompts",
"""# MOTION — ELITE AI VIDEO GENERATION KNOWLEDGE BASE

## I. VIDEO GENERATION MODELS (2024-2026)

### Model Landscape
RUNWAY GEN-3 ALPHA/TURBO: Industry leader for controllability. Camera controls, motion brush, style reference. 5-10 second clips.
SORA (OpenAI): Highest fidelity, best physics understanding, longest generation (up to 60 sec). Limited public access.
KLING 1.6 (Kuaishou): Strong character consistency, good motion quality. Chinese-developed, globally accessible.
MINIMAX/HAILUO: Excellent motion naturalism. Strong for character animation.
PIKA 2.0: Quick iterations, good for stylized content. Lip sync capability.
LUMA DREAM MACHINE: Fast generation, good for nature and environments.
STABLE VIDEO DIFFUSION: Open-source, customizable pipeline.
VIDU (Shengshu): Strong cinematic quality, good camera movement.

### Key Technical Limitations
DURATION: Most models generate 4-10 second clips. Story = multiple clips stitched.
CONSISTENCY: Characters may change between generations. Mitigation: reference frames, LoRA.
PHYSICS: AI still struggles with: object permanence, complex interactions, accurate shadows, fluid dynamics.
HANDS/FINGERS: Remain problematic. Frame accordingly or fix in post.
TEXT/SIGNAGE: Usually garbled. Add in post-production.

## II. VIDEO PROMPT ARCHITECTURE

### The Cinematic Prompt Formula
[Camera Movement] + [Shot Type] + [Subject Description] + [Action/Motion] + [Environment] + [Lighting] + [Atmosphere] + [Style Reference]

### Camera Movement Vocabulary
STATIC/LOCKED: "static camera," "tripod shot," "locked-off frame"
PAN: "slow pan left to right," "camera pans to reveal"
TILT: "camera tilts up from feet to face"
DOLLY/TRACK: "camera dollies forward," "tracking shot following subject"
CRANE: "crane shot rising above," "camera ascending"
ORBIT: "camera orbits around subject," "360-degree orbit"
PUSH IN: "slow push in on face," "camera moves closer"
PULL OUT: "camera pulls back to reveal"
HANDHELD: "handheld camera," "documentary style movement"
DRONE/AERIAL: "aerial drone shot," "bird's eye descending"
FIRST PERSON/POV: "first-person perspective," "POV walking through"

### Motion Description
Be SPECIFIC about motion. Not "person walks" but "a woman in a red dress walks confidently toward camera, her heels clicking on wet pavement, rain falling around her, reflections shimmering."

Temporal structure: Describe what happens at BEGINNING, MIDDLE, and END of the clip.
"Camera starts on a close-up of coffee being poured, then slowly pulls back to reveal a bustling cafe interior, ending on a wide shot of the entire space."

## III. SHOT-SPECIFIC PROMPTING

### Establishing Shot
"Aerial drone shot slowly descending over a foggy mountain range at dawn, golden light breaking through clouds, pine forests below, cinematic, 4K, slow motion"

### Character Introduction
"Medium shot of a woman in her 30s with short dark hair, wearing a leather jacket, turning to look at camera with a confident smile, urban street background, evening blue hour lighting, shallow depth of field, cinematic film grain"

### Action Sequence
"Dynamic tracking shot following a parkour runner leaping between rooftops, camera matching speed, urban skyline in background, sunset lighting, GoPro-style perspective, fast-paced, adrenaline"

### Emotional Close-Up
"Extreme close-up of an elderly man's weathered face, a single tear rolling down his cheek, warm golden side-lighting, shallow depth of field, soft focus background, intimate and raw"

### Dialogue Scene
"Two-shot of two people sitting across a cafe table, one person speaking animatedly while the other listens intently, warm interior lighting, coffee steam rising, gentle camera push-in, naturalistic"

## IV. MULTI-SHOT WORKFLOW FOR NARRATIVE

### Scene Construction
1. ESTABLISH: Wide shot of location (aerial or wide)
2. APPROACH: Character entering the space
3. ENGAGE: Medium shots of character interacting
4. EMOTION: Close-ups for key emotional beats
5. TRANSITION: Shot linking to next scene

### Maintaining Consistency
- Use REFERENCE FRAMES from previous generations as input for new ones
- Maintain consistent lighting direction across all shots in a scene
- Describe character identically in every prompt (save character descriptions as reusable blocks)
- Use same style/aesthetic keywords across all prompts in a project

## V. POST-PRODUCTION PIPELINE

### Editing AI Video
Raw AI clips → Trim best sections → Color grade for consistency → Add transitions → Layer sound design → Add music → Final composite.

### Fixing Common Issues
FLICKERING: Frame interpolation (RIFE, Topaz Video AI)
SHORT CLIPS: Extend with: reverse + forward loop, slow motion, frame interpolation
ARTIFACTS: Mask and inpaint specific frames, or regenerate problem sections
CHARACTER DRIFT: Use consistent reference frames, or composite face from reference in post

## VI. REFERENCES

Platforms: Runway ML (runwayml.com), Pika (pika.art), Kling (klingai.com), Luma (lumalabs.ai).
Tutorials: Runway YouTube channel, Theoretically Media (YouTube), Matt Wolfe (YouTube).
Communities: r/AIVideo, Runway Discord, Creative AI Discord.""")

# 20. ECHO — Audio Prompt Specialist
upload("audio-prompt", "World-Class AI Audio Generation & Sound Prompts",
"""# ECHO — ELITE AI AUDIO GENERATION KNOWLEDGE BASE

## I. AI AUDIO GENERATION MODELS (2024-2026)

### Music Generation
SUNO V4: Highest quality AI music. Full songs with vocals, instruments, and production. Style/genre specification. Up to 4 minutes.
UDIO: Strong musicality, good for complex arrangements. Excellent genre range.
STABLE AUDIO 2.0: Open-source, customizable. Good for loops and stems.
GOOGLE MUSICLM/MUSICFX: Research-grade, strong temporal coherence.
META MUSICGEN: Open-source, controllable. Good for instrumental.

### Voice Generation
ELEVENLABS: Industry leader. Voice cloning, multilingual, emotion control. Professional quality.
OPENAI TTS: Four voices, natural prosody, fast. Good for narration.
BARK (Suno): Open-source, emotional range, non-verbal sounds (laughing, sighing).
TORTOISE TTS: Open-source, high quality, slow generation.
XTTS (Coqui): Open-source multilingual voice cloning.

### Sound Effects
ELEVENLABS SFX: Text-to-sound-effect generation.
META AUDIOGEN: Research-grade sound effect generation.
STABLE AUDIO: Sound effects and ambient generation.

## II. MUSIC PROMPT ARCHITECTURE

### The Musical Prompt Formula
[Genre] + [Sub-genre] + [Tempo/Energy] + [Instruments] + [Mood/Emotion] + [Era/Influence] + [Structure] + [Production Quality]

### Genre Specification (Be Precise)
Not "rock" but "90s grunge rock with heavy distorted guitars, driving drums, and raw vocals, inspired by Nirvana and Soundgarden"
Not "electronic" but "deep house with warm analog synth pads, four-on-the-floor kick, subtle hi-hat patterns, 122 BPM, late-night club atmosphere"
Not "classical" but "romantic-era orchestral piece for full symphony, sweeping string melodies, French horn countermelody, building to triumphant brass climax, in the style of late Tchaikovsky"

### Tempo & Energy Keywords
SLOW (60-80 BPM): "ballad," "slow," "gentle," "laid-back," "contemplative"
MEDIUM (80-120 BPM): "moderate," "walking pace," "relaxed groove," "mid-tempo"
FAST (120-160 BPM): "upbeat," "driving," "energetic," "high-energy," "intense"
VERY FAST (160+ BPM): "frantic," "breakneck," "rapid-fire," "drum and bass tempo"

### Instrument Specification
STRINGS: "lush strings," "solo violin," "string quartet," "pizzicato," "tremolo strings"
KEYS: "grand piano," "Rhodes electric piano," "Hammond organ," "honky-tonk piano," "synthesizer pad"
GUITARS: "clean electric guitar," "overdriven," "acoustic fingerpicking," "slide guitar," "12-string"
DRUMS: "live acoustic drums," "808 drum machine," "brushed jazz drums," "tribal percussion," "electronic beats"
BASS: "upright bass," "slap bass," "sub bass," "Moog bass," "fretless"
WORLD: "sitar," "koto," "djembe," "pan flute," "oud," "gamelan," "didgeridoo"

### Film Scoring Prompts
"Tense orchestral underscore, low sustained strings, distant brass stabs, ticking percussion, building anxiety, similar to Hans Zimmer's Inception score, 90 BPM, cinematic quality"
"Whimsical fairy-tale theme, celeste and harp melody, light pizzicato strings, gentle woodwinds, music-box quality, enchanting and innocent, similar to Alexandre Desplat"

## III. VOICE GENERATION PROMPTS

### Character Voice Design
Specify: AGE (child/teen/adult/elderly), GENDER, ACCENT (British RP/Southern US/Brooklyn/etc.), PITCH (deep/mid/high), PACE (slow/measured/rapid), TEXTURE (smooth/gravelly/breathy/nasal), EMOTION (warm/cold/excited/weary).

### Narration vs Dialogue
NARRATION: "Calm, authoritative narrator voice, similar to David Attenborough, measured pace, warm British accent, documentary style"
DIALOGUE: "Young woman, mid-20s, excited and slightly breathless, American accent, speaking quickly as if sharing surprising news"

### Emotional Control
"Deliver with barely contained anger — voice is controlled and quiet but with tension underneath, like a person about to snap"
"Speak with deep sadness, voice cracking slightly on key words, as if holding back tears"

## IV. SOUND DESIGN PROMPTS

### Environmental Ambience
"Busy Tokyo street crossing — multiple pedestrian signals beeping, crowd footsteps, distant car horns, electronic store music bleeding out, bicycle bells, overhead train rumble, 60 seconds, stereo"

### Sound Effects
"Heavy medieval castle door creaking open slowly, iron hinges groaning, echo in stone hallway, dust particles settling"
"Futuristic weapon charging up — electrical hum building in pitch, plasma crackling, energy reaching critical level, then powerful discharge blast"

### Foley
"Footsteps on gravel — slow, deliberate pace, leather boots, outdoor, quiet night ambience underneath"

## V. AUDIO POST-PRODUCTION PIPELINE

### Integration Workflow
1. Generate base audio (music/voice/SFX)
2. Edit and trim in DAW (Pro Tools, Logic, Reaper)
3. EQ and dynamics processing to match production audio
4. Spatial placement (stereo pan, reverb for distance)
5. Level balancing with other audio elements
6. Format delivery (stereo, 5.1, Atmos stems)

### Quality Standards for AI Audio
Sample rate: 44.1kHz minimum, 48kHz preferred for video production.
Bit depth: 24-bit for production, 16-bit for final delivery.
Format: WAV/AIFF for production, AAC/MP3 for preview only.

## VI. REFERENCES

Platforms: Suno (suno.com), Udio (udio.com), ElevenLabs (elevenlabs.io).
DAWs: Pro Tools, Logic Pro, Reaper, Ableton Live.
Learning: Audio Production courses on Coursera/Berklee Online.""")

print("\n=== Batch 2 complete (agents 11-20) ===")
