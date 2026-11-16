---
generated_on: 2026-11-16
refresh_by: 2027-02-16
status: Proposed — owner approval pending
source: playbook/method.md §7, playbook/claims-guide.md, personas/personas.md, competitors/hooks-swipe.md, NutraEssence Studio formats (lib/prompts.js FORMATS, public/app.js, docs/STATUS.md, read 2026-11-16)
---
# Creator input: who should be on screen

## 1. Faces
- **Women about 45–58, age-matched to her** (method §7: show women her own age). A 49-year-old saying her age is one of
  MDhair's longest women's hooks (70 days, Verified). Ordinary, warm, a little tired; not glossy. Mix of ethnicities
  across the round (*Inferred*; we have no buyer data on this).
- **Hair that tells the story without a close-up:** a ponytail that looks thin at normal distance, a clip that slips, a
  hair tie that wraps four times, a wide part in daylight at arm's length. **Never** a zoomed scalp or bald-spot shot,
  never a before/after of hair or body (claims guide).
- **No body cues for weight loss:** no scale, no loose jeans, no tape measure, no "before" photo.

## 2. Voices (which kind of person explains)
| Role | Use it for | Rules |
|---|---|---|
| **The plain explainer**: a woman her age who "looked into it" (friend, sister, the woman herself) | the mechanism, in two or three sentences | no white coat, no "Dr.", no "specialist" or "nurse" label, no implied credentials (research §7.5: competitors use fake or hype doctors; that's our contrast) |
| **The woman herself** (talking to her phone, UGC) | the pain, the receipt of failed fixes | she tells the *problem*. She never claims the product worked for her (no GLP-1 testimonials exist) |
| **A narrator** (warm, 50s female voice) | animation and song | brand voice, can state label facts and the guarantee |
| **A real expert** | not in round 1 | only if a real, disclosed person agrees (Wellbel uses a named MD partner, Verified). Open loop |

Tone: calm, slower cuts (3–5 s per shot), big readable captions, clear over clever. "Permission" openers on cold traffic
beat loud fear (method §7).

## 3. AI people: what is allowed (proposed policy)
The Studio generates people with AI. Proposed rules:
1. **Disclose** every AI-generated person: an on-screen "AI-generated" or "Dramatization, AI-generated" label, plus
   Meta's AI-info label when uploading (claims guide: some US states now require disclosure).
2. **No results from an AI person.** She can tell a problem story and explain what she learned. She never says it worked,
   never shows "after" hair, never gives a timeline of her own results.
3. **First-person pain lines adapted from Reddit** are written lines for a dramatized character (VoC README rule), never
   shown as a review (no stars, no names styled as a reviewer, no "verified buyer").
4. **No AI "doctor" or "expert".**
5. Reuse the Studio's **Character Library** (avoid over-using one face; the library warns on overuse).

## 4. Studio format notes (read from the Studio repo, 2026-11-16)
- Live formats: `song` (animated song), `drama` (realistic drama), `adrama` (Pixar-style animated drama), `static`,
  `native`. **UGC is shown as "soon"** in this Studio build (`docs/STATUS.md`, `public/app.js`), although a
  `ugc-video-ads` skill exists. If UGC is not live at the office yet, the UGC brief can run as a one-character
  `drama` (she talks to her phone). (Verified in the repo; whether the office PC has a newer build is unknown.)
- Caption styles: 1a Pop, 1b Box, 1c Karaoke. Drama/adrama: alternate first-dialogue clips (max 6 s), cutdowns 60/90 s.
  Song: first-clip variations (visual only), lyric captions. Images: sizes 4:5, 1:1, 9:16.
- Studio rule: **video formats never use the Brand Brain** (claim words trip the generators' filters); image formats do.
  So video briefs must carry their own exact wording.

## Open questions
1. Approve the AI-people policy above (especially "no results from an AI person")? (owner)
2. Is UGC live in the office Studio? If not, run concept 1 as a one-character drama. (owner)
3. Can we get one real, disclosed woman (a customer or a real expert) for round 2? (owner)
