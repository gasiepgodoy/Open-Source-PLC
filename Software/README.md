# 🧠 Software Implementation Overview – MicroPython and OpenPLC

This document provides a general overview of the software implementations used in the Open-Source-PLC platform. The system was designed to support two complementary development environments:

- **OpenPLC**, an open-source platform that supports IEC 61131-3 programming languages (Ladder, Structured Text, etc.)
- **MicroPython**, a high-level scripting language adapted for microcontrollers, allowing flexible and modular control logic

The goal was to enable the platform to support both industry-standard and educational/research-friendly environments.

---

## 🔷 OpenPLC – IEC 61131-3-Based Programming

OpenPLC was used to validate the compatibility of the hardware with traditional industrial programming standards.

### ✅ Key Features Implemented:
- Integration with **OpenPLC Runtime** on the Raspberry Pi Pico 
- Development of a **color-sorting station** controlled entirely in **Ladder Diagram**
- Use of digital inputs for sensors and digital outputs for actuators
- Real-time monitoring via **MQTT and Node-RED dashboards**

### 🧩 Custom Function Blocks:
To enhance functionality and simplify reuse, custom blocks were created:
- **MQTT Interface Logic:** State variables exposed for integration with Node-RED

### 🧪 Application Example:
- The system uses a color sensor connected to a digital input
- Based on the detected color, an actuator is triggered to sort parts
- Status and results are published to a Node-RED dashboard via MQTT

More technical details will be available in [`OpenPLC/`](../Software/OpenPLC/).

---

## 🟢 MicroPython – Modular High-Level Control

MicroPython was used to develop a fully custom control application and validate the hardware using real-time scripting and communication.

### ✅ Key Features Developed:
- **Modular library** to abstract all I/O operations (Digital I/O, PWM, Analog, Encoder, Ethernet)
- Implementation of a **PID control loop** for DC motor speed using encoder feedback
- Real-time variable update and remote control via **MQTT**
- Integration with **Node-RED** for visualization and manual control

### 📦 Library Modules:
The custom MicroPython library includes:
- `DigitalIO` – digital input/output abstraction
- `PWMOutput` – PWM signal control with frequency and duty cycle options
- `AnalogInput` – basic analog reading with scaling support
- `Encoder` – quadrature encoder interface with real-time position/velocity
- `Ethernet` – W5500 communication interface with DHCP or static IP setup

### 🧪 Application Example:
- A DC motor is controlled via PWM
- An encoder provides speed feedback
- A PID algorithm adjusts the PWM to maintain desired RPM
- MQTT is used to receive setpoints and send actual speed to Node-RED

More technical details will be available in [`Micropython/`](../Software/Micropython/).

---

## 🔄 Coexistence of OpenPLC and MicroPython

Although OpenPLC and MicroPython are used in different contexts, they share the same hardware infrastructure. The platform supports:

- Independent flashing of either OpenPLC Runtime or MicroPython firmware
- Shared access to GPIOs, communication buses, and external interfaces
- Common interfaces with MQTT and Node-RED, allowing seamless monitoring regardless of backend

This dual-approach design enables the platform to be used in:
- **Industrial control scenarios** with standard IEC languages
- **Research and prototyping** using rapid development with MicroPython

