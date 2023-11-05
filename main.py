from io import BufferedReader
import struct


class SaveStruct:

    dig_verify = b''
    dump_random = b''
    name = b''
    level: int
    exp: int
    hp: int
    current_hp: int
    strength: int
    agility: int
    vitality: int
    intellect: int
    mind: int
    attack: int
    defense: int
    magic_defense: int

    def __init__(self, file: BufferedReader):
        self.dig_verify = file.read(16)
        self.dump_random = file.read(73)
        self.name = struct.unpack("6s", file.read(6))
        file.seek(0x0083)
        self.level = struct.unpack("b", file.read(1))
        self.exp = struct.unpack("h", file.read(2))
        file.seek(0x008c)
        self.hp = struct.unpack("h", file.read(2))
        print(file.read(2))
        self.current_hp = struct.unpack("h", file.read(2))
        file.seek(0x00ac)
        self.strength = struct.unpack("b", file.read(1))
        self.agility = struct.unpack("b", file.read(1))
        self.vitality = struct.unpack("b", file.read(1))
        self.intellect = struct.unpack("b", file.read(1))
        self.mind = struct.unpack("b", file.read(1))


file = open("save/SAVE_3.BIN", "rb")
print(file.read(16))
save = SaveStruct(file)
print(save.__dict__)

file.close()

# data[0xb22b] = 116
# print(data[0xb229:111].hex())

# file_write = open("save/edited/SAVE.BIN", "wb")
# file_write.write(data)
# file_write.close()
