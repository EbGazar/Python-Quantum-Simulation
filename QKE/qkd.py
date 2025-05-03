from interface import Qubit
from simulator import QuantumDevice, SingleQubitSimulator

def qrng(device: QuantumDevice) -> bool:
    with device.using_qubit() as q:
        q.h()
        return q.measure()
    

def prepare_classical_message(bit: bool, q:Qubit) -> None:
    if bit:
        q.x()

def eve_measure(q: Qubit) -> bool:
    return q.measure()

def send_classical_bit(device: QuantumDevice, bit: bool) -> None:
    with device.using_qubit() as q:
        prepare_classical_message(bit, q)
        result = eve_measure(q)
        q.reset()
    assert result == bit

if __name__ == "__main__":
    qrng_simulator = SingleQubitSimulator()
    key_bit = int(qrng(qrng_simulator))
    qkd_simulator = SingleQubitSimulator()

    with qkd_simulator.using_qubit() as q:
        prepare_classical_message(key_bit, q)
        print(f"You Prepared the classical key bit: {key_bit}")
        eve_measurent = int(eve_measure(q))
        print(f"Eve measured the classical key bit: {eve_measurent}")
