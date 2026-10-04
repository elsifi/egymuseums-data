# Batch 3 enrichment report

Checked 2026-10-04. Places: medinet-habu, luxor-museum, abu-simbel, philae-temple, nubia-museum, kom-ombo-temple, edfu-temple, dendera-temple, abydos-temple-of-seti-i, saint-catherines-monastery.

All 10 files validate against `data/schema/place.schema.json` (stdlib validator from `tools/seed/validate.py`; `jsonschema` is not installed). Each description is 160–180 English words, with 6 highlights and 3 Wikimedia Commons photos.

## How the hours and prices are backed (read this first)

- **Main sources: two live official MoTA pages per place, checked 2026-10-04.**
  - `egymonuments.gov.eg`, the portal: open and close times, tiers and add-ons.
  - `egymonuments.com/details/<Site>`, the official booking platform: last entry, summer/winter/Ramadan rows, free-entry groups.
  - **Neither page has a publication date.** I counted them as current because they are the live official channels. If a page with a visible 2025–2026 date is required, most figures need a dated source before release.
- **Figures that do have dated 2025–2026 sources:**
  - Luxor Museum prices and hours (elwatannews, 1 May 2026).
  - Abydos Ramadan hours (youm7, Feb 2025).
  - Sun-alignment logistics at Abu Simbel (youm7, Oct 2025 and Feb 2026).
  - St Catherine hours and closure calendar (masrawy, 9 Apr 2026).
  - The Arab-tier change (dostor, 9 Jul 2025).
- **Precedence when sources conflict:** venue's own site, then egymonuments.gov.eg, then the egymonuments.com booking platform, then MoTA's Nov 2024 PDF. The PDF was only used as a cross-check.
- **Arab tier:** the SCA ended the Arab = Egyptian pricing from Jan 2026 (dostor 5134866). The booking platform now shows only "Other Nationality" and "Egyptian". No `arab-resident` tiers were added.
- **Foreign-resident tier:** not shown on any official page for these places, so it was left out.
- **`effectiveFrom` = 2024-11-01** for Abu Simbel, Philae, Edfu and Kom Ombo. A 2024 report of the SCA decision lists exactly these foreign prices from 1 Nov 2024. For the other places no decision date was found, so the field is omitted.
- **`cashAccepted`:**
  - `false` for Abu Simbel, Philae, Edfu, Kom Ombo, Nubia Museum and Luxor Museum. MoTA made them card-only in May–June 2023 (youm7, Egypt Independent), and I found no reversal.
  - No 2025–2026 official re-confirmation was found.
  - `null` for Medinet Habu, Dendera and Abydos, which had no official card-only statement. Third-party 2026 guides say Medinet Habu is card-only.
- **`timedEntry`:** `null` everywhere. The booking pages show no time-slot information.
- **Not used:** a Sept 2026 MoTA "CPS" system for bulk tickets bought by tour companies. It is a B2B channel, not a visitor-facing change.
- **Oasis price rise:** a July 2026 SCA decision raises Western Desert oasis prices from 1 Oct 2026. It does not cover these places. No 2026 increase for these 10 places was found.

## Schema limitations (need a decision)

- `statusNote` and `area` are plain strings. I wrote them bilingually as `English ‖ Arabic` and `English | Arabic`. Should these become localized objects?
- `highlights` items are a single localized string. Title and one-line description are joined as `Title — description`. A `{title, desc}` structure would be cleaner.
- `dayHours` allows one session per day. Split days (Luxor Museum mornings and evenings, Nubia Museum Thu/Fri evenings) are written as two entries for the same day.
- `prices.extras` has no audience/group fields. Each audience is a separate labelled extra.
- No field holds a free-text price or visit note, such as "online price includes a surcharge" or the Philae boat. These went into `statusNote`, `hours.exceptions` labels and `visit.crowdNotes`.

## Per place

### medinet-habu — confidence: medium
- **Conflict:** foreign adult is EGP 230 on the portal and EGP 220 on the booking platform, MoTA's Nov 2024 PDF and third-party 2026 guides. Per precedence I recorded 230. Student 110 and Egyptian 20/10 agree everywhere. **A human should decide.**
- **Last-entry conflict:** the booking platform gives summer last entry 17:00, which is the portal's closing time, and winter/Ramadan last entry 16:00. I recorded 16:00 for the normal week and 17:00 as a "summer" exception. Season dates are not published.
- **Not verified:** card-only status. No accessibility or facilities data. The free-entry groups come from the booking platform's generic list.

### luxor-museum — confidence: medium
- Prices (400/200, 30/10) and the 09:00–14:00 / 17:00–21:00 winter schedule are confirmed by the booking platform and elwatannews (1 May 2026). There is no portal page.
- **Not verified:**
  - Summer closing times. The booking platform only gives summer last entries (12:00 and 19:00).
  - Ramadan closing times.
  - Summer/winter season dates.
- **Audio guide extra:** EGP 30 Egyptian / 50 foreign on the Nov 2024 PDF, with no 2025–2026 source. Left out.
- **No museum-specific phone or website.** Wikidata lists sca-egypt.org and egymonuments.com, which are generic.

### abu-simbel — confidence: medium
- **Conflict, needs a decision:**
  - The portal (and the 2024 decision) says foreign adult/student EGP 750/375, Egyptian 30/10, alignment day 1200/600 and 60/20. I recorded these.
  - The booking platform charges 822/445.5, 30.5/10.5, and 1272/670.5 on alignment days.
  - The gap is a flat +72 / +70.5 / +0.5 EGP, which looks like a surcharge or fee on the official channel. Third-party 2026 guides quote 822 as "the" price.
  - **It is not confirmed whether the gate also charges 822.**
- **Parking extras** (car 25, microbus 50, coaster 75, bus 100) come from the portal only. The Nov 2024 PDF has slightly different values (25 / 75 minibus / 100).
- **Not verified:**
  - Current road or convoy arrangements and flight schedules from Aswan. The visit notes only say "pre-dawn road trips… several hours".
  - Gate times for 22 Oct 2026. The exception uses Oct 2025 times: ticket office 03:00, gates 03:30, alignment about 06:55.
- **Not included:** the sound and light show. It is a separate ticket from a separate operator.

### philae-temple — confidence: medium
- Hours 07:00–16:00, last entry 15:00. Prices 550/275 and 40/20. Panorama extra 200/100 and 40/20 (portal only, matching the Nov 2024 PDF).
- **Boat fare:** deliberately not given as a number. Third-party sites quote about EGP 300 per boat for a 2026 round trip, but **no official source** was found. The visit notes only say boats are private, paid separately, and the fare should be agreed before boarding.
- **Not verified:** what the "panorama" ticket covers (presumably a raised viewpoint or roof).

### nubia-museum — confidence: medium
- **Ramadan conflict:** the portal says 09:00–15:00 with the ticket office closing at 14:00, which I used. The booking platform says Ramadan last entry 16:00.
- **Address:** "El Fanadek St., Aswan" comes from Wikidata P6375 only, with no official confirmation.
- **Issue for Wikidata:** Wikidata P856 points to `nubianmuseum.com`, which now redirects to a gambling site. It is not used here, and the Wikidata statement should be fixed or deprecated.
- **Phone numbers** in Wikidata (P1329) are unverified, so `contacts` was left out.
- **Photos:** artefacts only (Ramesses II from Gerf Hussein, Horemakhet, Taharqa). There are no images of the modern building or galleries because Egypt has no freedom of panorama.
- **Not verified:** the photography/tripod ticket price and the audio guide.

### kom-ombo-temple — confidence: medium
- Hours 07:00–21:00, last entry 20:00. Prices 450/225 and 40/20.
- **Not verified:**
  - Whether the Crocodile Museum is included in the temple ticket. The Nov 2024 PDF lists it "within Kom Ombo Temple" with no separate price; current booking and portal pages don't mention it. It is listed as a highlight only.
  - Parking extras (portal: microbus 50; Nov 2024 PDF: minibus 50).
- **`facilities.visitorCenter`** rests on an undated MoTA portal news item.

### edfu-temple — confidence: medium
- Opens 06:00 on Sun/Wed and 07:00 otherwise. Closes 17:00 and last entry is 16:00 (booking platform). Prices 550/275 and 40/20. The portal and booking platform agree.
- **Not verified:** the horse-carriage fare from the river landing, which is not an official ticket.

### dendera-temple — confidence: medium
- Main prices are 300/150 and 20/10 on both the portal and the booking platform.
- **Conflict:** an elwatannews article (Jan 2025) quotes foreign 120/60. Both official channels disagree, so it was ignored.
- **Extras** come from the portal only:
  - Roof/panorama: foreign 100, Egyptian 20.
  - Crypts: foreign 100, Egyptian 50. This matches the SCA decision effective 1 Jun 2023 (elbalad).
  - Parking.
  - **No 2025–2026 dated source** for these. The Nov 2024 PDF shows the roof as "50 | 100" with unclear columns.
- **Status of the roof and crypts:** the portal implies they are open. This was not separately confirmed.

### abydos-temple-of-seti-i — confidence: medium
- **Sources:** the booking platform for prices 260/130 and 10/5, opening 07:00 and last entry 16:00. youm7 (Feb 2025) for Ramadan: 09:00–16:00, ticket office closes 15:00. There is no portal page.
- **Closing time 17:00 is not confirmed by any 2025–2026 source.** It comes from the Nov 2024 PDF and the booking platform's "arrive one hour before closing" rule. A human should decide whether to keep `close`.
- **Not verified:**
  - Whether the Osireion is included or viewable, and whether the nearby Temple of Ramesses II needs a separate ticket.
  - Current transport or security-escort requirements from Luxor.

### saint-catherines-monastery — confidence: low
- **Hours conflict, needs a decision:**
  - masrawy (9 Apr 2026, quoting the monastery's adviser): Sat–Thu 08:45–11:30, Fri 10:45–11:30. Sunday appears open: the article reports a reopening "on Sunday 12 April". **This schedule was used.**
  - The monastery's own site (undated text): open 09:00–11:30, **closed Fridays and Sundays**.
  - The egymonuments portal: 08:45–12:45, Friday 10:30–11:30, Sunday closed.
- **Closures:** 28 feast-day closures in 2026, per month (masrawy). Exact November and December dates are not known.
- **Prices:** no official 2025–2026 source for any entry fee for the monastery or its museum. A 25 EGP museum fee appears only on old travel sites. `prices` and `tickets` are omitted. MoTA's Nov 2024 PDF lists the monastery with hours only, no price.
- **Dress code:** the monastery asks for appropriate "decorum in habit". The specific rule (shoulders and knees) was not found officially, so the text only says "modest dress".
- **Status context:** in 2025 the monastery closed to visitors for a period after the 28 May 2025 Ismailia appeals-court ruling on its lands. youm7 reports regular visitors in Jun–Sep 2026, so the status is `open`. The political situation should be watched.
- **Contacts:** the official site and a fax number (+20 69 3470 341) only. No public phone line was found.
- **Not verified:** Mount Sinai climbing logistics and fees, which are outside the monastery and set by others.

## Photos

30 files, all checked through the Commons API for licence and author: CC BY 3.0/4.0, CC BY-SA 2.0/3.0/4.0, CC0 or public domain. Subjects are ancient or historic structures and artefacts. The St Catherine walls are 6th century, and one St Catherine image is a 1911 public-domain photo. There are no modern buildings or interiors as main subjects.
