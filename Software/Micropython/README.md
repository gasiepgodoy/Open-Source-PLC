# Open-Source-PLC - Micropython 

The complexity inherent in these configurations can represent a barrier for users seeking to quickly integrate the platform into industrial systems. The configuration process requires the user to directly manipulate the microcontroller pins, establish communication via SPI for serialized access to I/Os, and deal with different communication interfaces, such as Ethernet, RS-232, and RS-485. These steps make the development more error-prone and increase the time required for implementation.

In view of this challenge, a MicroPython library was developed that abstracts these complexities and provides an intuitive interface for the end user.

The implementation of this library will allow the selection of inputs and outputs to be performed through logical identifications, eliminating the need for knowledge about the internal structure of the hardware. This approach significantly reduces the development and implementation time of industrial applications, in addition to increasing the reliability of the system, minimizing errors resulting from manual configurations.

The developed library was named Jaguar as well as the hardware