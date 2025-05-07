import machine
import utime
import network

class DigitalIO:
    """ Classe para manipulação de entradas e saídas digitais via SPI. """
    def __init__(self, spi_id=0, sck=10, mosi=11, miso=8, dio_cs=3, adc_cs=9, num_inputs=12, num_outputs=8):
        self.spi = machine.SPI(spi_id, baudrate=50000, polarity=0, phase=0,
                               sck=machine.Pin(sck), mosi=machine.Pin(mosi), miso=machine.Pin(miso))
        self.dio_cs = machine.Pin(cs, machine.Pin.OUT)
        self.adc_cs = machine.Pin(adc_cs, machine.Pin.OUT)
        self.num_inputs = num_inputs
        self.num_outputs = num_outputs
        self.output_state = 0  # Estado inicial das saídas (todos os bits em 0)
        self.dio_cs.value(1)
        self.adc_cs.value(1)
    
    def __getitem__(self, pin):
        """ Lê o estado de uma entrada digital. """
        if 1 <= pin <= self.num_inputs:
            self.adc_cs.value(1)  # Garante que o ADC está desativado
            self.dio_cs.value(0)
            raw_data = self.spi.read(2)  # Lê os 12 bits das entradas digitais
            self.dio_cs.value(1)
            value = (raw_data[0] << 8 | raw_data[1]) >> (16 - self.num_inputs)
            return (value >> (self.num_inputs - pin)) & 1
        raise IndexError("Entrada digital fora do alcance")
    
    def __setitem__(self, pin, state):
        """ Define o estado de uma saída digital. """
        if 1 <= pin <= self.num_outputs:
            if state:
                self.output_state |= (1 << (self.num_outputs - pin))
            else:
                self.output_state &= ~(1 << (self.num_outputs - pin))
            
            self.adc_cs.value(1)  # Garante que o ADC está desativado
            self.dio_cs.value(0)
            self.spi.write(bytearray([self.output_state]))  # Envia novo estado das saídas
            self.dio_cs.value(1)
        else:
            raise IndexError("Saída digital fora do alcance")

class AnalogInput:
    """ Classe para leitura de entradas analógicas via ADS8688IDBTR. """
      def __init__(self, spi_id=0, sck=10, mosi=11, miso=8, dio_cs=3, adc_cs=9, num_inputs=12, num_outputs=8):
        self.spi = machine.SPI(spi_id, baudrate=50000, polarity=0, phase=0,
                               sck=machine.Pin(sck), mosi=machine.Pin(mosi), miso=machine.Pin(miso))
        self.adc_cs = machine.Pin(adc_cs, machine.Pin.OUT)
        self.dio_cs = machine.Pin(dio_cs, machine.Pin.OUT)
        self.dio_cs.value(1)
        self.adc_cs.value(1)
    
    def __getitem__(self, channel):
        """ Lê o valor do ADC para um canal específico. """
        if 1 <= channel <= 8:
            self.dio_cs.value(1)
            self.adc_cs.value(0)  # Ativa o ADC
            self.spi.write(bytearray([0xC0 | (channel - 1)]))  # Envia comando de leitura
            utime.sleep_us(10)
            value = self.spi.read(2)
            self.adc_cs.value(1)  # Desativa o ADC
            return (value[0] << 8) | value[1]
        raise IndexError("Canal ADC fora do alcance")

class PWMOutput:
    """ Classe para controle de saídas PWM. """
    def __init__(self, pin, freq=1000):
        self.pwm = machine.PWM(machine.Pin(pin))
        self.pwm.freq(freq)
    
    def set_duty_cycle(self, duty):
        """ Define o duty cycle do sinal PWM. """
        self.pwm.duty_u16(int(duty * 65535 / 100))

class Encoder:
    """ Classe para leitura de encoder incremental. """
    def __init__(self, pin_a, pin_b):
        self.pin_a = machine.Pin(pin_a, machine.Pin.IN, machine.Pin.PULL_UP)
        self.pin_b = machine.Pin(pin_b, machine.Pin.IN, machine.Pin.PULL_UP)
        self.count = 0
        self.pin_a.irq(trigger=machine.Pin.IRQ_RISING, handler=self._callback)
    
    def _callback(self, pin):
        """ Callback para contar pulsos do encoder. """
        if self.pin_b.value():
            self.count += 1
        else:
            self.count -= 1
    
    def read(self):
        """ Retorna a contagem do encoder. """
        return self.count

class Ethernet:
    """ Classe para comunicação via Ethernet utilizando W5500. """
    def __init__(self, spi, cs_pin):
        self.nic = network.WIZNET5K(spi, cs=machine.Pin(cs_pin))
    
    def connect(self, timeout=10):
        """ Conecta a rede via DHCP e retorna o IP obtido. """
        self.nic.active(True)  # Ativa a interface Ethernet
        self.nic.ifconfig('dhcp')  # Solicita IP via DHCP
         # Aguarda até obter um IP válido
        for _ in range(timeout):
            ip = self.nic.ifconfig()[0]
            if ip and ip != '0.0.0.0':
                return ip
            time.sleep(1)
    
    def send(self, data):
        """ Envia dados pela rede Ethernet. """
        self.nic.send(data)
    
    def receive(self):
        """ Recebe dados da rede Ethernet. """
        return self.nic.recv(1024)

class RS232:
    """ Classe para comunicação via RS-232. """
    def __init__(self, uart_num=1, baudrate=9600, tx=4, rx=5):
        self.uart = machine.UART(uart_num, baudrate=baudrate, tx=machine.Pin(tx), rx=machine.Pin(rx))
    
    def send(self, data):
        """ Envia dados via RS-232. """
        self.uart.write(data)
    
    def receive(self):
        """ Recebe dados via RS-232. """
        return self.uart.read()

class RS485(RS232):
    """ Classe para comunicação RS-485, herdando de RS-232 e adicionando controle de transmissão. """
    def __init__(self, uart_num=1, baudrate=9600, tx=4, rx=5, de_re=6):
        super().__init__(uart_num, baudrate, tx, rx)
        self.de_re = machine.Pin(de_re, machine.Pin.OUT)
    
    def send(self, data):
        """ Envia dados via RS-485, ativando o transmissor. """
        self.de_re.value(1)
        utime.sleep_ms(1)
        self.uart.write(data)
        utime.sleep_ms(1)
        self.de_re.value(0)
    
    def receive(self):
        """ Recebe dados via RS-485. """
        return self.uart.read()
