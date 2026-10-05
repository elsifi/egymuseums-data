# Batch 12 enrichment report

Checked 2026-10-05. 28 minor places: el-tod-temple, howard-carter-house, qurnet-murai, temple-of-merenptah, temple-of-seti-i-qurna, wikalat-al-gidawi, archaeological-museum-of-matrouh, museum-of-marina-al-alamain, museum-of-siwan-traditions, rommels-cave-museum, gebel-el-mawta, aten-museum, mallawi-museum, minya-museum, open-air-museum-al-ashmunain, al-bahnasa, fraser-tombs, gebel-al-tayr-monastery, zawyet-sultan, denshway-museum, new-valley-museum, al-muzawwaqa-tombs, bashendi, deir-el-hagar, qasr-dush, qasr-el-ghueita, qasr-el-zayyan, qila-al-dabba-ain-asil.

- **Status:** 22 open, 3 renovation (Marina, el-Ashmunein, New Valley Museum), 2 closed (Aten Museum, Minya Museum: never opened), 1 unknown (Siwa House Museum).
- **Confidence:** 7 high, 16 medium, 5 low.
- **Validator:** 24 of 28 files pass with 0 errors. 4 files fail only the "at least one photo" rule, because no compliant Commons photo exists (house rule: leave photos empty and report it): archaeological-museum-of-matrouh, rommels-cave-museum, aten-museum, minya-museum. See question 1.
- English descriptions are 137–160 words; Arabic is written separately. Every place has 2–5 highlights except minya-museum (none: nothing verifiable).
- 7 WebSearch calls in total (Aten, Seti I, Marina, New Valley Museum, Denshway, el-Ashmunein, Siwa). All cited URLs return HTTP 200 (upload.wikimedia.org image URLs were rate-limited during the check; they come straight from the Commons API).

## Where the data comes from

- **MoTA "open sites/museums" guide pages** (mota.gov.eg, Arabic, undated, live): found for 15 places by trying slugs (Tod, Carter House, Merenptah, Wikala, Gebel el-Mawta, Matrouh, Rommel, Mallawi, Bahnasa, Fraser, Zawyet Sultan, Muzawwaqa, Deir el-Hagar, Dush, Ghueita, Zayyan). Not found (several slugs tried) for Qurnet Murai, Seti I Qurna, Bashendi, Qila al-Dabba, Gebel al-Tayr, New Valley Museum.
- **egymonuments.com booking platform:** Carter House, El-Tod, Merenptah, Gebel el-Mawta, Mallawi, Fraser, Zawyet Sultan, and Esna Temple (for the wikala).
- **egymonuments.gov.eg portal:** Carter House, Matrouh Museum, al-Bahnasa (text only).
- **MoTA Nov 2024 ticket PDF:** the only price source for Qurnet Murai, Seti I, Rommel and the six Dakhla/Kharga sites. Kept as `confirmed` (batch-7 Q4a precedent).
- **Press, 2025–2026:** Aten Museum opening date, Seti I restoration, Marina development, New Valley Museum works, Denshway visits.
- **German Wikivoyage** (Roland Unger's site articles): used for facts and for three sets of coordinates; never for prices.

## Conflicts and how I resolved them

- **Opening time at Gebel el-Mawta.** The guide says 08:00; the booking platform and PDF say 09:00. I used 09:00 (narrowest window, batch-7 Q1a). The booking platform's last entry of 17:00 equals the closing time, so I used 16:00 (one-hour rule).
- **Matrouh Museum hours.** The portal gives 08:00–15:00 + 17:00–22:00 all year. The guide and PDF give winter 09:00–17:00 and summer 09:00–15:00 + 17:00–22:00. I used the guide's seasons, opening at 09:00. The summer exception (24 Apr–29 Oct 2026) is in force today.
- **Qurna summer schedule** (06:00–18:00 from 24 Apr 2026). Applied to Carter House, Qurnet Murai and Seti I, as at the Ramesseum.
  - **Not applied to Merenptah:** its booking page gives last entry 16:00 in every season (earlier time wins).
  - **Not applied to El-Tod:** it is outside the Qurna area, and the guide says 07:00–17:00 all year.
- **Wikala Sun/Tue/Fri closing.** The guide says 19:00; the Esna booking page says 18:00. I used 18:00, the same as esna-temple.
- **Egyptian price at Fraser and Zawyet Sultan.** The booking platform says 10/5; the Nov 2024 list says 20/10. I used 10/5 (batch-7 Q3a, as at Amarna).
- **Ramadan rows equal to the normal week** were dropped (batch-4 Q13a): El-Tod, Carter House, Merenptah, Mallawi, Rommel and the wikala.

## Decisions needed (recommended answer in **bold**)

1. **Four places have no compliant photo** (Matrouh Museum, Rommel's Cave, Aten Museum, Minya Museum). The only Commons images show the modern buildings, or Rommel's modern stone-clad entrance with a decorative gate. The validator requires at least one photo.
   **(a) Keep `photos` empty and relax the validator rule to a warning for `tier: minor` places (other batches hit the same rule).**
   (b) Use the borderline Rommel cave-entrance photo and leave the other three failing.
   (c) Hide places without photos until one is found.
2. **minya-museum (Q130216212)** has no coordinates, sitelinks or official listing, and appears to be the Aten Museum project.
   **(a) Remove it from the dataset and keep aten-museum.**
   (b) Keep it as a `closed` stub.
3. **Matrouh Museum foreign price.** The portal says 80/40; the MoTA Nov 2024 list says 180/90. Egyptian 20/10 in both. There is no booking product.
   **(a) 180/90, from the newer list (like the St Simeon D4 pattern), and confirm via hotline 19654.**
   (b) 80/40, from the portal.
   (c) `unconfirmed`.
4. **museum-of-marina-al-alamain** is really the site museum of the Marina el-Alamein archaeological area, which is closed for development until about H1 2027.
   **(a) Re-scope the place as "Marina el-Alamein archaeological site" (Q778942) with status `renovation`.**
   (b) Keep it as a museum.
5. **open-air-museum-al-ashmunain.** The display was reduced to the two baboon colossi after 2011, and the area has been closed since late 2025. Both points rest on Wikivoyage only.
   **(a) Re-scope the place as "el-Ashmunein (Hermopolis Magna)", keep `renovation` at low confidence, and confirm via hotline 19654.**
   (b) Mark it `unknown`.
6. **Denshway photo.** The building (1999) and its artworks are in copyright, so the only photo is a public-domain 1906 picture of the trial prisoners, the kind of image the museum exhibits.
   **(a) Keep it.**
   (b) Remove it, which fails the validator.
7. **Wikalat al-Gidawi `includedIn: esna-temple`** rests only on the Nov 2024 list ("Within Esna Temple Ticket"). The esna-temple record says "not claimed".
   **(a) Keep `includedIn` and add a note to esna-temple, which I did not edit.**
   (b) Set the wikala to `unconfirmed`.
8. **PDF-only `open` status** (Qurnet Murai, Seti I, Bashendi, Qila al-Dabba). No live official page exists, only the dated Nov 2024 list, plus Commons photos from Dec 2025 at Qurnet Murai.
   **(a) Keep `open` at medium confidence.**
   (b) Set them to `unknown`.

## Scheduled rechecks

- **After 29 Oct 2026:** winter hours for Carter House, Qurnet Murai, Seti I and the Matrouh Museum.
- **During 2026:** whether the New Valley Museum has reopened; if it has, restore hours (PDF: 09:00–15:00) and prices (PDF: 150/75, 10/5).
- **H1 2027:** Marina el-Alamein reopening.
- **Q4 2027:** Aten Museum opening.
- **Early 2027:** Ramadan 2027 announcements for the 10 records with Ramadan exceptions.

## Per place

### el-tod-temple — open, high
- Guide, booking platform and PDF agree: 07:00–17:00, 100/50, 10/5.
- **Not verified:** Wikivoyage (Nov 2024) says tickets had to be bought at the Luxor Temple office. The crowdNotes only advise buying online.

### howard-carter-house — open, high
- Portal, booking and guide agree: 220/110, 10/5.
- **Unofficial:** Wikivoyage says the ticket includes the Tutankhamun tomb replica, and lists car parking at EGP 25 (not added).
- **Name:** kept "Howard Carter House"; the guide's "بيت كارتر" was added as an alias.

### qurnet-murai — open, medium
- **PDF only** (120/60, 10/5); see question 8.
- **Not verified:** which tombs are open (TT40, TT277 and TT278 per Wikivoyage).
- **Photos:** the village photos are excluded (houses as the main subject). I used a tomb-entrance crop and an aerial view with the tomb marked.

### temple-of-merenptah — open, high
- **Summer schedule not applied:** see Conflicts.
- **Not mentioned:** the site's small lapidarium, closed in 2023 per Wikivoyage.

### temple-of-seti-i-qurna — open, medium
- **Prices:** PDF only (200/100, 10/5).
- **Restoration:** relief cleaning began in Apr 2026 (MoTA, via elnabaa); no closure was announced. Mentioned in the statusNote.

### wikalat-al-gidawi — open, medium
- **Price:** see question 7. The tiers mirror esna-temple.
- **Not verified:** the restoration year.

### archaeological-museum-of-matrouh — open, medium
- **Prices:** see question 3. **Photos:** none; see question 1.

### museum-of-marina-al-alamain — renovation, low
- See question 4. Coordinates are from the site item Q778942; the photos show the ancient ruins.

### museum-of-siwan-traditions — unknown, low
- **Renamed** "Siwa House Museum" (the old name is kept as an alias).
- **Operator:** the town council, not MoTA. The latest status evidence is from Dec 2022.
- **Prices:** quoted fees (5/2/10) are unverified, so prices are unconfirmed.
- **Coordinates:** none from an allowed source.

### rommels-cave-museum — open, medium
- **Opening year:** Wikipedia says 1977; the guide says 1988 (used).
- **Hours:** no last entry is stated on its guide page, so none is given.
- **Photos:** none; see question 1.

### gebel-el-mawta — open, high
- **Hours:** see Conflicts.
- **Prices:** the Jul 2026 oasis price rise covers Bahariya only, so it is not applied.

### aten-museum — closed, medium
- **Opening:** planned for Q4 2027 (SCA Secretary-General, elwatannews, 7 Jul 2026).
- **Object counts conflict:** 5,000 vs 10,000.
- **No coordinates, no photos.**

### mallawi-museum — open, high
- **Photos:** objects only (the 1963 building is excluded). After the 2013 looting, the pictured pieces may not all be on display.

### minya-museum — closed, low
- See question 2.

### open-air-museum-al-ashmunain — renovation, low
- See question 5. Coordinates are those of Hermopolis (Q732908).
- **Not verified:** the colossi heights. Their material was left out because sources disagree (quartzite vs sandstone).

### al-bahnasa — open, medium
- **Price unconfirmed:** the PDF shows dashes.
- **Scope:** the guide page covers the Islamic cemetery while the seed identity is Oxyrhynchus; the prose covers both.

### fraser-tombs — open, high
- See Conflicts (Egyptian price).

### gebel-al-tayr-monastery — open, low
- **Identity:** the seed Wikidata item is the village.
- **Coordinates:** from Wikivoyage.
- **Price unconfirmed:** Wikivoyage says free, but that is not official.
- **Not verified:** the feast dates (July pilgrimages, 22 Aug), so the prose says "summer feast" only.
- **Hours:** 09:00–17:00 from the PDF only.

### zawyet-sultan — open, high
- **Death year left out:** Sultan Pasha's death year conflicts (guide 1883, other references 1884).
- **Tickets:** Wikivoyage (Nov 2024) says there is no ticket office on site. The crowdNotes say to buy online.

### denshway-museum — open, medium
- **Operator:** Ministry of Culture. No hours or fees are published, so hours are omitted and prices are unconfirmed.
- **Photo:** see question 6.

### new-valley-museum — renovation, medium
- **Status:** works reported 8 Apr 2026. The start date of the closure was not found.
- **Not verified:** "opened 17 Feb 1993" and "4,087 objects" come from search summaries.

### al-muzawwaqa-tombs — open, medium
- **No Wikidata item;** coordinates are from Wikivoyage. Prices are from the PDF.

### bashendi — open, medium
- **PDF only** (see question 8). There is no Ramadan schedule.

### deir-el-hagar — open, medium
- **Distance from al-Qasr:** the guide says about 20 km, Wikivoyage about 7 km, so the prose gives no figure.

### qasr-dush — open, medium
- **Typo in the guide:** "117 متراً" (AD 117), so the prose says only "under Trajan".
- **Not added:** an unofficial one-day Kharga combination ticket (LE 120/60, Feb 2024).

### qasr-el-ghueita — open, medium
- **First building:** the 25th Dynasty per the guide, the 26th elsewhere; the prose says "25th or 26th".

### qasr-el-zayyan — open, medium
- **Distance from Kharga:** sources give 21–30 km; the address says about 25 km.

### qila-al-dabba-ain-asil — open, medium
- **PDF only;** one joint ticket covers both sites.
- **Not verified:** whether Ain Asil itself is open for walking visits, and the count of "five mastabas".
