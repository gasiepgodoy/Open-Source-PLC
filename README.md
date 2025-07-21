# Open-Source-PLC

**Open-Source-PLC** is an open automation platform developed as part of a master's degree project, focused on accessibility, customization, and compatibility with both industrial and educational applications. The goal is to democratize access to industrial automation through a fully open, documented hardware and software solution based on widely adopted technologies.

This repository centralizes all files, documentation, schematics, and source code required to understand, replicate, and extend the system—ensuring long-term continuity and community collaboration.

---

## 🎯 Project Purpose

For an open-source platform to be truly applicable in industrial settings, it must go beyond basic functionality and meet criteria for engineering quality, physical robustness, and scalability. Therefore, the following strategic requirements were defined:

- Full Openness: The project provides complete access to all hardware files (schematics, PCB layout, BOM) and software libraries with public documentation, enabling full transparency, replication, and community-driven evolution.
- Flexibility and Customization: The modular hardware design, combined with support for multiple languages and protocols, allows the platform to be adapted to a variety of processes, from test benches to full-scale industrial lines.
- Industrial Compatibility: The adoption of industrial voltage levels, standard connectors, and protocols such as Modbus and MQTT ensures direct adherence to realworld industrial operating conditions.
- Low Learning Curve: The use of familiar environments (OpenPLC Editor, Thonny IDE) and the development of simplified MicroPython libraries make the platform accessible even to teams with limited experience in advanced programming.
- Experimental Feasibility and Scalability: The architecture has been validated in two distinct setups (PID control and part-sorting station), demonstrating its ability to operate reliably in real applications while remaining scalable for future expansions. 

This combination of elements allows the solution to serve as a bridge between the maker/open-source ecosystem and the technical demands of industry, fostering an environment of continuous innovation, operational cost reduction, and greater technological freedom.

---

## ⚙️ Functional Requirements

- Support for both MicroPython and IEC 61131-3 (via OpenPLC)
- Digital and analog input/output, PWM support
- Ethernet communication (via W5500), with MQTT protocol
- Encoder interface and compatibility with industrial sensors
- Compatibility with standard industrial protocols and connectors
- Modular hardware design with plug-and-play expandability

---

## 🧩 Hardware Summary

The architecture is organized into independent functional blocks, with modular I/O expansion via SPI serialization, allowing the number of inputs and outputs to be tailored to the specific application. The base version of the platform includes:

- **Main controller:** Raspberry Pi Pico (RP2040)
- **Expansion:** Up to 12 digital inputs, 8 digital outputs, 1 dedicated PWM output, 4 analog inputs, and 1 encoder input
- **Networking:** W5500 Ethernet chip with RJ45 connector, SPI communication
- **Electrical Interface:** Level shifters, opto-isolated inputs, and industrial-grade buffers
- **Additional Support:** Optional RS-232/RS-485 communication bus

All schematics and PCB layout files are available in the [`/hardware`](./hardware) folder.

---

## 🖥️ Software Summary

The platform offers native support for two complementary paradigms:

### MicroPython
which supports high-level scripting for control, communication, and integration with platforms such as Node-RED, databases, and dashboards.

### OpenPLC
which enables the development of control logic using IEC 61131-3 standardized languages such as Ladder and Structured Text, with an accessible development environment

More details are available in the [`/Software`](./Software) folder.

---

## 🔬 Validation and Testing

Two practical experiments were conducted to validate the system's functionality:

1. **DC Motor PID Control (MicroPython):**
   - Speed control using encoder feedback
   - MQTT communication with Node-RED
   - Validation through manual shaft load variation

2. **Color Sorting Station (OpenPLC):**
   - Color detection with automated part separation
   - Controlled via ladder logic
   - Monitored through MQTT and Node-RED dashboards
