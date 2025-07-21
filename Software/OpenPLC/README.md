# OpenPLC Integration Overview

This section documents the adaptations, extensions, and validation of the OpenPLC framework on the Open-Source-PLC platform. OpenPLC was selected due to its compliance with the IEC 61131-3 standard, open-source nature, and flexibility for embedded applications.

## Purpose and Context

The integration of OpenPLC into the hardware platform aimed to:

- Validate the compatibility of the custom hardware with standard industrial automation software.
- Demonstrate the use of IEC 61131-3 languages (LD, ST, FBD, etc.) on open hardware.
- Provide an alternative path for users familiar with PLC programming.

## Hardware Compatibility

The hardware was adapted to be recognized by the OpenPLC runtime. This included:

- Setting up correct GPIO mapping on the Raspberry Pi Pico (RP2040).
- Developing a compatible hardware layer using the OpenPLC Embedded runtime.
- Ensuring electrical interface compatibility with standard sensors and actuators (24V DC logic, relay modules, etc.).

## Firmware Customizations

Several adaptations were made to the OpenPLC firmware to support the custom hardware:

- **Pin Mapping Layer**: A dedicated mapping file was created to align logical I/Os in the OpenPLC Editor with physical pins on the board.
- **Startup Sequence**: Modified initialization code to work with the board’s peripherals and power-on behavior.
- **I/O Expansion Support**: Extensions to support multiplexed or serialized I/Os.

## Function Block Development

Custom function blocks were developed and tested to enhance OpenPLC’s capabilities:

All blocks were created using the **Structured Text (ST)** language, and are included in the repository as `.st` or `.xml` files for reuse.

## Example Application: Color Sorting Station

A complete application was developed using OpenPLC to automate a color-based separation process.

### Overview

- A TCS230 color sensor detects object color.
- OpenPLC reads the sensor and triggers actuators (e.g., air jets or conveyors) based on the detected color.
- The system is fully programmable and customizable using the OpenPLC Editor.

### Runtime Details

- Program written in OpenPLC Editor (FBD + ST).
- Downloaded to board running OpenPLC Embedded runtime.
- I/Os monitored in real-time via the OpenPLC Web Interface.

## Development Tools

- **Editor**: OpenPLC Editor (IEC 61131-3 compliant)
- **Runtime**: OpenPLC for RP2040 Embedded (customized)

## Conclusion

The successful integration of OpenPLC on the Open-Source-PLC platform demonstrates its suitability for educational and industrial control systems. It enables users to program the controller using standardized IEC languages while benefiting from the openness and flexibility of custom hardware.

This hybrid approach allows for experimentation, interoperability, and easier learning for students and professionals alike.
