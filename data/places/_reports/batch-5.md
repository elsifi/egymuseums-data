# Batch 5 enrichment report

Checked 2026-10-04. Places: al-gawhara-palace, al-ghuri-complex, al-rifai-mosque, amr-ibn-al-as-mosque, bab-zuwayla, baron-empain-palace, bayt-al-suhaymi, ben-ezra-synagogue, egyptian-geological-museum, egyptian-national-military-museum, egyptian-railway-museum, gamal-abdel-nasser-museum, gayer-anderson-museum, imam-al-shafii-mausoleum, manial-palace-museum, mukhtar-museum, museum-of-islamic-ceramics, museum-of-modern-egyptian-art, national-police-museum, obelisk-of-senusret-i.

All 20 files pass `python3 tools/validate_all.py` (schema v1.1, 0 errors). Each has 140–200-word EN/AR descriptions written from scratch, 4–6 highlights and 2–3 Wikimedia Commons photos (licence metadata from the Commons API).

## How the hours and prices are backed

- **SCA sites (12):** the same three official channels as batches 1–3, all live and undated, checked 2026-10-04.
  - `egymonuments.com/details/<Site>` and `/book-date/<n>`: prices, last entry, Ramadan last entry and free-entry groups.
  - `egymonuments.gov.eg`: open and close times, prices and services.
  - The MoTA "open sites/museums guide" (`mota.gov.eg/ar/...دليل-...-جديد/<site>/`): open and close times, Ramadan close, address, and the "last entry one hour before closing" rule.
  - **Online vs gate prices:** none of these places shows a gap between the booking platform and the portal, so there is no `onlineAmount`.
  - **Arab tier:** none (dostor 5363965).
- **Fine Arts Sector museums (Mukhtar, Modern Art, Islamic Ceramics, Nasser):**
  - Hours: dated youm7 statements by the sector head (16 Feb 2025, 21 Feb 2026 Ramadan, 4 Jun 2026 summer).
  - Prices and free groups: the sector's own visitor pages on `fineart.gov.eg`. These are undated and visibly stale: they show 10:00–16:00 hours and say Ceramics is "under development".
- **Railway Museum:** Egyptian National Railways' 2024 announcement, as quoted by elwatannews and youm7 on 12 May 2024.
- **Geological Museum:** none. The museum's operator (EMRA) publishes no hours or fees.
- **Citadel museums (Military, Police):** the current Citadel area ticket (550/275 foreign, 60/30 Egyptian) from the Citadel portal page and egymonuments.com. Each museum's own portal page still shows the old 200/100.
- **Ramadan:** every Ramadan exception runs 2027-02-08 to 2027-03-08, with the standard `curationNote`.
- **Conflicting times:** the earlier time is used and noted per place.
- **Not set:** `cashAccepted` (no 2025–26 official statement) and `effectiveFrom` (no dated decision cited).

## Per place

### al-gawhara-palace — medium
- **Status `renovation`.** The SCA secretary-general inspected the ongoing restoration on 17 Mar 2026 (dostor 5462469): artefacts wrapped, structural consolidation done, roof insulation under way. No article says "closed" in so many words, and no reopening date is given.
- No hours or tickets are set; `prices.status` is unconfirmed.
- **Portal bug:** the egymonuments.gov.eg slug `monuments/al-jawhara-palace/` shows the text for Wasila House (100/50 ticket). Not used.
- **Not verified:** whether the Citadel ticket will cover it after reopening (only third-party guides say so).

### al-ghuri-complex — medium
- 150/75 foreign, 10/5 Egyptian. 09:00–17:00, last entry 16:00. Ramadan: last entry 15:00 only; no closing time published.
- **Assumption:** booking slug `AlGhuriDome` is the ticketed eastern half (dome, khanqah, sabil). The portal lists the same prices for "Sultan al-Ghuri Complex".
- The Wikala of al-Ghuri (100/50) is a separate ticket and is only mentioned in `statusNote`.
- **Not verified:** the evening Tannoura and cultural-show schedule, so the visit notes only say "evening performances, ticketed separately".

### al-rifai-mosque — high
- Joint ticket with Sultan Hassan: the portal shows 220/110 foreign, Egyptians EGP 0. The record mirrors `sultan-hassan-mosque`.
- 09:00–17:00; Ramadan 09:00–16:00, last entry 15:00 (MoTA guide).

### amr-ibn-al-as-mosque — medium
- 09:00–16:00 tourist hours from both the MoTA guide and the portal; Ramadan the same.
- `prices.status` unconfirmed: no official page lists a ticket.
- Reported but not used in user text: the restoration and the new Fustat plaza (alkhaleej, Jan 2025).
- Only 2 photos (entrance, 19th-c. Rijksmuseum CC0). Most Commons images are Eid crowds.

### bab-zuwayla — high
- 100/50, 10/5. 09:00–17:00, last entry 16:00; Ramadan 09:00–16:00, last entry 15:00. All three official sources agree.
- **Not officially stated:** that the ticket includes the minaret climb. It is widely known and shown in the photos.

### baron-empain-palace — high
- 220/110, 60/30. Roof (panorama) add-on: 120 foreign, 30 Egyptian, the same for students.
- 09:00–18:00, last entry 17:00.
- **Ramadan conflict:** MoTA 09:00–16:00 (implying last entry 15:00) vs booking platform last entry 15:30. **15:00 used.**

### bayt-al-suhaymi — medium
- 220/110, 10/5.
- **Friday conflict:** the portal says 09:00–16:00; the MoTA guide says 09:00–17:00 daily; the booking platform says last entry 16:00 daily. **Friday close 16:00, last entry 15:00 used.**

### ben-ezra-synagogue — medium
- 09:00–16:00 daily, Ramadan the same (MoTA guide and portal).
- `prices.status` unconfirmed, as for the Hanging Church (D9).
- **Not found:** the photography rule, and any 2025–26 status news.

### egyptian-geological-museum — low
- **No official hours or prices**, so no `hours` and `prices.status` unconfirmed.
- A third-party listing (cairo360, Aug 2025) gives 09:00–15:00, closed Fri and Sat, EGP 25. Not used.
- **Status `open`:** the operator's (EMRA) live page describes the museum in the present tense and no closure was found.
- The riverside plot is on the state's inventory of Nile-front land. On 2026-09-29 the Urban Development Fund said no tender has started (elbalad 7124445). **Watch for relocation.**
- The fall year of the Nakhla meteorite conflicts between sources (1908 vs 1911), so none is given.

### egyptian-national-military-museum — medium
- **Hours:** the portal says 08:00–16:00 and that the "ticket window closes 16:00" (contradictory). Close 16:00 is used with no `lastEntry`.
- **No Ramadan data**, so no exception.
- **Prices:** the current Citadel ticket. The museum page's stale 200/100, a "night visit" ticket (160/80, 30/10) and camera fees (50/20, video 300) are left out.

### egyptian-railway-museum — low
- **Prices (ENR 2024):**
  - Egyptian 10; foreign 100; foreign student 50.
  - Extras: Egyptian student groups 5 (with an official letter), international schools 25, photography 10, entry to Said Pasha's locomotive 20.
- **Hours conflict, same day:** 09:00–14:00 (elwatan) vs 09:00–13:00 (youm7). **13:00 used.**
- **Friday:** closed only according to cairo360 (non-official). Set closed as the cautious choice.
- Status open in 2026: free weeks in May and July 2026 (youm7). No Ramadan data.

### gamal-abdel-nasser-museum — low
- **Operator:** Ministry of Culture (Fine Arts Sector), not the Bibliotheca Alexandrina.
- 10/5 Egyptian, 20 foreign (fineart page and elwatan 2021). No newer price found.
- **Hours:** fineart 10:00–16:00 vs elwatan 2021 10:00–15:00 (public) and 09:00–15:00. **10:00–15:00 used**, closed Mon and Fri.
- **Ramadan:** the sector-wide 10:00–14:00 is assumed to apply.
- **Photos:** Commons has no image of the house. Two public-domain historical photos of Nasser are used (see D7).

### gayer-anderson-museum — high
- 100/50, 10/5. 09:00–17:00, last entry 16:00; Ramadan 09:00–15:00, last entry 14:00. All sources agree.
- The Gayer-Anderson Cat (British Museum) is deliberately not listed.

### imam-al-shafii-mausoleum — medium
- **Hours conflict:** MoTA guide 09:00–17:00 vs portal 09:00–16:00. **16:00 used.**
- **`prices.status` free** rests on "It's free of charge" on the portal's *Imam al-Shafi'i Mosque* page, which the seed links for this dome (see D5).
- The operator was left as the seed's `other`, although the MoTA SCA guide lists the dome.

### manial-palace-museum — medium
- 220/110 foreign; Egyptian 60 adult / **20** student on both official pages.
- **Ramadan conflict:** MoTA 09:00–15:00 (last entry 14:00) vs booking platform last entry 15:00. **14:00 used.**

### mukhtar-museum — medium
- **Hours:** 09:00–16:00, closed Mon and Fri (sector head, youm7, 4 Jun 2026). The undated sector page says 10:00–16:00.
- **Prices** 5/3 Egyptian, 10 foreign: undated sector page only (stale, see D1).
- **Not verified:** the exact location of the tomb (basement vs garden), and the number of works (85 vs ~175), so neither is given.

### museum-of-islamic-ceramics — low
- **Hours conflict:**
  - Sector decision (youm7, 16 Feb 2025): 09:00–21:00, Friday closed.
  - maspero.eg (National Media Authority, 28 Jan 2026): 09:30–13:30, Friday closed.
  - At reopening (Oct 2024): 09:00–16:00.
  - **09:30–13:30 used** (see D2).
- **No official price.** maspero gives 25 foreign / 15 resident / 15 foreign student, with the Egyptian figure missing. `prices.status` unconfirmed.

### museum-of-modern-egyptian-art — low
- **Summer 2026 hours:** 09:00–15:00 and 17:00–20:00, from the sector head, closed days not stated.
- **Closed days:** Monday closed and Friday afternoon-only come from the Feb 2025 decision, so Friday is set to 17:00–20:00 only. The winter schedule is unknown (D3).
- **Prices** 10/5 Egyptian, 20 foreign: undated sector page (D1).
- **Seed Arabic name** "مركز الجزيرة للفن الحديث" is the Gezira Art Center, not this museum. Kept per the rules (D6).

### national-police-museum — medium
- **Hours:** the portal says 08:00–17:00, ticket window 16:00; the MoTA guide says 09:00–17:00. **08:00 used**, consistent with D5 for the Citadel.
- **Ramadan:** 09:00–15:00, last entry 14:00 (MoTA).
- **Prices:** the Citadel ticket (the page's 200/100 is stale).
- **Operator:** left as `interior`.

### obelisk-of-senusret-i — medium
- 200/100, 10/5. 08:00–17:00, last entry 16:00; Ramadan 09:00–16:00, last entry 15:00. Official sources agree.
- **Not verified:** any open-air display around the obelisk. The Virgin Mary's Tree is listed as a nearby, separately ticketed highlight.

## Decisions needed (recommended answer in **bold**)

1. **Fine Arts Sector prices** (Mukhtar 5/3/10; Modern Art and Nasser 10/5/20) come only from undated `fineart.gov.eg` pages that are visibly stale:
   **(a) Keep them as confirmed per the "live official page" rule, and verify by phone.**
   (b) Set `prices.status` to unconfirmed.
2. **Islamic Ceramics hours:**
   **(a) 09:30–13:30, Fri closed (maspero Jan 2026, shorter).**
   (b) 09:00–21:00, Fri closed (sector decision, Feb 2025).
   (c) Omit hours.
3. **Modern Art Museum:** the summer split schedule is set as the weekly hours:
   **(a) Keep it until a winter schedule is announced.**
   (b) Use the Feb 2025 09:00–21:00 schedule.
4. **Geological Museum hours and price:** official sources have none.
   **(a) Leave them empty.**
   (b) Use cairo360 (09:00–15:00, closed Fri and Sat, EGP 25), marked low confidence.
5. **Imam al-Shafi'i shown as free:** the portal's "free of charge" is on the adjoining mosque's page.
   **(a) Keep `free`.**
   (b) Set it to unconfirmed, like Ibn Tulun.
6. **Seed Arabic name for `museum-of-modern-egyptian-art`:**
   **(a) Change it to "متحف الفن المصري الحديث" in the seed.**
   (b) Keep it.
7. **Nasser Museum photos:** Commons has no image of the house.
   **(a) Keep the 2 public-domain historical photos of Nasser for now.**
   (b) Drop the photos (this fails the validator's ≥1-photo rule).
   (c) Source a free photo of the house.
8. **Railway Museum on Fridays** (closed only per cairo360):
   **(a) Keep Friday closed.**
   (b) Open daily, as youm7 2024 says.
9. **Operators for monuments that MoTA lists but another body runs** (Amr: Awqaf; al-Shafi'i: SCA dome plus Awqaf mosque; Police Museum: Interior):
   **(a) Keep the seed values.**
   (b) Switch them to `mota-sca`.
10. **Military Museum:** keep 16:00 close, with no Ramadan exception?
    **(a) Yes.**
    (b) Inherit the Citadel's 17:00 and Ramadan rows.

## Scheduled rechecks

- Al-Gawhara reopening (SCA projects sector).
- Geological Museum site (Nile-front inventory).
- Fine Arts Sector winter 2026–27 schedule (Modern Art, Ceramics).
- Ramadan 2027 announcements for all 20 places.

## Photos

56 files, all checked through the Commons API: CC0, public domain, CC BY 2.0/3.0/4.0 and CC BY-SA 2.5/3.0/4.0, with licence strings verbatim.

- **Freedom of panorama:** no modern building or modern artwork is a main subject.
  - The 1962 Mukhtar Museum, the 1980s–90s Police Museum building and the Modern Art Museum building are avoided.
  - Mukhtar's own sculptures are shown (he died in 1934).
  - The Modern Art Museum uses PD works by Mukhtar and Ali El-Ahwani (d. 1954).
  - The Geological Museum shows fossils, not the building.
  - The Ceramics Museum shows the 1920s palace and a Fatimid bowl (CC0).
- Borderline images were checked visually: the Police Museum door, terrace view and wall sign; the Railway locomotive; the Mukhtar works.
