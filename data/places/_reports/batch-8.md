# Batch 8 enrichment report

Checked 2026-10-05. 28 minor places: alexandria-hydrobiological-museum, alexandria-museum-of-fine-arts, alexandria-underwater-museum, arabic-calligraphy-museum, cavafy-museum, history-of-science-museum, manuscripts-museum, planetarium-science-center, sadat-museum, abu-mena, anfushi-necropolis, mostafa-kamel-necropolis, shatby-necropolis, aswan-excavations-museum, aswan-museum, aswan-nile-museum, amada-temple, elkab, gebel-el-silsila, sehel-island, wadi-el-sebua, college-museum-university-of-assiut, national-museum-of-asyut, al-hammamiya-tombs, meir-tombs, alwan-house, baramus-monastery, fort-qaitbay-rosetta.

**Validation:** 22 of the 28 files pass `python3 tools/validate_all.py`. The other 6 fail only on "at least one photo required", because no compliant photo exists (see "Read this first", item 1). Every file has:
- an English description of 119–148 words, with the Arabic written separately;
- `verifiedAt` 2026-10-05;
- Ramadan 2027 exceptions dated 2027-02-08 to 2027-03-08 where an official Ramadan row differs from the normal week.

## Read this first

### 1. Six places have no compliant photo, so the validator fails them

The house rule says to leave `photos` empty when nothing compliant exists. The validator treats an empty `photos` array as an error. The six places:

| id | why there is no photo |
|---|---|
| arabic-calligraphy-museum | The only Commons file shows the modern façade under works. |
| history-of-science-museum | Every candidate shows the modern BA/PSC building. |
| planetarium-science-center | Every candidate shows the 2002 planetarium sphere. |
| aswan-nile-museum | No Commons files exist, and the building dates from 2016. |
| college-museum-university-of-assiut | No Commons files exist. |
| alwan-house | No Commons files exist. |

See decision 1.

### 2. Status by evidence

| status | places |
|---|---|
| open (20) | hydrobiological, fine arts, Cavafy, manuscripts, planetarium, Sadat, Abu Mena, Anfushi, Mustafa Kamel, Shatby, Aswan excavations annex, Amada, El-Kab, Silsila, Sehel, Wadi el-Sebua, Hammamiya, Meir, Baramus, Rosetta fort |
| renovation (3) | Arabic Calligraphy Museum (youm7, Jun 2026), History of Science Museum (BA page "closed for maintenance"), Aswan Museum main building (closed since 2010; works began 2024) |
| closed (1) | Alexandria Underwater Museum (never built) |
| unknown (4) | Aswan Nile Museum, College Museum Asyut, National Museum of Asyut, Alwan House |

Confidence: high 11, medium 13, low 4.

### 3. Where the data comes from

- **SCA sites:** three official sources, all live and checked 2026-10-05:
  - the egymonuments.gov.eg portal;
  - egymonuments.com booking pages, with keys found on `/locations`;
  - the MoTA Arabic "open sites/museums guide".

  The Nov 2024 MoTA ticket PDF was used as a cross-check. It is the **only** price source for Anfushi, Mustafa Kamel and the Rosetta fort, used as was done for temple-of-hibis.
- **Bibliotheca Alexandrina** (Manuscripts, Sadat, Planetarium, History of Science):
  - bibalex.org admission page for prices;
  - bibalex.org home-page opening-hours box, which is dated by its notes for October 2026.
- **Ministry of Culture** (Fine Arts, Calligraphy): youm7 statements by the sector head (4 Jun 2026 and 26 Jun 2026) plus the sector's stale visitor page.
- **Others:**
  - NIOF's own museum page;
  - press reports: Cavafy (May 2024), Aswan Museum (May 2024 director interview), Asyut (Mar 2025), Baramus (Jan 2025).
- **Web searches:** 9 in total, at most 2 per place.
- **Link check:** all 176 cited URLs return HTTP 200 except three behind bot protection:
  - niof-eg.com museum and aquarium pages: their content was read through WebFetch;
  - the Ahram daily item: it could not be read.

## Per place

### alexandria-hydrobiological-museum — open, medium
- **Hours:** the NIOF page (live, undated) gives winter 09:00–18:00 and summer 09:00–24:00, open every day including holidays.
  - Summer start and end dates are not published, so `weekly` uses the winter hours. The late summer evenings are mentioned only in `statusNote`. See decision 4.
- **Price:** no price is published, so `unconfirmed`. The page lists only discounts.
- **Photos:** 1 photo, the whale skeleton. The EWUG photo of the entrance was rejected because it shows modern signage and screens.

### alexandria-museum-of-fine-arts — open, medium
- **Hours:** 09:00–18:00, closed Monday and official holidays (youm7, 4 Jun 2026).
  - Friday 13:00–18:00 comes from the Feb 2025 decision. The narrower window was used.
- **Prices:** foreign 20, Egyptian 10, Egyptian student 5, plus 6 free groups. All come from the official visitor page, which still says "closed, moving to a new building" and is clearly stale. This follows the batch-5 D1a pattern.
- **Photos:** one public-domain 1895 painting in the collection. The 1954 building is excluded.
- **Wording:** the founding collector's name differs between sources (Friedheim / "Farid Heim"), so the description leaves it out.

### alexandria-underwater-museum — closed, medium
- The museum is a proposal that was never built. There are no coordinates.
- The Nov 2024 list has an "Underwater Antiquities" line (EGP 35/35, 180/90). That is a **dive permit**, not a museum ticket. It is only mentioned in `crowdNotes`. See decision 6.

### arabic-calligraphy-museum — renovation, medium
- It sits inside the Fine Arts complex and opened on 22 Aug 2015 (official sector page).
- On 26 Jun 2026 the sector head inspected "renovation and development works" (youm7).
- The seed operator `other` was changed to `ministry-of-culture`.

### cavafy-museum — open, medium
- **Hours and price:** reopened 12 May 2024. Open daily except Monday, 10:00–17:00, and **free**. Source: the head of the Alexandria regional tourism authority, quoted by elwatannews on 17 May 2024.
- **Unverified:** Before 2022 entry cost 15/5 (Wikipedia), and the Onassis pages are script-rendered and unreadable. See decision 3.

### history-of-science-museum — renovation, medium
- **Status:** BA labels it "closed for maintenance". `hours` are omitted and `prices` is `unconfirmed`, as for Rashid. The BA list still shows its old prices.
- **Coordinates:** borrowed from the BA building (Q501851).

### manuscripts-museum — open, high
- **Hours:** BA hours, Sun–Thu 09:30–17:00, Sat 10:00–14:00, Fri closed.
- **Prices:** 60/30 foreign; 20/10 Egyptian, senior 10. Inclusive-ticket extras mirror the BA Antiquities Museum record.
- **Rule:** no children under 12.
- **Coordinates:** borrowed from Q501851.

### planetarium-science-center — open, high
- **Prices:** the planetarium show is used for the tiers (foreign 200; Egyptian 50/20, senior 50). ALEXploratorium and the 12D theatre are extras.
- No photos.

### sadat-museum — open, high
- **Location resolved:** this is the Bibliotheca Alexandrina museum, not Mit Abu al-Kum.
- **Operator:** changed to `other` (BA).
- **Price:** the BA Main Library ticket, which includes the museum: foreign 150/20, Egyptian 10/5, senior 5.
- **Photos:** two public-domain photos of Sadat, following the Nasser-museum precedent.
- **Time-limited:** the `statusNote` line about the October 2026 "Sadat panorama" expires after 31 Oct 2026.

### BA-wide time-limited exception
- On **Thu 8 Oct 2026** (October War holiday), BA opens 10:00–14:00. This is a dated one-day exception on manuscripts, planetarium and sadat.
- Remove it after 8 Oct 2026.

### abu-mena — open, medium
- **Hours:** 07:00–19:00, last entry 18:00. Ramadan 09:00–16:00. The MoTA guide and Nov 2024 list agree.
- **Price:** none is listed ("-" in the PDF), so `unconfirmed` (D9). See decision 5.
- The 2025 removal from UNESCO's danger list (EN Wikipedia) is not stated in the user text.

### anfushi-necropolis — open, medium
- **Conflict:** the guide says it opens at 08:00; the PDF says 09:00. **09:00 used** (narrowest window).
- **Price:** 100/50 and 10/5, from the PDF only.

### mostafa-kamel-necropolis — open, medium
- **Hours:** 09:00–17:00 (guide and PDF). There is no Ramadan row.
- **Price:** 100/50 and 10/5, from the PDF only.

### shatby-necropolis — open, high
- The portal, guide and PDF agree: 09:00–17:00, 100/50, 20/10, Ramadan 09:00–16:00.

### aswan-excavations-museum — open, medium
- **Identification:** this is the **Aswan Museum annex** (MoTA guide "متحف أسوان الملحق"), which shows the German mission's finds. It was built in 1993 and reopened in 2017.
- **Hours conflict:** the guide says 08:00–17:00; the island site closes at 16:00. **16:00 used**, last entry 15:00. Ramadan 09:00–15:00.
- **Price:** `includedIn: elephantine-island`, mirroring its tiers. No separate ticket exists on any list. See decision 2.
- **Coordinates:** borrowed from the Aswan Museum.

### aswan-museum — renovation, medium
- **Status:** closed since 2010. Works started in March 2024, with opening planned about two years later (director interview, May 2024). No 2026 reopening news was found.
- Dec 2025 Commons photos show building materials at the site.
- **Founding date:** 1912 vs 1917, so the description says "the 1910s".

### aswan-nile-museum — unknown, low
- **Operator:** Ministry of Irrigation.
- No source newer than 2022 was found. Older hours conflict (09:00–21:00 vs 07:00–17:00), so `hours` are omitted.

### amada-temple, wadi-el-sebua — open, high
- The portal, booking page, guide and PDF agree: 07:00–16:00, last entry 15:00, 150/75 and 10/5.
- The Ramadan row equals the normal week, so there is no Ramadan exception.

### elkab — open, high
- 07:00–17:00, last entry 16:00. 200/100 and 10/5.
- Parking extras come from the booking-date page.
- **City:** Edfu added.

### gebel-el-silsila, sehel-island — open, high
- 07:00–16:00, last entry 15:00. 100/50 and 10/5.
- **City:** Kom Ombo added for Silsila.

### college-museum-university-of-assiut — unknown, low
- **Identity unclear:** Wikidata only says "museum of the university of Assiut with Egyptian antiquities". It may be the historic American "Assiut College" collection.
- **Coordinates:** borrowed from Assiut University (Q246534).
- No hours, prices, photos or highlights. See decision 7.

### national-museum-of-asyut — unknown, low
- **Identification:** taken to be the Alexan Pasha Palace project. Coordinates come from Q29514123.
- **Status:** works were ongoing "ahead of opening to the public" (masrawy, Mar 2025). An Ahram daily item of 29 Aug 2025 headlined "finally sees the light" returned 403, so **it may have opened**. Recheck.

### al-hammamiya-tombs, meir-tombs — open, high
- The guide, booking page and PDF agree: 08:00–17:00, last entry 16:00. Ramadan 09:00–16:00, last entry 15:00. 100/50 and 10/5.
- **Meir city:** "Cusae" (the ancient name) was replaced by El-Qusiya.
- **Meir photos:** only 1 photo.

### alwan-house — unknown, low
- It is not on any MoTA channel. Which houses the "Rosetta City Monuments" ticket covers is unknown, so there is no `includedIn` and the price is `unconfirmed`. See decision 8.

### baramus-monastery — open, medium
- **Hours:** 08:00–17:00 (Nov 2024 list only). No last entry.
- **Feast-day closures:** in Jan 2025 visits were closed on the 24th for the Maximus and Domitius feast. No 2027 exception has been added.
- **Price:** `unconfirmed` (D9).

### fort-qaitbay-rosetta — open, medium
- **Hours:** 08:30–16:00, last entry 15:00. Ramadan 09:00–16:00 (guide and PDF).
- **Price:** 30/15 and 10/5, from the PDF only. This is a separate ticket from Rosetta City Monuments.
- Unlike rosetta-historic-houses, which only mentions the fort, this record carries prices. See decision 9.

## Decisions needed (recommended answer in **bold**)

1. **Empty photos versus the validator** (6 places):
   **(a) Allow an empty `photos` array for minor places when the record's `curationNote` says why, by relaxing the validator rule to a warning.**
   (b) Use a loosely related public-domain image (for example, calligraphy by the masters named, or a Nile painting).
   (c) Hide these places until a photo exists.
2. **Aswan excavations museum = Aswan Museum annex, included in the Elephantine ticket:**
   **(a) Keep it as a separate place with `includedIn: elephantine-island`.**
   (b) Fold it into elephantine-island as a highlight and drop the record.
3. **Cavafy "free" entry** (official quote from May 2024; it was paid before 2022):
   **(a) Keep `free` and confirm with the museum or the Greek consulate.**
   (b) Set the price to `unconfirmed`.
4. **Hydrobiological museum summer evening hours** (to 24:00, dates unpublished):
   **(a) Keep winter hours in `weekly` with a `statusNote` mention, until NIOF publishes dates.**
   (b) Add an undated summer exception.
5. **Abu Mena price** (no fee on the 2024 list):
   **(a) Keep `unconfirmed` and ask hotline 19654 (D9).**
   (b) Mark it free.
6. **Underwater museum:**
   **(a) Keep it as `closed` (never built) with the dive-permit note.**
   (b) Remove it from the app.
   (c) Turn it into an "Eastern Harbour underwater antiquities" dive site priced from the 2024 list.
7. **College Museum, University of Assiut** (identity unclear, no data):
   **(a) Hide it from the app until it is identified.**
   (b) Keep it as `unknown`/`low`.
8. **Alwan House** (unclear whether visitable):
   **(a) Keep it as `unknown`/`low` and ask the Rosetta antiquities office whether the Rosetta ticket covers it.**
   (b) Fold it into rosetta-historic-houses as a highlight.
9. **Rosetta Qaitbay fort price** (30/15, 10/5, Nov 2024 list only):
   **(a) Keep it as confirmed here (temple-of-hibis pattern). rosetta-historic-houses stays unpriced for the fort.**
   (b) Set it to `unconfirmed`, matching batch-4 D6.
10. **Borrowed coordinates** (BA building for Manuscripts and History of Science; Aswan Museum for its annex; university campus for the College Museum; Alexan Palace for the Asyut museum):
    **(a) Keep them, noted in `curationNote` (BA precedent).**
    (b) Set them to null.

## Scheduled rechecks

- **After 8 Oct 2026:** remove the BA 2026-10-08 exception from manuscripts-museum, planetarium-science-center and sadat-museum.
- **After 31 Oct 2026:** remove the Sadat panorama line from sadat-museum `statusNote`.
- **Now:** the National Museum of Asyut status, following the Ahram item of 29 Aug 2025.
- **2026–27:** Aswan Museum reopening (planned for about 2026); Calligraphy Museum reopening; History of Science Museum reopening.
- **Winter 2026–27:** Fine Arts Sector winter schedule for alexandria-museum-of-fine-arts.
- **Early 2027:** Ramadan 2027 announcements, and the Baramus feast closure around 23–24 Jan 2027.
