# Open-Source-PLC

Design of a low-cost and highly versatile open-source programmable logic controller for industrial Internet of Things applications.
All development was carried out using KiCad and the controller follows the following specifications:

Power: Powered via direct current signal and with a voltage of 24V to facilitate integration into industrial panels.

Inputs: 12 digital inputs at 24v and opto-coupled, 4 programmable analog inputs via ADC that operate from -10 to 10V, and 3 dedicated encoder inputs.

Outputs: 8 digital relay outputs and 4 PWM outputs.

Connectivity: Communication via RS-232, RS-485, Ethernet TCP/IP, and support for IoT standards such as MQTT, and Modbus TCP/IP.

CPU: RP2040 - Raspberry Pi Pico

The developed controller can be programmed using the languages stipulated in the IEC 61131-3 standard through OpenPLC (https://autonomylogic.com/) under the name Project Jaguar.
