# Batch 6 enrichment report

Checked 2026-10-04. Places: october-war-panorama, qaitbay-funerary-complex, rawda-nilometer, royal-carriages-museum, umm-kulthum-museum, virgin-marys-tree, wikala-of-al-ghuri, wadi-al-hitan, agricultural-museum, imhotep-museum, mit-rahina-museum, mohamed-mahmoud-khalil-museum, colossi-of-memnon, deir-el-medina, esna-temple, karnak-open-air-museum, mummification-museum, ramesseum, tombs-of-the-nobles-luxor, valley-of-the-queens.

All 20 files pass `python3 tools/validate_all.py` (schema v1.1, 0 errors). Each has a 157–196-word English description and a matching Arabic one written from scratch, 4–6 highlights, and 2–3 Wikimedia Commons photos (licence and author from the Commons API).

## How the hours and prices are backed

- **SCA sites (14):** the same official channels as earlier batches, all live and undated, checked 2026-10-04.
  - `egymonuments.com/details/<Site>` and `/book-date/<n>` (per-ticket price fields): prices, add-on tickets, parking, last entry by season, free-entry groups.
  - `egymonuments.gov.eg`: open and close times, prices, ticket-window times. Only about half of the 14 have their own portal page.
  - The MoTA "open sites/museums guide" (`mota.gov.eg/ar/...دليل-...-جديد/<site>/`): open and close times, Ramadan close, address, and the "last entry one hour before closing" rule.
  - MoTA Nov 2024 PDF: cross-check only.
- **Online vs gate prices:** no gap between the booking platform and the portal for any of these places, so there is no `onlineAmount`.
- **Arab tier:** none (dostor 5134866).
- **Luxor summer:** the 2026 summer exception (2026-04-24 to 2026-10-30) is dated from the Luxor antiquities announcement (elwatannews 8271816, vetogate 5641700): Qurna zone 06:00–18:00, Karnak 06:00–18:00. Last entries come from the booking platform. **The winter 2026–27 schedule had not been announced on 4 Oct**; the standard `weekly` rows are the published winter hours. Recheck after 30 Oct.
- **Ramadan:** every exception runs 2027-02-08 to 2027-03-08 with the standard `curationNote`.
- **Not set:** `cashAccepted` (no 2025–26 official statement for any place), and `effectiveFrom` except Wadi Al-Hitan, which has a dated decree.
- **Non-SCA venues:**
  - Ministry of Defence: Panorama.
  - Ministry of Culture: Umm Kulthum Museum (Cultural Development Fund page) and Mohamed Mahmoud Khalil Museum (Fine Arts Sector page plus dated sector statements).
  - Ministry of Agriculture: Agricultural Museum, from dated news quoting the ministry.
  - Ministry of Environment (EEAA): Wadi Al-Hitan, from the signed fee decree.
- **Research limits:** the session's WebSearch budget ran out partway through. Later checks used WebFetch, curl on official pages, and DuckDuckGo/Bing results fetched with curl.

## Places

Today is Sunday 4 Oct 2026; **bold** = the Luxor summer schedule in force today.

| id | conf. | foreign adult (EGP) | Egyptian adult (EGP) | Sun 4 Oct hours (last entry) | online ticket | photos |
|---|---|---|---|---|---|---|
| october-war-panorama | medium | unconfirmed (free 3–6 Oct) | unconfirmed | 09:00–15:00 + 17:00–21:00 | no | 2 |
| qaitbay-funerary-complex | medium | unconfirmed | unconfirmed | 09:00–16:00 | no | 3 |
| rawda-nilometer | high | 120 | 20 | 09:00–17:00 (16:00) | yes | 3 |
| royal-carriages-museum | high | 300 | 30 | 09:00–17:00 (16:00) | yes | 3 |
| umm-kulthum-museum | medium | 20 | 5 | 09:00–16:00, Tue closed | no | 3 |
| virgin-marys-tree | high | 120 | 10 | 09:00–17:00 (16:00) | yes | 3 |
| wikala-of-al-ghuri | high | 100 | 10 | 09:00–17:00 (16:00) | yes | 3 |
| wadi-al-hitan | medium | USD 15 (in EGP) | 50 | not published | no | 3 |
| agricultural-museum | low | — | 20 | 09:00–15:00 (halls) | no | 3 |
| imhotep-museum | medium | 600 (Saqqara ticket) | 30 | 08:00–17:00 (16:00) | yes | 3 |
| mit-rahina-museum | high | 200 | 10 | 08:00–17:00 (16:00) | yes | 3 |
| mohamed-mahmoud-khalil-museum | medium | 100 | 30 | 09:00–18:00, Mon closed | no | 3 |
| colossi-of-memnon | medium | unconfirmed | unconfirmed | 06:00–17:00 | no | 3 |
| deir-el-medina | medium | 220 (+Pashedu 120) | 10 | **06:00–18:00 (17:00)** | yes | 3 |
| esna-temple | medium | 200 | 20 | 07:00–18:00 (17:00) | yes | 3 |
| karnak-open-air-museum | medium | 600 (Karnak ticket) | 40 | **06:00–18:00 (16:00)** | yes | 3 |
| mummification-museum | medium | 220 | 20 | **09:00–? (12:00) + 17:00–? (19:00)** | yes | 3 |
| ramesseum | high | 220 | 20 | **06:00–18:00 (17:00)** | yes | 3 |
| tombs-of-the-nobles-luxor | medium | 120–200 per tomb group | 10–20 | **06:00–18:00 (17:00)** | yes | 3 |
| valley-of-the-queens | medium | 220 | 30 | **06:00–18:00 (17:00)** | yes | 3 |

## Cross-batch issue (outside this batch's files)

**Imhotep Museum is recorded as open here, but `saqqara.json` says it is closed for restoration.**
- **Evidence for open:**
  - Its own MoTA museums-guide page lists hours (08:00–17:00; Ramadan 09:00–15:00).
  - elwatannews (27 Apr 2026) describes it open daily.
  - Research notes report it reopened in Dec 2023 after closing in Mar 2022, with a temporary exhibition in June 2026 (Maspero).
- **Evidence for closed:** only the Saqqara page of the same MoTA guide.
- `saqqara.json` was not edited (see decision 1).

## Per place

### october-war-panorama — medium
- **Hours:** the official MoD page gives daily 09:00–15:00 (3 tours of 2 h) and 17:00–21:00 (2 tours). Split into two sessions; no `lastEntry`, because the last tour start times are not stated.
- **Conflict on closed day:** the MoD page says every day; elwatannews (2021) says Tuesday closed; aggregators say Friday. The official page is followed.
- **Price unconfirmed:** the MoD page lists what the ticket covers but no amounts. Figures from 2021 news and aggregators conflict.
- **Free entry 3–6 Oct 2026** (elbalad, shorouknews): in `statusNote`. Remove it after 6 Oct.
- **Photos:** only war hardware in the yard (Su-20, MiG-21). The 1989 building and its painted panorama are modern works, so they are not used.

### qaitbay-funerary-complex — medium
- **Hours:** portal, 09:00–16:00 daily. No ticket on any official channel, so `prices.status` is unconfirmed (as D9).
  - The "Sabil-Kuttab of Sultan Qaitbay" on the Nov 2024 list is a different monument (Saliba Street).
- **Dome restoration** completed July 2026 (elwatannews, maspero). The upper floor has long been closed (sinai.news, Aug 2026; not official).
- **Not verified:** street address, and whether Awqaf or the SCA manages visits. Operator kept as `other`.

### rawda-nilometer — high
- Portal, booking platform and guide agree: 120/60, 20/10; 09:00–17:00, last entry 16:00; Ramadan close 16:00, last entry 15:00.
- **Not claimed:** the Manasterly Palace being "within Nilometer ticket". That comes only from the Nov 2024 list.
- City changed from "Rhoda Island" (seed) to "Cairo"; the island is in `area`.

### royal-carriages-museum — high
- Prices and hours agree across all three channels.
- **Ramadan** (MoTA guide, undated): 09:00–15:00 daily, plus 19:00–23:00 on Friday and Sunday. Evening `lastEntry` 22:00 comes from the guide's one-hour rule (decision 12).
- Phone from Wikidata (not verified with the museum).

### umm-kulthum-museum — medium
- **CDF official page:** daily 09:00–16:00 except Tuesday; Egyptians 5 (student 2), foreigners 20 (student 10). elwatannews (Apr 2026) agrees.
- No last entry published.
- **Photos:** objects only. The 2001 interior and the modern memorial sculpture outside are not used.

### virgin-marys-tree — high
- 120/60, 10/5; 09:00–17:00, last entry 16:00; Ramadan close 16:00, last entry 15:00. Restored and reopened Sept 2022 (MoTA guide).
- The 1 June feast date in `bestTime` is general knowledge, not from a MoTA source.

### wikala-of-al-ghuri — high
- 100/50, 10/5; 09:00–17:00, last entry 16:00.
- **Tanoura show:** the CDF calendar puts it at the Ghuri Dome across the street (Wed and Sat 19:30), not in the Wikala. Only the location and nights are used. The CDF price (15 Egyptian / 90 foreign) may be stale and is not shown.

### wadi-al-hitan — medium
- **Fees:** Ministerial Decision 360 of 2025 (EEAA PDF; issued 2 Dec 2025, effective 15 Dec 2025). Egyptians EGP 50, foreigners USD 15 charged in EGP at the CBE daily rate; camping EGP 250 / USD 25. Free: Egyptian children under 12 with a guardian, Egyptians 60+, people with disabilities.
  - **Conflict:** the EEAA HTML fee table still shows the old 25 EGP / USD 10. The decree is followed.
- **Not verified:**
  - Whether the Wadi El Rayan fee (EGP 25 / USD 10, car EGP 20) is also charged on the way; only third parties say so. It is mentioned as advice without amounts.
  - Opening hours. Only non-official sites say 08:00–17:00, so `hours` is omitted.
  - A separate museum fee.
  - Whether a 4x4 is required.

### agricultural-museum — low
- **Status:** trial opening from 16 Aug 2025 (youm7, quoting the ministry); open in Oct 2026.
- **Price:** EGP 20 "per visitor" for the Flowers of Egypt exhibition, explicitly including the museum halls (vetogate and dostor, 1 Oct 2026). Recorded as the Egyptian adult tier only.
  - **Conflict on foreign price:** EGP 150 (2025 pages) vs "USD 3" (dostor, Sept 2025). No foreign tier.
  - Parking EGP 25 (youm7, Apr 2026).
- **Hours:** halls until 15:00; the grounds 09:00–21:00.
- **Not verified:** a closed day (an aggregator says Friday), the address details, and the official website and phones.

### imhotep-museum — medium
- **Status:** see the cross-batch issue above.
- **Prices:** the portal says the Saqqara ticket (600/300, 30/10) includes the museum. elwatannews' 450/230 looks outdated.
- **Ramadan:** 09:00–15:00 (museum guide page), last entry 14:00 by the one-hour rule.
- **Not verified:** the Djoser statue base naming Imhotep. Wikipedia says it was a short loan in 2006; the MoTA guide and elwatannews (2026) list it on display. Kept as a highlight.

### mit-rahina-museum — high
- 200/100, 10/5; 08:00–17:00, last entry 16:00; Ramadan 09:00–16:00, last entry 15:00.
- **Parking:** the booking platform says microbus 50; the Nov 2024 list says 75. The booking platform is used.
- The colossus that moved to GEM is the Ramses Square statue, not this one.

### mohamed-mahmoud-khalil-museum — medium
- Reopened April 2021, after the 2010 theft closure; active in 2026.
- **Hours conflict** (decision 9):
  - Fine Arts Sector summer-2026 statement (youm7, 4 Jun 2026): daily 09:00–18:00 except Monday and official holidays. **Used.**
  - Feb 2025 decision: Friday 13:00–18:00.
  - Official fineart.gov.eg page (undated, stale): 10:00–16:00, Monday and Friday closed.
- **Ramadan:** sector-wide 10:00–14:00 (Ramadan 2026 statement, which does not name this museum).
- **Prices** from the official page (undated): 100/50 foreign, 30/10 Egyptian, foreign teaching staff 50. Free: veterans, over-65s, under-6s, Syndicate of Plastic Artists members.
- **Not verified:** which named works are currently hung; the highlights list artists only.

### colossi-of-memnon — medium
- **Hours:** 06:00–17:00 (MoTA guide).
- **Price unconfirmed:**
  - No booking-platform page.
  - The guide page has no online-ticket link.
  - The Nov 2024 list shows dashes.
  - "Free" appears only in non-official guides.
- **No summer exception:** the Qurna 06:00–18:00 schedule is not stated for the Colossi (decision 13).
- **Not verified:** public access to the Kom el-Hettan temple area. `statusNote` says it is not open.

### deir-el-medina — medium
- 220/110, 10/5, plus Pashedu (TT3) 120/60, 10/5; parking 25/50/75/100.
- **Conflict:** the booking platform shows last entry 17:00 in all seasons. 16:00 is used for winter and Ramadan, the earlier time (decision 7).
- **Not verified:** which tombs are open.
  - A non-official Aug 2026 report lists Inherkhau (TT359), the Amennakht family tomb (TT218–220) and Pashedu.
  - Sennedjem (TT1) is named in the MoTA guide but not confirmed open, so it is not a highlight.

### esna-temple — medium
- 200/100, 20/10.
- **Hours conflict on Sun/Tue/Fri** (decision 6):
  - Booking platform: 07:00–18:00. **Used** (the earlier time), with last entry 17:00.
  - MoTA guide: 07:00–19:00.
  - Nov 2024 list: 07:00–17:00.
  - Other days: 07:00–17:00, last entry 16:00.
- **Not verified:** the reason for the longer days (cruise schedules?), the 2018 start of the Egyptian–German project (official news pages are undated), and Wikalat al-Gedawi being on the same ticket (Nov 2024 list only; not claimed).

### karnak-open-air-museum — medium
- **Modelled as its own place, but there is no separate ticket.** The portal sells an "inclusive ticket allowing entry into Karnak Temple and Open Museum". Tiers repeat the Karnak ticket (decision 3).
- Hours mirror `karnak.json`, including the D3 summer last entry of 16:00.
- **Portal trap:** `egymonuments.gov.eg/en/monuments/open-air-museum/` is the Tell Basta museum. Not linked.
- **Not verified:** the walking directions in `bestTime` ("left of the first court").

### mummification-museum — medium
- **Hours:** portal 09:00–14:00 and 17:00–21:00.
  - **Conflict on evening last entry:** portal 20:00 vs booking platform 19:00. 19:00 is used.
  - **Summer:** last entries 12:00 and 19:00 only (booking platform), dated to the Luxor summer.
- **Ramadan conflict** (decision 8): MoTA guide 09:00–15:00 (one session) vs booking platform two sessions. The guide is used, with the earlier 13:00 last entry.
- **Highlights are kept generic.** Wikipedia names the Masaharta mummy and the Padiamun coffin, but their current display could not be confirmed. The highlights match objects in Dec 2025 Commons photos (crocodile, coffin with mummy, ankh).

### ramesseum — high
- 220/110, 20/10, plus parking. Portal, booking platform and guide agree.
- **Restoration:** Egyptian–Korean restoration of the first pylon's north tower; block lifting from 1 Oct 2026, completion 2027. There is also a plan to move the entrance to the east side (elwatannews 8360839, masrawy, Sept 2026). This is in `statusNote` and `crowdNotes`.

### tombs-of-the-nobles-luxor — medium
- **There is no single ticket** (decision 2). Tiers show the most common group price (120/60, 10/5); every group is in `extras`:

  | Group | Foreign adult / student | Egyptian adult / student |
  |---|---|---|
  | Rekhmire & Sennefer | 120 / 60 | 10 / 5 |
  | Nakht & Menna | 200 / 100 | 20 / 10 |
  | Ramose | 200 / 100 | 20 / 10 |
  | Khonsu & Userhat | 120 / 60 | 10 / 5 |
  | el-Khokha | 120 / 60 | 10 / 5 |
  | Qurnet Murai | 120 / 60 | 10 / 5 |
  | Dra Abu el-Naga north | 120 / 60 | 20 / 10 |
  | Dra Abu el-Naga south | 50 / 25 | 20 / 10 |

- **Not verified:**
  - The exact tombs in each group (booking labels give one name). "Khonsu & Userhat" follows the Nov 2024 list. Whether Userhat (TT56) and Khaemhat (TT57) go with Ramose is unknown.
  - The low south Dra Abu el-Naga price (50). The Egyptian tab lists north and south in the opposite order.
- The Seti I temple at Qurna appears on the same booking page; it is a separate monument and is left out.

### valley-of-the-queens — medium
- 220/110, 30/10, plus parking. The booking platform offers only the general ticket.
- **Nefertari (QV66) closed** since March 2024. On 18 Sep 2026 the ministry said reopening is under study, with strict limits on numbers and visit duration; no date or price (masrawy, maspero). No extra is shown (decision 11).
  - Last known price (Nov 2024 list): foreign 2,500, Egyptian 600, Egyptian student 300.
- **Not verified:** which tombs are open. QV44, QV52 and QV55 come from a non-official Aug 2026 report.
- **Photo:** the Nefertari image was swapped for a CC0 facsimile from QV55, so no picture of the closed tomb is shown.

## Photos

- 59 photos, 2–3 per place. Licence strings are Commons' own.
- **Licence quirk** (decision 14): Amr F.Nagy uploads (Egypt Wikimedians) show "Public domain" in the Commons API `LicenseShortName`, but the file pages carry `{{self|cc-by-sa-4.0}}`. **CC BY-SA 4.0** was recorded for the 2 affected agricultural-museum files.
- **No freedom of panorama — avoided:**
  - the Panorama building and paintings;
  - the 2006 Imhotep Museum building;
  - the 1997 Mummification Museum interior;
  - the Royal Carriages courtyard under its modern glass roof;
  - modern sculptures at the Agricultural Museum and on Rawda;
  - the 2016 Wadi Al-Hitan museum building.
- **Checked visually:** the borderline images (Mummification, Royal Carriages, Panorama, Agricultural Museum).

## Decisions needed (recommended answer in **bold**)

1. **Imhotep Museum open or closed?**
   **(a) Open in both records: update `saqqara.json` `statusNote` and the all-inclusive label.**
   (b) Keep both "closed" until an on-site or hotline check.
   (c) Leave the two records inconsistent.
2. **Tombs of the Nobles: no single ticket.**
   **(a) Tiers = the common 120/60 group price, with all groups in `extras`.**
   (b) `prices.status` unconfirmed, with the groups only in text.
   (c) Schema change for component-only pricing.
3. **Karnak Open-Air Museum covered by the Karnak ticket.**
   **(a) Tiers repeat the Karnak ticket, plus a `statusNote`.**
   (b) `prices.status` unconfirmed, with a note.
   (c) Add a schema field such as `includedIn: "karnak"`.
4. **Colossi of Memnon free?**
   **(a) Keep unconfirmed until MoTA (hotline 19654) confirms.**
   (b) Mark free, because no ticket is listed anywhere.
5. **Wadi Al-Hitan USD fee.**
   **(a) Egyptian EGP tier plus `usdPegged`/`usdAmount` 15 for foreigners.**
   (b) Convert to EGP at the CBE rate and refresh monthly.
   (c) Add a per-tier currency to the schema.
6. **Esna Sun/Tue/Fri closing.**
   **(a) 18:00 (booking platform; the earlier official time).**
   (b) 19:00 (MoTA guide).
7. **Deir el-Medina winter and Ramadan last entry.**
   **(a) 16:00 (earlier, consistent with 17:00 closing).**
   (b) 17:00 (booking platform).
8. **Mummification Museum Ramadan.**
   **(a) One morning session (MoTA guide), last entry 13:00.**
   (b) Two sessions (booking platform).
9. **Mohamed Mahmoud Khalil hours.**
   **(a) The June 2026 sector statement (daily 09:00–18:00, Monday closed).**
   (b) The undated official page (10:00–16:00, Monday and Friday closed).
10. **Agricultural Museum price.**
    **(a) Egyptian EGP 20 only; recheck when the flower exhibition ends.**
    (b) `prices.status` unconfirmed.
11. **Nefertari while closed.**
    **(a) No extra; `statusNote` explains.**
    (b) List the last known price with a "closed" label.
12. **Royal Carriages Ramadan evening session (Fri/Sun 19:00–23:00, MoTA guide).**
    **(a) Keep it.**
    (b) Drop it until the Ramadan 2027 announcement.
13. **Colossi summer hours.**
    **(a) No summer exception.**
    (b) Apply the Qurna 06:00–18:00.
14. **Commons licence mismatch (Amr F.Nagy uploads).**
    **(a) Record the file-page tag (CC BY-SA 4.0).**
    (b) Use the API's "Public domain".
    (c) Swap the photos.

## Scheduled rechecks (no decision needed)

- **After 6 Oct 2026:** remove the Panorama free-entry `statusNote`.
- **After 30 Oct 2026:** the Luxor winter 2026–27 schedule for the 7 Luxor SCA records. The summer exceptions end on 30 Oct.
- **Winter 2026:** whether Mohamed Mahmoud Khalil's Friday afternoon-only opening returns.
- **When the Flowers of Egypt exhibition ends:** the Agricultural Museum price and hours.
- **2027:** the Ramesseum entrance move and the end of the pylon restoration; the Nefertari reopening.
