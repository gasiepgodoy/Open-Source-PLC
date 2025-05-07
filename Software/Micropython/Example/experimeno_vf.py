import utime
from machine import SPI, Pin
from umqtt.simple import MQTTClient
from jaguar import DigitalIO, PWMOutput, Encoder, Ethernet

# Configuração do hardware
pwm_motor = PWMOutput(pin=6)  # Controle de velocidade do motor

# Configuração da comunicação Ethernet
spi = SPI(0,2_000_000, mosi=Pin(19),miso=Pin(16),sck=Pin(18))
eth = Ethernet(spi, cs_pin=17)
eth.connect()

# Configuração do PID
class PIDController:
    def __init__(self, setpoint, kp, ki, kd, integral_max):
        self.setpoint = setpoint
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.integral_max = integral_max
        self.prev_error = 0
        self.integral = 0

    def compute(self, feedback_value):
        error = self.setpoint - feedback_value
        self.integral += error
        # Limita a parte integral para evitar integral windup
        self.integral = min(max(self.integral, -self.integral_max), self.integral_max)
        derivative = error - self.prev_error
        output = self.kp * error + self.ki * self.integral + self.kd * derivative
        self.prev_error = error
        return output

RPMdesejado = 750
KP = 0.035 
KI = 0.01 
KD = 0.05
INTEGRAL_MAX = 10
duty_cycle = 25

# Criação do objeto PIDController
pid = PIDController(RPMdesejado, KP, KI, KD, INTEGRAL_MAX)

# Configuração do Encoder
tachometerPin = Pin(28, Pin.IN, Pin.PULL_DOWN)
counter = 0

# Função de interrupção do Encoder
def tachometer(pin):
    global counter
    counter += 1
    
tachometerPin.irq(trigger = Pin.IRQ_RISING,
                  handler = tachometer)

# Função de callback para receber mensagens MQTT
def on_message(topic, msg):
    global RPMdesejado, KP, KD, KI, pid
    if topic == b"motor/setpoint":
        print("setpoint atualizado", int(msg))
        RPMdesejado = int(msg)
        pid = PIDController(RPMdesejado, KP, KI, KD, INTEGRAL_MAX)
    elif topic == b"motor/kp":
        KP = float(msg)
        pid = PIDController(RPMdesejado, KP, KI, KD, INTEGRAL_MAX)
    elif topic == b"motor/ki":
        KI = float(msg)
        pid = PIDController(RPMdesejado, KP, KI, KD, INTEGRAL_MAX)
    elif topic == b"motor/kd":
        KD = float(msg)
        pid = PIDController(RPMdesejado, KP, KI, KD, INTEGRAL_MAX)


# ===== COMUNICAÇÃO MQTT =====
BROKER = '192.168.0.22'

def conectar_mqtt():
    cliente = MQTTClient('jaguar', BROKER, port=1883, keepalive=60)
    cliente.set_callback(on_message)
    res = cliente.connect()
    print("Resultado da conexão:", res)  # geralmente 0 = sucesso
    utime.sleep(0.5)
    return cliente

mqtt_client = conectar_mqtt()
utime.sleep(1)
mqtt_client.subscribe(b'motor/setpoint')
mqtt_client.publish("motor/setpoint", str(RPMdesejado))
mqtt_client.subscribe(b'motor/kp')
mqtt_client.publish("motor/kp", str(KP))
mqtt_client.subscribe(b'motor/kd')
mqtt_client.publish("motor/kd", str(KD))
mqtt_client.subscribe(b'motor/ki')
mqtt_client.publish("motor/ki", str(KI))

last_check = utime.ticks_ms()

# Loop principal
while True:
    
    if utime.ticks_diff(utime.ticks_ms(), last_check) > 200:
        try:
            mqtt_client.check_msg()
        except Exception as e:
            print("MQTT erro:", e)
        last_check = utime.ticks_ms()
    
    # Leitura do encoder para cálculo de RPM
    SAMPLING_TIME = 0.25 # in seconds 
    rpm = 0
    i = 0
    while i < 3:
        utime.sleep(SAMPLING_TIME)
        revolutions_per_sampling_time = counter/600
        revolutions_per_sec = revolutions_per_sampling_time/SAMPLING_TIME
        revolutions_per_minute = round(revolutions_per_sec * 60, 0)
        rpm = rpm + revolutions_per_minute
        # reset the counter to zero 
        counter = 0
        i = i + 1

    RPM = rpm/3
    print("RPM: ", int(RPM))
    
# Cálculo do sinal de controle pelo PID
    pid_output = pid.compute(RPM)

# Constante para limitar o aumento gradual
    MAX_INCREMENT = 20
    MAX_DECREMENT = 20

# Cálculo da Nova Compensação
    newduty_cycle = pid_output + duty_cycle

# Limitação do Ciclo de Trabalho para evitar aumento repentino
    if newduty_cycle - duty_cycle > MAX_INCREMENT:
        newduty_cycle = min(duty_cycle + MAX_INCREMENT, 100)
    elif newduty_cycle - duty_cycle < -MAX_DECREMENT:
        newduty_cycle = max(duty_cycle - MAX_DECREMENT, 0)

# Aplicação do Ciclo de Trabalho ao Motor
    pwm_motor.set_duty_cycle(int(newduty_cycle))

# Atualização do ciclo de trabalho atual
    duty_cycle = newduty_cycle
    print("duty_cycle: ", duty_cycle)
    
# Publicação dos dados via MQTT
    mqtt_client.publish("motor/rpm", str(RPM))
    mqtt_client.publish("motor/desejado", str(RPMdesejado))
    mqtt_client.publish("motor/duty", str(duty_cycle))
    