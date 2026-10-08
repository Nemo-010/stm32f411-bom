#!/usr/bin/env python3
"""Generate the Robu-only BOM CSV from the KiCad BOM + live Robu lookups.

Source: sounddrill31 gist bom2.csv (revision with BMI270 IMU), retrieved 2026-10-08.
"""
import csv, os

DATE = "2026-10-08"
OUT = os.path.dirname(os.path.abspath(__file__))
R = "https://robu-prod-media.s3.ap-south-1.amazonaws.com/uploads"

# Reference, Qty, Value, Package, Robu product, SKU, MPN, unit price, availability,
# lead time, match, url, notes, datasheet
rows = [
 ["SW1",1,"SW_Push","SMD tact (Alps SKRK footprint)",
  "LCK-TA003H43-1WL LCKELEC 3x6x4.3mm SMD Tact Switch","R234533","LCK-TA003H43-1WL","1.91","In Stock","Not published",
  "nearest-not-exact","https://robu.in/product/lck-ta003h43-1wl-lckelec-364-3-smd-without-column-180g-force-black-button-tact-switch/",
  "BOM value is generic SW_Push; Alps SKRK is not stocked. Generic SMD tact switch, not the exact Alps footprint. KFC-003B R132503 also in stock.",
  f"{R}/2025/08/LCK-TA003HXX-1WL.pdf"],
 ["SW2",1,"SW_SPDT","MSK12C02 SPDT slide, SMD",
  "MSK12C02-HB Shouhan SPDT SMD Slide Switch","R235199","MSK12C02-HB","8.00","In Stock","Not published",
  "exact","https://robu.in/product/msk12c02-hb-shou-han-horizontal-attachment-50ma-single-pole-double-throw-spdt-12v-10000-times-black-smd-slide-switches-rohs/",
  "Exact MSK12C02 (Shouhan). Also MSK12C02-SHOU HAN R235206 in stock.",
  f"{R}/2025/08/C431541.pdf"],
 ["C8,C9",2,"22p","0402 MLCC",
  "GRM1555C1H220JA01D Murata 22pF 50V C0G 5% 0402","R137672","GRM1555C1H220JA01D","0.68","In Stock","Not published",
  "exact","https://robu.in/product/grm1555c1h220ja01d-murata-cap-ceramic-22pf-50v-c0g-5-pad-smd-0402-125c-t-r/","",
  f"{R}/2024/06/C76960.pdf"],
 ["C2,C4,C5,C10,C11,C12,C14,C15",8,"100n","0603 MLCC",
  "GRM188R71H104KA93D Murata 100nF 50V X7R 0603","R207385","GRM188R71H104KA93D","1.88","In Stock","Not published",
  "exact","https://robu.in/product/grm188r71h104ka93d-murata-electronics-50v-100nf-x7r-%c2%b110-0603-multilayer-ceramic-capacitors-mlcc-smd-smt-rohs/",
  "Revision merged the old 100u/0603 and 10n/0603 lines into eight 100nF; this covers all eight.",
  f"{R}/2025/02/C77055.pdf"],
 ["C1",1,"4.7u","0805 MLCC",
  "0805X475K500NT-FH 4.7uF 50V X5R 0805","R136796","0805X475K500NT-FH","1.89","In Stock","Not published",
  "exact","https://robu.in/product/0805x475k500nt-fh-50v-4-7uf-x5r%c2%b110-0805-multilayer-ceramic-capacitors-mlcc-smd-smt-rohs/","",
  f"{R}/2024/06/C967591.pdf"],
 ["C6,C7,C13",3,"10u","0805 MLCC",
  "CC0805KKX7R7BB106 Yageo 10uF 16V X7R 0805","R139368","CC0805KKX7R7BB106","6.00","In Stock","Not published",
  "exact","https://robu.in/product/cc0805kkx7r7bb106-yageo-16v-10uf-x7r-%c2%b110-0805-multilayer-ceramic-capacitors-mlcc-smd-smt-rohs/",
  "Cheaper alternative 0805X106K500NT-FH R139409 (Rs4.55) also in stock. GRM21BC71C106KE11L R183924 is OOS.",
  f"{R}/2024/07/C326595.pdf"],
 ["J6",1,"Conn_01x02_Socket","PinHeader 1x02 P1.00mm",
  "PH1.0-01-02PZD XUNPU 1x2 1.0mm Pin Header","R219011","PH1.0-01-02PZD","3.19","In Stock","Not published",
  "exact","https://robu.in/product/ph1-0-01-02pzd-xunpu-plugin1x2-pin-1mm-pin-headers-rohs/",
  "Matches 1.00mm pitch header footprint. Female-header variant FH1.0-01-02PZD R219058 also exists.",
  f"{R}/2025/06/C30607484.pdf"],
 ["J3,J4,J5",3,"Conn_01x04_Socket","PinHeader 1x04 P1.00mm",
  "PH1.0-01-04PZD XUNPU 1x4 1.0mm Pin Header","R219013","PH1.0-01-04PZD","4.25","In Stock","Not published",
  "exact","https://robu.in/product/ph1-0-01-04pzd-xunpu-plugin1x4-pin-1mm-pin-headers-rohs/","",
  f"{R}/2025/06/C30607486.pdf"],
 ["J2",1,"Conn_01x05_Socket","PinHeader 1x05 P1.00mm",
  "PH1.0-01-05PZD XUNPU 1x5 1.0mm Pin Header","R219014","PH1.0-01-05PZD","8.00","In Stock","Not published",
  "exact","https://robu.in/product/1-month-warranty-891/",
  "Matches 1.00mm pitch header footprint. Female-header variant FH1.0-01-05PZD R219061 also exists.",
  f"{R}/2025/06/C30607487.pdf"],
 ["J1",1,"USB_C_Receptacle_USB2.0_14P","JAE DX07S016JA1R1500",
  "TYPE-C-31-M-12 Hroparts 16P Female USB-C SMD","R243053","TYPE-C-31-M-12","26.00","In Stock","Not published",
  "nearest-not-exact","https://robu.in/product/type-c-31-m-12-hroparts-5a-1-16p-female-type-c-smd-usb-connectors-rohs/",
  "Exact JAE DX07S016JA1R1500 not stocked. 16P SMD USB-C; verify pad layout vs the 14P footprint. Original BOM ref: usb.org USB Type-C spec zip.",
  f"{R}/2025/08/C165948.pdf"],
 ["J7,J8",2,"Conn_01x01_Socket","SolderWirePad 1x01 SMD 1x2mm",
  "","","","","n/a","n/a",
  "no-component","",
  "Bare exposed SMD solder pad on the PCB for soldering a wire to; it is board copper, not a part you buy. Nothing to source on Robu.",
  ""],
 ["Y2",1,"Crystal_GND24 (8MHz)","Crystal 3225 4-pin",
  "X32258MOB4SI YXC 8MHz 12pF SMD3225-4P","R233569","X32258MOB4SI","26.00","In Stock","Not published",
  "exact","https://robu.in/product/x32258mob4si-yxc-crystal-oscillators-8mhz-surface-mount-crystal-12pf-%c2%b110ppm-%c2%b120ppm-smd3225-4p-crystals-rohs/",
  "Schematic labels 8MHz; 4-pad 3225 SMD crystal.",
  f"{R}/2025/06/C2682775.pdf"],
 ["D3,D4",2,"PMEG2010EJ","SOD-323F",
  "PMEG2010EJ,115 Nexperia 20V 1A SOD-323F","R242172","PMEG2010EJ,115","10.00","In Stock","Not published",
  "exact","https://robu.in/product/pmeg2010ej115-nexperia-20v-500mv1a-1a-sod-323f-schottky-diodes-rohs/","",
  "https://assets.nexperia.com/documents/data-sheet/PMEG2010EH_EJ_ET.pdf"],
 ["D2",1,"ESD5Zxx","SOD-523",
  "PESD5V0S1BB,115 Nexperia SOD-523 ESD (nearest)","R196522","PESD5V0S1BB,115","4.66","In Stock","Not published",
  "not-found","https://robu.in/product/pesd5v0s1bb115-nexperia-pesd5v0s1bb115-esd-protection-device-tvs-14-v-sod-523-2-pins-130-w/",
  "No ESD5Z-series (onsemi) part on Robu; ESD5B5.0ST1G R191325 is OOS. Nearest is a different ESD family. Datasheet is the original BOM part.",
  "https://www.onsemi.com/pdf/datasheet/esd5z2.5t1-d.pdf"],
 ["D1",1,"LED","LED 0201/0603",
  "XL-1608SURC-06 XINGLIGHT red 0603 LED","R199352","XL-1608SURC-06","0.50","In Stock","Not published",
  "exact","https://robu.in/product/xl-1608surc-06-xinglight-20ma-330mcd-colorless-transparent-lens-20%e2%84%8385%e2%84%83-positive-stick-620nm630nm-red-120-50mw-2-3v-0603-led-indication-discrete-rohs/",
  "Generic LED; 0603. Pick colour as needed.",
  f"{R}/2025/01/C965799.pdf"],
 ["U5",1,"MCP73831-2-MC","DFN-8 (MC)",
  "MCP73831T-2ACI/MC Microchip Li-Ion charger DFN-8","R193604","MCP73831T-2ACI/MC","145.00","In Stock","Not published",
  "exact","https://robu.in/product/mcp73831t-2aci-mc-microchip-battery-charger-1-cell-of-li-ion-li-pol-battery-6v-input-4-2v-500ma-charge-dfn-8/",
  "Exact MCP73831-2ACI/MC in DFN-8 (tape variant). Non-T/MC R194841 is OOS.",
  "https://ww1.microchip.com/downloads/en/DeviceDoc/20001984g.pdf"],
 ["R3",1,"330","0402",
  "RC0402FR-07330RL Yageo 330R 1% 0402","R135686","RC0402FR-07330RL","0.09","In Stock","Not published",
  "exact","https://robu.in/product/rc0402fr-07330rl-yageo-res-thick-film-0402-330-ohm-1-0-063w1-16w-%c2%b1100ppm-c-pad-smd-t-r/","",
  f"{R}/2024/07/C105875.pdf"],
 ["R1,R2",2,"5.1k","0603",
  "WR06X5101FTL Walsin 5.1k 1% 0603","R179052","WR06X5101FTL","0.08","In Stock","Not published",
  "exact","https://robu.in/product/wr06x5101ftl-walsin-100mw-thick-film-resistors-75v-%c2%b1100ppm-%e2%84%83-%c2%b11-5-1k%cf%89-0603-chip-resistor-surface-mount-rohs/","",
  f"{R}/2024/11/C113390.pdf"],
 ["R4,R5,R6,R7",4,"10k","0603",
  "RC0603JR-0710KP Yageo 10k 5% 0603","R232165","RC0603JR-0710KP","0.83","In Stock","Not published",
  "exact","https://robu.in/product/rc0603jr-0710kp-yageo-100mw-thick-film-resistors-%c2%b15-%c2%b1150ppm-%e2%84%83-10k%cf%89-0603-chip-resistor-surface-mount-rohs/",
  "FRC0603F1002TS R204890 is OOS; this is in stock.",
  f"{R}/2025/07/2506161050_YAGEO-RC0402FR-07220RP_C7038454.pdf"],
 ["U1",1,"STM32F411CEU6","UFQFPN-48",
  "STM32F411CEU6TR ST UFQFPN-48","R233574","STM32F411CEU6TR","850.00","In Stock","Not published",
  "exact","https://robu.in/product/stm32f411ceu6tr-stmicroelectronics-arm-m4-100mhz-ufqfpn-487x7-microcontrollers-mcu-mpu-soc-rohs/",
  "Only the TR (tape/reel) variant is in stock. Tray part STM32F411CEU6 R233665 is OOS.",
  f"{R}/2025/06/C2054095.pdf"],
 ["U3",1,"TLV75533PDBVR","SOT-23-5",
  "TLV75533PDBVR TI 3.3V 500mA LDO SOT-23-5","R242009","TLV75533PDBVR","25.00","In Stock","Not published",
  "exact","https://robu.in/product/tlv75533pdbvr-texas-instruments-500ma-52db1khz-fixed-3-3v-positive-electrode-5-5v-sot-23-5-voltage-regulators-linear-low-drop-out-ldo-regulators-rohs/","",
  f"{R}/2025/08/C404027.pdf"],
 ["U4",1,"USBLC6-2SC6","SOT-23-6",
  "USBLC6-2SC6-MS MSKSEMI USB ESD protection SOT-23-6","R243041","USBLC6-2SC6-MS","11.00","In Stock","Not published",
  "alt-manufacturer","https://robu.in/product/usblc6-2sc6-ms-msksemi-4-5a-15v-150w-6v-5v-sot-23-6-esd-and-surge-protection-tvs-esd-rohs/",
  "Exact part number in stock from MSKSEMI. ST original USBLC6-2SC6 R191248 is Out of Stock.",
  f"{R}/2025/08/C3029034.pdf"],
 ["U6",1,"BMI270","LGA-14 (XDCR_BMI270)",
  "BOSCH BMI270 6-Axis IMU Motion Sensor LGA-14","R155006","BMI270","599.00","Out of Stock","Not published",
  "exact-but-oos","https://robu.in/product/bosch-bmi270motion-sensoric22-g-4-g-8-g-16-g/",
  "Exact Bosch BMI270 listed but currently Out of Stock; no ETA published. Only bare BMI270 on Robu. Sensor breakout modules exist but are not the IC.",
  "https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bmi270-ds000.pdf"],
]

header = ["Reference","Qty","Value","Package","Robu_Product","Robu_SKU","MPN",
          "Unit_Price_INR","Availability","Lead_Time","Match","Robu_URL","Notes","Datasheet"]

with open(f"{OUT}/bom-robu.csv","w",newline="") as f:
    w = csv.writer(f)
    w.writerow(header)
    w.writerows(rows)

nf = [r for r in rows if r[10] in ("nearest-not-exact","not-found","no-component")]
with open(f"{OUT}/not-found-exact.csv","w",newline="") as f:
    w = csv.writer(f)
    w.writerow(["Reference","Qty","Value","Package","Why_not_exact","Nearest_on_Robu","Nearest_URL","Datasheet"])
    w.writerows([[r[0],r[1],r[2],r[3],r[12],r[4],r[11],r[13]] for r in nf])

cost = sum(r[1] * float(r[7]) for r in rows if r[8] == "In Stock")
print("lines:", len(rows))
print("in-stock (price*qty) subtotal: Rs %.2f" % cost)
print("not-found/no-exact/no-component:", len(nf),
      "| rows-with-datasheet:", sum(1 for r in rows if r[13]))
