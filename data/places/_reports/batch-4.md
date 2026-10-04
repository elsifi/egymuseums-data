# Batch 4 enrichment report

Checked 2026-10-04. Places: abu-al-abbas-al-mursi-mosque, alexandria-national-museum, bibliotheca-alexandrina-antiquities-museum, kom-el-dikka, mahmoud-said-museums-center, pompeys-pillar, royal-jewelry-museum, crocodile-museum, elephantine-island, kalabsha-temple, monastery-of-st-simeon, qubbet-el-hawa, unfinished-obelisk, deir-al-muharraq, rashid-national-museum, rosetta-historic-houses, meidum-pyramid, abdeen-palace-museum, abu-serga-church, al-azhar-mosque.

All 20 files pass `python3 tools/validate_all.py` (0 errors). Each English description is 163–197 words, with 4–7 highlights and 2–3 Wikimedia Commons photos.

## How the data is backed (read this first)

- **SCA sites and museums (13):** three official MoTA channels, all live and undated, checked 2026-10-04:
  - `egymonuments.gov.eg` portal pages: opening and closing times, prices, Ramadan hours and ticket-window times (museums only), free groups.
  - `egymonuments.com/details/<Key>` booking pages: prices, last entry, summer/winter/Ramadan rows, free groups. Keys found from `egymonuments.com/locations`.
  - MoTA's Arabic open-sites and museums guide (`mota.gov.eg/ar/…/دليل-…-جديد/<name>/`): hours, Ramadan closing, address, and the rule "last entry one hour before closing".
  - The Nov 2024 MoTA PDF was used only as a cross-check.
- **Other operators:**
  - Bibliotheca Alexandrina's own admission pages (BA museum).
  - The Fine Arts Sector site plus a dated youm7 report of its decision (Mahmoud Said).
  - Arabic news, because no official page was found (Abdeen, Rashid museum status, Mursi square works, Muharraq Lent closure).
- **Arab tier:** none, following the SCA change from 1 Jan 2026 (dostor 5363965).
- **Foreign-resident tier:** not shown on any official page, so not added.
- **`cashAccepted`:** not set anywhere. No official 2025–26 statement was found.
- **`timedEntry`:** `null` for every place.
- **`effectiveFrom`:** not set anywhere. No dated decision was cited.
- **Ramadan exceptions:**
  - Added only where the Ramadan schedule really differs, dated 2027-02-08 to 2027-03-08 with the standard `curationNote`.
  - Where the official Ramadan row equals the normal week (Elephantine, Kalabsha, St Simeon, Unfinished Obelisk, Abu Serga), no exception was added. See decision 13.
- **Photos:** 58 files, all checked through the Commons API for licence and author (CC0, PD, CC BY 2.0/3.0, CC BY-SA 2.0–4.0).
  - Subjects are ancient sites, artefacts, or historic buildings and interiors from before the 1950s: the 1919 Royal Jewelry palace, the 1870s Abdeen palace, the late-1920s National Museum villa, and the Mursi mosque of 1930s–40s design.
  - No photo of the modern Bibliotheca Alexandrina building is used.
  - Thumbnails of borderline candidates were checked visually. A door-only Abu Serga shot and a modern walkway at Pompey's Pillar were swapped out.
- **Search budget:** the session's web-search budget ran out near the end. Direct page fetches still worked, but two minor cross-checks could not be run: Mahmoud Said 2026 hours and Royal Jewelry summer evening hours. They are listed under rechecks below.

## Per place

### abu-al-abbas-al-mursi-mosque — confidence: medium
- **Not verified:** official visiting hours. Ministry of Awqaf mosque; none were published, so `hours` is omitted.
- **Price:** `prices.status: unconfirmed` (D9).
- **Status:** works on the square were 90% complete in Sept 2026 and are due to finish at the end of 2026 (youm7 18 Sep 2026). This is mentioned in `statusNote`; recheck early 2027.

### alexandria-national-museum — confidence: high
- **Conflict (Ramadan last entry):** the portal says the ticket window closes at 14:00; the booking page says 15:00. **D3 applied: 14:00**, with closing at 15:00.
- Prices 220/110 and 20/5 agree on the portal, the booking page and elwatannews (Apr 2026).

### bibliotheca-alexandrina-antiquities-museum — confidence: high
- **Prices:** the museum's and the BA's own pages agree.
  - Egyptian: 20 adult, 10 student, 10 senior.
  - Foreign: 100 adult, 50 student.
  - Extras: inclusive tickets and camera fees.
- **Hours:**
  - Sun–Thu 09:30–16:45 (last ticket 16:30).
  - Sat 10:00–13:45 (last ticket 13:30).
  - Closed Friday.
  - No Ramadan schedule is published.
- **Online tickets:** `onlineticketing.bibalex.org` sells event tickets only, so `onlineUrl` is null and the platform is `onsite`.
- **Unclear:** the BA note "Egyptians over 70 free" sits under the inclusive ticket. It is not listed.
- **Coordinates:** the seed had none. I used the BA building (Q501851, 31.208889 / 29.909167). See decision 10.

### kom-el-dikka — confidence: high
- The portal, MoTA guide and booking page agree:
  - 09:00–17:00, last entry 16:00.
  - Ramadan 09:00–16:00, last entry 15:00.
  - Prices 200/100 and 20/10.
- **Free groups:** the booking page shows no free-entry list, so `freeGroups` is omitted.
- **Not verified:** whether the Villa of the Birds still needs a separate ticket. It did in the past.

### mahmoud-said-museums-center — confidence: medium
- **Conflict (hours):**
  - The undated official visitor page says 10:00–16:00, closed Monday and Friday.
  - A Feb 2025 Fine Arts Sector decision (youm7) set daily 09:00–21:00, Friday 15:00–21:00, Monday closed. **This was used.**
  - No 2026 confirmation was found. No last entry is published.
- **Prices:** foreign 20, Egyptian 10, Egyptian student 5 come only from the undated official page, so they may be outdated. No foreign-student price is published.
- **Photos:** two paintings uploaded by the Center itself (CC BY-SA 4.0). The artist died in 1964, so the works are public domain in Egypt. There is no usable photo of the villa.
  - Commons file `Mohamed Mahmoud Khalil Museum.jpg` is captioned "Mahmoud Said Museum" but shows a different building. It was not used.

### pompeys-pillar — confidence: high
- There is no `egymonuments.gov.eg` page.
- The MoTA guide (09:00–17:00; Ramadan to 16:00) and the booking page (last entry 16:00; Ramadan 15:00) agree.
- Prices 200/100 and 20/5.

### royal-jewelry-museum — confidence: high
- The portal and booking page agree:
  - 09:00–17:00, last entry 16:00.
  - Ramadan 09:00–15:00, last entry 14:00.
  - Prices 220/110 and 30/10.
- **Not verified:** whether summer evening openings exist in 2026. This could not be searched.

### crocodile-museum — confidence: high
- **Ticket:** the Kom Ombo combined ticket (450/225, 40/20); the portal says it is "inclusive". `onlineUrl` points to the KomOmboTemple booking page.
- **Conflict (Ramadan):**
  - The museum's portal page and the MoTA museum guide say 09:00–15:00, last ticket 14:00. **These were used.**
  - The existing kom-ombo-temple record uses the booking page's Ramadan row (07:00, last entry 20:00).
  - The two records therefore differ. See decision 3.

### elephantine-island — confidence: high
- **Conflict (last entry):**
  - The portal and MoTA guide close at 16:00, and the guide says last entry is one hour before closing.
  - The booking page says last entry 16:00, which is the closing time.
  - **D3 applied: 15:00.** See decision 2.
- **Not verified:** whether the small display of excavation finds that the portal mentions is open.

### kalabsha-temple — confidence: high
- The portal (07:00–16:00) and the booking page (last entry 15:00; 200/100, 10/5) agree.
- **Not verified:** whether the ticket also covers Beit el-Wali and the Qertassi kiosk on the same site.
- **Boat fare:** no official figure, so only described in `crowdNotes`.

### monastery-of-st-simeon — confidence: medium
- **Conflict (price):**
  - The portal says foreign adult 150, student 50.
  - The booking page and the Nov 2024 list say **100**/50. **100 was used**, by analogy with D4. See decision 1.
- Hours 07:00–17:00, last entry 16:00, agree across sources.

### qubbet-el-hawa — confidence: medium
- **Not on the booking platform:** `onlineUrl` is null and the platform is `onsite`.
- **Single source:** hours (07:00–16:00) and prices (200/100, 20/10) come from the portal only, matched by the Nov 2024 list.
- **Not published:** last entry, Ramadan hours and free groups.
- **Not verified:** which tombs are open, especially Sarenput II and Harkhuf.

### unfinished-obelisk — confidence: high
- The portal, MoTA guide and booking page agree: 07:00–16:00, last entry 15:00; prices 220/110 and 20/10.

### deir-al-muharraq — confidence: medium
- **Hours:** 09:00–17:00 (last entry 16:00) and Ramadan 09:00–16:00, from the MoTA guide.
  - Another non-official snippet said 08:00–18:00. It was not used.
- **Price:** no price in any source, so `unconfirmed`.
- **Lent closure:** the monastery closes for most of Great Lent (2026: 24 Feb–11 Apr, egyptke).
  - The 2027 dates are not announced. Orthodox Easter is 2 May 2027, so Lent probably starts in early March and overlaps Ramadan 2027.
  - For now this is only in `statusNote`. See decision 9.
- **Not used:** the Wikipedia claim about a 2013 arson attack. It is unsourced and possibly confused with another site.

### rashid-national-museum — confidence: medium
- **`status: renovation`.** The Prime Minister inspected the restoration works on 13 Jun 2026 (masrawy, ahram). No reopening date was found.
- `hours` and `tickets` are omitted, and `prices` is `unconfirmed`.
- Not on the booking platform.

### rosetta-historic-houses — confidence: medium
- **Conflict (hours):**
  - The booking page and the Nov 2024 list say 08:30–16:00, last entry 15:00.
  - The MoTA guide gives the Amasyali House as 09:00–17:00.
  - **The booking/PDF schedule was used** (earlier closing). See decision 7.
- **Price:** "Rosetta City Monuments" ticket, 120/60 and 10/5.
- **Not verified:** which houses this ticket covers.
- **Qaitbay fort (6 km north):** separately priced in Nov 2024 (foreign 30/15, Egyptian 10/5), with no 2025–26 source. It is not priced, only flagged as "may need a separate ticket". See decision 6.
- **Restoration:** the 2026 programme of restoration and pedestrian streets may close houses at times.

### meidum-pyramid — confidence: high
- The portal, MoTA guide and booking page agree:
  - 08:00–17:00, last entry 16:00.
  - Ramadan 09:00–16:00, last entry 15:00.
  - Prices 150/75 and 10/5.
- **Not verified:** whether the pyramid interior is currently open. It is handled as an "ask at the ticket office" tip.
- **Highlights:** the Meidum geese and the Rahotep and Nofret statues are described as being in the Egyptian Museum (Tahrir), which matches the MoTA guide and the egyptian-museum record.

### abdeen-palace-museum — confidence: low
- **No official page was found.** The palace is run by the Presidency's museums administration.
- **Hours:** Sat–Thu 09:00–15:00, Friday closed, from elwatannews (6 Apr 2026) citing the Cairo Governorate portal. A Dec 2022 announcement said open all week.
- **Prices conflict and are old:**
  - Dec 2022: Egyptians and Arabs 20, students 10; foreigners 100, foreign students 50.
  - Apr 2026: 20 adults, 5 students, audience unstated.
  - Set to `unconfirmed`. See decision 5.

### abu-serga-church — confidence: medium
- **Hours:** 09:00–16:00, last entry 15:00, agreed by the MoTA guide, the portal and the Nov 2024 list. Ramadan is the same.
- **Price:** `unconfirmed` (D9, same as Hanging Church).
- **Not verified:** the "crypt may be closed at times" note is general advice.

### al-azhar-mosque — confidence: medium
- **Hours:** the MoTA guide says only "according to its managing authority" (Al-Azhar), so `hours` is omitted.
- **Price:** `unconfirmed` (D9).

## Decisions needed (recommended answer in **bold**)

1. **St Simeon foreign adult price.** The portal says 150; the booking page and the Nov 2024 list say 100.
   **(a) 100, as recorded (same logic as D4).**
   (b) 150.
2. **Elephantine last entry.** The booking page says 16:00, which equals closing; the MoTA one-hour rule gives 15:00.
   **(a) 15:00, as recorded (D3).**
   (b) 16:00.
3. **Crocodile Museum and Kom Ombo Temple disagree on Ramadan hours.**
   **(a) Keep the museum's own 09:00–15:00 (portal plus MoTA guide) and recheck the temple in Ramadan 2027.**
   (b) Align the museum with the temple's booking row (07:00, last entry 20:00).
4. **Mahmoud Said hours and prices.**
   **(a) Keep the Feb 2025 extended hours and the 20/10/5 prices from the official page.**
   (b) Use the official page's 10:00–16:00 hours.
   (c) Mark the price `unconfirmed`.
5. **Abdeen prices.**
   **(a) Keep `unconfirmed` until confirmed by phone (02 2391 6909) or an official page.**
   (b) Use the Dec 2022 announcement (100/50, 20/10).
6. **Rosetta Qaitbay fort ticket.**
   **(a) Keep it as an unpriced note.**
   (b) Add the Nov 2024 prices as extras.
7. **Rosetta hours.**
   **(a) 08:30–16:00, last entry 15:00 (booking page plus PDF).**
   (b) 09:00–17:00 (Amasyali House page in the MoTA guide).
8. **Mosque, church and monastery prices** (Azhar, Mursi, Abu Serga, Muharraq).
   **(a) Keep `unconfirmed` (D9).**
   (b) Mark `free`. No official source says so.
9. **Muharraq Great Lent closure.**
   **(a) Keep it in `statusNote` and add a dated exception once the monastery announces the 2027 dates.**
   (b) Add an estimated exception now.
10. **BA museum coordinates** (borrowed from the BA building Q501851).
    **(a) Keep them, and add P625 to Q113289726 on Wikidata.**
    (b) Leave them null.
11. **Rashid National Museum while closed.**
    **(a) Keep the record with `status: renovation` and no hours or prices.**
    (b) Hide it from the app until it reopens.
12. **Qubbet el-Hawa last entry.**
    **(a) Leave it empty.**
    (b) Infer 15:00 from MoTA's one-hour rule.
13. **Ramadan rows identical to the normal week** (Elephantine, Kalabsha, St Simeon, Obelisk, Abu Serga).
    **(a) No exception (rule: real schedule changes only).**
    (b) Add "same hours" exceptions to match abu-simbel, kom-ombo and hanging-church. Those three could then be cleaned up the same way.

## Wikidata notes (no edits made)

- The seed already lists duplicate Wikidata items for crocodile-museum (Q63122572), kalabsha-temple (Q1721920), rashid-national-museum (Q45108397) and abdeen-palace-museum (Q307747). The seed IDs were kept.
- Q113289726 (BA Antiquities Museum) has no coordinates (P625).

## Scheduled rechecks

- **Nov–Dec 2026:**
  - Mahmoud Said 2026 hours.
  - Royal Jewelry seasonal hours.
  - Abu al-Abbas square reopening (expected end of 2026).
- **Jan–Feb 2027:**
  - Ramadan 2027 announcements.
  - The Muharraq Lent 2027 closure dates.
- **Any time:**
  - Rashid National Museum reopening.
  - Abdeen official prices.
  - Which houses the Rosetta ticket covers.
  - Qubbet el-Hawa open tombs.
  - The Meidum interior.
