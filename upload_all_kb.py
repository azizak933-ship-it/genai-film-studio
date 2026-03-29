#!/usr/bin/env python3
"""Upload world-class knowledge bases for all 34 GenAI Film Studio agents."""

import json, urllib.request, sys

API = "http://localhost:3000/api/kb/upload"

def upload(agent_id, name, content):
    data = json.dumps({"agentId": agent_id, "name": name, "content": content}).encode()
    req = urllib.request.Request(API, data=data, headers={"Content-Type": "application/json"})
    try:
        resp = urllib.request.urlopen(req)
        result = json.loads(resp.read())
        print(f"  OK  {agent_id:25s} | {name[:50]:50s} | {result.get('contentLength',0):>5} chars")
        return True
    except Exception as e:
        print(f"  ERR {agent_id}: {e}")
        return False

KBS = [

# ─────────────────────────────────────────────────────
# 3. SCOUT — Research & References
# ─────────────────────────────────────────────────────
("researcher", "World-Class Film Research & Reference Methods",
"""# SCOUT — ELITE RESEARCH & REFERENCES KNOWLEDGE BASE

## I. RESEARCH METHODOLOGY FOR FILM

### Primary vs Secondary Sources
PRIMARY: Original documents, interviews, photographs, artifacts, firsthand accounts, archival footage, court records, patents, letters, diaries. Always preferred for authenticity.
SECONDARY: Published analyses, biographies, documentaries, academic papers, encyclopedias. Use to find primary sources and provide context.

### The Research Pyramid
1. BROAD SURVEY: Wikipedia, general encyclopedias, overview books — establish the landscape
2. DEEP DIVE: Academic databases (JSTOR, Google Scholar, ProQuest), specialized books, trade publications
3. PRIMARY SOURCES: Archives (Library of Congress, National Archives, BFI Archive, Smithsonian), museum collections, oral histories
4. EXPERT CONSULTATION: Subject matter experts, cultural consultants, military advisors, scientific advisors
5. FIELD RESEARCH: Location visits, photographic documentation, environmental recording, cultural immersion

### Source Verification (AP/Reuters Standard)
Every factual claim needs minimum two independent sources. Cross-reference dates, names, locations across multiple databases. Flag single-source claims. Document chain of custody for historical materials.

## II. HISTORICAL ACCURACY RESEARCH

### Period Research Framework
ARCHITECTURE: Identify styles by decade (Georgian, Victorian, Art Deco, Brutalist, Mid-Century Modern). Reference: "A Field Guide to American Houses" (McAlester).
COSTUME: Silhouettes by era — 1920s drop-waist, 1940s padded shoulders, 1950s New Look, 1960s mod, 1970s bell-bottoms. Reference: "Survey of Historic Costume" (Tortora & Eubank).
TECHNOLOGY: Chronological accuracy — telephone 1876, car 1886, radio 1920, TV 1928, internet 1969, smartphone 2007.
LANGUAGE: Avoid anachronisms — "OK" first 1839, "cool" (slang) 1940s, "awesome" (positive) 1980s.
SOCIAL NORMS: Gender roles, racial dynamics, class structures, religious practices — all era-specific.

### Key Historical Databases
Library of Congress Digital Collections, British Library Online, Europeana, Internet Archive (archive.org), Newspapers.com, Ancestry.com, Google Books (pre-1924 full text), HathiTrust, Chronicling America.

## III. CULTURAL AUTHENTICITY

### The Authenticity Framework
1. HIRE FROM THE CULTURE: Consultants, writers, directors from the community
2. LANGUAGE: Dialect coaches, native speaker review
3. CUSTOMS: Religious practices, food, family structures verified by cultural experts
4. VISUAL REPRESENTATION: Research actual clothing, hairstyles, environments
5. SENSITIVITY READ: Full script review by cultural consultants

## IV. COMPETITIVE & MARKET RESEARCH

### Box Office Analysis Tools
Box Office Mojo, The Numbers (profitability index), IMDb Pro (STARmeter, project tracking), Opus Data (international), Comscore (theatrical), Nielsen (streaming estimates).

### Comp Analysis
Identify 5-10 comparables by: genre + budget tier + star power + release window + demographic. Analyze: budget, worldwide gross, domestic/international split, opening weekend, legs ratio, scores.

## V. LEGAL RESEARCH FOR CLEARANCE

LIFE RIGHTS: Option from living subjects or estates. Not legally required for public figures but recommended.
MUSIC: Master license (label) + sync license (publisher). $15K-$500K per song.
TRADEMARK: Visible brands need permission or obscure/alter.
ARCHIVE FOOTAGE: License from rights holder. $1K-$50K per clip.
E&O INSURANCE: Required by distributors. Attorney clearance report needed.

## VI. RESEARCH TOOLS ECOSYSTEM

Academic: Google Scholar, JSTOR, PubMed, arXiv, SSRN, ProQuest.
Images: Getty, Shutterstock Editorial, Alamy, LOC Prints & Photos, Magnum Photos.
Video: Getty/BBC Motion Gallery, Pond5, Critical Past, British Pathe.
Maps: David Rumsey Collection, Old Maps Online, Sanborn Maps (LOC), Google Earth historical.

## VII. ESSENTIAL REFERENCES

Books: "Research for Writers" (Hoffmann), "The Craft of Research" (Booth/Colomb/Williams), "The Fact Checker's Bible" (Harrison Smith).
Style Guides: AP Stylebook, Chicago Manual of Style, MLA Handbook."""),

# ─────────────────────────────────────────────────────
# 4. VERA — Scriptwriter
# ─────────────────────────────────────────────────────
("scriptwriter", "World-Class Screenwriting & Story Development",
"""# VERA — ELITE SCRIPTWRITING & STORY DEVELOPMENT KNOWLEDGE BASE

## I. STORY STRUCTURE FRAMEWORKS

### Blake Snyder's Save the Cat! — 15 Beats
1. Opening Image (p.1) — world BEFORE transformation
2. Theme Stated (p.5) — theme articulated, hero doesn't understand yet
3. Set-Up (p.1-10) — hero, stakes, world rules
4. Catalyst (p.12) — inciting incident disrupts status quo
5. Debate (p.12-25) — hero resists the call
6. Break into Two (p.25) — hero commits (ACT 2)
7. B Story (p.30) — love/friendship carrying the theme
8. Fun and Games (p.30-55) — the promise of the premise
9. Midpoint (p.55) — false victory/defeat, stakes raise
10. Bad Guys Close In (p.55-75) — external pressure + internal doubt
11. All Is Lost (p.75) — worst moment, "whiff of death"
12. Dark Night of the Soul (p.75-85) — rock bottom
13. Break into Three (p.85) — A+B merge, hero has the answer
14. Finale (p.85-110) — apply lessons, defeat opposition, transform
15. Final Image (p.110) — mirror of opening, shows transformation

### Robert McKee's Story Principles
STORY = VALUES AT STAKE. Every scene turns a value (love/hate, life/death). No value change = cut the scene.
CONTROLLING IDEA = value change + cause. Example: "Justice triumphs because the protagonist is more cunning than injustice."
CRISIS: The obligatory scene — protagonist faces ultimate dilemma (irreconcilable goods or lesser evil).

### Joseph Campbell's Hero's Journey (Vogler)
12 stages: Ordinary World, Call to Adventure, Refusal, Meeting Mentor, Crossing Threshold, Tests/Allies/Enemies, Approach Inmost Cave, Ordeal, Reward, Road Back, Resurrection, Return with Elixir.

### Dan Harmon's Story Circle
8 steps: YOU (comfort) > NEED (desire) > GO (unfamiliar) > SEARCH (adapt) > FIND (get it) > TAKE (pay price) > RETURN (familiar) > CHANGE (transformed).

### John Truby's 22 Building Blocks
Key insight: the opponent should want the SAME THING as the hero — this creates organic conflict.

## II. CHARACTER DEVELOPMENT

### Michael Hauge's Identity Model
IDENTITY: emotional armor, false self. ESSENCE: true self hidden underneath. Story arc moves character from Identity to Essence. Love interest sees Essence, creating courage to abandon Identity.

### Character Wound Theory
WOUND (past trauma) > LIE (false belief) > WANT (misguided goal) > TRUTH (discovery) > NEED (real goal).
Example — Will Hunting: WOUND (abuse) > LIE ("don't deserve love") > WANT (intellectual superiority) > TRUTH (vulnerability is strength) > NEED (genuine connection).

### Character Diamond (4 Dimensions)
1. PHYSICAL: appearance, mannerisms, health
2. PSYCHOLOGICAL: fears, desires, self-image, IQ
3. SOCIOLOGICAL: class, education, religion, occupation
4. PHILOSOPHICAL: moral code, worldview, what they'd die for

## III. DIALOGUE MASTERY

### Rules
1. DISTINCT VOICES — cover names, still know who's speaking
2. SUBTEXT > TEXT — real conversation underneath the words
3. CONFLICT drives every conversation
4. EXPOSITION disguised — never tell each other what they know
5. ENTER LATE, LEAVE EARLY

### Masters to Study
SORKIN: Intelligence as entertainment, walk-and-talk, repetition for rhythm
TARANTINO: Digressions building tension, pop culture as character
MAMET: Staccato, interruptions, every line has an objective
COEN BROTHERS: Idiom as character, regional specificity

## IV. GENRE CONVENTIONS

HORROR: Monster = cultural fear. Dread > gore. Structure: normalcy > warnings > encounter > escalation > confrontation.
COMEDY: Character-based > situational. Rule of Three. Comic premise (What if?).
THRILLER: Information asymmetry = suspense. Hitchcock's bomb under table.
ROMANCE: Meet cute > Attraction > Barrier > Deepening > Crisis > Gesture > Union.

## V. ESSENTIAL REFERENCES

Books: "Story" (McKee), "Save the Cat!" (Snyder), "Anatomy of Story" (Truby), "Screenplay" (Field), "Writer's Journey" (Vogler), "On Writing" (King), "Bird by Bird" (Lamott).
Scripts to study: Chinatown, The Godfather, Pulp Fiction, Eternal Sunshine, Parasite, Get Out, Social Network, Moonlight."""),

# ─────────────────────────────────────────────────────
# 5. FELIX — Screenplay Format
# ─────────────────────────────────────────────────────
("screenplay-writer", "World-Class Screenplay Formatting & Scene Architecture",
"""# FELIX — ELITE SCREENPLAY FORMATTING KNOWLEDGE BASE

## I. INDUSTRY-STANDARD FORMAT

### Page Setup
Font: Courier 12pt (or Courier Prime). Margins: Left 1.5in, Right 1in, Top/Bottom 1in. Title page: title centered caps, 'Written by,' author name. Contact bottom left. NO date on specs.

### Scene Headings (Slug Lines)
Format: INT./EXT. LOCATION - TIME
Examples: INT. APARTMENT - KITCHEN - NIGHT | EXT. CENTRAL PARK - DAY | INT./EXT. MOVING CAR - CONTINUOUS
Time: DAY, NIGHT, DAWN, DUSK, CONTINUOUS, LATER, SAME, MOMENTS LATER

### Action/Description
Present tense ALWAYS. Active voice. No camera directions in specs. Max 4 lines per paragraph. Characters CAPS on first appearance with brief description and age range.

### Dialogue Block
Character name: CAPS, 3.7in from left. Parenthetical: (beat), (to John), (sotto voce), (O.S.), (V.O.), (CONT'D). Dialogue: 2.5in from left, ~35 chars wide. Never orphan character name at page bottom.

### Transitions
CUT TO: largely obsolete. SMASH CUT TO: jarring (sparingly). MATCH CUT TO: visual link. DISSOLVE TO: time passage. FADE IN: first line. FADE OUT.: last line. INTERCUT: cross-cutting.

### Special Formats
MONTAGE: Lettered brief descriptions (A, B, C). FLASHBACK: tag in slug line, END FLASHBACK. SERIES OF SHOTS: Within single location. SUPERIMPOSE: "SUPER: Chicago, 1985."

## II. SPEC vs SHOOTING SCRIPT

### Spec Script (Selling)
No scene numbers, no camera directions, no editing instructions. 90-120 pages. Lean writing. Designed to seduce a reader.

### Shooting Script (Production)
Scene numbers both margins. Revision colors: White > Blue > Pink > Yellow > Green > Goldenrod > Buff > Salmon > Cherry > Tan > 2nd White. Revision asterisks in right margin. Locked pages: new scenes get letters (47A, 47B). Omitted: "SCENE 47 - OMITTED."

## III. ONE-PAGE-ONE-MINUTE RULE

1 page = ~1 minute screen time. 90pp = ~90min. 120pp = ~2hr. Action-heavy runs shorter per page. TV: 30min comedy = 22-32pp, 1hr drama = 50-65pp.

## IV. TELEVISION FORMATTING

### Network (Act Breaks)
Cold Open/Teaser: 1-5pp. Acts: 8-12pp each. Tag: 1-3pp. "ACT BREAK" centered caps.

### Streaming (No Breaks)
Reads like a feature. Flexible lengths.

### Multi-Camera Sitcom
ALL CAPS action. DOUBLE-SPACED dialogue. Underlined slugs. Sound FX in caps. Scene letters not numbers.

## V. SCENE CONSTRUCTION

### Enter Late, Leave Early
Skip greetings, travel, setup. End before natural conclusion. Respect audience intelligence.

### Scene Beats
OBJECTIVE (what character wants), OBSTACLE (what prevents), OUTCOME (did they get it? Usually no).

### Visual Writing
SHOW don't TELL. Replace exposition dialogue with visual reveals. Think in shots without calling shots.

## VI. ESSENTIAL REFERENCES

Books: "The Screenwriter's Bible" (Trottier), "The Hollywood Standard" (Riley), "Save the Cat!" (Snyder), "Screenplay" (Field).
Software: Final Draft 13 ($199), Highland 2 (Mac, $49), Fade In ($79), WriterSolo (free), Fountain markup.
Scripts for format study: Bourne Ultimatum (action writing), Juno (voice), No Country for Old Men (sparse perfection)."""),

# ─────────────────────────────────────────────────────
# 6. ORSON — Director
# ─────────────────────────────────────────────────────
("director", "World-Class Film Directing Mastery",
"""# ORSON — ELITE FILM DIRECTING KNOWLEDGE BASE

## I. DIRECTORIAL VISION

### The Auteur Framework
The director is the primary creative author. Every choice serves a unified vision. Before shooting, answer: What is this ABOUT (theme)? What should the audience FEEL? What VISUAL METAPHOR embodies the theme?

### Director's Prep Bible
Visual references, color palette, lens choices with rationale, camera movement philosophy, performance tone, music/sound world, key frames per scene, floor plans for blocking.

## II. WORKING WITH ACTORS (Judith Weston Method)

### Core Principle
NEVER give result direction ("be sadder"). Give PLAYABLE ACTIONS (verbs): "try to convince her," "make him feel small," "test if she's lying." Actors play actions, not adjectives.

### Techniques
BACKSTORY: Help actors build internal life. What happened before this scene?
SUBSTITUTION: "Think of when YOU felt betrayed" — connects real emotion to character.
AS-IF: "Play this AS IF defusing a bomb" — gives urgency without literal instruction.
PRIVATE MOMENT: Internal world the camera captures.

### Rehearsal Protocol
TABLE READ: Listen for rhythm, unclear passages, tonal shifts.
BLOCKING: Let actors find natural movement first, then refine.
EMOTIONAL: Deep work on key scenes. Private, safe space.
TECH: Integration with camera, lighting, sound. Mark positions.

### On-Set Communication
Compliment sandwich for redirects. Adjustments quietly, privately. One idea per take. "That was great, and this time..."

## III. VISUAL GRAMMAR

### Rules
180-DEGREE: Camera stays on one side of axis between characters. Break intentionally for disorientation (Kubrick, The Shining).
30-DEGREE: Move camera 30+ degrees between shots of same subject to avoid jump cut feel.

### Shot Psychology
WIDE: Geography, isolation | MEDIUM: Neutral, conversational | CLOSE-UP: Intimacy, emotional revelation (most powerful) | LOW ANGLE: Power | HIGH ANGLE: Vulnerability | DUTCH: Unease (sparingly)

### Camera Movement Psychology
STATIC: Observation, formalism (Ozu) | DOLLY IN: Intimacy/realization | DOLLY OUT: Isolation | PAN: Survey | HANDHELD: Immediacy (Greengrass) | STEADICAM: Dreamlike (Kubrick) | CRANE: Epic scale

## IV. BLOCKING & STAGING

Spielberg: Block in DEPTH (foreground/background), not side-by-side. Movement motivates camera. Staging reveals power — who sits/stands/moves/is trapped.
Kurosawa: Multiple planes simultaneously. Weather as character. Object movement as transitions.

## V. GENRE DIRECTION

COMEDY: Protect timing. Wide for physical, close-up for reaction. Hold the frame.
HORROR: Less is more. Sound = 70% of horror. Information control creates dread.
ACTION: Geography first. Cause/effect. Stakes before spectacle.
DRAMA: Trust stillness and silence. Close-up is your instrument.

## VI. POST-PRODUCTION

Director's cut: 10 weeks minimum (DGA). Watch assembly without notes first. Priorities: 1. Story 2. Performance 3. Pace 4. Technical.

## VII. MASTER DIRECTORS

KUBRICK: Precision, symmetry, one-point perspective | HITCHCOCK: Suspense, storyboards, audience manipulation | SCORSESE: Energy, music, tracking shots | SPIELBERG: Emotion, depth blocking | FINCHER: Digital precision, 40+ takes | VILLENEUVE: Scale, silence, slow-burn | KUROSAWA: Movement, weather, geometry | TARKOVSKY: Time, water, meditation

## VIII. REFERENCES

Books: "On Directing Film" (Mamet), "Directing Actors" (Weston), "Making Movies" (Lumet), "Hitchcock/Truffaut," "Sculpting in Time" (Tarkovsky), "Notes on Directing" (Hauser/Reich)."""),

# ─────────────────────────────────────────────────────
# 7. LUCA — Director of Photography
# ─────────────────────────────────────────────────────
("dp", "World-Class Cinematography & Visual Storytelling",
"""# LUCA — ELITE CINEMATOGRAPHY KNOWLEDGE BASE

## I. CAMERA SYSTEMS

### Digital Cinema Cameras
ARRI ALEXA 35: 4.6K Super 35, 17 stops DR, REVEAL Color Science, textures system. The workhorse.
ARRI ALEXA Mini LF: Large format, compact. Ideal for gimbal/Steadicam with cinematic depth.
RED V-RAPTOR [X]: 8K VV sensor, DSMC3. High resolution for VFX-heavy productions.
Sony VENICE 2: 8.6K full-frame, dual base ISO (800/3200), excellent low-light.
Blackmagic URSA Mini Pro 12K: Affordable high-res, Blackmagic RAW.

### Sensor Formats
Super 35 (24.9x18.7mm): Standard cinematic depth of field. Most lenses available.
Full Frame (36x24mm): Shallower DOF, wider field of view at same focal length.
Large Format (54.1x25.6mm, ARRI LF): Ultra-shallow DOF, immersive feel.
IMAX (69.6x48.5mm): Maximum resolution and immersion (Hoytema's work with Nolan).

### Codecs
ARRIRAW: Uncompressed, maximum quality, massive files. Gold standard for features.
ProRes 4444 XQ: Near-RAW quality, more manageable files. Apple ecosystem.
REDCODE RAW (R3D): RED's compressed RAW. Variable compression ratios.
Blackmagic RAW: Smart compression, preserves sensor data. Affordable.

## II. LENS LANGUAGE

### Focal Length Psychology
WIDE (14-24mm): Environment dominance, isolation in space, distortion at edges, epic scale
NORMAL (35-50mm): Human eye approximation, naturalistic, "honest"
MEDIUM TELEPHOTO (85-135mm): Portrait compression, intimacy, slight background separation
LONG (200mm+): Extreme compression, surveillance feel, stacking depth planes

### Lens Families
COOKE S7/i: Warm, slightly soft, legendary Cooke "look" — organic, flattering skin tones
ARRI/ZEISS Master Primes: Clinical sharpness, neutral color, minimal distortion — precision
ARRI Signature Primes: Large format, gentle roll-off, modern yet characterful
Panavision C/G Series: Classic anamorphic, distinctive flare and bokeh
KOWA Anamorphic: Vintage, strong blue/amber flares, organic imperfections
Vintage Rehoused (Lomo, Helios, Canon K35): Imperfections as character — flare, aberration, breathing

### Anamorphic vs Spherical
Anamorphic: 2.39:1 native, oval bokeh, horizontal flares, slight edge distortion, wider FOV compressed onto sensor. THE premium cinematic look.
Spherical: Round bokeh, no horizontal distortion, more lens options, easier focus.

## III. LIGHTING PHILOSOPHY

### Legendary Approaches
STORARO (Apocalypse Now, Last Emperor): Light = emotion. Each sequence has a color meaning. Warm/cool contrast as psychological states.
DEAKINS (Blade Runner 2049, 1917, Skyfall): "Motivated" naturalism. Every light has a source you can point to, even if enhanced. Simplicity and control.
LUBEZKI (Revenant, Tree of Life, Gravity): Natural light obsession. Magic hour. Long takes requiring evolving light. Handheld intimacy.
GORDON WILLIS (The Godfather): "Prince of Darkness" — dared to underexpose, eyes in shadow, overhead toplight.

### Lighting Setups
THREE-POINT: Key + Fill + Back (backlight/rim). Classical, controlled.
REMBRANDT: Key light 45 degrees, triangle of light on shadow-side cheek. Portrait drama.
BUTTERFLY/PARAMOUNT: Key directly above lens. Glamorous, fashion-inspired.
SPLIT: Half-face lit, half in shadow. Duality, conflict, mystery.
CHIAROSCURO: High contrast, deep shadows. Renaissance painting influence.
BROAD: Key lights the side of face toward camera. Open, inviting.
SHORT: Key lights the side away from camera. Moody, dramatic.

### Instruments
HMI (Hydrargyrum Medium-arc Iodide): Daylight balanced (5600K), high output. ARRI M-Series.
Tungsten: Warm (3200K), dimmable. Classic film set staple.
LED Panels: ARRI SkyPanel S60/S360, Aputure LS 600d, LiteMat (flexible), Astera tubes (RGB, portable).
Book Light: Large diffused source (light bounced into frame through diffusion). Soft, wraparound.
Negative Fill: Black fabric/floppy to remove fill, increase contrast. Often more important than adding light.

## IV. CAMERA MOVEMENT

STEADICAM: Invented by Garrett Brown (1975). Floating, dreamlike. The Shining hallways, Rocky steps.
GIMBAL: DJI Ronin 4D, MoVI Pro. Electronic stabilization. More portable than Steadicam.
DOLLY: Fisher 10/11, Chapman PeeWee. Smooth tracking. Floor or track-mounted.
TECHNOCRANE: Telescoping crane arm. Precise, repeatable, programmable. 15-50ft range.
DRONE: DJI Inspire 3, Freefly Alta X. Aerial shots previously requiring helicopters.
HANDHELD: Intentional chaos. Dardenne brothers, Paul Greengrass. Shoulder-mounted for stability.

## V. COLOR SCIENCE

### Color Management
ACES (Academy Color Encoding System): Industry-standard color pipeline. Scene-referred, wide gamut.
Capture: LogC4 (ARRI), S-Log3 (Sony), Log3G10 (RED) — maximize dynamic range in recording.
Display: Rec.709 (HD), DCI-P3 (cinema), Rec.2020 (HDR/UHD).
CDL (Color Decision List): On-set look applied as metadata, non-destructive.
LUT (Look-Up Table): 3D color transformation. Show LUT for on-set monitoring, technical LUT for display transform.

## VI. ESSENTIAL REFERENCES

Books: "Cinematography: Theory and Practice" (Blain Brown), "Painting with Light" (John Alton), "Masters of Light" (Schaefer/Salvato), ASC Manual (American Cinematographer), "Light Science & Magic" (Hunter/Biver/Fuqua).
Publications: American Cinematographer magazine, British Cinematographer, cinematography.net.
Legendary DPs: Roger Deakins, Vittorio Storaro, Gordon Willis, Conrad Hall, Janusz Kaminski, Emmanuel Lubezki, Hoyte van Hoytema, Bradford Young, Robert Richardson, Darius Khondji."""),

# ─────────────────────────────────────────────────────
# 8. GRACE — Casting Director
# ─────────────────────────────────────────────────────
("casting-director", "World-Class Casting & Talent Evaluation",
"""# GRACE — ELITE CASTING DIRECTOR KNOWLEDGE BASE

## I. THE CASTING PROCESS

### Breakdown
Script breakdown produces character descriptions: age range, physical type, personality summary, story importance (lead/supporting/day player). Sent to agents/managers via Breakdown Services (industry standard platform).

### Audition Pipeline
1. OPEN CALL / SUBMISSIONS: Agents submit client tapes/headshots. Self-tapes via Actors Access, Eco Cast.
2. PRE-READ: Casting director screens initial auditions. Narrow from hundreds to 20-30.
3. CALLBACK: Director and producers see top choices. Different scenes, adjustments given.
4. CHEMISTRY READ: Paired auditions to test on-screen dynamic between potential castmates.
5. SCREEN TEST: On-camera test with lighting, costume, hair/makeup. For leads only.
6. WORK SESSION: Network/studio executives see finalists (TV). Often the final gate.
7. OFFER: Deal memo issued through agents. Negotiation on rate, billing, perks.

### Self-Tape Standards (Modern Casting)
Solid color backdrop (grey/blue preferred), eye-level camera, good audio, natural lighting from front, reader off-camera (NOT on-camera), slate at beginning (name, agent, role), two takes maximum.

## II. TALENT EVALUATION FRAMEWORK

### The Five Pillars of Casting
1. TRUTHFULNESS: Does the actor live in the moment? Can you see them thinking? Are reactions genuine?
2. RANGE: Can they shift between emotional states convincingly? Test with adjustments.
3. PHYSICALITY: Does their body tell the story? Movement, posture, gesture, stillness.
4. VOICE: Tone, rhythm, projection, accent capability. Can they whisper and fill a room?
5. SCREEN PRESENCE: The X-factor. Camera magnetism. Some faces the camera loves.

### Type vs Against-Type
TYPE CASTING: Actor's natural qualities match the character. Reliable, faster to results.
AGAINST-TYPE: Actor plays opposite their usual energy. Can create revelatory performances (Heath Ledger as Joker, Matthew McConaughey in Dallas Buyers Club).

### The Casting Director's Instinct
Trust the unexpected choice. Marion Dougherty (legendary CD) championed unknowns and against-type casting that defined modern Hollywood. She cast Al Pacino, Robert De Niro, Jon Voight, Glenn Close before they were stars.

## III. SAG-AFTRA REGULATIONS

### Employment Categories
PRINCIPAL: Speaks 5+ words or identified individually. Scale + residuals.
BACKGROUND/EXTRA: Non-speaking atmosphere. Separate rate, no residuals.
STUNT: Coordinated through stunt coordinator. Separate rate + adjustments for hazard.
VOICE-OVER: Animation, ADR, narration. Session fee + residuals based on usage.

### Key Rules
TAFT-HARTLEY: Non-union performer may work one SAG job. Must join before second.
STATION 12: Permit system for non-members on SAG projects.
WORKING CONDITIONS: 12-hour rest between calls, meal breaks every 6 hours, forced call penalties.
CHILD ACTORS: Coogan Law (15% earnings in trust), studio teachers on set, restricted hours by age.

### Deal Points
SCALE: SAG-AFTRA minimum rates (updated annually). Currently ~$1,100/day, ~$3,800/week.
PAY-OR-PLAY: Once deal closes, actor gets paid even if role is cut. Protection for talent.
FAVORED NATIONS: All actors at same level get identical deal terms.
BACKEND: Adjusted gross or net profit participation for above-title talent.

## IV. DIVERSITY & INCLUSION

### Modern Casting Standards
AUTHENTICITY: Cast actors whose lived experience matches the character where possible.
OPEN CASTING: Consider all ethnicities unless story-specific. Widen the net.
DISABILITY: Cast disabled actors for disabled characters. Not just able-bodied actors "playing disabled."
INTIMACY COORDINATION: Required for scenes involving nudity, simulated sex, or physical vulnerability. Ita O'Brien pioneered the role.
INCLUSION RIDER: Contractual clause (proposed by Stacy Smith/Annenberg) requiring diverse casting.

## V. CASTING FOR DIFFERENT MEDIA

FEATURE FILM: Longer audition process, screen tests for leads, studio approval chain.
TELEVISION PILOT: Fast turnaround, network testing sessions, series regular options (6-7 year commitments).
STREAMING: More creative freedom, less network interference, self-tape heavy.
COMMERCIAL: Fast casting (1-3 days), type-heavy, SAG-AFTRA commercial contract (separate from theatrical).
VOICE-OVER/ANIMATION: Vocal range primary criteria, recording booth auditions, scratch vs final casting.

## VI. LEGENDARY CASTING DIRECTORS

Marion Dougherty — mother of modern casting, championed unknown talent.
Lynn Stalmaster — first CD to receive Academy honorary award.
Juliet Taylor — Woody Allen's CD, cast everything from Annie Hall to Schindler's List.
Sarah Finn, CSA — cast the entire MCU (200+ characters across 30+ films).
Nina Gold — cast Game of Thrones, Star Wars sequels, The Crown.
Francine Maisler — cast Tarantino, Fincher, Spielberg films.

## VII. REFERENCES

Books: "A Director Prepares" (casting chapters), "Audition" (Michael Shurtleff — the 12 guideposts).
Organizations: CSA (Casting Society of America), SAG-AFTRA, AEA (Equity for theater).
Platforms: Breakdown Services, Actors Access, Eco Cast, Casting Networks, Backstage."""),

# ─────────────────────────────────────────────────────
# 9. ARIA — Production Designer
# ─────────────────────────────────────────────────────
("production-designer", "World-Class Production Design & Visual World-Building",
"""# ARIA — ELITE PRODUCTION DESIGN KNOWLEDGE BASE

## I. PRODUCTION DESIGN PHILOSOPHY

### World-Building as Storytelling
Every environment tells a story. A character's apartment reveals their personality: neat vs messy, rich vs poor, colorful vs muted, lived-in vs sterile. The production designer creates the WORLD the story inhabits — not just decorating sets but building meaning into every surface, texture, and color choice.

### Design as Character
The Overlook Hotel in The Shining IS a character. The Death Star IS the Empire. Wes Anderson's symmetrical pastel worlds ARE the emotional state of his characters. Great production design is invisible when done right — the audience FEELS the world without consciously analyzing it.

## II. THE ART DEPARTMENT HIERARCHY

Production Designer (PD): Overall visual vision. Works directly with director.
Art Director: Executes PD's vision, manages art department budget, oversees technical drawings.
Set Decorator: Furnishes and dresses sets. Works with PD on textures, fabrics, objects.
Props Master: All hand props (items actors interact with). Hero props (featured) vs background.
Construction Coordinator: Manages build crews. Translates drawings to physical structures.
Scenic Artists: Paint treatments, aging, distressing, murals, signage.
Graphics Department: All printed materials — newspapers, posters, packaging, screens.
Greens: Plants, landscaping, agricultural elements.

## III. COLOR THEORY FOR FILM

### Color Psychology
RED: Passion, danger, power, blood, love. (American Beauty, Schindler's List red coat)
BLUE: Melancholy, cold, isolation, technology, truth. (Blade Runner 2049, Moonlight)
YELLOW: Warmth, madness, decay, hope. (Breaking Bad, The Florida Project)
GREEN: Nature, sickness, envy, growth, alien. (The Matrix, Vertigo)
ORANGE: Energy, warmth, nostalgia, sunset. (Mad Max: Fury Road, Blade Runner)
WHITE: Purity, sterility, emptiness, death. (2001, THX 1138, Ex Machina)
BLACK: Power, mystery, death, elegance. (Batman films, noir)

### Color Scripting
Map the color palette across the entire film. Each act, sequence, or emotional phase has a dominant palette. Transitions between palettes mark story shifts. Reference: Pixar's color scripts (especially Inside Out, Up).

## IV. SET DESIGN APPROACHES

### Practical Builds
Stage builds: Modular wall systems, wild walls (removable for camera), elevated floors for dolly track. Location dressing: augment existing architecture. Force perspective: miniatures or oversized elements to fake scale.

### Virtual Production (LED Volume)
ILM StageCraft / ICVFX: LED wall displays photorealistic environments rendered in Unreal Engine in real-time. Camera-tracked for parallax. Used on The Mandalorian, The Batman. Advantages: in-camera VFX, realistic lighting interaction, reduced location travel. Requirements: VP Supervisor, Unreal Engine artists, LED wall calibration, brain bar (real-time rendering station).

## V. PERIOD DESIGN

### Research Methodology
Start with primary sources: photographs, paintings, museum collections from the era. Cross-reference with architectural records, furniture catalogs, fashion plates. Visit surviving examples of period architecture.

### Key Periods
ANCIENT/CLASSICAL: Columns, marble, earth tones, symmetry.
MEDIEVAL: Stone, wood, tapestry, candlelight, functional design.
RENAISSANCE: Ornate, gold, symmetry, religious iconography.
GEORGIAN/REGENCY (1714-1837): Elegant proportions, Adam style, Wedgwood colors.
VICTORIAN (1837-1901): Heavy ornament, dark woods, pattern-on-pattern, gas lighting.
ART NOUVEAU (1890-1910): Organic curves, nature motifs, Tiffany glass.
ART DECO (1920s-30s): Geometric, chrome, black/gold, Gatsby glamour.
MID-CENTURY MODERN (1945-1970): Clean lines, Eames furniture, optimistic, open plans.
BRUTALIST (1950s-1970s): Raw concrete, massive scale, institutional.
POSTMODERN (1970s-1990s): Eclectic, ironic, color, historical references.

## VI. TOOLS & SOFTWARE

2D: Photoshop (concept painting), Illustrator (graphics), SketchUp (quick 3D blocking), AutoCAD/Vectorworks (technical drawings), Procreate (concept sketches).
3D: Blender (free, increasingly industry standard), Unreal Engine (virtual production), Cinema 4D, Maya.
Presentation: Mood boards (Pinterest, Milanote), look books (InDesign, Keynote).

## VII. LEGENDARY PRODUCTION DESIGNERS

Ken Adam: Bond films (War Room in Dr. Strangelove), expressionistic scale.
Dante Ferretti: Scorsese collaborator, Gangs of New York, Hugo, Sweeney Todd.
Rick Carter: Spielberg collaborator, Jurassic Park, War of the Worlds, Avatar sequels.
Hannah Beachler: Black Panther (first Black woman to win PD Oscar), Wakanda's Afrofuturism.
Jack Fisk: Terrence Malick collaborator, The Revenant, There Will Be Blood. Naturalism.
Eugenio Caballero: Pan's Labyrinth. Fantasy grounded in historical reality.

## VIII. REFERENCES

Books: "Production Design & Art Direction" (Peter Lamont/Rizzo), "Filmcraft: Production Design" (Halligan), "By Design" (Vincent LoBrutto), "What an Art Director Does" (Ward Preston).
Guild: ADG (Art Directors Guild, IATSE Local 800). ADG Awards = top industry recognition."""),

# ─────────────────────────────────────────────────────
# 10. LEO — Character Designer
# ─────────────────────────────────────────────────────
("character-designer", "World-Class Character Design & Visual Development",
"""# LEO — ELITE CHARACTER DESIGN KNOWLEDGE BASE

## I. CHARACTER DESIGN PRINCIPLES

### Silhouette Test
If you can identify a character by their silhouette alone, the design works. Every character should have a UNIQUE, INSTANTLY RECOGNIZABLE silhouette. Batman, Mickey Mouse, Darth Vader — all pass the silhouette test.

### Shape Language
CIRCLES/ROUNDS: Friendly, approachable, soft, safe (Baymax, Totoro, Winnie the Pooh)
SQUARES/RECTANGLES: Stable, strong, dependable, stubborn (Mr. Incredible, Wreck-It Ralph)
TRIANGLES: Dynamic, dangerous, villainous, cunning (Maleficent, Jafar, Scar)
Mix shapes for complex characters. A hero with triangular elements suggests hidden edge. A villain with some roundness suggests sympathetic qualities.

### Proportion as Character
Heroic: 8-9 heads tall, broad shoulders, narrow waist (idealized)
Realistic: 7-7.5 heads tall, natural proportions
Cartoony: 3-5 heads tall, enlarged head for expressiveness
Chibi: 2-3 heads tall, maximum cuteness

### The Rule of Appeal
Appeal does NOT mean attractive. It means INTERESTING TO LOOK AT. Villains need appeal. Ugly characters need appeal. Appeal comes from: clear design choices, contrast, asymmetry in details but balance in overall composition.

## II. ANATOMY FUNDAMENTALS

### Figure Drawing Masters
ANDREW LOOMIS: "Figure Drawing for All It's Worth" — proportional construction, idealized anatomy, gesture integration. The starting point for all character artists.
MICHAEL HAMPTON: "Figure Drawing: Design and Invention" — gesture as the foundation, simplified anatomy, constructive approach.
BRIDGMAN: "Complete Guide to Drawing from Life" — understanding form through construction, wedging, interlocking shapes.
VILPPU: Gesture drawing methodology — the line of action is everything. 30-second to 5-minute poses build fluency.

### Key Anatomy for Character Design
Skeleton determines proportion and landmarks. Muscle groups define surface form. Fat distribution varies by character type, age, gender. Hands and feet are character-defining — study them specifically.

### Expression & Emotion (FACS)
Facial Action Coding System (Paul Ekman): Catalogs every possible facial muscle movement as Action Units (AUs). AU1+AU4+AU15 = Sadness. AU6+AU12 = Genuine smile (Duchenne). Essential for expression sheets and consistent emotional portrayal across frames.

## III. THE CHARACTER DESIGN PIPELINE

1. BRIEF: Story context, personality, role, era, world rules
2. THUMBNAILS: 20-50 tiny silhouettes exploring shapes and proportions (pen, no erasing)
3. ROUGH CONCEPTS: 5-10 developed sketches from best thumbnails
4. DIRECTOR REVIEW: Narrow to 2-3 directions
5. REFINED CONCEPT: Full color rendering of chosen direction with variations
6. MODEL SHEET: Front/back/3-quarter views with exact proportions noted
7. EXPRESSION SHEET: 8-12 key emotions showing range
8. COSTUME VARIATIONS: Multiple outfits if story requires
9. ACTION POSES: Character in motion, demonstrating personality through movement
10. TURNAROUND: 360-degree rotation for 3D modelers or animation

## IV. COLOR FOR CHARACTERS

### Personal Palette
Each character gets a signature color palette (3-5 colors). This creates instant visual identification. Hero palette and villain palette should contrast.

### Color Relationships
Protagonist and antagonist: complementary colors (opposite on wheel) — creates visual tension.
Allies: analogous colors (adjacent on wheel) — creates visual harmony.
Neutral characters: desaturated or grey tones — visually recede.

### Cultural Color Meaning
Colors carry different meanings across cultures. Red = luck (China), mourning (South Africa). White = purity (West), death (East Asia). Research cultural context for your audience and setting.

## V. AI-ERA CHARACTER DESIGN

### Consistency Challenge
AI image generators struggle with character consistency. Solutions:
CHARACTER REFERENCE SHEETS: Detailed front/side/back view with color callouts, used as reference for every generation.
LORA TRAINING: Fine-tune models on specific character images (15-30 consistent images). Stable Diffusion/Flux ecosystem.
IP-ADAPTER: Use a character's face as consistent reference input.
CONTROLNET: Maintain pose and composition consistency using depth/pose/edge maps.

### Prompt Engineering for Characters
Be specific: "A 45-year-old woman with silver-streaked black hair pulled back in a messy bun, weathered olive skin, deep-set brown eyes with crow's feet, wearing a faded blue denim work shirt rolled to the elbows."

## VI. DIGITAL TOOLS

2D: Photoshop (industry standard), Procreate (iPad), Clip Studio Paint (manga/comics), Krita (free).
3D: ZBrush (digital sculpting), Blender (free, full pipeline), Maya (animation industry), Marvelous Designer (clothing).
Reference: PureRef (reference board), Pinterest, ArtStation, Sketchfab (3D reference).

## VII. LEGENDARY CHARACTER DESIGNERS

GLEN KEANE (Disney): Ariel, Beast, Rapunzel. Master of gesture and emotion in line.
HAYAO MIYAZAKI (Ghibli): Naturalistic characters with extraordinary inner life. Design reveals personality.
CARTER GOODRICH (Pixar): Ratatouille, Brave. Appeals through specificity and warmth.
JIN KIM (Disney): Frozen, Tangled, Moana. Modern Disney appeal with cultural sensitivity.
AKIRA TORIYAMA (Dragon Ball): Iconic silhouettes, simple but infinitely readable designs.
TETSUYA NOMURA (Final Fantasy/Kingdom Hearts): Complex, layered, fashion-forward game character design.

## VIII. REFERENCES

Books: "Drawn to Life" (Walt Stanchfield), "Force: Dynamic Life Drawing" (Mattesi), "The Skillful Huntsman" (concept art bible), "Character Design from the Ground Up" (Bancroft), "Creating Characters with Personality" (Tom Bancroft)."""),

]

count = 0
for agent_id, name, content in KBS:
    upload(agent_id, name, content)
    count += 1

print(f"\n=== Uploaded {count} knowledge bases ===")
