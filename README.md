# STM32F411 board — Robu-only BOM

Sourcing sheet for the KiCad BOM published as a gist, restricted to
[Robu.in](https://robu.in) only. Price and availability were read from each
Robu product page (the live "Availability:" field) on **2026-10-08**.

- Source BOM: <https://gist.githubusercontent.com/sounddrill31/6033fce903dc97a49997e22489ee7827/raw/ae3c2071f13c0b4f5d1b50b0dd172a400ebc95cb/bom.csv>
- Output: [`bom-robu.csv`](bom-robu.csv) — 24 BOM lines, one chosen Robu part per line
- No-exact-match list: [`not-found-exact.csv`](not-found-exact.csv)

## Availability at a glance

| Match | Lines |
|---|---|
| Exact match, in stock | 18 |
| Exact part number, alternate manufacturer | 1 (`U4` USBLC6-2SC6, MSKSEMI) |
| Exact but **out of stock** | 1 (`U2` ICM-42688-P) |
| Nearest part only — **not exact** | 3 (`SW1`, `C2`, `J1`) |
| Not found | 1 (`D2` ESD5Zxx) |

In-stock subtotal (unit price × qty) for the rows marked `In Stock`:
**₹1210.83** (excludes shipping).

## Datasheet links

Every line carries a `Datasheet` link except one:

- Unchanged BOM parts keep the original datasheet that was on the source
  BOM/CAD page (`D3,D4` PMEG2010EJ, `D2` ESD5Z, `U5` MCP73831).
- Everything else links the datasheet attached to the exact Robu product
  page for the part being bought (mostly LCSC-hosted PDFs under Robu's media
  bucket).
- `C4` is a generic "10nF 0603" pack with no datasheet; the branded 10nF 0603
  parts on Robu (`R183944`, `R183959`, `R183991`) are all currently out of
  stock. If you want a datasheet-backed 10nF, re-check those.

## Parts with no exact match on Robu

Searched by exact MPN / value+package and checked the product page, not just
the search result.

| Ref | BOM part | Status |
|---|---|---|
| `D2` | `ESD5Zxx` (onsemi ESD5Z series, SOD-523) | **Not found.** Robu carries no ESD5Z part at all. `ESD5B5.0ST1G` (R191325) is a different onsemi family and is itself Out of Stock. Other SOD-523 ESD diodes exist (e.g. `PESD5V0S1BB,115` R196522) but none are ESD5Z. [BOM datasheet](https://www.onsemi.com/pdf/datasheet/esd5z2.5t1-d.pdf) |
| `C2` | `100u` in a **0603** footprint | **No exact part.** 100 µF is not made in 0603. Nearest is 100 µF 6.3 V 0805: `CL21A107MQYNNWE` (R172120, ₹32, in stock). Footprint must change. [datasheet](https://robu-prod-media.s3.ap-south-1.amazonaws.com/uploads/2024/09/C6882730.pdf) |
| `J1` | `USB_C_Receptacle_USB2.0_14P`, footprint `JAE DX07S016JA1R1500` | **Exact MPN not stocked.** Robu sells generic 16P SMD USB-C receptacles (`TYPE-C-31-M-12` R243053, ₹26, in stock) — same idea, different part and pad layout. Original reference was the [USB Type-C spec](https://www.usb.org/sites/default/files/documents/usb_type-c.zip); bought part [datasheet](https://robu-prod-media.s3.ap-south-1.amazonaws.com/uploads/2025/08/C165948.pdf). |
| `SW1` | `SW_Push`, footprint `SW_Push_SPST_NO_Alps_SKRK` | **Exact Alps SKRK not stocked.** Generic 2-pin SMD tact switches are available (`LCK-TA003H43-1WL` R234533, ₹1.91, in stock; `KFC-003B` R132503 also in stock); the value is generic, so treat the footprint as approximate. |

Availability caveats on otherwise exact parts:

- `U2` **ICM-42688-P** (R184326, ₹2139) is listed but **Out of Stock**, no ETA published. The `601N1-ICM42688` breakout module (R243090, ₹669) is in stock, but it is not the bare IC.
- `U1` **STM32F411CEU6**: only the tape/reel part `STM32F411CEU6TR` (R233574, ₹850) is in stock. The tray part `STM32F411CEU6` (R233665, ₹704) is currently Out of Stock.
- `U4` **USBLC6-2SC6**: the ST original (R191248) is Out of Stock; the in-stock unit is the same part number from MSKSEMI (R243041, ₹11).
- `R4–R7` **10k 0603**: `FRC0603F1002TS` (R204890) went Out of Stock; `RC0603JR-0710KP` (R232165, ₹0.83) is in stock.
- `C6,C7,C13` **10u 0805**: `GRM21BC71C106KE11L` (R183924) is Out of Stock; `CC0805KKX7R7BB106` (R139368, ₹6.00) is in stock.

## Lead time

Robu does not publish a lead time. Each product page offers only a
"Check estimated delivery" widget that needs a delivery pincode; there is no
ships-in / restock / ETA field, including on out-of-stock items. So the
`Lead_Time` column is `Not published` throughout, and Out of Stock parts have
no announced restock date. If lead time matters, Robu's support/B2B channel
(`sales@robu.in`) is the only place to ask.

## Method

1. Parsed the KiCad BOM (24 lines).
2. Searched robu.in per part (exact MPN, then value + package) via the
   rendered site.
3. Opened each chosen product page and recorded the live `Availability:`
   field, price, SKU, MPN and attached datasheet. Search-result badges were
   **not** trusted — several disagreed with the product page.
4. Marked a line `exact` only when the MPN (or value + package) matched.

Regenerate with `gen_bom.py` (edit the table, re-run) — the checked numbers
are baked into that file as of the date above.
