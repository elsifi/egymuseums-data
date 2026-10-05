# Batch 10 enrichment report

Checked 2026-10-05. 28 minor places in Cairo/Giza: mashrabia-art-gallery, mostafa-kamel-museum, museum-of-egyptian-capitals, museum-of-folklore-arts, museum-of-the-national-library-of-egypt, naguib-mahfouz-museum, people-s-assembly-museum, petrified-forest-protectorate-open-air-museum, prince-wahid-selim-museum, qasr-al-eini-museum, revolution-command-council-museum, science-museum, talaat-harb-pasha-museum, zaafarana-palace, abu-al-dahab-mosque, al-muayyad-mosque, al-zahir-baybars-mosque, bayt-al-harawi, fustat, hosh-al-basha, house-of-gamal-al-din-al-dhahabi, house-of-sitt-wasila, khanqah-of-faraj-ibn-barquq, maimonides-synagogue, mawlawiyya-takiyya, prince-taz-palace, sabil-kuttab-of-nafisa-al-bayda, sabil-kuttab-of-qaitbay.

`python3 tools/validate_all.py`: 24 of my files are `ok`. The other **4 fail only on "at least one photo required"** (Gamal al-Din al-Dhahabi, Mashrabia, Egyptian Capitals, Science Museum). Commons has no usable photo of them, and the house rule says to leave `photos` empty in that case. See question 1.

Every file has:
- an English description of 118–159 words, with the Arabic written separately;
- 2–5 highlights;
- sources with `checkedAt` 2026-10-05.

Ramadan exceptions run 2027-02-08 to 2027-03-08.

## Summary

| | count | places |
|---|---|---|
| **open** | 18 | Mostafa Kamel, Folklore Arts, National Library museum, Naguib Mahfouz, Petrified Forest, Mashrabia, Abu al-Dahab, al-Muayyad, al-Zahir Baybars, Bayt al-Harawi, Hosh al-Basha, al-Dhahabi, Sitt Wasila, Faraj ibn Barquq, Mawlawiyya, Taz, Nafisa al-Bayda, Sabil-Kuttab of Qaitbay |
| **closed** | 1 | Museum of Egyptian Capitals (built, never opened) |
| **renovation** | 1 | Fustat (excavation area being developed inside the Fustat Hills Gardens, Aug 2026) |
| **unknown** | 8 | People's Assembly, Wahid Selim, Qasr al-Eini, Revolution Command Council, Science Museum, Talaat Harb, Zaafarana, Maimonides |
| confidence high / medium / low | 5 / 12 / 11 | high: Mostafa Kamel, Harawi, Dhahabi, Sitt Wasila, Nafisa |
| prices confirmed / free / unconfirmed | 8 / 1 / 19 | free: Mostafa Kamel (official Fine Arts Sector page) |
| online booking (egymonuments.com) | 4 | Harawi, Dhahabi, Sitt Wasila, Nafisa al-Bayda |

**Searches.** I made 22 WebSearch calls in total, no more than 2 per place. Everything else came from direct fetches:
- the MoTA open-sites guide pages (slugs found by guessing);
- egymonuments.gov.eg and egymonuments.com;
- the Nov 2024 MoTA ticket list;
- Wikipedia EN/AR;
- the Fine Arts Sector and Cultural Development Fund (CDF) sites;
- dated Arabic press.

## Read this first

1. **Ministry of Culture houses.** Taz Palace, Bayt al-Harawi (Arab Oud House), Sitt Wasila (House of Arab Poetry) and the Naguib Mahfouz Museum are SCA monuments run as CDF cultural centres. Harawi and Sitt Wasila are still sold on the MoTA booking platform. Taz has no price on any MoTA channel.
2. **Prices from the Nov 2024 PDF only.** Abu al-Dahab, Hosh al-Basha and the Sabil-Kuttab of Qaitbay have no portal or booking page, so I followed the batch-7 Q4a precedent: `confirmed`, with the PDF as source.
3. **Four non-SCA museums have no verifiable public access:** People's Assembly, Revolution Command Council, Qasr al-Eini and Talaat Harb. All four are `unknown`/`low`.
4. **Arab tier.** None is used. SCA sites have none from 2026, and the Ministry of Culture museums here are free or unpriced.

## Per place: unverified items and conflicts

**mashrabia-art-gallery** (open, low)
- A commercial gallery. Its status rests on dated exhibitions in 2025 and up to Jan 2026.
- No hours, no address (two street names are in circulation), and its website is dead (404).
- No photo.

**mostafa-kamel-museum** (open, high)
- Hours: 10:00–16:00, closed Mon and Fri. The Fine Arts Sector's dated summer-2026 statement and the official visitor page agree.
- Free entry, from the official page.
- The Ramadan hours (10:00–14:00) are sector-wide and assumed to apply here.
- The photos show the 1949 mausoleum (Q6).

**museum-of-egyptian-capitals** (closed, medium)
- The SCA said it was "100% complete, ready to open" (31 Dec 2024).
- It is absent from the booking platform and the MoTA guide.
- The number of capitals is inconsistent in the source, so none is given.
- No photo.

**museum-of-folklore-arts** (open, low)
- Governorate changed from cairo to **giza** (Q4).
- Visits are arranged through the Academy of Arts. There is an Aug 2026 open day.
- No hours or price.
- The photo is a thematic stand-in (Q2).

**museum-of-the-national-library-of-egypt** (open, medium)
- The coordinates point to the Corniche building, not to Bab al-Khalq (Q5).
- Hours from 2020 were not used.
- The price is unknown: free open days imply a normal paid entry.

**naguib-mahfouz-museum** (open, low)
- Hours conflict:
  - official site (page dated 2019, still live): 09:00–14:00 and 17:00–21:00;
  - press, 2020: 09:00–17:00, closed Tuesday.
- I used the official site (Q7). There are many dated 2026 events.

**people-s-assembly-museum** (unknown, low)
- The museum is inside the old parliament building, which was vacated in Dec 2025.
- No public access has been documented.
- No coordinates.

**petrified-forest-protectorate-open-air-museum** (open, medium)
- Coordinates filled from Wikidata Q12241337, the protectorate (Q15).
- Ticketing was confirmed in Jan 2026, but no fee amount was found.
- Hours appear only in a travel guide, so they are not used.

**prince-wahid-selim-museum** (unknown, low)
- A development project was announced in Jul 2025. The museum is on neither of the Fine Arts Sector's 2026 lists (open or closed).
- The operator in the seed is `unknown` (Q13).
- The photo is a stand-in: Prince Youssef Kamal's portrait.

**qasr-al-eini-museum** (unknown, low)
- A faculty museum with no public hours.
- The 1827 founding date of the medical school is general knowledge.
- The photo is the faculty gate (stand-in).

**revolution-command-council-museum** (unknown, low)
- Fitted out as a museum, but no opening was found. Press from Jul 2025 still asks for it to be put "on the tourist map".
- No coordinates.
- The photo is the 1953 council photo (stand-in).

**science-museum** (unknown, low)
- Only a two-sentence ar-wiki stub exists. There is no location, operator or photo (Q3).

**talaat-harb-pasha-museum** (unknown, low)
- The museum is inside Banque Misr's working head office. Visits are arranged by the bank, and there is a virtual tour.
- No coordinates.

**zaafarana-palace** (unknown, low)
- The basement museum opened in May 2023, and public entry was announced as free.
- No 2024–2026 confirmation was found.

**abu-al-dahab-mosque** (open, medium)
- Hours from the MoTA guide; prices from the 2024 PDF.
- It is unknown whether the ticket covers the Mahfouz museum in the takiyya (Q14).

**al-muayyad-mosque** and **al-zahir-baybars-mosque** (open, medium)
- Working mosques. No hours are published and the price is `unconfirmed` (D9).
- Baybars: the photos predate the 2023 reopening.

**bayt-al-harawi** (open, high)
- The booking platform, MoTA guide and PDF agree.
- The date of al-Harawi's ownership conflicts between sources (1798 vs 1881), so none is given.
- The photos show oud classes inside the house; there is no architectural photo.

**fustat** (renovation, medium)
- Works are ongoing on the excavation hill (youm7, 19 Aug 2026).
- The 2024 list price (Egyptian 10/5, foreign 20/10) is not shown (Q8).

**hosh-al-basha** (open, medium)
- Prices from the PDF; hours from the MoTA guide.
- en-wiki's date of 1854 and its burial list conflict with MoTA, so MoTA is used.

**house-of-gamal-al-din-al-dhahabi** (open, high)
- Every official channel agrees.
- **No photo exists on Commons.**

**house-of-sitt-wasila** (open, high)
- Every official channel agrees. The photos are small (693 px).

**khanqah-of-faraj-ibn-barquq** (open, medium)
- Hours 09:00–16:00 from the portal. No price.

**maimonides-synagogue** (unknown, low)
- No hours or ticket on any MoTA channel.
- The photography-permission note comes from a search summary, so the text is worded softly.

**mawlawiyya-takiyya** (open, medium)
- The portal price matches the PDF.
- No coordinates in Wikidata.
- MoTA's theatre date "1255 AH / 1810 AD" is internally inconsistent, so the text says "nineteenth century".

**prince-taz-palace** (open, medium)
- No fee on the MoTA list ("–"), so the price is `unconfirmed` (Q11).
- The 1992 earthquake and the restoration are general knowledge.

**sabil-kuttab-of-nafisa-al-bayda** (open, high)
- Ramadan conflict: the guide closes at 16:00, while the booking platform gives last entry 16:00. I used the earlier time: close 16:00, last entry 15:00.

**sabil-kuttab-of-qaitbay** (open, medium)
- The only official source is the 2024 PDF: 09:00–17:00 and prices. Open status is also supported by cairo360 (Mar 2026).
- No last entry and no Ramadan hours.

## Decisions needed (recommended answer in **bold**)

1. **The validator requires a photo, but the house rule says to leave `photos` empty** (Dhahabi, Mashrabia, Capitals, Science Museum):
   **(a) Make "no photo" a warning when `curationNote` records that no compliant photo exists.**
   (b) Add thematic stand-ins as well.
   (c) Hide these places until a photo exists.
2. **Thematic stand-in photos** (Folklore: 1925 Mahmal; People's Assembly: 1922 dome plan; Wahid Selim: Youssef Kamal portrait; RCC: 1953 council photo; Qasr al-Eini: faculty gate):
   **(a) Keep them until real photos appear (each is noted in `curationNote`).**
   (b) Remove them and accept validator errors.
3. **Mashrabia (a commercial gallery) and the Science Museum (no evidence it exists):**
   **(a) Drop both from the dataset.**
   (b) Keep them as `unknown`/`low`.
4. **Folklore Arts governorate** (changed from cairo to giza; the Academy of Arts is in al-Haram, and Wikidata P131 says Giza):
   **(a) Keep giza.**
   (b) Revert to the seed.
5. **National Library museum location and name.** The coordinates point to the Corniche HQ, not the museum. The name is title-cased ("Museum Of The National Library Of Egypt").
   **(a) Override the coordinates locally to Bab al-Khalq (about 30.0444, 31.2526) and fix the name to "Museum of the National Library of Egypt".**
   (b) Keep both as they are.
6. **Mostafa Kamel building photos** (the mausoleum was completed in 1949):
   **(a) Keep them: the building predates the post-1950s cut-off.**
   (b) Drop them.
7. **Naguib Mahfouz hours:**
   **(a) Keep the live official page (two daily sessions) at `low` confidence and confirm by phone.**
   (b) Remove the hours.
8. **Fustat:**
   **(a) Keep `renovation` with the price unconfirmed until the gardens' archaeological zone opens.**
   (b) Mark it `open` with the 2024 list price.
9. **Museum of Egyptian Capitals:**
   **(a) Keep `closed` ("not yet opened").**
   (b) Use `unknown`.
   (c) Hide it.
10. **PDF-only prices** (Abu al-Dahab, Hosh al-Basha, Sabil-Kuttab of Qaitbay):
    **(a) Keep them `confirmed`, as batch-7 Q4a did.**
    (b) Mark them `unconfirmed`.
11. **Taz Palace price** (the MoTA list shows "–"):
    **(a) `unconfirmed` (D9).**
    (b) `free`.
12. **Prince Wahid Selim operator** (`unknown` in the seed; all sources say Ministry of Culture):
    **(a) Set it to `ministry-of-culture`.**
    (b) Keep the seed value.
13. **Does the Abu al-Dahab SCA ticket also cover the Naguib Mahfouz Museum?**
    **(a) Keep them separate and ask the hotline (19654).**
    (b) Set `includedIn`.
14. **Petrified Forest coordinates** (taken from the protectorate's Wikidata item Q12241337):
    **(a) Keep them.**
    (b) Leave them null.

## Rechecks

- Fustat Hills Gardens: watch for the opening of the archaeological zone.
- Museum of Egyptian Capitals: watch for an inauguration.
- Wahid Selim: watch for reopening after the development project.
- Ramadan 2027: announced hours for the SCA houses and the Fine Arts Sector.
