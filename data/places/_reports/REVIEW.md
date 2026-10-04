# Review: 30 enriched places

Reviewed 2026-10-04 (a Sunday). All 30 files plus `data/seed/places.json` (274 records) pass `python3 tools/validate_all.py` with 0 errors. `v1/` was rebuilt: 274 places, 30 of them enriched.

## Clean-up applied

- **Arabic:** filled all 40 missing `area.ar` / `statusNote.ar` values. Also corrected `medinet-habu` `area.ar`, which did not match the English.
- **Highlights:** every title/desc split is non-empty in both languages.
  - Rewrote 6 fragment descriptions, e.g. "including …" became a full sentence, and fixed the garbled St Catherine "Burning Bush" line.
  - Normalised case and final full stops across all three batches.
- **`effectiveFrom`:** removed for abu-simbel, philae, edfu and kom-ombo. Their only source is a news report of the decision, not the dated official decision itself.
- **`cashAccepted`:**
  - Kept only for GEM: `false`, because the official FAQ says tickets are online-only from 1 Dec 2025.
  - Removed elsewhere: 9 values set to `false` from 2023 sources, plus 17 `null`s. The reasons are recorded in `curationNote`.
- **Photos removed:**
  - `GEM_Khufus_Boat_front_2025.jpg`: the modern GEM hall dominates the frame.
  - `Muizz_Street_between_Al_Mousky_Street_and_Qalawun_complex_01.jpg`: the subject is a row of modern shopfronts. This was a cautious call.
  - All 89 photos were checked against their Commons titles, descriptions and categories, and the borderline ones were also checked visually. Every place still has 2 or more photos.
- **Source citations removed from user-facing text:**
  - 8 `statusNote`s
  - 9 exception labels ("per booking page", "announced by Luxor antiquities")
  - 4 `rule` strings
  - 2 `freeGroups` entries

## Places

Today's hours use the Sunday row. **Bold** marks a summer schedule that is in force today: the Luxor 2026 summer runs 24 Apr–30 Oct.

| id | conf. | foreign adult (EGP) | Egyptian adult (EGP) | Sun 4 Oct 2026 hours | online ticket | photos |
|---|---|---|---|---|---|---|
| abu-simbel | medium | 750 | 30 | 06:00–17:00 (last 16:00) | yes | 3 |
| abydos-temple-of-seti-i | medium | 260 | 10 | 07:00–17:00 (last 16:00) | yes | 3 |
| al-muizz-street | medium | 220 | 20 | 09:00–17:00 (last 16:00) | yes | 2 |
| cairo-citadel | medium | 550 | 60 | 08:00–17:00 (last 16:00) | yes | 3 |
| coptic-museum | high | 280 | 20 | 09:00–17:00 (last 16:00) | yes | 4 |
| dahshur | high | 200 | 10 | 08:00–17:00 (last 16:00) | yes | 3 |
| dendera-temple | medium | 300 | 20 | 07:00–17:00 (last 16:00) | yes | 3 |
| edfu-temple | medium | 550 | 40 | 06:00–17:00 (last 16:00) | yes | 3 |
| egyptian-museum | high | 550 | 30 | 09:00–17:00 (last 16:00) | yes | 3 |
| giza-pyramids | medium | 700 | 60 | 07:00–17:00 (last 16:00) | yes | 3 |
| graeco-roman-museum | medium | 400 | 40 | 09:00–17:00 (last 16:30) | yes | 3 |
| grand-egyptian-museum | high | 1,590 (USD 30 peg) | 200 | 09:00–18:00 (last 17:00) | yes | 2 |
| hanging-church | medium | free¹ | free¹ | 09:00–16:00 (last 15:00) | no | 2 |
| ibn-tulun-mosque | medium | free¹ | free¹ | 09:00–17:00 (last 16:00) | no | 3 |
| karnak | medium | 600 | 40 | **summer: 06:00–18:00**; std 06:00–17:00 (last 16:00) | yes | 3 |
| kom-el-shoqafa | medium | 200 | 30 | 09:00–17:00 (last 16:00) | yes | 3 |
| kom-ombo-temple | medium | 450 | 40 | 07:00–21:00 (last 20:00) | yes | 3 |
| luxor-museum | medium | 400 | 30 | **summer: 09:00–? (last 12:00) + 17:00–? (last 19:00)** ²; std 09:00–14:00 (last 13:00) + 17:00–21:00 (last 20:00) | yes | 3 |
| luxor-temple | medium | 500 | 40 | **summer: 07:00–21:00**; std 06:00–20:00 (last 19:00) | yes | 3 |
| medinet-habu | medium | 230 | 20 | **summer: 06:00–? (last 17:00)** ²; std 06:00–17:00 (last 16:00) | yes | 3 |
| museum-of-islamic-art | high | 340 | 20 | 09:00–17:00 (last 16:00) | yes | 3 |
| national-museum-of-egyptian-civilization | high | 550 | 90 | 09:00–17:00 (last 16:00) | yes | 3 |
| nubia-museum | medium | 400 | 30 | 09:00–17:00 (last 16:00) | yes | 3 |
| philae-temple | medium | 550 | 40 | 07:00–16:00 (last 15:00) | yes | 3 |
| qaitbay-citadel | high | 200 | 60 | **summer: 09:00–20:00 (last 19:00)** ²; std 09:00–18:00 (last 17:00) | yes | 2 |
| saint-catherines-monastery | low | — | — | 08:45–11:30 | no | 3 |
| saqqara | medium | 600 | 30 | 08:00–17:00 (last 16:00) | yes | 3 |
| sultan-hassan-mosque | high | 220 | free | 09:00–17:00 (last 16:00) | yes | 3 |
| temple-of-hatshepsut | medium | 440 | 40 | **summer: 06:00–18:00 (last 17:00)**; std 06:00–17:00 (last 16:00) | yes | 3 |
| valley-of-the-kings | high | 750 | 60 | **summer: 06:00–18:00 (last 17:00)**; std 06:00–17:00 (last 16:00) | yes | 3 |

¹ Inferred: no ticket is listed by any official source.
² The summer exception has no start/end dates, so it is assumed active today.

## Decisions needed (recommended answer in **bold**)

1. **GEM foreign price** (USD-pegged; EGP 1,590 is from April 2026 and is re-set monthly):
   **(a) Keep the EGP amount plus `usdAmount`. On 1 Nov 2026, update to USD 35 / Egyptian EGP 220.**
   (b) Store USD only, with the EGP amount null.
   (c) Hide the price until tickets.gem.eg can be read.
2. **Online surcharge at Abu Simbel.** The booking site charges 822, the portal 750.
   **(a) Show the portal price (750) and mention in `statusNote` that online costs more.**
   (b) Show 822.
   (c) Add schema fields for online price.
3. **Official sources disagree on last entry** (Graeco-Roman 16:30 vs 15:00; Karnak summer; MIA and Nubia Ramadan):
   **(a) Use the earlier time.**
   (b) Use the venue/portal page.
   (c) Use the booking platform.
4. **Medinet Habu foreign adult.** The portal says 230; the booking site, the 2024 MoTA list and 2026 guides say 220.
   (a) 230.
   **(b) 220.**
5. **Cairo Citadel summer opening** (09:00 appears only on the booking page):
   **(a) 08:00 all year.**
   (b) 09:00 in summer.
6. **Do live but undated official pages count as current sources?** (egymonuments.gov.eg / .com, e.g. Dendera roof and crypt fees, Philae panorama, parking)
   **(a) Yes, with `checkedAt`.**
   (b) No: require a dated 2025–26 source.
7. **Ramadan closing time missing** (Karnak, Luxor Temple, Valley of the Kings, Hatshepsut, Sultan Hassan):
   **(a) Show last entry only.**
   (b) Infer closing as last entry + 1 h, using MoTA's rule.
8. **Abydos closing at 17:00** (from the 2024 MoTA list plus the 1-hour rule):
   **(a) Keep it.**
   (b) Drop `close`.
9. **Hanging Church and Ibn Tulun shown as free** (inferred):
   **(a) Keep "free (no ticket listed)" and confirm by MoTA hotline 19654.**
   (b) Mark the price unknown.
10. **St Catherine hours**:
    **(a) masrawy, Apr 2026: Sat–Thu 08:45–11:30, Fri 10:45–11:30.**
    (b) The monastery's undated site: 09:00–11:30, closed Fri and Sun.
    (c) MoTA portal: Sunday closed.
11. **Narmer Palette** (Tahrir or GEM?):
    **(a) Leave it out until confirmed.**
    (b) List it at Tahrir.
12. **NMEC `tickets.platform`**:
    **(a) Keep `nmec`: its own flow and prices.**
    (b) Use `egymonuments`, which hosts the flow.
13. **Parking fees in `extras`** (Abu Simbel, Dendera, Kom Ombo and Saqqara have them; Giza and the Citadel don't):
    **(a) Keep where a live official page lists them, and omit at Giza, where private cars no longer enter.**
    (b) Remove all parking fees.
14. **Non-hours notes stored as `hours.exceptions`** (sound & light at Karnak/Qaitbay, Philae boats, Abu Simbel logistics):
    (a) Keep as they are.
    **(b) Move them to `visit.crowdNotes` and keep only real schedule changes as exceptions.**
15. **Split-session days** (Luxor Museum; Nubia Thu/Fri evenings):
    **(a) Keep two `dayHours` entries per day and document that the app must handle them.**
    (b) Add `sessions[]` to the schema.
16. **`prices.extras` has no audience/group fields:**
    (a) Keep encoding them in labels.
    **(b) Add optional `audience` and `group` to extras (schema v1.1).**
17. **Wikidata problems** (Hatshepsut duplicate Q373909/Q660692; Nubia P856 now points to a gambling site; Dahshur city):
    **(a) Fix them on Wikidata and override locally meanwhile.**
    (b) Override locally only.
18. **Unsourced general accessibility notes** (Kom el-Shoqafa stairs):
    **(a) Keep them, worded as general advice.**
    (b) Remove them.
19. **Ported licence strings** ("CC BY 3.0 pl"):
    **(a) Keep the Commons string exactly as it is.**
    (b) Normalise to the generic licence name.

## Scheduled rechecks (no decision needed)

- **22 Oct 2026:** Abu Simbel alignment-day gate times. The record uses 2025 times.
- **After 30 Oct 2026:** Luxor winter 2026–27 schedule and Qaitbay winter hours.
- **1 Nov 2026:** GEM price change (see decision 1).
- **Nov/Dec 2026:** St Catherine feast-day closure dates.
- **Any time:** which tombs the Valley of the Kings general ticket covers, and which pyramid interiors are open at Dahshur and Giza (Menkaure).

## Applied decisions (2026-10-04)

All 19 decisions plus the Ramadan-dating and text clean-up rules are applied. The tables above show the state **before** these changes. After them, `python3 tools/validate_all.py` reports 0 errors (30 files + 274 seed records), and `v1/` was rebuilt with `schemaVersion: 1, schemaMinor: 1`.

**Schema v1.1** (additive only; every 1.0 record is still valid):
- `prices.status`: `confirmed` (the default when tiers exist), `free` or `unconfirmed`.
- `prices.tiers[].onlineAmount`: the booking-platform price, given only when it differs from `amount` (gate or portal price).
- `prices.extras[].audience`, `.group` and `.onlineAmount`, using the same enums as tiers through the shared `$defs/audience` and `$defs/group`.
- Descriptions now document split sessions (repeated `day` in `weekly`) and say that exceptions are only for real schedule changes.
- The version note is in `$comment` and `title`. `$id` is unchanged because it is the jsDelivr fetch URL.

The validator now also checks:
- `prices.status` consistency.
- `onlineAmount` ≠ `amount`.
- No duplicate tiers.
- Exception `from` ≤ `to`.
- Ramadan exceptions carry dates.
- `open` < `close`.

| # | Applied |
|---|---|
| 1 | GEM keeps EGP 1,590 plus the USD 30 peg. Its `curationNote` has a recheck for 1 Nov 2026: USD 35 / Egyptian EGP 220. |
| 2 | Abu Simbel `onlineAmount`: 822 / 445.5 / 30.5 / 10.5 on the tiers, and 1,272 / 670.5 on the foreign alignment-day extras. `amount` stays at the portal price of 750 etc. No other place has a portal vs booking-site price gap (Medinet Habu: see 4). |
| 3 | Earlier last entry used: <ul><li>Graeco-Roman Sun–Thu 15:00</li><li>Karnak summer 16:00</li><li>MIA Ramadan 14:00</li><li>Nubia Ramadan 14:00 (unchanged)</li></ul> The same rule was applied to the same conflict type at: <ul><li>Giza, Saqqara and the Citadel: Ramadan 15:30 → 15:00</li><li>Luxor Temple: summer last entry 19:00</li></ul> |
| 4 | Medinet Habu foreign adult is 220. No source says the gate charges 230, so there is no `onlineAmount`. The `statusNote` about the two websites was removed. |
| 5 | Citadel opens at 08:00 all year (`curationNote` added). |
| 6 | No change needed: undated live official pages stay as sources with `checkedAt`. |
| 7 | No change needed: those Ramadan rows already show last entry only. |
| 8 | Abydos closing time of 17:00 kept. |
| 9 | Hanging Church and Ibn Tulun: `prices` is now `{status: "unconfirmed"}` with no tiers or free groups. The "no ticket listed" `statusNote` text was removed. `curationNote` says to confirm via hotline 19654. |
| 10 | St Catherine keeps the masrawy Apr 2026 hours (Sat–Thu 08:45–11:30, Fri 10:45–11:30) at confidence `low`. The conflicting sources are listed in `curationNote`. |
| 11–13 | No change: the Narmer Palette stays out, `nmec` is kept, and parking stays only where a live official page lists it (none at Giza). |
| 14 | Moved to `visit.crowdNotes` (EN and AR merged): <ul><li>Karnak and Qaitbay sound & light shows</li><li>Philae boat logistics</li><li>Abu Simbel alignment timing (the dated 22 Oct early-opening exception stays, with a shorter label)</li></ul> NMEC's Friday evening session moved from exceptions into `weekly`. |
| 15 | Split sessions stay as repeated `dayHours` (documented in the schema). Luxor Museum's summer label was tidied. |
| 16 | `audience`/`group` were filled on 73 of 91 extras where the label encodes them. Extras that cover mixed audiences or several groups (some GEM tour combos) and parking extras are left without them. |
| 17 | Fixed locally only (no Wikidata edits): <ul><li>Hatshepsut keeps Q660692 (Q373909 is the wider Deir el-Bahari item)</li><li>Nubia P856 is noted as not used</li><li>Dahshur and Saqqara `city` changed to "Badrashin" (`area` "Dahshur" / "Saqqara necropolis")</li></ul> |
| 18–19 | No change. |

**Ramadan dating:** all 29 Ramadan exceptions now run from 2027-02-08 to 2027-03-08.
- IslamicFinder and hijria.com (Egypt) both put 1 Ramadan 1448 on 8 Feb 2027, with 29 days and Eid al-Fitr on 9 Mar.
- That is one day earlier than the proposed end date of 9 Mar.
- Each record's `curationNote` says "update when officially announced".
- Rule strings were normalised to "Ramadan". The Abydos rule keeps its note about Eid.

**Text clean-up:**
- Slashes removed from `area`: Egyptian Museum "Tahrir Square, Downtown", Coptic Museum, Giza, Hanging Church, NMEC, Qaitbay, Medinet Habu.
- Slashes also removed from extras labels (GEM, NMEC, parking "car or taxi"), free-group strings, best-time text, Saqqara `statusNote` and the summer `rule` strings.
- "Not verified/confirmed" remarks in `statusNote` were reworded as visitor advice: Citadel, Dahshur, Kom el-Shoqafa, Valley of the Kings.
