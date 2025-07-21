# 🧩 Hardware Details – Open-Source-PLC

This section provides an overview of the hardware developed for the Open-Source-PLC platform. The system was designed to be open, modular, and compatible with both industrial devices and educational environments. All design files, schematics, and PCB layouts are included in the repository for replication or adaptation.

---

## 1. 🧱 Architecture Overview

The hardware architecture was based on the following core principles:

- **Modularity:** Independent functional blocks (I/O, communication, power, etc.)
- **Openness:** All design files (schematics, layouts, BOM) are fully available
- **Compatibility:** Designed for use with sensors, actuators, and protocols commonly found in industrial systems
- **Accessibility:** Easily programmable using MicroPython or OpenPLC

---

## 2. 🔧 Main Components

| Component                  | Description                                                                 |
|---------------------------|------------------------------------------------------------------------------|
| **Microcontroller**        | Raspberry Pi Pico (RP2040)                                                  |
| **Ethernet Interface**     | W5500 chip with SPI interface and RJ45 connector                            |
| **Digital Inputs**         | Up to 12 channels, opto-isolated                                            |
| **Digital Outputs (PWM)**  | 2 PWM-capable outputs with transistor drivers                               |
| **Analog Inputs**          | 4 channels, -10 – 10 V (external sensors, potentiometers)                   |
| **Encoder Input**          | Incremental encoder interface (A/B channels with interrupt support)         |
| **Power Supply**           | 24 V DC input with onboard voltage regulation                               |
| **Protection**             | ESD protection, buffering, opto-isolators, flyback diodes for outputs       |
| **Optional**               | RS-232 / RS-485 transceivers for future protocol expansions                 |

---

## 3. 🧾 PCB and Schematics

All design files are located in the [`hardware`](../hardware) folder. This includes:

- Schematics in PDF and source format (KiCad)
- PCB layout and 3D view files
- Bill of Materials (BOM)
- Gerber files ready for fabrication


---

## 4. 🧰 Assembly and Integration

The hardware is designed to be easily assembled using through-hole and SMD components. Key integration considerations:

- Headers and terminal blocks follow a modular layout for easier cabling
- The platform includes pin labeling and silkscreen guidance
- Power input protection and reverse polarity safeguards included
