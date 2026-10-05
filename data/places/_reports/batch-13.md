# Batch 13 enrichment report

Checked 2026-10-05. 26 minor places: al-arish-national-museum, al-nasr-museum-of-modern-art, port-said-military-museum, port-said-national-museum, suez-canal-authority-museum, museum-of-irrigation-models, nag-hammadi-barrages-museum, sira-hilaliya-museum-abnoudi, prince-youssef-kamal-palace, hurghada-marine-museum-aquarium, mini-egypt-park, sand-city-hurghada, quseir-fortress, ahmed-orabi-museum, archaeological-museum-university-of-zagazig, heriyet-rezna-museum, san-el-hagar-museum, tell-basta-museum, sohag-national-museum, akhmim-meritamun, athribis-sohag, el-hawawish, taba-museum, ayun-musa, pharaohs-island-citadel, suez-national-museum.

Every file has:
- an English description of 139–160 words, with Arabic written separately;
- `verifiedAt` 2026-10-05;
- 2–5 highlights, except port-said-national-museum (none: the collection is in storage).

All 26 files pass `python3 tools/validate_all.py` except for one rule. **12 files report "at least one photo required"** because no compliant Commons photo exists (see "Read this first", item 1). There are no other errors.

## Summary

| id | status | conf. | foreign adult / Egyptian adult (EGP) | hours (normal week) | online | photos |
|---|---|---|---|---|---|---|
| al-arish-national-museum | unknown | low | — | — | no | 0 |
| al-nasr-museum-of-modern-art | open | medium | 10 / 5 | 09:00–16:00, closed Mon, Fri | no | 0 |
| port-said-military-museum | open | medium | unconfirmed | 09:00–15:00 + 18:00–21:00 | no | 0 |
| port-said-national-museum | closed | medium | — | — | no | 0 |
| suez-canal-authority-museum | unknown | low | — | — | no | 0 |
| museum-of-irrigation-models | open | low | unconfirmed | not published | no | 0 |
| nag-hammadi-barrages-museum | unknown | low | — | — | no | 1 |
| sira-hilaliya-museum-abnoudi | open | low | free | 10:00–16:00, closed Mon, Fri | no | 0 |
| prince-youssef-kamal-palace | open | high | 100 / 10 | 08:00–17:00 (last 16:00) | yes | 1 |
| hurghada-marine-museum-aquarium | open | low | unconfirmed | not published | no | 3 |
| mini-egypt-park | open | low | unconfirmed | not published | tours | 0 |
| sand-city-hurghada | unknown | low | unconfirmed | — | no | 0 |
| quseir-fortress | open | medium | 100 / 10 | 09:00–17:00 (last 16:00) | no | 3 |
| ahmed-orabi-museum | closed | medium | — | — | no | 1 |
| archaeological-museum-university-of-zagazig | unknown | low | — | — | no | 0 |
| heriyet-rezna-museum | closed | medium | — | — | no | 1 |
| san-el-hagar-museum | unknown | low | unconfirmed | — | no | 1 |
| tell-basta-museum | open | medium | 150 / 10 (included in tell-basta) | 09:00–15:00 (last 14:00) | no | 3 |
| sohag-national-museum | open | high | 150 / 20 | 09:00–15:00 (last 14:00) + Fri/Sat 17:00–21:00 | yes | 3 |
| akhmim-meritamun | open | medium | 120 / 10 | 07:00–17:00 (last 16:00) | yes | 3 |
| athribis-sohag | open | high | 150 / 10 | 07:00–17:00 (last 16:00) | yes | 2 |
| el-hawawish | open | high | 150 / 10 | 07:00–17:00 (last 16:00) | yes | 2 |
| taba-museum | unknown | low | — | — | no | 0 |
| ayun-musa | unknown | low | unconfirmed | — | no | 3 |
| pharaohs-island-citadel | open | medium | 400 / 20 | 09:00–17:00 (last 16:00) | no | 3 |
| suez-national-museum | open | high | 180 / 20 | 09:00–15:00 (last 14:00) | no | 0 |

**Counts:**
- Status: 15 open, 8 unknown, 3 closed.
- Confidence: 5 high, 9 medium, 12 low.

**Ramadan 2027 exceptions:** quseir-fortress, akhmim-meritamun, athribis-sohag, el-hawawish, pharaohs-island-citadel, al-nasr-museum-of-modern-art and sira-hilaliya-museum-abnoudi.
- Each is dated 2027-02-08 to 2027-03-08 and carries "update when officially announced".
- The last two use the Fine Arts Sector's sector-wide Ramadan hours.
- tell-basta-museum, sohag-national-museum, suez-national-museum and prince-youssef-kamal-palace have no Ramadan exception, because their Ramadan hours equal their normal hours.

## Read this first

1. **Validator vs photo rule.** The validator requires at least one photo; the house rule says to leave `photos` empty when nothing compliant exists. These 12 files have no photo:
   - al-arish-national-museum, al-nasr-museum-of-modern-art, port-said-military-museum, port-said-national-museum, suez-canal-authority-museum, museum-of-irrigation-models, sira-hilaliya-museum-abnoudi, mini-egypt-park, sand-city-hurghada, archaeological-museum-university-of-zagazig, taba-museum, suez-national-museum.

   For each one, Commons has either nothing, or only modern buildings or works still in copyright (Egypt has no freedom of panorama). Other batches show the same error (e.g. arabic-calligraphy-museum, aswan-nile-museum). See question G1.
2. **Duplicates.**
   - ahmed-orabi-museum and heriyet-rezna-museum are the same institution: the Sharqia National Museum in Hurriya Razna, closed since 2000.
   - san-el-hagar-museum is probably not a separate museum. The Tanis site itself is presented as an open-air museum.

   See questions G2 and G3.
3. **Not SCA.** These places are not run by the antiquities authority:
   - Port Said Military Museum: Ministry of Defence.
   - Al-Nasr and Abnoudi: Ministry of Culture, Fine Arts Sector.
   - Irrigation and Nag Hammadi museums: Ministry of Water Resources and Irrigation.
   - Hurghada marine museum: National Institute of Oceanography and Fisheries.
   - Suez Canal Authority Museum: Suez Canal Authority.
   - Mini Egypt Park and Sand City: private companies.

   SCA tier rules are not applied to any of them.
4. **Price-only-from-PDF.** Quseir and Pharaoh's Island have no portal or booking page, so their only official price source is the Nov 2024 MoTA list. They are kept as `confirmed`, as batch-7 Q4a decided for Hibis and Al-Qasr.

## Per place

### al-arish-national-museum
- **Unverified:** current status. The museum is missing from both the MoTA open-museums guide and the Nov 2024 list.
  - An Akhbar el-Yom article announced a reopening "by the October celebrations". I could not open it (403), and its id suggests it is from about 2022.
  - The governorate page carries data from July 2010.
- **Decision:**
  - A1. Status: **(a) keep `unknown` with a "check before travelling" note**; (b) mark `closed`; (c) hide from the app.

### al-nasr-museum-of-modern-art
- **Sources:** the Fine Arts Sector schedule of 4 Jun 2026 names this museum (09:00–16:00, closed Fri and Mon). The undated fineart.gov.eg page says 10:00–16:00; the dated statement is used.
- **Unverified:**
  - Prices 5/3/10 come from an undated official page.
  - The official phone number (066-347676) looks truncated, so it is omitted.
- **Changed locally:** the seed alias "Museum of Modern Art in Egypt" (the Wikidata label, ambiguous with the Cairo museum) is replaced by "Museum of Modern Art – Port Said". This follows batch-5 Q6.
- **Decision:**
  - A2. Wikidata label: **(a) leave Wikidata alone and keep the local fix**; (b) also correct the Wikidata label.

### port-said-military-museum
- **Sources:** hours from the live, undated MoD page: 09:00–15:00 and 18:00–21:00. No days off or last entry are published.
- **Unverified:**
  - Price. A 2026 blog says EGP 10, so `prices` is `unconfirmed`.
  - An Ahram Gate piece on free October entry could not be fetched.
  - The museum is not in the Armed Forces free-entry list for 3–6 Oct 2026.
- **Decision:**
  - A3. Treat the hours as daily: **(a) yes, as for Alamein**; (b) leave the days unknown.

### port-said-national-museum
- **Status `closed`:** the newest dated source (Asharq Al-Awsat, Mar 2023) says the rebuilding has stalled since 2011. I found no 2024–2026 news.
- **Not set:** no coordinates (Wikidata has none) and no highlights.
- **Decision:**
  - A4. **(a) keep as `closed`** with a badge (REVIEW Q1a); (b) hide until rebuilt.

### suez-canal-authority-museum
- **Unverified:** status. No source after 2015 covers this villa museum.
- **Possible confusion with other projects:** recent news is about the large Suez Canal Museum in Ismailia and the plan (under restoration since 2025) to turn the domed Canal Authority building in Port Said into a museum.
- **Conflict:** the Wikidata coordinates sit at the Dome building on the canal front, while ar-wiki puts the museum in the Eugénie villa (Bazaar/Safiya Zaghloul streets).
- **Decision:**
  - A5. **(a) keep `unknown` and ask the Suez Canal Authority**; (b) mark `closed` (collection presumed moved to Ismailia); (c) re-point the record to the future Dome-building museum.

### museum-of-irrigation-models
- **Status `open`:** the Qanater irrigation director presented the museum to Eid visitors (youm7, 27 May 2026).
- **Not published:** hours and a museum fee. Garden entry is EGP 10–20, or 20–40 on holidays; this is not modelled as the museum price.
- **Decision:**
  - A6. **(a) keep `prices: unconfirmed` and mention the garden ticket in crowdNotes (done)**; (b) model the garden ticket as the price.

### nag-hammadi-barrages-museum
- **Unverified:** public opening. I found nothing after the 2021 opening reports.
- **Photo:** a public-domain 1930 official print of the barrage (no image of the museum exists).
- **Ambiguous:** the direction of the old barrage in ar-wiki. The text says only "a few kilometres away".
- **Decision:**
  - A7. Use the barrage image as the museum photo: **(a) yes**; (b) no, leave photos empty.

### sira-hilaliya-museum-abnoudi
- **Status `open`, low confidence:**
  - The museum held a children's workshop on 27 Sep 2026.
  - But youm7 found it shut to visitors on Tue 21 Apr 2026, a normal opening day.
- **Price:** `free` comes from the official fineart.gov.eg page ("الدخول مجاناً").
- **Conflict:** ar-wiki puts Abnud in Qift district; youm7 says Qena. The address is kept to "Abnud village, Qena".
- **Decision:**
  - A8. **(a) keep `open` with the "check locally" note**; (b) `unknown`.

### prince-youssef-kamal-palace
- **Sources agree:** the guide, portal, booking page and Nov 2024 list.
- **Conflict:** the build date is 1908 in ar-wiki but 1925 in the MoTA guide. The text says "early twentieth century".
- **Photo:** only one compliant photo exists.
- **Decision:** none needed.

### hurghada-marine-museum-aquarium
- **Status:** from youm7 (Aug 2025). The quoted EGP 20 is not official, so `prices` is `unconfirmed`.
- **Not confirmed:** whether live aquarium tanks are still shown, so the text omits them.
- **Watch for:** search engines mix this museum up with the private Hurghada Grand Aquarium.
- **Decision:**
  - A9. Arabic name: the seed's editor-added "المتحف البحري والأكواريوم بالغردقة" is not what locals or the press use ("متحف الأحياء البحرية"). Options: **(a) switch `name.ar` to "متحف الأحياء البحرية بالغردقة" and keep the seed form as an alias**; (b) keep the seed name (current file; the press name is already an alias).

### mini-egypt-park
- **Status `open`:** based on the live official booking site (copyright line 2022). No dated statement exists.
- **Not used:** third-party hours and prices.
- **Photos:** the models are recent copyrighted works, so none are used.
- **Decision:**
  - A10. **(a) keep `open` at low confidence**; (b) `unknown` until the park confirms by phone (+20 111 986 0033).

### sand-city-hurghada
- **Status `unknown`:** the official site dates from 2014; only resellers show 2025–26 activity.
- **Conflict:** the official site gives two different sculpture counts.
- **Arabic name:** editor-added.
- **Decision:**
  - A11. **(a) keep `unknown`**; (b) `open` on the reseller evidence.

### quseir-fortress
- **Sources:** the MoTA guide and the Nov 2024 list agree on 09:00–17:00 (Ramadan 09:00–16:00).
- **Price:** from the PDF only.
- **Not used:** the en-wiki "replica dhow" exhibit, which is not officially confirmed.
- **Decision:** none needed (Read-first item 4).

### ahmed-orabi-museum / heriyet-rezna-museum
- **Status `closed`:** almawq3 reported on 10 Sep 2026 that the building has been abandoned since 2000; youm7 said the same in 2022.
- **Duplicate:** Q130218217 ("Heriyet Rezna Museum", dissolved 2006) is the same museum as Q6852382. heriyet-rezna-museum takes its coordinates from Q6852382.
- **Operator:** the seed says ministry-of-culture for Orabi and mota-sca for Heriyet. The antiquities section was SCA material; the operator is left as in the seed.
- **Photo:** the 1879 public-domain portrait of Orabi.

### archaeological-museum-university-of-zagazig
- **Unverified:** public access. The university museum site refused connections on 2026-10-05.
- **Conflict:** the object count is 2,537 (2017) or 2,173 (later snippet); the text says "some 2,500".
- **Decision:**
  - A12. **(a) keep as `unknown` ("contact the university")**; (b) hide (not a public museum).

### san-el-hagar-museum
- **No separate museum found:** no MoTA list, guide or booking page names a museum at San el-Hagar.
- **Photo:** reused from tanis.
- See G3.

### tell-basta-museum
- **Hours conflict:** the MoTA guide (and elwatannews, May 2026) say summer 18:00 / winter 17:00; the Nov 2024 list says 09:00–15:00. The earlier time is used (close 15:00, last entry 14:00).
- **Price:** `includedIn: tell-basta`, from the 2024 list ("Within Tell Basta Ticket"). The tiers mirror the site.
- **Photos:** Jan 2026 Commons uploads of open-air objects, checked visually.
- **Decision:**
  - A13. **(a) keep 09:00–15:00 (earlier-time rule)**; (b) follow the guide's seasonal 17:00/18:00, matching tell-basta.json.

### sohag-national-museum
- **Last-entry conflict:** the guide implies 14:00 (15:00 close); the booking page says winter 14:30 and summer 16:00. 14:00 is used all year, with no summer exception.
- **Evening session:** Fri/Sat 17:00–21:00 from the guide; last entry 20:00 is inferred.
- **Unknown:** whether the evening session runs in Ramadan.

### akhmim-meritamun
- **Coordinates:** none (no Wikidata item, no geotag).
- **Not from an official source:** "one of the largest standing statues of a queen".
- **Decision:**
  - A14. Coordinates: **(a) add them from a site visit or OSM node id only (no OSM-derived data)**; (b) leave null.

### athribis-sohag
- **Conflict:** the temple's builder is Ptolemy XII on the portal but Ptolemy XV Caesarion on en-wiki. The portal is used.
- **Ignored:** an undated portal note on "free for Egyptians until end of March".

### el-hawawish
- **Ramadan opening conflict:** the guide says 09:00, the booking page 07:00. The narrowest window (09:00–16:00, last entry 15:00) is used, following batch-7 Q1a.

### taba-museum
- **Status `unknown`:** the museum is missing from the guide and the 2024 list, and I found no news.
- **Not used:** ar-wiki's unsourced hours and prices (EGP 160/80 foreign).

### ayun-musa
- **Operator:** changed from seed `other` to `mota-sca`. The 2026 development is run by the SCA's antiquities sector (youm7, 25 Apr 2026).
- **Governorate conflict:** ar-wiki says the springs are administered by Suez; the seed says south-sinai and is kept.
- **Decisions:**
  - A15. Operator: **(a) `mota-sca`**; (b) back to `other`.
  - A16. Governorate: **(a) keep `south-sinai` (physically in Sinai, Ras Sudr area)**; (b) `suez`.

### pharaohs-island-citadel
- **Sources:** guide hours, and the price from the PDF only.
- **Watch for:** search engines confuse this site with the Cairo Citadel (550/275).
- **Unknown:** how the boat crossing is arranged or priced. The text says only "reached by boat".

### suez-national-museum
- **Sources agree:** the portal, guide and 2024 list.
- **TIME-LIMITED:** the statusNote mentions the "Blue, the secret of eternity" exhibition (from about 4 Oct 2026, three months). Remove it after about 2027-01-04.
- **Photos:** none. The only Commons image shows the 2014 building.

## General questions (recommended answer in **bold**)

- **G1. Places with no compliant photo** (12 files fail the validator's photo rule):
  - **(a) Relax the validator to a warning for `tier: minor`, and show a placeholder in the app.**
  - (b) Allow loosely related images (city views, historic prints) to satisfy the rule.
  - (c) Keep the rule and hide these places until photos exist.
- **G2. Orabi / Heriyet Rezna duplicate:**
  - **(a) Keep ahmed-orabi-museum, delete heriyet-rezna-museum, and record Q130218217 as a duplicate item in its sources.**
  - (b) Keep both.
- **G3. san-el-hagar-museum:**
  - **(a) Drop the record (or merge it into tanis as an alias), because the open-air site is already covered.**
  - (b) Keep it as `unknown`.
- **G4. Minor places that are closed or unknown** (11 here):
  - **(a) Show them with the "Closed" or "Details may be out of date" badge (REVIEW Q1a/Q2a) and exclude them from "open now" and itineraries.**
  - (b) Hide `unknown` places entirely.

## Scheduled rechecks

- **After 29 Oct 2026:** Sohag National Museum winter last entry (the booking page says 14:30).
- **About 4 Jan 2027:** remove the Suez "Blue" exhibition sentence.
- **Early 2027:** Ramadan 2027 announcements (7 exceptions in this batch).
- **Any time:**
  - Arish and Taba museum reopenings.
  - Port Said National Museum rebuilding.
  - The Ayun Musa works.
  - The Port Said Dome-building museum project.
