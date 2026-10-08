# STM32F411 board — Robu-only BOM

Sourcing sheet for the KiCad BOM published as a gist, restricted to
[Robu.in](https://robu.in) only. Price and availability were read from each
Robu product page (the live "Availability:" field) on **2026-10-08**.

This is the second revision of the BOM (BMI270 IMU, merged 100n cap bank).

- Source BOM: <https://gist.github.com/sounddrill31/d541ce976d5dd1ef796bc9f4f8303f96> (`bom2.csv`)
- Previous revision (ICM-42688-P): gist `6033fce903dc97a49997e22489ee7827`
- Output: [`bom-robu.csv`](bom-robu.csv) — 23 BOM lines, one chosen Robu part per line
- No-exact-match list: [`not-found-exact.csv`](not-found-exact.csv)

## Availability at a glance

| Match | Lines |
|---|---|
| Exact match, in stock | 17 |
| Exact part number, alternate manufacturer | 1 (`U4` USBLC6-2SC6, MSKSEMI) |
| Exact but **out of stock** | 1 (`U6` BMI270) |
| Nearest part only — **not exact** | 2 (`SW1`, `J1`) |
| Not found | 1 (`D2` ESD5Zxx) |
| No component to buy | 1 (`J7,J8` bare solder pad) |

In-stock subtotal (unit price × qty) for the rows marked `In Stock`:
**₹1181.87** (excludes shipping, excludes the out-of-stock `U6`).

## IMU swap

`U2 ICM-42688-P` was replaced by `U6 BMI270`. The BMI270 bare IC **is** on
Robu but is currently **Out of Stock**:

| Ref | Robu part | SKU | Price | Availability |
|---|---|---|---|---|
| `U6` | BOSCH BMI270 6-Axis IMU, LGA-14 | R155006 | ₹599 | **Out of Stock** — no ETA |

It is the only bare BMI270 listing on Robu; the other BMI270 hits are flight
controllers/boards, not the IC. So the swap did not fix the availability
problem — the exact IMU is still not orderable today. Datasheet:
[BMI270 (Bosch)](https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bmi270-ds000.pdf).

## Datasheet links

Every line carries a `Datasheet` link except `J7,J8` (nothing to buy):

- Unchanged BOM parts keep the original datasheet from the source CAD page
  (`D3,D4` PMEG2010EJ, `D2` ESD5Z, `U5` MCP73831).
- Everything else links the datasheet attached to the exact Robu product page
  for the part being bought (mostly LCSC-hosted PDFs under Robu's media
  bucket), or the manufacturer datasheet where the product page has none.

## Parts with no exact match on Robu

Searched by exact MPN / value+package and checked the product page, not just
the search result.

| Ref | BOM part | Status |
|---|---|---|
| `D2` | `ESD5Zxx` (onsemi ESD5Z series, SOD-523) | **Not found.** Robu carries no ESD5Z part at all. `ESD5B5.0ST1G` (R191325) is a different onsemi family and is itself Out of Stock. Other SOD-523 ESD diodes exist (e.g. `PESD5V0S1BB,115` R196522) but none are ESD5Z. [BOM datasheet](https://www.onsemi.com/pdf/datasheet/esd5z2.5t1-d.pdf) |
| `J1` | `USB_C_Receptacle_USB2.0_14P`, footprint `JAE DX07S016JA1R1500` | **Exact MPN not stocked.** Robu sells generic 16P SMD USB-C receptacles (`TYPE-C-31-M-12` R243053, ₹26, in stock) — same idea, different part and pad layout. Original reference was the [USB Type-C spec](https://www.usb.org/sites/default/files/documents/usb_type-c.zip); bought part [datasheet](https://robu-prod-media.s3.ap-south-1.amazonaws.com/uploads/2025/08/C165948.pdf). |
| `SW1` | `SW_Push`, footprint `SW_Push_SPST_NO_Alps_SKRK` | **Exact Alps SKRK not stocked.** Generic 2-pin SMD tact switches are available (`LCK-TA003H43-1WL` R234533, ₹1.91, in stock; `KFC-003B` R132503 also in stock); the value is generic, so treat the footprint as approximate. |
| `J7,J8` | `Conn_01x01_Socket`, footprint `SolderWirePad_1x01_SMD_1x2mm` | **No component to buy.** This is a bare 1×2 mm exposed SMD solder pad on the PCB for soldering a wire to — board copper, not a purchased part, so there is nothing to source on Robu. |

Availability caveats on otherwise exact parts:

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

1. Parsed the KiCad BOM (23 lines) from the gist.
2. Searched robu.in per part (exact MPN, then value + package) via the
   rendered site.
3. Opened each chosen product page and recorded the live `Availability:`
   field, price, SKU, MPN and attached datasheet. Search-result badges were
   **not** trusted — several disagreed with the product page.
4. Marked a line `exact` only when the MPN (or value + package) matched.

Regenerate with `gen_bom.py` (edit the table, re-run) — the checked numbers
are baked into that file as of the date above.
