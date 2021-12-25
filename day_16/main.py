import abc
import math
import uuid
from dataclasses import dataclass
from typing import List


class Packet(abc.ABC):
    def __init__(self, bits: str, version: int, type_id: int) -> None:
        self.uid = uuid.uuid4()
        self.bits = bits
        self.version = version
        self.type_id = type_id

    @abc.abstractmethod
    def get_value(self) -> int:
        ...

class LiteralPacket(Packet):
    def __init__(self, bits: str, version: int, type_id: int, number: int) -> None:
        if type_id != 4: raise ValueError('Literals must have a type id of 4.')
        super().__init__(bits, version, type_id)
        self.number = number

    def get_value(self) -> int:
        return self.number

class OperatorPacket(Packet):
    def __init__(self, bits: str, version: int, type_id: int, length_type_id: int, length_type_value: int, subpackets: List[Packet]) -> None:
        if type_id == 4: raise ValueError('Operators must not have type id of 4.')
        super().__init__(bits, version, type_id)
        self.length_type_id = length_type_id
        self.length_type_value = length_type_value
        self.subpackets = subpackets

    def __repr__(self) -> str:
        ids = [str(s.uid)[:8] for s in self.subpackets]
        return f'{{uid: {str(self.uid)[:8]}, version: {self.version}, type_id: {self.type_id}, length_type_id: {self.length_type_id}, length_type_value: {self.length_type_value}, subpackets: {ids}}}'

    def add_subpacket(self, p: Packet) -> None:
        if not isinstance(p, Packet): raise ValueError('A packet was not provided.')
        self.subpackets.append(p)

    def get_subpackets_bits(self) -> int:
        bits = 0
        for p in self.subpackets:
            bits += len(p.bits)
            if isinstance(p, OperatorPacket): bits += p.get_subpackets_bits()
        return bits

    def has_all_packets(self) -> bool:
        if self.length_type_id == 0 and self.get_subpackets_bits() == self.length_type_value: return True
        if self.length_type_id == 1 and len(self.subpackets) == self.length_type_value: return True
        return False

    def get_value(self) -> int:
        values = [p.get_value() for p in self.subpackets]
        if self.type_id == 0: return sum(values)
        if self.type_id == 1: return math.prod(values)
        if self.type_id == 2: return min(values)
        if self.type_id == 3: return max(values)
        if self.type_id == 5: return 1 if values[0] > values[1] else 0
        if self.type_id == 6: return 1 if values[0] < values[1] else 0
        if self.type_id == 7: return 1 if values[0] == values[1] else 0

def hex_to_binary(char: str) -> str:
    if len(char) != 1: raise ValueError('Argument must be 1 character')
    return bin(int(char, 16))[2:].zfill(4)


def part_one():
    with open('input.txt') as f:
        data = f.readline().strip()

    # Convert hex string to binary string
    msg = ''.join(hex_to_binary(x) for x in data)

    # Initialize values
    version_sum, superpackets, cursor = 0, [], 0

    # Get version and type id from binary string
    version, type_id = int(msg[cursor:cursor+3], 2), int(msg[cursor+3:cursor+6], 2)
    version_sum += version
    cursor += 6
    
    # If first packet is literal, then version sum is just that packet's version
    if type_id == 4:
        print(f'Version sum: {version}')
        return
    
    # Get length type id, length type value, and add to superpackets list as outter wrapper
    # Length type id how many bits are in length type value and whether it's # of packets or total bits
    # 0 -> 15 bits -> total bits vs. 1 -> 11 bits -> # of subpackets
    length_type_id = int(msg[cursor], 2)
    cursor += 1
    value_length = 15 if length_type_id == 0 else 11
    length_type_value = int(msg[cursor:cursor+value_length], 2)
    cursor += value_length
    superpackets.append(OperatorPacket(msg[:cursor], version, type_id, length_type_id, length_type_value, []))
    
    # While there is a packet that does not have all children parsed
    while superpackets:
        while True:
            if superpackets and superpackets[-1].has_all_packets():
                superpackets.pop()
            else:
                break

        if not superpackets:
            break

        # Get starting point of new packet
        initial_cursor = cursor

        # Get latest superpacket and current packet's version, type id
        curr = superpackets[-1]
        version, type_id = int(msg[cursor:cursor+3], 2), int(msg[cursor+3:cursor+6], 2)
        version_sum += version
        cursor += 6

        # If literal, simply parse it and add it as child to parent
        if type_id == 4:
            num = ''

            while True:
                num += msg[cursor+1:cursor+5]
                cursor += 5
                if msg[cursor - 5] == '0': break
            new_packet = LiteralPacket(msg[initial_cursor:cursor], version, type_id, int(num, 2))
            curr.add_subpacket(new_packet)
            continue

        # Otherwise, parse as an operator (which is complicated)
        # Get length type id and length type value
        length_type_id = int(msg[cursor], 2)
        cursor += 1
        value_length = 15 if length_type_id == 0 else 11
        length_type_value = int(msg[cursor:cursor+value_length], 2)
        cursor += value_length
        new_packet = OperatorPacket(msg[initial_cursor:cursor], version, type_id, length_type_id, length_type_value, [])
        curr.add_subpacket(new_packet)

        # Append to superpackets
        superpackets.append(new_packet)

    print(f'Version sum: {version_sum}')


def part_two():
    with open('input.txt') as f:
        data = f.readline().strip()

    # Convert hex string to binary string
    msg = ''.join(hex_to_binary(x) for x in data)

    # Initialize values
    version_sum, superpackets, cursor = 0, [], 0

    # Get version and type id from binary string
    version, type_id = int(msg[cursor:cursor+3], 2), int(msg[cursor+3:cursor+6], 2)
    version_sum += version
    cursor += 6
    
    # If first packet is literal, then version sum is just that packet's version
    if type_id == 4:
        num = ''
        while True:
            num += msg[cursor+1:cursor+5]
            cursor += 5
            if msg[cursor - 5] == '0': break
        print(f'Value of packet: {int(num, 2)}')
        return
    
    # Get length type id, length type value, and add to superpackets list as outter wrapper
    # Length type id how many bits are in length type value and whether it's # of packets or total bits
    # 0 -> 15 bits -> total bits vs. 1 -> 11 bits -> # of subpackets
    length_type_id = int(msg[cursor], 2)
    cursor += 1
    value_length = 15 if length_type_id == 0 else 11
    length_type_value = int(msg[cursor:cursor+value_length], 2)
    cursor += value_length
    root_packet = OperatorPacket(msg[:cursor], version, type_id, length_type_id, length_type_value, [])
    superpackets.append(root_packet)
    
    # While there is a packet that does not have all children parsed
    while superpackets:
        while True:
            if superpackets and superpackets[-1].has_all_packets():
                superpackets.pop()
            else:
                break

        if not superpackets:
            break

        # Get starting point of new packet
        initial_cursor = cursor

        # Get latest superpacket and current packet's version, type id
        curr = superpackets[-1]
        version, type_id = int(msg[cursor:cursor+3], 2), int(msg[cursor+3:cursor+6], 2)
        version_sum += version
        cursor += 6

        # If literal, simply parse it and add it as child to parent
        if type_id == 4:
            num = ''

            while True:
                num += msg[cursor+1:cursor+5]
                cursor += 5
                if msg[cursor - 5] == '0': break
            new_packet = LiteralPacket(msg[initial_cursor:cursor], version, type_id, int(num, 2))
            curr.add_subpacket(new_packet)
            continue

        # Otherwise, parse as an operator (which is complicated)
        # Get length type id and length type value
        length_type_id = int(msg[cursor], 2)
        cursor += 1
        value_length = 15 if length_type_id == 0 else 11
        length_type_value = int(msg[cursor:cursor+value_length], 2)
        cursor += value_length
        new_packet = OperatorPacket(msg[initial_cursor:cursor], version, type_id, length_type_id, length_type_value, [])
        curr.add_subpacket(new_packet)

        # Append to superpackets
        superpackets.append(new_packet)

    print(f'Values of packet: {root_packet.get_value()}')


if __name__ == '__main__':
    part_one()
    part_two()
