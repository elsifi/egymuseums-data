# Batch 11 enrichment report

Checked 2026-10-05. 28 minor places: dar-ibn-luqman, damietta-science-museum, fayoum-art-center, karanis-site-museum, hawara-pyramid, karanis, lahun-pyramid, medinet-madi, qasr-qarun, tanta-museum, adam-henein-museum, ahmed-shawki-museum, giza-solar-boat-museum, giza-zoo-zoological-museum, mohamed-nagy-museum, pharaonic-village, ramses-wissa-wassef-art-centre, taha-hussein-museum, bahariya-oasis-antiquities, al-turathiya-museum-ismailia, archaeological-museum-of-ismailia, suez-canal-historical-exhibition, suez-canal-museum, kafr-el-sheikh-museum, deir-el-shelwit, el-assasif-tombs, el-khokha-tombs, el-moalla-tombs.

`python3 tools/validate_all.py`: 25 of the 28 files pass. Three fail only the "at least one photo" rule: adam-henein-museum, mohamed-nagy-museum and damietta-science-museum. The house rule says to leave photos empty when no compliant photo exists (see question 1).

| Status | Count | Places |
|---|---|---|
| open | 20 | 5 Fayoum sites, Kom Aushim museum, Tanta, Kafr el-Sheikh, Bahariya, 4 Luxor-area necropolises and temples, Dar Ibn Luqman, Ahmed Shawki, Mohamed Nagy, Taha Hussein, Adam Henein, Wissa Wassef, Suez Canal Museum |
| unknown | 6 | Ismailia Antiquities Museum, Pharaonic Village, Fayoum Art Center, Damietta Science Museum, Al-Turathiya, Suez Canal historical exhibition |
| renovation | 1 | Giza Zoo Zoological Museum |
| closed | 1 | Giza Solar Boat Museum |

| Confidence | Count |
|---|---|
| high | 3 (kafr-el-sheikh-museum, deir-el-shelwit, giza-solar-boat-museum) |
| medium | 17 |
| low | 8 (Ismailia museum, Pharaonic Village, Fayoum Art Center, Damietta, Al-Turathiya, Suez Canal historical exhibition, Zoo museum, Wissa Wassef) |

URL check (5 Oct 2026, 250 URLs):
- All source pages return HTTP 200, with three exceptions:
  - pharaonicvillage.com and yellowpages.com.eg return 403, because they block bots;
  - cairoscene.com timed out, though it had loaded earlier in the session.
- Commons image URLs returned 429 (rate limit) to the bulk check. All of them were taken from the Commons API in this session.

## Where the data comes from

- **MoTA open-sites and open-museums guides** (mota.gov.eg, live, undated). Their listing is loaded by JavaScript. I read it through the site's own `POST /GenericList/GetAllGrouped` API: page 17737 for museums and 17739 for sites. This gave guide pages for 13 of my SCA places, with hours, Ramadan hours and addresses.
- **egymonuments.com booking platform** (`/details/<Key>` and `/book-date/<n>`): Kafr el-Sheikh, Deir el-Shelwit, Assasif (plus Pabasa), Khokha (via Tombs of the Nobles), Mo'alla and the Suez Canal Museum.
- **Nov 2024 MoTA ticket PDF**: the only official price source for the 5 Fayoum sites, Kom Aushim, Tanta and the Ismailia museum.
- **Fine Arts Sector**: the fineart.gov.eg visitor pages (IDs 2, 7, 9, 32) give prices and older hours. The sector's dated statements on youm7 (4 Jun 2026 for summer hours, Feb 2026 for Ramadan) are used as in batch 5.
- **Private places**: official websites where they could be read (Adam Henein, Fayoum Art Center) and dated press.
- **Arab tier**: none at SCA sites (house rule). The Fine Arts and private places have no Arab tier anyway.

## Per place: unverified items and conflicts

**Fayoum: hawara-pyramid, karanis, lahun-pyramid, medinet-madi, qasr-qarun, karanis-site-museum**
- Hours come from the MoTA guide: sites 08:00–17:00 (last entry 16:00), with a Ramadan exception of 09:00–16:00 (last entry 15:00). The museum is open 09:00–15:00 with the same hours in Ramadan.
- Prices come only from the Nov 2024 list: 150/75 at four sites, 120/60 at Medinet Madi, 100/50 at the museum; Egyptian 10/5 everywhere.
- None of these places is on the booking platform, so there is no `onlineUrl` and no official free groups.
- Not verified:
  - whether the Hawara and Lahun pyramid interiors are open (the text only says Lahun "opened to visitors in 2019");
  - sunrise access at Qasr Qarun on 21 December.
- `name.ar` of karanis-site-museum: changed locally to the official "متحف كوم أوشيم". The seed form is kept as an alias.

**tanta-museum**
- Open: dostor reported an exhibition there on 18 May 2026.
- Prices 150/75, 20/10, from the Nov 2024 list only.

**kafr-el-sheikh-museum**
- The portal, guide, booking site and 2024 list all agree.
- The photo is a Buto site statue, not a museum object (question 6).

**archaeological-museum-of-ismailia**
- **Not in the live MoTA open-museums list** and not on egymonuments.com. The last dated report of visitors is youm7, Aug 2024.
- Set to `unknown`/low. Hours and prices are kept from the Nov 2024 list (question 3).

**bahariya-oasis-antiquities**
- The SCA board decision of 9 Jul 2026 is published on mota.gov.eg: **400/200 foreign, 40/20 Egyptian from 1 Oct 2026**.
- `effectiveFrom` is set to 2026-10-01 because MoTA's own dated statement is the source (question 4).
- Not verified: which monuments one ticket covers.

**Luxor West Bank: deir-el-shelwit, el-assasif-tombs, el-khokha-tombs**
- These use the standard West Bank pattern: 06:00–17:00 with last entry 16:00, and a summer 2026 exception of 06:00–18:00 (last entry 17:00) running until 29 Oct.
- No Ramadan exception: Ramadan hours equal the winter week.
- The Pabasa tomb is an extra on the Assasif record (100/50, 10/5).
- Khokha is sold as a Tombs of the Nobles group (120/60, 10/5).
- Not verified: which tombs each ticket opens.

**el-moalla-tombs**
- Opening-time conflict: the guide and the 2024 list say 07:00, the booking site says 08:00 (last entry 16:00). I used the narrowest window, 08:00–17:00 (batch-7 Q1a).
- Ramadan: last entry 15:00 only.

**Fine Arts Sector museums: dar-ibn-luqman, ahmed-shawki-museum, taha-hussein-museum, mohamed-nagy-museum**
- Prices 5/3/10 and the free groups come from the undated official visitor pages.
- Mohamed Nagy is named in the sector's 4 Jun 2026 statement (09:00–16:00, closed Fri and Mon).
- The other three are not named in that statement. For them I used the official page's 10:00–16:00 with the same closed days (question 2).
- Ramadan is sector-wide 10:00–14:00.
- Dar Ibn Luqman is the Fine Arts Sector's "Mansoura National Museum".

**adam-henein-museum**
- Hours conflict: the official site says daily 09:00–16:00, CairoScene (Oct 2025) says 10:00–16:00. I used 10:00–16:00, with last entry 15:30 (the site says ticket sales stop 30 minutes before closing).
- Prices from the official site: Egyptians 10, non-Egyptians 50.
- No Wikidata item and no coordinates.
- No compliant photo.

**ramses-wissa-wassef-art-centre**
- I added `wikidataId` Q126920240, its coordinates and the en-wiki link (question 7).
- The official site could not be read, so there are no hours and prices are `unconfirmed`.
- The photo shows the centre's gate (question 6).

**pharaonic-village**
- Set to `unknown`/low. The official site is behind a browser challenge, and the newest dated price list is from 2020.

**fayoum-art-center**
- I added `wikidataId` Q134292187 and its coordinates.
- Set to `unknown`/low. No visiting hours or fees are published, and the newest dated press item is from 2024.
- The photo is a landscape of Lake Qarun at Tunis village, not the centre.

**giza-solar-boat-museum**
- `closed`/high: the museum was dismantled after the boat moved to the GEM in 2021.
- No hours or prices.
- The one photo shows the boat inside the old museum, with the 1980s interior visible (question 6).

**giza-zoo-zoological-museum**
- `renovation`. The whole zoo is closed, and its reopening is planned for Q4 2026 (elbalad, 2 Oct 2026).
- Coordinates are the Giza Zoo's Wikidata point (approximate).

**suez-canal-museum**
- It is on the MoTA booking site, which charges 400/200 foreign and 40/20 Egyptian.
- The foreign price rose on 1 Jul 2026 by an SCA board decision (5 May 2026). That decision is known only from a news report, so there is no `effectiveFrom`.
- Hours 09:00–17:00 with last entry 16:00; Ramadan last entry 14:00.
- The photo is the 1862 de Lesseps house. It is likely, but not confirmed, to be the museum building.
- This is a different place from batch 13's `suez-canal-authority-museum` (a villa in Port Said).

**suez-canal-historical-exhibition**
- `unknown`/low. No source after 2017 mentions it; it may have been replaced by the Suez Canal Museum (question 5).

**damietta-science-museum, al-turathiya-museum-ismailia**
- Nothing verifiable beyond a directory listing and the ar-wiki list, so neither has a description or highlights.
- The Al-Turathiya photo is a generic simsimiyya player, used as a placeholder.
- Question 5 asks whether to remove both.

## Decisions needed (recommended answer in **bold**)

1. **Places with no compliant photo** (adam-henein-museum, mohamed-nagy-museum, damietta-science-museum; the validator fails them):
   **(a) Allow 0 photos for minor places and relax the validator to a warning.**
   (b) Use a loosely related compliant image, such as a landscape or portrait.
   (c) Drop these places until a photo exists.
2. **Fine Arts museums not named in the sector's June 2026 hours statement** (Dar Ibn Luqman, Ahmed Shawki, Taha Hussein):
   **(a) Keep 10:00–16:00 from the official page (narrowest window) and confirm by phone.**
   (b) Apply the sector's 09:00–16:00 to all of them.
3. **Ismailia Antiquities Museum is missing from MoTA's current open-museums list:**
   **(a) Keep it as `unknown` with the 2024 hours and prices, and confirm via hotline 19654.**
   (b) Mark it `closed`.
   (c) Mark it `open` on the strength of the Nov 2024 price list.
4. **Bahariya `effectiveFrom` 2026-10-01** (the source is MoTA's own dated statement of the board decision):
   **(a) Keep it.**
   (b) Remove it, as was done for the Abu Simbel/Philae news-only cases.
5. **Unverifiable or superseded records** (damietta-science-museum, al-turathiya-museum-ismailia, suez-canal-historical-exhibition):
   **(a) Hide them from the app until confirmed. Keep the files for curation.**
   (b) Delete them from the seed.
   (c) Show them with a "Details unconfirmed" badge.
6. **Borderline photos:**
   - the Wissa Wassef gate (the architect died in 1974, so the building is public domain in Egypt, but it dates from the 1950s);
   - the Solar Boat inside the 1980s museum;
   - the Buto statue for Kafr el-Sheikh;
   - the Lake Qarun landscape for the Fayoum Art Center;
   - the de Lesseps house for the Suez Canal Museum.

   **(a) Keep them and replace them when better files appear.**
   (b) Remove all five.
7. **Wikidata IDs and coordinates added where the seed had none** (Wissa Wassef Q126920240, Fayoum Art Center Q134292187, Zoo museum coordinates taken from the Giza Zoo item):
   **(a) Keep them and backport them to the seed.**
   (b) Revert to the seed values.
8. **Giza Solar Boat Museum (demolished):**
   **(a) Keep it as `closed`, with a note pointing to the Grand Egyptian Museum.**
   (b) Remove it from the catalogue.
9. **Fayoum Art Center: what to list.** Its public-facing part is the Caricature Museum.
   **(a) Keep the centre as the place and the Caricature Museum as a highlight.**
   (b) Rename it to "Caricature Museum (Fayoum Art Center)".

## Scheduled rechecks

- **After 29 Oct 2026:** winter hours for Deir el-Shelwit, Assasif and Khokha.
- **Q4 2026:** Giza Zoo reopening, and whether the zoological museum reopens with it.
- **Early 2027:** Ramadan 2027 hours for the Fayoum sites, Bahariya, Kafr el-Sheikh, Mo'alla, the Suez Canal Museum and the Fine Arts museums.
- **Any time:** Ismailia museum status, and Pharaonic Village hours and prices (phone).
