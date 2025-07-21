# MicroPython Firmware Overview

This section details the developments made using MicroPython on the Open-Source-PLC platform. MicroPython was chosen for its ease of use, flexibility, and compatibility with embedded systems, enabling fast prototyping and direct interaction with hardware.

## Purpose and Justification

The use of MicroPython in this project aimed to:

- Enable a high-level programming alternative to IEC 61131-3, reducing the entry barrier for new users.
- Allow rapid testing and customization of control strategies without complex toolchains.
- Leverage open tools and existing MicroPython support on the RP2040 (Raspberry Pi Pico).

## Firmware Architecture

The firmware follows a modular architecture centered around a custom-developed library named `jaguar`, which abstracts access to the hardware resources of the automation platform.

### Key Modules

- **Digital I/O**: Easy mapping and handling of digital inputs and outputs.
- **Analog I/O**: Support for reading analog sensors and controlling outputs.
- **PWM Output**: Allows precise control of actuators such as motors.
- **Encoder**: Interface for reading motor or shaft position using quadrature encoders.
- **Ethernet (W5500)**: Enables communication with external systems via MQTT over Ethernet.

## Jaguar Library

The core of the firmware is the `jaguar` library, created specifically to make hardware programming more intuitive and abstracted. It provides a set of classes that simplify the use of GPIO, ADC, PWM, encoders, and network connectivity.

### Main Features

- Simple pin mapping system aligned with the platform’s labeling.
- Built-in compatibility with the RP2040 hardware features.
- MQTT-ready interface via W5500 Ethernet chip.
- Easy integration with dashboards and external monitoring tools (e.g., Node-RED).

## MQTT and Real-Time Communication

The firmware uses the `umqtt.simple` library to implement publish/subscribe communication via MQTT. This allows real-time data exchange between the controller and a remote dashboard or data logger.

### Applications

- Remote monitoring of motor speed, encoder position, and control parameters.
- Real-time update of PID parameters from a web interface.
- Logging of system behavior under varying load conditions.

## PID Control Use Case

A complete PID loop was implemented to control a DC motor’s speed using feedback from a quadrature encoder. The system supports real-time adjustment of PID parameters via MQTT and maintains target RPM despite manual load variations.


## Development Environment

- **Firmware Language**: MicroPython (latest stable)
- **IDE**: Thonny IDE
- **Board**: Raspberry Pi Pico
- **Network**: W5500 Ethernet via SPI
- **External Tool**: Node-RED (for visualization)

## Conclusion

The MicroPython firmware, paired with the custom `jaguar` library, enabled the Open-Source-PLC to serve not only as a traditional automation controller but also as a flexible experimentation platform. Its modular design, real-time communication capabilities, and ease of programming make it an ideal solution for educational, experimental, and IIoT applications.
