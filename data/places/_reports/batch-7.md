# Batch 7 enrichment report

Checked 2026-10-04. 18 places: el-alamein-military-museum, shali-fortress, temple-of-the-oracle-of-amun, beni-hasan, tell-el-amarna, tuna-el-gebel, al-bagawat, al-qasr-dakhla, temple-of-hibis, muhammad-ali-palace-shubra, hurghada-museum, monastery-of-st-anthony, monastery-of-st-paul, tanis, tell-basta, red-monastery, white-monastery, sharm-el-sheikh-museum.

All 18 files pass `python3 tools/validate_all.py` with 0 errors. Every file has:
- an English description of 168–192 words, with Arabic written separately (not translated line by line);
- 5–6 highlights;
- 1–3 Commons photos (licence and author taken from the Commons API);
- a Ramadan 2027 exception dated 2027-02-08 to 2027-03-08 wherever an official Ramadan schedule exists;
- every cited URL checked for an HTTP 200 response on 2026-10-04 (Facebook pages excluded).

## Read this first

### 1. The July 2026 oasis price rise does not apply to Siwa, Kharga or Dakhla

The SCA board decision of 9 Jul 2026 raises prices to foreign 400/200 and Egyptian 40/20 from 1 Oct 2026. MoTA's own statement (mota.gov.eg, 9 Jul 2026) names only "المواقع الأثرية بالواحات البحرية", the **Bahariya Oasis** sites. Dostor, Vetogate and Egypt Telegraph report it the same way.

- In MoTA's ticket list, Siwa is filed under Matrouh and Kharga/Dakhla under New Valley, as entries separate from Bahariya.
- Some search-engine summaries wrongly widened the decision to "Siwa, Kharga and Dakhla". No source text says that.
- The SCA board statements of 8 Mar, 5 May and 10 Sep 2026 contain no price change for these oases.

So I kept these prices:

| Site | Foreign adult/student (EGP) | Egyptian adult/student (EGP) |
|---|---|---|
| Aghurmi | 120/60 | 10/5 |
| Bagawat | 120/60 | 10/5 |
| Hibis | 180/90 | 10/5 |
| Al-Qasr | 100/50 | 10/5 |

Each of these files cites the MoTA statement with the note "not applied". **If you know of a separate decision for Siwa/Kharga/Dakhla, send me the link.**

### 2. Where the hours and prices come from

- **MoTA "open sites/museums guide" pages (mota.gov.eg, Arabic, undated, live):** the main source for hours, Ramadan hours and addresses. They state "last entry one hour before closing".
- **egymonuments.gov.eg portal:** used for Beni Hasan, Bagawat, Tell Basta, the Red Monastery, Hurghada, Sharm and Shubra.
- **egymonuments.com booking pages:** used for Aghurmi, Beni Hasan, Amarna, Tuna el-Gebel, Tanis, Hurghada and Sharm.
- **Nov 2024 MoTA ticket PDF:** a cross-check, and the **only** price source for Hibis and Al-Qasr (see question 4).
- **Not on any MoTA channel:** El Alamein (Ministry of Defence page), the two Red Sea monasteries (church statements quoted in the press) and the two Sohag monasteries (free entry per the governor, reported in the press).

## Conflicts and how I resolved them (house rule: earlier time)

- **Opening-time conflicts.** At Aghurmi the MoTA guide says 08:00, while the booking platform and PDF say 09:00. At Bagawat the portal says 09:00–16:00, while the guide and PDF say 08:00–17:00. In both cases I used the **narrower window**: the later opening and the earlier closing. The "earlier" rule covers closing and last-entry times; applying it to opening times too could send visitors to a locked gate. See question 1.
- **Hurghada and Sharm, Ramadan.** The portal says 10:00–12:00 (ticket window closes 11:00) plus 20:00–23:00. The MoTA guide says the morning runs to 14:00, and the booking platform gives last entry 13:00. I used the earlier times: 12:00 close, 11:00 last entry.
- **Hurghada, last entry.** The portal and booking platform say 12:00 / 22:00; youm7 (May 2026) says 12:30 / 22:30. I kept 12:00 / 22:00.
- **Beni Hasan, Ramadan.** The guide says 09:00–16:00; the booking platform says 08:00 with last entry 16:00. I used 09:00–16:00 with last entry 15:00.
- **Tell Basta, summer.** The portal gives 17:00 all year; the guide gives 18:00 in summer. I used 17:00 all year, so there is no summer exception.
- **Aghurmi, last entry.** The booking platform shows 17:00, which equals the closing time. I used 16:00 under MoTA's one-hour rule.

## Decisions needed (recommended answer in **bold**)

1. **Opening times that conflict** (Aghurmi 08:00 vs 09:00; Bagawat 08:00–17:00 vs 09:00–16:00):
   **(a) Use the narrowest window: the later opening and the earlier closing.**
   (b) Apply "earlier" literally to both ends (08:00 open, 16:00 close).
   (c) Prefer the MoTA guide (08:00–17:00).
2. **Beni Hasan Egyptian price.** The portal and the Nov 2024 PDF say 20/10; the booking platform charges 10/5. I applied the house rule: `amount` 20/10 with `onlineAmount` 10/5. A cheaper online price is odd; the platform may simply be out of date.
   **(a) Keep as is and ask the hotline 19654.**
   (b) Use 10/5 everywhere.
   (c) Use 20/10 with no `onlineAmount`.
3. **Amarna and Tuna el-Gebel Egyptian price.** The booking platform says 10/5, the Nov 2024 PDF 20/10, and there is no portal page. I used 10/5 because it is the only live official price.
   **(a) Keep 10/5.**
   (b) Use 20/10 with `onlineAmount` 10/5, matching how Beni Hasan is handled.
4. **Hibis and Al-Qasr.** Their only price source is the Nov 2024 MoTA list; there is no live official price page.
   **(a) Keep the prices as `confirmed` with the PDF as source, and recheck when MoTA publishes a new list.**
   (b) Set `prices.status: unconfirmed`.
5. **Red and White Monasteries shown as `free`.** The Sohag governor said both are open free all week (dostor, Jun 2025), and elwatannews (May 2026) repeats "free". No MoTA page says it.
   **(a) Keep `free`. A governor's statement counts as an official source.**
   (b) Set `unconfirmed`, as for the Hanging Church.
6. **Coptic fast exceptions for the Red Sea monasteries.** I added Nativity Fast exceptions for 25 Nov 2026 – 6 Jan 2027: St Anthony open Fri–Sun only, St Paul closed. They are projected from the monasteries' 2021, 2023 and 2025 announcements.
   **(a) Keep them, labelled "expected", and confirm in mid-November.**
   (b) Remove them and leave a statusNote only.
7. **Summer season dates (Tanis).** I used 2026-04-24 to 2026-10-29, the daylight-saving period (DST ends at midnight on Thu 29 Oct). Karnak uses 2026-10-30.
   **(a) Align all summer exceptions to the last DST day (29 Oct) and fix Karnak.**
   (b) Use 30 Oct everywhere.
8. **Muhammad Ali Palace (Shubra) status.** Restoration is finished, but no public opening has been announced. The palace hosts official events, and news since 2022 has repeatedly called the opening "imminent".
   **(a) `closed`, with a statusNote saying it is restored but not open for regular visits.**
   (b) `renovation`.
   (c) Remove it from the app until it opens.
9. **Minya escort note.** The crowdNotes for Beni Hasan, Amarna and Tuna say police "may" ask foreigners to register their route or travel with an escort. This comes only from travel forums; I found no official 2025–26 source.
   **(a) Keep it, worded with "may".**
   (b) Remove it.
10. **Sharm photos of loaned objects.** No CC photo taken inside the museum exists. The two photos used show Sharm museum objects (a cat-mummy coffin and a lion-cub mummy) photographed in Paris in 2023, while they were on loan to a touring exhibition. They may still be abroad.
    **(a) Keep them, and do not name them as highlights.**
    (b) Remove them, leaving the place with no photo (that fails the validator).

## Per place

### el-alamein-military-museum — confidence: medium
- **Hours:** daily 09:00–16:00, from the Ministry of Defence museum page (undated). No last entry and no Ramadan schedule are published.
- **Price unconfirmed:** news reports say only "رسوم رمزية" (a nominal fee).
- **Free entry 3–6 Oct 2026:** announced by the Armed Forces for the October War anniversary and mentioned in the statusNote. **Remove that sentence after 6 Oct.**
- **Contacts:** phone 046-4100031, from the MoD page.
- **Photos:** WWII vehicles and guns only; the building is excluded.

### shali-fortress — confidence: medium
- **No official hours or price:** Shali is not in the MoTA ticket list, the MoTA guide or the booking platform. Blogs say it is free and always open. Hours are omitted and the price is `unconfirmed`.
- **Reopening date:** the egymonuments news item has no date in its text; press coverage puts it in Nov 2020. The prose gives no year.
- **Siwa travel note:** based on FCDO advice (updated 4 Aug 2026), which exempts Siwa town and the Matrouh road. Checkpoints and desert permits are general advice.

### temple-of-the-oracle-of-amun — confidence: medium
- **Prices:** 120/60 and 10/5. The booking platform and PDF agree.
- **Hours:** 09:00–17:00 with last entry 16:00; Ramadan 09:00–16:00 with last entry 15:00 (see the conflicts section).
- **Not verified:** any 2025–26 status news for the temple itself.

### beni-hasan — confidence: medium
- **Prices:** see question 2.
- **Open tombs:** Khety, Baqet III, Khnumhotep II and Amenemhat (youm7, Jul 2026).
- **Accessibility:** "stairs, no wheelchair" is general knowledge, not sourced.

### tell-el-amarna — confidence: medium
- **Prices:** see question 3.
- **Royal Tomb:** the Nov 2024 PDF lists a separate ticket (foreign 120/60, Egyptian 20/10). There is no 2025–26 source and no booking product, so no extra is given; the statusNote says "historically".
- **Not verified:** which tombs open daily, the ferry schedule and site transport.
- **Booking-page typo:** the winter opening shows "08:00 pm".

### tuna-el-gebel — confidence: medium
- **Prices:** see question 3.
- **Isadora tomb:** stated as included in the ticket, based on the MoTA guide describing it as part of the site. No separate ticket appears anywhere.

### al-bagawat — confidence: medium
- **Hours:** see question 1.
- **Not on egymonuments.com:** so there is no `onlineUrl`.
- **freeGroups:** not stated on any official Bagawat page, so omitted.
- **Not verified:** whether the Chapel of Peace is currently open. The Chapel of the Exodus is reported as visitable (masrawy, Jan 2026).

### al-qasr-dakhla — confidence: medium
- **Prices:** see question 4.
- **Restoration detail:** the Japanese grant and 2015 start appear only in search summaries, so the prose just says "begun in the 2010s with international support".
- **Not used, not verified:** the Nasr el-Din mosque name and the ethnographic house.
- **Wikipedia:** there is no English article, so the Arabic Wikipedia is cited.

### temple-of-hibis — confidence: medium
- **Status:** reopened 29 Oct 2015 after restoration (Arab Contractors magazine; masrawy, May 2025).
- **Prices:** see question 4.

### muhammad-ali-palace-shubra — confidence: low
- **Status:** see question 8.
- **Not used:** a 60/30 EGP Egyptian ticket reported around 2022, "before the official opening".
- **Location label:** the egymonuments page says "Cairo"; I kept the seed governorate (qalyubia).

### hurghada-museum — confidence: high
- **Prices:** 300/150 and 80/40, plus audio guide 50/30. The portal and booking platform agree.
- **Hours:** split sessions, with Ramadan resolved as described in the conflicts section.
- **Contacts:** omitted. Wikidata's phone number and the Facebook page could not be verified as official.
- **Only 1 photo (house rule says 2–4).** Commons has a single CC artefact photo, the Meritamun statue. The other photos show the modern building, which is excluded.

### sharm-el-sheikh-museum — confidence: high
- **Prices:** 200/100 and 40/20, plus audio guide 50/30.
- **Temporary exhibition:** the statusNote mentions "Stone and Ink", running from 29 Aug 2026 for about three months. **Remove it around the end of Nov 2026.**
- **Photos:** see question 10.

### monastery-of-st-anthony — confidence: low
- **Hours:** gates 04:00–18:00, with tours of the ancient section at 09:00, 11:00, 14:00 and 16:00. The source is the diocese spokesman quoted in **Nov 2022**; no newer source was found.
- **Fast closures:** see question 6.
- **Price:** no fee is mentioned anywhere, but nothing official says it is free, so it is `unconfirmed`.
- **Cave climb:** 1,420 steps (youm7, Apr 2025).
- **Facebook page:** unverified, so contacts are omitted.

### monastery-of-st-paul — confidence: low
- **Hours:** Thu–Sat 08:00–18:00, closed for the whole Nativity Fast, per diocese officials quoted in **Oct 2023**. Blogs say daily 09:00–17:00.
- **No official site, phone or fee information** was found.

### tanis — confidence: medium
- **Hours:** winter 09:00–17:00 and summer 09:00–18:00 (see question 7); Ramadan 09:00–16:00. The MoTA guide and booking platform agree.
- **Not verified:** whether visitors can enter the royal tombs, and whether the 2022 visitor centre still operates. A 2026 report says there are no visitor facilities.
- **Tanis gold on tour:** some pieces are touring (the Psusennes I collar is at the de Young, San Francisco, Aug 2026 – Jan 2027), so the text refers to the Egyptian Museum only in general terms.

### tell-basta — confidence: medium
- **Prices:** 150/75 and 10/5, plus parking (25 / 50 / 75 / 100) from the live portal.
- **Not on egymonuments.com:** tickets are sold at the gate.
- **Museum:** not re-confirmed for 2026 whether the site ticket includes it, or what its hours are (the Nov 2024 PDF says 09:00–15:00).

### red-monastery — confidence: medium
- **Status:** ARCE conservation is complete, and the church is back in use for worship.
- **Hours:** 09:00–17:00 with last entry 16:00. The MoTA guide, portal and elwatannews agree.
- **Price:** free; see question 5.
- **Dress code and passport checks:** general advice only.

### white-monastery — confidence: medium
- **Hours:** the same as the Red Monastery.
- **Price:** free; see question 5.
- **Feast of St Shenoute:** 14 July, with crowds from mid to late July (youm7, 2025).
- **Photo excluded:** the modern monastery gate ("White Monastery 01.JPG").

## Photos

51 photos across the 18 places:
- **Licences:** CC BY 2.0/2.5/3.0/4.0, CC BY-SA 2.0/3.0/4.0, and public domain (for example the Coste drawing, the Bonfils albumen print, and the PD-released Aghurmi photos).
- **Rejected because a modern building, gate, church or restaurant dominates the frame:**
  - Hurghada and Sharm museum buildings
  - the modern towers at St Anthony
  - the modern gate of the White Monastery
  - "Shali castle" at night (restaurant furniture)
- **Rejected because of a disallowed licence:** GFDL-only images (several Alamein interiors).

## Scheduled rechecks

- **6 Oct 2026:** drop the Alamein free-entry sentence.
- **Mid-Nov 2026:** confirm the Nativity Fast rules at both Red Sea monasteries.
- **End of Nov 2026:** drop the Sharm "Stone and Ink" sentence.
- **Any time:** a new MoTA ticket list (for Hibis and Al-Qasr), any public opening of the Shubra palace, and Tell Basta museum hours.
