# Batch 1 enrichment report

Checked 2026-10-04. 10 places: grand-egyptian-museum, giza-pyramids, egyptian-museum, national-museum-of-egyptian-civilization, saqqara, cairo-citadel, museum-of-islamic-art, al-muizz-street, sultan-hassan-mosque, coptic-museum.

All 10 files pass the stdlib schema check (`check()` from `tools/seed/validate.py`): 0 errors. Each file keeps the seed's id, wikidataId, names, governorate, coordinates and links.

## How sources were ranked

1. **The venue's own official site**
   - GEM: gem.eg FAQ / Plan your visit / Accessibility and tickets.gem.eg.
   - NMEC: nmec.gov.eg opening hours / accessibility / policies, plus its ticket flow egymonuments.com/nmec/tickets.
2. **egymonuments.com/details/<X> and /book-date/<n>**, MoTA's official ticketing site, read live on 2026-10-04. It gave current prices including add-ons, last entry, Ramadan last entry and free-entry rules. It no longer shows an Arab tier at SCA sites (NMEC still shows an "Arab" row, priced the same as foreigners).
3. **MoTA "open sites/museums" visitor guide (mota.gov.eg, Arabic)**. It gave closing times, Ramadan closing times and addresses, and states the rule "last entry 1 h before closing".
4. **egymonuments.gov.eg** gave weekly hours, prices, the free-entry policy and fact checks for descriptions.
5. **Arabic and English news from 2026**, used for GEM prices and the Nov 2026 increase, Ramadan 2026 hours and the Tahrir objects on display in July 2026:
   - youm7 (2026-04-19, 2026-02-18, 2026-07-02)
   - masrawy (2026-04-15)
   - dostor (2026-01-01 and a post-Eid 2026 article)
   - cairo24, egypttoday

## Cross-cutting issues (need a human decision)

- **`effectiveFrom` is left empty everywhere.**
  - The SCA amounts (e.g. Tahrir 550/275, Citadel 550/275, MIA 340/170) match the MoTA list dated 2024-11-05. They therefore predate 2025.
  - The 2026-01-01 decision (board decision of 2025-06-30, dostor 2026-01-01) changed only the audience structure, by dropping the Arab tier. I found no decision date for the amounts themselves.
  - Batch 2 also left the field empty. Batch 3 used 2024-11-01 for some Aswan sites. **Decide one convention.**
- **GEM foreign price is USD-pegged.**
  - Stored values: `usdPegged: true`, `usdAmount: 30`, amount EGP 1,590 (adult) / 800 (child/student). These come from April 2026 reports (youm7, masrawy, dostor).
  - The museum's executive director says the EGP amount is updated monthly, so the Oct 2026 EGP figure may differ. tickets.gem.eg shows prices only inside the booking flow, which needs JS/OTP, so I could not read them.
  - **From 2026-11-01** the foreign/Arab non-resident ticket becomes USD 35 and the Egyptian adult EGP 220 (this is in `statusNote`). **Recheck and update the record on/after 1 Nov 2026.** The new resident, student and child amounts were not announced.
- **`cashAccepted`**
  - Set to `false` for GEM, which is online-only from 1 Dec 2025 per the official FAQ.
  - Set to `false` for Giza, the Egyptian Museum and the Citadel. This rests on the June 2023 MoTA card-only decision for those sites plus 2026 secondary guides; no 2025–26 official restatement was found.
  - Left `null` for the others.
  - **Human decision:** accept the 2023 official source for those three or reset them to null. Batch 2 chose null in the same situation.
- **`timedEntry`**: `true` only for GEM. SCA online booking is by date only, so it is `false`. NMEC's plain ticket is date-only; its guided-tour ticket has a time slot.
- **Description fact checks.** Description facts were checked against Wikipedia and egymonuments.gov.eg, but the prose is original. Highlights were picked from official pages and 2026 news.
- **Photos**
  - 3–4 per place, with licence and author read from the Commons API (all CC0, PD, CC BY or CC BY-SA). Upload URLs have tracking query strings stripped.
  - Dropped: a GEM Ramesses II photo where the modern atrium dominated (freedom-of-panorama risk).
  - Kept: "GEM Khufus Boat front 2025" (CC0), where the boat is the subject but the modern hall is visible. **Reviewer may want to drop it.**
  - A second HEAD check of upload URLs was rate-limited (HTTP 429) after 7 successes. The URLs come straight from the API's `imageinfo.url`.
- **Holidays.** No official public-holiday closures or extended holiday hours were found for any of the 10 places, so none were added.

## Per place

### grand-egyptian-museum — confidence: high
- Hours are official: galleries 09:00–18:00, or 09:00–21:00 on Wed/Sat, with last entry 1 h before. The complex opens 08:30–19:00/22:00, noted in `statusNote`.
- Ramadan hours (09:00–16:00, last ticket 15:00) come from youm7 2026-02-18 for Ramadan 2026 only. Ramadan 2027 is not yet announced.
- Not verified:
  - Exact EGP price in Oct 2026 (see above).
  - Whether the guided-tour totals (2,090 / 1,050 etc.) also float with the USD rate.
  - Children's Museum and other add-on prices.
  - An official venue phone. The only number published is the ticketing partner's (eAswaaq +20 2 3531 7344), so `phone` is null.
- Conflict: the gem.eg footer says "Open daily 09:00–18:00", which omits the Wed/Sat late opening that the FAQ and ticket site show. I used the FAQ and ticket site.

### giza-pyramids — confidence: medium
- Hours:
  - MoTA guide: 07:00–17:00, Ramadan 08:00–16:00, last entry 1 h before closing.
  - egymonuments.com: open 07:00, last entry 16:00, Ramadan last entry 15:30.
  - egymonuments.gov.eg: 08:00–16:00.
  - **Conflict:** I used MoTA/ticketing (07:00–17:00, last entry 16:00; Ramadan last entry 15:30 from ticketing, not 15:00 per the 1-hour rule).
- Prices come from the live official booking page:
  - Plateau: 700/350 foreign, 60/30 Egyptian.
  - Khufu interior: 1,500/750 foreign, 150/75 Egyptian (the 1,500 figure is also reported from Jan 2025).
  - Khafre: 280/140 and 30/10. Meresankh: 200/100 and 20/5. Workers' tombs: 700/350, minimum 5 tickets.
  - Older 2024 articles quoted Khufu 1,000 or 900. These are superseded.
- Not verified:
  - **Menkaure pyramid interior.** gov.eg says the area ticket excludes it, but there is no price on the booking page. It is unknown whether it is open.
  - Parking fees. gov.eg lists car 25 to bus 100, but private cars no longer enter the plateau, so I omitted them.
  - Sound & Light show.
  - Whether the old Mena House/Sphinx gate is still usable by individual visitors.
- The new entrance and electric buses come from Egyptian Streets (Apr 2025), a news source, not MoTA.

### egyptian-museum — confidence: high
- Hours 09:00–17:00 with last entry 16:00; Ramadan 09:00–16:00 with last entry 15:00. Official sources and cairo24 for Ramadan 2026 agree.
- **Highlights are limited to objects confirmed on display by youm7 on 2026-07-02.**
  - The Narmer Palette is left out because sources conflict on its location. MoTA's undated guide still lists it at Tahrir; some 2026 tour sites claim it moved to GEM. **Needs checking.**
  - Yuya & Thuya and Hetepheres were also not confirmed.
- Not verified: whether any galleries are closed under the EU-funded redisplay project mentioned by the MoTA guide.

### national-museum-of-egyptian-civilization — confidence: high
- Hours and prices come from the official site and ticket flow: 09:00–17:00 with last entry 16:00, plus Friday 18:00–21:00 with last entry 20:00.
- Prices: 90/45 Egyptian, 550/300 foreign (the "Arab" row equals foreign). Ticket plus tour: 400/355 and 1,510/1,260.
- A 2026 secondary report mentions an April price rise "to be determined". The official ticket page still shows 550/300, so I used the official figure.
- Not verified:
  - Photography ticket price (the policy says one is required).
  - Ramadan closing time (only last entry 15:00 from ticketing).
  - The second official YouTube channel (the site links two), so YouTube was omitted.
- `platform` is set to `nmec`, but the ticket flow is hosted on egymonuments.com/nmec/tickets. Switch to `egymonuments` if preferred.

### saqqara — confidence: medium
- **Status:** the MoTA guide says the **Imhotep Museum is currently closed for restoration**. gov.eg still lists it as included in the all-inclusive ticket. Text and highlights reflect the closure.
- Hours:
  - MoTA guide: 08:00–17:00, Ramadan 08:00–16:00.
  - egymonuments.com: last entry 16:00, Ramadan 15:30.
  - gov.eg: 08:00–16:00.
  - **Conflict:** I used MoTA/ticketing.
- Prices come from the live booking page: area 600/300 and 30/10; all-inclusive 1,400/700 and 120/60. All add-ons and parking are included. The "New Tombs" add-on is interpreted as noble plus New Kingdom tombs, following gov.eg.
- Not verified:
  - Whether the Pyramids of Unas and Teti and the tomb of Mehu are open now. Unas is described but not claimed as open.
  - Whether the Djoser interior (Egyptian student 20) is open every day.

### cairo-citadel — confidence: medium
- Hours:
  - MoTA guide and gov.eg: 08:00–17:00, Ramadan 08:00–16:00.
  - egymonuments.com: "Summer 09:00 / Winter 08:00" opening, last entry 16:00, Ramadan last entry 15:30.
  - **Conflict:** the summer 09:00 opening appears only on the ticketing page and looks like a data error. I used 08:00 all year. **Human check.**
- Not verified:
  - Opening status of the individual museums (Military, Police, Al-Gawhara Palace) and of Joseph's Well. The highlights avoid Al-Gawhara and Joseph's Well.
  - gov.eg also lists a "cart" fee and parking (car 25 / minibus 75 / bus 100). Both are undated and absent from the booking page, so I omitted them.

### museum-of-islamic-art — confidence: high
- Hours 09:00–17:00 with last entry 16:00. Ramadan: closing 15:00 (MoTA guide) but last entry 14:30 (ticketing), which breaks the 1-hour rule. **Minor conflict;** I kept both as published.
- Founding date conflict: gov.eg and Wikipedia say collecting began in 1880; the MoTA guide says the idea dates to 1869 under Khedive Ismail. The description uses 1880.
- Not verified: object-level gallery locations, i.e. whether the Kaaba key and Kufic textile are currently on display (taken from official descriptions).

### al-muizz-street — confidence: medium
- The street is public and always open. Hours (09:00–17:00, last entry 16:00; Ramadan 09:00–16:00, last entry 15:00) apply to the ticketed monuments.
- One area ticket costs 220/110 foreign and 20/10 Egyptian. The covered monuments, per gov.eg: Qalawun group, Sulayman Agha al-Silahdar, al-Kamil school, al-Nasir Muhammad, Barquq, Maimonides synagogue, Hammam Inal, Bashtak Palace.
- Bayt al-Suhaymi, Wikalat Bazaraa and Bab Zuwayla have separate tickets that were not captured, so they are excluded.
- Not verified:
  - Whether al-Hakim and al-Aqmar are free-entry mosques or covered by the ticket. They are described as highlights, with no price claim.
  - Opening status of each covered monument.

### sultan-hassan-mosque — confidence: high
- Price 220/110 foreign; Egyptians free (gov.eg shows EGP 0, the ticketing site has no Egyptian price). The ticket includes al-Rifa'i Mosque (gov.eg).
- Hours 09:00–17:00 with last entry 16:00. Ramadan last entry is 15:00, but the Ramadan closing time is unknown because there is no MoTA guide page. The slug was not found, so close is omitted.
- Not verified: prayer-time restrictions for tourists. The crowd note is general advice, not a sourced rule.

### coptic-museum — confidence: high
- Hours 09:00–17:00 with last entry 16:00; Ramadan 09:00–15:00 with last entry 14:00. Official sources agree.
- Not verified:
  - Whether all Nag Hammadi codices are on display.
  - Opening of the 1947 new wing, which the MoTA guide says has been linked to the old wing since 2006.
- Photo "Coptic Museum in Cairo.jpg" shows the 1910 façade and garden (historic, not modern), so it was kept.
