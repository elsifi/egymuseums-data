# Batch 9 enrichment report

Checked 2026-10-05. 28 minor places: monastery-of-st-macarius, monastery-of-st-pishoy, syrian-monastery, beni-suef-museum, aisha-fahmy-palace, ali-labib-house, bayt-al-sinnari, beit-el-umma, beshtak-palace, cairo-airport-museum-terminal-2, cairo-airport-museum-terminal-3, child-museum, citadel-carriage-museum-former, citadel-prison-museum, confiscated-antiquities-museum, dr-naguib-pasha-mahfouz-museum, effat-naghi-saad-el-khadem-museum, egx-museum, egyptian-air-force-museum, egyptian-geographic-society-museum, egyptian-postal-museum, egyptian-textile-museum, espace-karim-francis, farouk-corner-museum, hassan-heshmat-museum, heliopolis-open-air-museum, helwan-wax-museum, hunting-museum-manial.

`python3 tools/validate_all.py`: 24 of 28 files pass. The other 4 fail only on "at least one photo required": both airport museums, effat-naghi-saad-el-khadem-museum and espace-karim-francis. No compliant Commons photo exists for them, so the photos are left empty as the house rule says (see question 1).

## Summary

| Status | Count | Places |
|---|---|---|
| open | 17 | 3 Wadi Natrun monasteries, Aisha Fahmy, Ali Labib, Sinnari, Beshtak, airport T2 and T3, Child Museum, Citadel Prison, Effat Naghi, Postal, Farouk Corner, Hassan Heshmat, Heliopolis open-air, Hunting Museum |
| closed | 5 | Beni Suef Museum, former Citadel carriage museum, Confiscated Antiquities, Naguib Pasha Mahfouz (not public), Textile Museum |
| renovation | 2 | Beit el-Umma, Helwan Wax Museum |
| unknown | 4 | EGX Museum, Air Force Museum, Geographic Society Museum, Espace Karim Francis |

Confidence: high 0, medium 14, low 14.

Prices:
- **Confirmed tiers:** Ali Labib, Farouk Corner, both airport museums, Effat Naghi and Hassan Heshmat.
- **Mirrored from the parent place (`includedIn`):**
  - Beshtak → al-muizz-street
  - Citadel Prison → cairo-citadel
  - Heliopolis open-air → obelisk-of-senusret-i
  - Hunting Museum → manial-palace-museum
- **Free:** Aisha Fahmy. Both the official Fine Arts page and a July 2026 report say entry is free.
- **Unconfirmed:** all other places.

Photos: every file was checked visually from its thumbnail, and licences were read from the Commons API. Excluded as modern buildings, interiors or artworks:
- modern bell towers, icons and paintings at the monasteries
- wax figures at the Citadel Prison and Helwan
- the 1990s Beni Suef and Child Museum buildings
- the airport terminals
- Hassan Heshmat's sculptures

Three files by Egypt Wikimedians uploaders show "Public domain" in extmetadata, but their file pages carry `{{self|cc-by-sa-4.0}}`, so CC BY-SA 4.0 is recorded. This is the same handling as agricultural-museum.

## Per place: unverified items and conflicts

### Wadi Natrun monasteries (St Macarius, St Pishoy, Syrian)
- **Hours:** 08:00–17:00 comes only from the Nov 2024 MoTA ticket list. The Syrian Monastery's portal page gives the same hours. No ticket is listed, so prices are unconfirmed.
- **St Macarius:**
  - Its own website says day visits are arranged by phone (+20 122 288 4278).
  - A search summary claimed "permit required, no group tours, closed in fasts", but I could not find that wording on the site, so the statusNote keeps a general caution.
  - The John the Baptist and Elisha relics are left out of the highlights because the claim is contested.
- **St Pishoy:** the monastery's own statement (youm7, 7 Apr 2025) closed it in Holy Week 2025 and reopened it afterwards.
- **Syrian:** the portal dates the Church of the Virgin to 645, while Wikipedia gives a later date. The prose gives no date.
- **Exceptions:** no fast-period exceptions were added, because no 2025–26 notice specific to any of the three monasteries was found. St Anthony has a projected one; see question 6.

### beni-suef-museum
- **Status: closed.** It is missing from the Nov 2024 MoTA list and from the MoTA guide. The latest detailed report (elbalad, Oct 2019) says it was emptied in 2012 and the works stopped in 2013.
- I found no 2024–26 news about it.
- The opening year conflicts: 1997 (AR wiki) against "early 1990s".

### aisha-fahmy-palace
- **Hours conflict:**
  - The official Fine Arts page (undated) says 10:00–13:30 and 17:30–21:30, closed Friday.
  - elwatannews (5 Jul 2026) says daily 09:00–21:00 and Friday 17:00–21:00.
  - The dated 2026 report is used, as in batch 5.
- **Builder:** AR Wikipedia contradicts itself (Aisha's father or her brother, both called Ali Fahmy Pasha). The prose says "the family of Ali Fahmy Pasha".

### ali-labib-house
- **Sources:** the portal, the MoTA guide and the Nov 2024 list all agree: 09:00–17:00 and 100/50/10/5. Ramadan 09:00–16:00 comes from the guide.
- **Operator:** the house is assigned to the Cultural Development Fund (House of Egyptian Architecture). The operator stays `mota-sca` as in the seed.
- **Date:** the guide's date is inconsistent (1051 AH printed as "1661 AD"), so no date is given.
- **Booking:** the house is not on egymonuments.com, so the platform is `onsite`.

### bayt-al-sinnari
- It is a Bibliotheca Alexandrina cultural centre, with events listed up to May 2026. No visiting hours or fee are published, so hours are omitted and the price is unconfirmed.

### beit-el-umma
- **Status: renovation.** The Fine Arts Sector head said on 16 Aug 2026 that the works would finish "within a year". It is not stated whether the museum is fully closed.
- **Hours and prices:** the official page shows 10:00–16:00 and 5/3/10, but these are withheld until it reopens.
- **Photo:** Commons has only the neighbouring mausoleum, so a public-domain portrait of Saad Zaghloul is used instead.

### beshtak-palace
- It is included in the al-Muizz area ticket; the existing al-muizz-street record lists Bashtak among its ticketed monuments. Its data mirrors that record.
- No official page specific to Bashtak was found. The palace also hosts the Cultural Development Fund's Beit al-Ghinaa al-Arabi.

### cairo-airport-museum-terminal-2 and -3
- **Hours:** 24 hours, written as 00:00–23:59, with Ramadan 09:00–15:00. The source is the portal plus the MoTA guide.
- **Prices:** Egyptians EGP 25, foreigners USD 5. Encoded as an Egyptian tier plus `usdPegged`/`usdAmount` 5 (see question 2).
- **Access:** both museums are airside, so in practice only passengers can visit.
- **T2 alias:** the seed alias on T2 named the T3 museum and was removed.
- **Data gaps:** there are no coordinates and no photos.

### child-museum
- The operator (Heliopolis Society) lists programmes up to Aug 2026, so the status is open.
- Public hours and fees are posted only on Facebook. An aggregator's prices belong to the GEM children's museum and were not used.
- The founding and renovation dates conflict between sources.
- The phone number comes from the operator's page.

### citadel-carriage-museum-former
- **Status: closed.** Only AR Wikipedia says so, and it only says the collection is "believed" to have moved to Bulaq.
- The MoTA guide and the 2026 Citadel ticket do not mention it. The exact closing year is unknown.

### citadel-prison-museum
- youm7 (18 Apr 2026) lists it among the ten sites on the single Citadel ticket.
- **Hours:** the portal says 08:00–16:00, earlier than the Citadel's 17:00. No last entry or Ramadan hours are published.

### confiscated-antiquities-museum
- Its closure rests only on AR Wikipedia. The photo shows the Citadel's northern enclosure, where the museum stood, not the museum itself.

### dr-naguib-pasha-mahfouz-museum
- It is a teaching museum, open only to medical students and doctors (2019 and 2022 reports). I found no change in 2025–26, so it is listed as `closed` to the public.

### effat-naghi-saad-el-khadem-museum
- **Hours:** the Sector head named it on 4 Jun 2026: 09:00–16:00, closed Friday and Monday.
- **Prices:** 5/3/10 from the undated official page, following the mukhtar-museum pattern.
- **Ramadan:** the Sector-wide 10:00–14:00.
- **No photo.**

### egx-museum
- It has been open to the public since July 2016. The only 2025 evidence is organised university group visits, so the status is `unknown`.

### egyptian-air-force-museum
- The only visitor details found are from 2019 (cairo360: closed Tuesday, 09:00–15:00, EGP 30) and are not used. Status `unknown`.

### egyptian-geographic-society-museum
- The building is inside the guarded Parliament compound. The only 2025 evidence is a congress delegates' visit. Status `unknown`.

### egyptian-postal-museum
- It reopened in 2022, and Egypt Post opened it free on Postal Day 2025. No regular hours or fees are published.
- The area conflicts: 543 m² against "7,000 m²".

### egyptian-textile-museum
- **Status: closed.** The collection moved to NMEC between 2020 and 2022 (AR Wikipedia, youm7 2020). It is also missing from the 2024 list.

### espace-karim-francis
- It is a private commercial gallery. Its website is live but undated. The Arabic name is still unverified (from the seed note). There is no photo.

### farouk-corner-museum
- **Hours conflict:** the portal and the MoTA guide say 09:00–17:00 with the ticket window closing at 16:00. The Nov 2024 PDF says 09:00–15:00.
- I kept 09:00–17:00 / 16:00, because the PDF's hours are also ignored at gayer-anderson-museum, which has the same PDF conflict. See question 3.
- Ramadan is 09:00–15:00 with last entry 14:00.

### hassan-heshmat-museum
- **Status:** the evidence that it is open is only an SIS headline (Nov 2025, GEM-opening initiative), whose body could not be retrieved.
- **Hours and prices:** 10:00–16:00, closed Monday and Friday, 5/3/10, all from the undated official page. It is not named in the Sector's June 2026 statement.

### heliopolis-open-air-museum
- This is the open-air museum around the Senusret I obelisk (opened 17 Feb 2018, 135 objects, SIS). It is entered on the obelisk ticket, so its data mirrors that record, and the coordinates were copied from it.

### helwan-wax-museum
- **Status: renovation.** The official page says "under development and preparation", and a ministry plan was reported in Feb 2026.
- The founding year conflicts: 1934 against 1937.

### hunting-museum-manial
- It reopened in 2017 inside the Manial Palace (MoTA guide), and its data mirrors manial-palace-museum. The coordinates were copied from that record.
- Who assembled the collection is unverified.

## Decisions needed (recommended answer in **bold**)

1. **Four records fail validation because no compliant photo exists** (airport T2 and T3, Effat Naghi, Karim Francis):
   **(a) Keep `photos` empty, as the house rule says, and add an exemption to the validator (for example a `noPhotoReason` curation flag).**
   (b) Use a loosely related compliant photo, such as an aircraft at Cairo Airport.
   (c) Hide these places until a photo exists.
2. **Airport museums charge foreigners USD 5, with no EGP figure published.**
   **(a) Keep the Egyptian tier (EGP 25) plus `usdPegged: true, usdAmount: 5`, and have the app show "USD 5 (foreigners)".**
   (b) Add a USD-currency foreign tier (needs a schema change).
   (c) Show "Price not confirmed" for foreigners.
3. **Farouk Corner closing time.** The live portal and the MoTA guide say 17:00 (last ticket 16:00); the Nov 2024 PDF says 15:00.
   **(a) 17:00 / 16:00, matching the Gayer-Anderson precedent.**
   (b) 15:00, under the "earlier time" rule.
4. **Places that are not visitable museums.** Several records are duplicates, parts of other places, or not tourist sites: the former Citadel carriage museum, the Textile Museum (collection now at NMEC), the Confiscated Antiquities Museum, Espace Karim Francis (a commercial gallery) and the Naguib Pasha Mahfouz museum (medical students only).
   **(a) Hide Karim Francis and Confiscated Antiquities. Keep the other three as "Closed" records, each with a note pointing to where the collection now is.**
   (b) Keep all of them as closed records.
   (c) Delete all five.
5. **Sub-places of existing records** (Heliopolis open-air museum = Obelisk of Senusret I; Hunting Museum = part of Manial Palace):
   **(a) Merge both into their parents (as aliases or highlights) and drop the separate ids.**
   (b) Keep them as separate places marked "Included in the X ticket", like the Karnak Open-Air Museum.
6. **Fast-period closures at the Wadi Natrun monasteries.** No 2026 notices exist yet.
   **(a) Add no exception now. Recheck in mid-Nov 2026 (Nativity Fast) and Feb 2027 (Lent and Holy Week).**
   (b) Project a Nativity Fast exception, as was done at St Anthony.
7. **Aisha Fahmy hours.** The official page says split sessions with Friday closed; the July 2026 report says daily 09:00–21:00 with Friday evenings only.
   **(a) Use the dated 2026 report (current data).**
   (b) Use the official page.
8. **Beit el-Umma.** It is under development, but a September 2026 listicle still recommends visiting.
   **(a) Keep `renovation` and confirm with the Fine Arts Sector.**
   (b) Mark it `open` with the official page's hours and prices.
9. **Places with status `unknown`** (EGX, Air Force, Geographic Society):
   **(a) Keep them, flagged as "Check before you go", and include them in the phone-verification round (decision 4 in REVIEW.md).**
   (b) Hide them until verified.

## Scheduled rechecks

- **Mid-Nov 2026:** Nativity Fast visiting rules at the three Wadi Natrun monasteries.
- **Early 2027:** Ramadan 2027 announcements. The records with Ramadan exceptions are Ali Labib, both airport museums, Effat Naghi, Hassan Heshmat and Farouk Corner, plus the mirrored records: Beshtak, Heliopolis and Hunting.
- **Aug 2027:** Beit el-Umma reopening. Helwan Wax Museum, any time.
- **Any time:** public hours and fees at the Child Museum, Postal Museum and Hassan Heshmat (by phone).
