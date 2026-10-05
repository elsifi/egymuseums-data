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

## Batches 4–7: applied decisions (2026-10-04)

78 new places (batch reports `batch-4.md` to `batch-7.md`) were reviewed together with the 30 earlier ones. After the changes below, `python3 tools/validate_all.py` reports 0 errors (108 place files + 274 seed records), and `v1/` was rebuilt: 274 places, 108 of them enriched.

**Rule used:** every multiple-choice question in the four reports takes its recommended answer, except where a rule above wins or Mo gave a specific instruction (Imhotep, portal vs booking prices, label errors, time-limited notes).

### Decisions applied

| Report | Question | Applied |
|---|---|---|
| batch-4 | 1 St Simeon | Foreign adult 100 / student 50, no `onlineAmount`. This is the D4 pattern: the booking site matches the Nov 2024 list, and the portal's 150 is treated as outdated (its own student price of 50 is not half of 150). |
| batch-4 | 2–9, 11–12 | Recommended answers kept as recorded: Elephantine 15:00; Crocodile Museum keeps its own Ramadan hours; Mahmoud Said Feb 2025 hours and prices; Abdeen `unconfirmed`; Rosetta Qaitbay fort unpriced; Rosetta 08:30–16:00; worship sites `unconfirmed`; Muharraq Lent in `statusNote`; Rashid kept as `renovation`; Qubbet el-Hawa has no last entry. |
| batch-4 | 10 BA museum coordinates | Kept. Wikidata was not edited (D17 wins over the "add P625" half of the answer). |
| batch-4 | 13 Same-hours Ramadan rows | No exception when the Ramadan row equals the normal week (same opening and last entry; Ramadan rows without a closing time count as the same). Removed from 20 records: al-bagawat, amr-ibn-al-as, ben-ezra, imam-al-shafii, deir-el-medina, karnak-open-air-museum, ramesseum, tombs-of-the-nobles-luxor, valley-of-the-queens, and, from the first 30, abu-simbel, kom-ombo, dendera, edfu, philae, hanging-church, karnak, luxor-temple, temple-of-hatshepsut, valley-of-the-kings, medinet-habu. Each `curationNote` records it. |
| batch-5 | 1–5, 7–10 | Recommended answers kept as recorded (Fine Arts prices confirmed; Ceramics 09:30–13:30; Modern Art summer split; Geological empty; al-Shafi'i free; Nasser photos kept; Railway closed Fri; seed operators; Military Museum 16:00 with no Ramadan exception). |
| batch-5 | 6 Modern Art Arabic name | Fixed locally in our record only: `name.ar` "متحف الفن المصري الحديث". The wrong aliases ("Gezira Center for Modern Art", the old name duplicate) were dropped. The seed and Wikidata are unchanged. |
| batch-6 | 1 Imhotep Museum | The newest dated source wins (elwatannews, 27 Apr 2026: open daily). imhotep-museum stays `open`. `saqqara.json` changes, in both languages: <ul><li>`statusNote`: the museum is included in the site ticket</li><li>description: the "closed for restoration" clause is gone</li><li>all-inclusive extra label: lists the museum</li><li>new "Imhotep Museum" highlight</li><li>3 sources added</li><li>`curationNote` records the conflict</li></ul> |
| batch-6 | 2–14 | Recommended answers kept as recorded. |
| batch-7 | 1–6, 8–10 | Recommended answers kept as recorded. Beni Hasan keeps `amount` 20/10 with `onlineAmount` 10/5 (portal and list agree, booking differs). Amarna and Tuna keep 10/5 (no portal page; the only live official price, as for Pompey's Pillar). |
| batch-7 | 7 Summer end date | Every summer exception now ends on **2026-10-29**, the last day of daylight-saving time. The rule text reads "until the last Thursday of October". <ul><li>The 10 Luxor-area records moved from 30 Oct.</li><li>The undated summer exceptions at luxor-museum, medinet-habu and qaitbay-citadel are now dated 2026-04-24 to 2026-10-29, so REVIEW footnote ² no longer applies.</li></ul> |
| Mo | Time-limited notes | All are still valid on 2026-10-04 and kept. Each `curationNote` has a `TIME-LIMITED` line with the expiry: <ul><li>Alamein and October War Panorama free entry: expires after 2026-10-06</li><li>Sharm "Stone and Ink" exhibition: about 2026-11-29</li></ul> |

### Consistency pass (all 108 files)

- **Prose:** removed source talk from user text:
  - Mursi `statusNote` ("was reported")
  - Railway `crowdNotes` ("some sources report…"; Friday is already closed in `weekly`)
  - Islamic Ceramics `bestTime` ("times vary between sources")
- **`freeGroups`:** wording normalised in 66 lists:
  - sentence case
  - "Egyptians aged 60+"
  - "Mobile-phone photography is free"
  - a single Rehla-platform wording
  - the slash in an NMEC entry removed
- **`city`:** amr-ibn-al-as is "Cairo" (Old Cairo stays in `area`). temple-of-hibis is "Kharga", matching al-bagawat.
- **`tickets`:**
  - `{onlineUrl: null, platform: "onsite"}` added for priced places with no online booking: al-bagawat, temple-of-hibis, al-qasr-dakhla, tell-basta, umm-kulthum-museum.
  - `timedEntry: null` filled where it was missing.
- **`prices`:** saint-catherines-monastery now has `{status: "unconfirmed"}` (D9). It previously had no `prices` object.
- **Photos:**
  - `utm_*` tracking parameters stripped from 140 Commons URLs.
  - Every place has 2 or more photos except hurghada-museum (1). Commons has only 4 files in its category, and the other 3 show the 2020 building, which the no-FoP rule excludes.
- **Labels:** time ranges in the Hurghada and Sharm Ramadan labels now use en dashes.
- **Open-question remarks:** curationNote remarks such as "see batch-7 question" and "pending a decision" were replaced with the decision applied.
- **Checked, no change needed:**
  - Every remaining Ramadan exception (60) runs 2027-02-08 to 2027-03-08.
  - Mirrored "included-in" records match their parent's tiers: Karnak Open-Air Museum, Crocodile Museum, Military and Police museums, al-Rifai, Imhotep.
  - `onlineAmount` is used only at Abu Simbel and Beni Hasan.
  - No exception holds visit tips.

### Questions for Mo (recommended answer in **bold**)

1. **Places that cannot be visited right now** (Shubra palace `closed`; al-Gawhara and Rashid museum `renovation`):
   **(a) Keep them in the app with a clear "Closed" badge, and leave them out of "open now" and itinerary suggestions.**
   (b) Hide them until they reopen.
   (c) Show them like any other place.
2. **Low-confidence records** (11 places, e.g. Abdeen, Railway Museum, St Anthony, St Paul, Islamic Ceramics, whose hours rest on old or conflicting reports):
   **(a) Show a small "Details may be out of date. Check before you go" notice on these places.**
   (b) Hide low-confidence places until they are verified.
   (c) No notice; treat them like the rest.
3. **Places covered by another place's ticket** (Karnak Open-Air Museum, Crocodile Museum, Imhotep Museum, Military and Police museums, al-Rifai):
   **(a) Keep them as separate places that say "Included in the X ticket" (current data).**
   (b) Fold them into the parent place as highlights.
4. **21 places show "Price not confirmed"**, mostly working mosques, churches and monasteries, plus 6 Fine Arts museums with stale prices:
   **(a) Do one phone-verification round before launch (MoTA hotline 19654 and the venues), then update the data.**
   (b) Launch with "Price not confirmed" and fix prices as reports come in.
   (c) Add an in-app "Report a price" link and rely on visitors.

### Scheduled rechecks added

- **After 6 Oct 2026:** remove the Alamein and Panorama free-entry sentences.
- **After 29 Oct 2026:** winter 2026–27 hours for every place that had a summer exception (14 records).
- **Mid-Nov 2026:** confirm the Nativity Fast rules at St Anthony and St Paul.
- **End of Nov 2026:** remove the Sharm exhibition sentence.
- **Early 2027:** the Mursi square works; Ramadan 2027 announcements, including the 20 records whose same-hours Ramadan exceptions were removed.

## Batches 8–13: applied decisions (2026-10-05)

166 new minor places (batch reports `batch-8.md` to `batch-13.md`) were reviewed together with the 108 earlier ones. 14 seed records were excluded from the catalogue (see below), so 152 of the new places remain. After the changes, `python3 tools/validate_all.py` reports 0 errors (260 place files + 274 seed records, 14 seed ids excluded), and `v1/` was rebuilt: 260 places, all enriched.

**Rule used:** every multiple-choice question in the six reports takes its recommended answer, except where a rule above or one of Mo's decisions of 2026-10-05 wins (photo rule, exclusions).

### New house rules

- **Photos for minor places (decided).** A place with `tier: "minor"` may have an empty `photos` list when no compliant photo exists; its `curationNote` says why. Major and notable places still need at least one photo. The validator enforces this. 27 minor places currently have no photo.
- **Exclusions (decided).** Duplicates and records that are not real visitable places are listed in `tools/seed/excluded.json` as `{id, reason}`. `tools/build_catalog.py` leaves them out of `v1/`. The seed record stays in `data/seed/places.json` for provenance, and the `data/places/<id>.json` file is deleted. Useful facts are folded into the parent record first, and the old names become aliases so search still finds them. When it is unclear whether a place exists, it is kept as `unknown`/`low` instead.
- **Validator additions:**
  - `freeGroups` needs a matching `freeGroupsLocalized`.
  - `prices.includedIn` must name an existing, non-excluded place.
  - `excluded.json` ids must be seed ids, carry a reason and have no place file.
- `v1/meta.json` gains an additive `excluded` count.

### Exclusions (14)

| id | reason | folded into |
|---|---|---|
| heriyet-rezna-museum | duplicate (same Sharqia National Museum) | ahmed-orabi-museum: summary, duplicate Wikidata item Q130218217 in sources, aliases |
| minya-museum | duplicate of the Aten Museum project | aten-museum: alias "Minya Museum" |
| san-el-hagar-museum | duplicate: Tanis itself is the open-air museum | tanis: aliases |
| heliopolis-open-air-museum | part of the obelisk site, same ticket | obelisk-of-senusret-i: "Open-air museum" highlight (about 135 objects, opened Feb 2018), statusNote, aliases, SIS source |
| hunting-museum-manial | part of the palace museum, same ticket | manial-palace-museum: aliases and its one photo (the highlight already existed) |
| mashrabia-art-gallery | commercial gallery | — |
| espace-karim-francis | commercial gallery | — |
| science-museum | no evidence that it exists | — |
| damietta-science-museum | no evidence that it exists today | — |
| al-turathiya-museum-ismailia | unverifiable | — |
| suez-canal-historical-exhibition | superseded by the Suez Canal Museum | — |
| confiscated-antiquities-museum | no longer exists (batch-9 Q4a) | — |
| college-museum-university-of-assiut | not identifiable as a visitable museum (batch-8 Q7a) | — |
| alexandria-underwater-museum | never built. Mo's exclusion rule wins over batch-8 Q6a. | — |

**Canonical Sharqia record.** `ahmed-orabi-museum` is now named "Sharqia National Museum" / "متحف الشرقية القومي", with status `closed`. "Ahmed Orabi Museum" and "Heriyet Rezna Museum" are kept as aliases.

### Decisions applied

| Report | Question | Applied |
|---|---|---|
| all | photo questions (b8 Q1, b9 Q1, b10 Q1, b11 Q1, b12 Q1, b13 G1) | The minor-photo rule above. Stand-in and borderline photos are kept (b10 Q2a, b11 Q6a, b12 Q6a, b13 A7a). |
| batch-8 | 2–5, 8–10 | Kept as recorded: <ul><li>Aswan annex `includedIn: elephantine-island`</li><li>Cavafy `free`</li><li>hydrobiological museum's winter hours in `weekly`</li><li>Abu Mena `unconfirmed`</li><li>Alwan House `unknown`/`low`</li><li>Rosetta fort confirmed</li><li>borrowed coordinates noted</li></ul> |
| batch-8 | 6, 7 | Underwater museum and College Museum excluded. |
| batch-9 | 2, 3, 6–9 | Kept as recorded: <ul><li>airport museums: Egyptian tier plus `usdAmount` 5</li><li>Farouk Corner 17:00 / 16:00</li><li>no monastery fast exceptions</li><li>Aisha Fahmy July 2026 hours</li><li>Beit el-Umma `renovation`</li><li>EGX, Air Force and Geographic Society `unknown`</li></ul> |
| batch-9 | 4 | Karim Francis and Confiscated Antiquities excluded. The former Citadel carriage museum, the Textile Museum and the Naguib Pasha Mahfouz museum stay `closed`; their statusNotes point to Bulaq, to NMEC and to "not open to the public". |
| batch-9 | 5 | Heliopolis open-air museum and Hunting Museum folded into their parents and excluded. |
| batch-10 | 3 | Mashrabia and the Science Museum excluded. |
| batch-10 | 5 | National Library museum: <ul><li>name "Museum of the National Library of Egypt"</li><li>coordinates 30.044722, 31.252778, the historic Bab al-Khalq Dar al-Kutub building it shares with the Museum of Islamic Art (ar-wiki; Wikidata Q3330629)</li></ul> Seed and Wikidata are unchanged. |
| batch-10 | 12 | Prince Wahid Selim operator is `ministry-of-culture`. |
| batch-10 | 2, 4, 6–11, 13, 14 | Kept as recorded. |
| batch-11 | 5 | Damietta Science Museum, Al-Turathiya and the Suez Canal historical exhibition excluded. |
| batch-11 | 7 | Wikidata ids and coordinates backported to `data/seed/places.json`: <ul><li>Wissa Wassef: Q126920240</li><li>Fayoum Art Center: Q134292187</li><li>Giza Zoo museum: coordinates</li></ul> The seed has been hand-edited before (commit 41ca824). |
| batch-11 | 2–4, 6, 8, 9 | Kept as recorded (Bahariya keeps `effectiveFrom` 2026-10-01; Solar Boat Museum stays `closed` and points to GEM). |
| batch-12 | 2 | minya-museum excluded. |
| batch-12 | 4 | Re-scoped as "Marina el-Alamein Archaeological Site": <ul><li>`kind: site`, Q778942</li><li>"Site museum" highlight</li><li>the old museum name is an alias</li><li>id unchanged</li></ul> |
| batch-12 | 5 | Re-scoped as "El-Ashmunein (Hermopolis Magna)": <ul><li>`kind: site`, Q732908</li><li>`renovation`/`low`</li><li>id unchanged</li></ul> |
| batch-12 | 7 | esna-temple gains a "Nearby: Wikalat al-Gedawi … same ticket" highlight, and its curationNote no longer says "not claimed". |
| batch-12 | 3, 6, 8 | Kept as recorded (Matrouh 180/90; Denshway photo; PDF-only places `open`/`medium`). |
| batch-13 | G2, G3 | Sharqia merge and San el-Hagar exclusion (above). |
| batch-13 | A9 | Hurghada `name.ar` is now "متحف الأحياء البحرية بالغردقة"; the seed form is an alias. |
| batch-13 | A14 | No coordinates added for Akhmim: no site visit or OSM node id is available, so it stays null. |
| batch-13 | A1–A8, A10–A13, A15, A16 | Kept as recorded. |
| batch-13 | G4 | Product question; see question 4 below. |

**Time-limited notes.** All are still valid on 2026-10-05 and kept, with a `TIME-LIMITED … still valid on 2026-10-05` line in `curationNote`:

| Place | Note | Expires |
|---|---|---|
| Alamein and October War Panorama | free entry | after 2026-10-06 |
| BA (manuscripts, planetarium, Sadat) | 8 Oct holiday hours | after 2026-10-08 |
| Sadat museum | "Sadat panorama" line | after 2026-10-31 |
| Sharm | exhibition | about 2026-11-29 |
| Suez National Museum | "Blue" exhibition | about 2027-01-04 |

Two expired notes were removed:
- the Umm Kulthum Museum Day 2026 free-entry sentence;
- the Deir al-Muharraq Great Lent 2026 dates.

### Consistency pass (all 260 files)

- **`curationNote`:**
  - About 30 open remarks ("see batch-N report", "Recommend …", "validator error expected") replaced with the decision applied.
  - The Marina, Ashmunein, National Library and Sharqia notes were rewritten.
- **Prose:** removed source talk from 5 statusNotes (al-Arish, Ismailia, Zagazig university, Ayun Musa, Suez Canal Authority museum) and from the Egyptian Capitals description, in both languages.
- **Time ranges:** en dashes in the NMEC and Qaitbay statusNote/bestTime.
- **`freeGroups`:** wording normalised in 12 records:
  - "Egyptians with special needs" replaces "Egyptians with disabilities" (8 major places).
  - Fine Arts lists use "Seniors over 60", "Veterans", "Members of artists' professional syndicates" and the Arabic "ذوو الهمم".
- **Mirrored records:** the 5 older `includedIn` records (crocodile, military, police, Imhotep, Karnak open-air) now copy the parent's free groups as well as its tiers.
- **Checked, no change needed:**
  - `freeGroupsLocalized` is present wherever `freeGroups` is.
  - No `en` text lacks `ar`, and no `ar` text lacks `en`.
  - Every Ramadan exception runs 2027-02-08 to 2027-03-08 with "update when officially announced".
  - Every summer exception ends 2026-10-29.
  - Every `includedIn` target exists.
  - Every priced place has a `tickets` object with `timedEntry`.
  - No `utm_` parameters and no slashes in area, labels or rules.

### Counts

| | open | unknown | renovation | closed | high | medium | low |
|---|---|---|---|---|---|---|---|
| New places kept (152) | 109 | 24 | 10 | 9 | 31 | 77 | 44 |
| Whole catalogue (260) | 214 | 24 | 12 | 10 | 62 | 143 | 55 |

- Catalogue tiers: 30 major, 78 notable, 152 minor.
- New-place prices: 81 confirmed, 4 free, 59 unconfirmed, 8 without a `prices` object.

### Questions for Mo (recommended answer in **bold**)

1. **Minor places without a photo** (27, e.g. Suez National Museum, Rommel's Cave, Adam Henein):
   **(a) Show a category illustration as the placeholder and leave these places out of photo-led carousels.**
   (b) Show a map tile instead.
   (c) Show them like any other place, with a blank image.
2. **Museums that are built or announced but not yet open** (Aten Museum, due Q4 2027; Museum of Egyptian Capitals):
   **(a) Use an "Opening soon" badge, separate from "Closed", and leave them out of "open now" and itineraries.**
   (b) Use the same "Closed" badge.
   (c) Hide them until they open.
3. **Places with restricted access** (airside airport museums: passengers only; university and faculty museums, the parliament museum, the Banque Misr museum: by appointment):
   **(a) Add an optional `access` field ("public", "appointment", "passengers") in schema 1.4, and show a badge.**
   (b) Keep it in `statusNote` text only.
   (c) Hide these places.
4. **Places with status `unknown`** (24, mostly minor; batch-13 G4):
   **(a) Show them with the "Check before you go" badge, and leave them out of "open now" and itineraries.**
   (b) Show them only in search results.
   (c) Hide them until they are verified.

### Scheduled rechecks added

- **After 8 Oct 2026:** remove the BA holiday exception (3 records).
- **After 31 Oct 2026:** remove the Sadat panorama line.
- **After 29 Oct 2026:** winter hours for Carter House, Qurnet Murai, Seti I, Matrouh, Deir el-Shelwit, Assasif, Khokha and the Sohag last entry.
- **Mid-Nov 2026:** Nativity Fast rules at the Wadi Natrun monasteries.
- **Q4 2026:** Giza Zoo reopening.
- **About 4 Jan 2027:** remove the Suez "Blue" exhibition line.
- **Early 2027:**
  - Ramadan 2027 announcements;
  - Muharraq and Baramus Lent and feast closures.
- **H1 2027:** Marina el-Alamein reopening.
- **2027:** reopenings of Aswan Museum, Beit el-Umma, the Calligraphy and History of Science museums, and the Aten Museum (Q4).
- **Any time:** National Museum of Asyut status; Arish, Taba and Ismailia museums; phone checks for prices marked `unconfirmed` (hotline 19654).
