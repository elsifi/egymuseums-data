# Batch 2 enrichment report

Checked 2026-10-04. 10 places: hanging-church, ibn-tulun-mosque, dahshur, qaitbay-citadel, graeco-roman-museum, kom-el-shoqafa, karnak, luxor-temple, valley-of-the-kings, temple-of-hatshepsut. All 10 files pass the stdlib schema check (the `check()` function in `tools/seed/validate.py`, 0 errors).

## Sources used and how they were ranked

1. **egymonuments.com/details/<X>** is MoTA's official ticketing site. It gave current prices with "Other Nationality" and Egyptian tiers, and it no longer has an Arab tier. It also gave the free-entry policy and the "Last Entry" times for summer, winter and Ramadan.
2. **egymonuments.gov.eg** gave the weekly hours, prices and descriptions, plus services for the Graeco-Roman Museum.
3. **The MoTA open-sites visitor guide (mota.gov.eg, Arabic)** gave hours, Ramadan hours and addresses, and states that last entry is one hour before closing.
4. **Arabic news from 2026** (elwatannews, vetogate, masrawy, youm7) gave the summer 2026 schedules, the Ramadan 2026 schedule and sound & light times.

Every price matches the MoTA list dated 2024-11-05 (`tools/seed/cache/mota_tickets.txt`). The amounts therefore have not changed since at least Nov 2024. Only the audience structure changed on 2026-01-01, when the Arab tier was abolished (masrawy, 2025-07-10). I could not find the date of the decision that set these amounts, so **`effectiveFrom` is left empty everywhere**.

The schema allows only `{ar, en}` strings for `highlights`, so each highlight is written as "Title — one-line description".

## Applies to all places

- **`cashAccepted` is null everywhere.** A cashless system at the nine Luxor sites was announced in June 2023 (Egypt Independent), and a Visa-only rule was reported at the Graeco-Roman reopening in Oct 2023. Qaitbay's April 2026 coverage says its tickets are "fully electronic" but does not say card-only. The September 2026 youm7 story on the CPS system covers tour-company bulk purchases only. I found no 2025–2026 official statement of card-only payment for individual visitors. **Human decision:** accept the 2023 sources and set `false` for the Luxor sites, or keep null.
- **`timedEntry` is null everywhere.** egymonuments.com did not show whether bookings use time slots.
- **Camera / photography fees.** egymonuments.com says only "Photography with mobile phone is free of charge". The commonly quoted 300 EGP Valley of the Kings camera pass comes only from blogs, so **I left it out.**
- **Summer and winter windows.** The 2026 summer schedule ran from 2026-04-24 to the last Friday of October (2026-10-30), according to the Luxor articles. The `weekly` block holds the standard schedule from gov.eg/MoTA, which matches the winter "Last Entry" times on egymonuments.com. Summer is stored as an exception. The winter 2026–27 Luxor schedule has not been published yet, so it needs a recheck after 2026-10-30.
- **Ramadan closing times.** For Karnak, Luxor Temple, Valley of the Kings and Hatshepsut, egymonuments.com gives only the opening time and last entry for Ramadan, so no closing time is set.
- **Contacts.** No official per-site website or phone exists apart from the MoTA hotline 19654 and the egymonuments.com support line, so `contacts` is omitted. A Facebook page "St. Mary-The Hanging Church (@TheHangingChurch)" exists, but I could not confirm it is official.

## Per place

### hanging-church — confidence: medium
- **Price:** no ticket is listed. MoTA's guide page has no "buy ticket" link, gov.eg shows no price and the 2024 list has blank cells. I stored this as `freeGroups: ["all visitors …"]`, and **this needs human confirmation**. A separate church donation or charge was not checked.
- **Hours:** daily 09:00–16:00, the same in Ramadan, with last entry at 15:00 by MoTA's general one-hour rule. The site may close for liturgies; I could not verify service times.
- **Conflicts:**
  - Pulpit: gov.eg says ten columns and 11th century; MoTA says 13 columns and 14th century. The description says only "slender columns".
  - Oldest icon: gov.eg says 15th century; Wikipedia gives an older date. The text uses gov.eg.
  - Founding date: MoTA says 4th–5th century. The text says only "late antiquity".
- Only 2 photos are used. I rejected a candidate showing a modern exterior mosaic (Egypt has no freedom of panorama).

### ibn-tulun-mosque — confidence: medium
- **Price:** free, inferred the same way as the Hanging Church (no ticket on MoTA, gov.eg or the 2024 list). Needs confirmation, including whether the minaret climb is charged.
- **Hours:** 09:00–17:00, Ramadan 09:00–16:00 (MoTA). Closures at prayer time were not confirmed; the Friday-prayer advice in `crowdNotes` is general guidance.
- I found no 2025–2026 report of restoration or closure. A 2024 Asharq al-Awsat story about sewage seepage was not followed up.

### dahshur — confidence: high
- **Prices:** foreign 200/100, Egyptian 10/5, consistent across gov.eg, egymonuments.com and the 2024 list.
- **Hours:** 08:00–17:00, last entry 16:00; Ramadan 09:00–16:00 (MoTA).
- **Not verified:** whether the Bent Pyramid interior (opened 2019) and the Red Pyramid interior are both open in Oct 2026. The description mentions entering only the Red Pyramid. gov.eg describes wooden stairs into the Bent Pyramid's north entrance.
- **Data issue:** the seed has `city` = "Markaz al Badrashayn" from Wikidata. I left it unchanged.

### qaitbay-citadel — confidence: high
- **Hours:** winter 09:00–18:00 (MoTA). Summer 2026 was 09:00–20:00 with the ticket window closing at 19:00 (masrawy, 2026-04-26), which matches egymonuments.com's summer last entry of 19:00. Ramadan 2026 was 09:00–16:00 with the window closing at 15:00 (youm7, 2026-02-18).
- **Conflict:** gov.eg shows 09:00–20:00 all year. I treated that as the summer schedule.
- **Sound & light (stored as a note only):** shows at 20:30 and 21:30 in summer 2026. Masrawy also quoted show prices (about 1,350 EGP for foreigners); these are not stored because they are not an SCA ticket.
- 2 photos are used; I rejected a night shot with crowds and modern lighting.

### graeco-roman-museum — confidence: medium
- **Hours conflict:**
  - gov.eg (English and Arabic): Sun–Thu 09:00–17:00 with the ticket window closing at 16:30; Fri–Sat 09:00–20:00 with the window closing at 19:00; Ramadan 09:00–16:00 with the window closing at 15:00.
  - egymonuments.com: Sun–Thu last entry **15:00**; Fri–Sat last entry 19:00.
  - I used gov.eg because it is the venue page. **A human should decide.**
  - The English gov.eg "insider tips" also has a typo ("sunday & friday") that contradicts its own table, which says Fri & Sat.
- **Highlights:** chosen from Commons photos taken after the 2023 reopening (Marcus Aurelius, Septimius Severus) and from undated uploads (the Hadrian bust and Osiris-Antinous by Allan Gluck). Whether each object is on display today was not verified piece by piece; the Pharos coins and Tanagra figurines especially should be checked against the current galleries.
- **Address:** given as "Graeco-Roman Museum Street"; I did not confirm a house number.

### kom-el-shoqafa — confidence: medium
- The seed has no egymonuments.gov.eg page for this site. Hours come from MoTA (09:00–17:00, Ramadan 09:00–16:00); prices and last entry come from egymonuments.com (foreign 200/100, Egyptian 30/10).
- **Not verified:** whether the lowest level, which has historically been flooded by groundwater, is accessible today. Accessibility notes about steep stairs and no lift are general and unsourced; reword or drop them if that is required.
- The 1900 discovery date and the "Hall of Caracalla" tradition come from Wikipedia. I wrote the text myself.

### karnak — confidence: medium
- **Prices:** foreign 600/300 covers Karnak and the Open-Air Museum (gov.eg says so explicitly). Egyptian 40/20. Mut Temple extra: foreign 200/100, Egyptian 10/5.
- **Hours conflict:**
  - gov.eg and MoTA: 06:00–17:00. egymonuments.com: last entry 16:00 in all seasons, including summer.
  - The April 2026 news gives summer 06:00–18:00. That implies a 17:00 last entry under MoTA's one-hour rule, but egymonuments.com still says 16:00.
  - I left `lastEntry` off the summer exception. **A human should decide.**
- The Avenue of Sphinxes is shared with Luxor Temple, and its ticketing was not checked separately. The 2024 list says it is visited on the Karnak/Luxor tickets.
- A July 2026 youm7 story mentions a new VR experience in the Karnak plaza; it is not included.

### luxor-temple — confidence: medium
- **Hours conflict:**
  - gov.eg and MoTA: 06:00–20:00; egymonuments.com: last entry 19:00 in all seasons.
  - April 2026 news (elwatan, vetogate): summer **07:00–21:00**, with no last entry given.
  - Many travel sites claim it closes at 22:00, which no official source supports.
  - The winter 2026–27 schedule is unknown.
- Prices: foreign 500/250, Egyptian 40/20, consistent across sources.

### valley-of-the-kings — confidence: high
- **Prices:** general ticket foreign 750/375, Egyptian 60/30.
- **Extras (gov.eg tomb pages, matching the 2024 list):**
  - KV62 Tutankhamun: foreign 700/350, Egyptian 40/20.
  - KV17 Seti I: foreign 2000/2000, Egyptian 500/250.
  - KV9 Ramesses V & VI: foreign 220/110, Egyptian 30/10.
- **Not included:**
  - The tomb of Ay (WV23, West Valley) was priced at 200/100 in the 2024 list, but no 2025–2026 source confirms it.
  - Neither the official list of tombs open on the general ticket in Oct 2026 nor the "three tombs" rule is confirmed by an official source. The text says only "a rotating selection".
  - The electric shuttle ("tuf-tuf") from the visitor centre and its fee are not included.
- **Hours:** standard 06:00–17:00 with last entry 16:00; summer 2026 06:00–18:00 with last entry 17:00 (news plus egymonuments.com, which agree).

### temple-of-hatshepsut — confidence: medium
- **Price conflict:** gov.eg's Hatshepsut Temple page, egymonuments.com and the 2024 list all give foreign **440/220**, Egyptian 40/20. The gov.eg *Deir al-Bahari* site page still shows **360/180**, which looks outdated. I used 440/220.
- **Hours:** same as the Valley of the Kings, since the Qurna area shares one schedule.
- **Wikidata issue:** the seed notes a duplicate item, Q373909 vs Q660692, which still needs resolving.

## Photos

All 28 photos were checked through the Commons API (`extmetadata` LicenseShortName/Artist). Every one is CC0, CC BY or CC BY-SA, and the subjects are ancient or historic architecture and artefacts. `url` is the direct upload URL and `sourceUrl` is the file page.

Two licence strings need a human eye:
- **"CC BY 3.0 pl"** (Hanging Church interior) is a ported CC BY licence.
- **"Darer101", "Asmaa.khallaf12" and "Rowyda elshaer"** are own-work uploads by individual users. The licences look fine; I did not check whether the uploads are genuine.
