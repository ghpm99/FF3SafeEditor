from io import BufferedReader


class SaveStruct:

    dig_verify = b''
    dump_random = b''
    name = b''
    level = b''
    exp = b''
    strength = b''

    def __init__(self, file: BufferedReader):
        self.dig_verify = file.read(16)
        self.dump_random = file.read(73)
        self.name = file.read(6)

    def print_name(self):
        print(self.name)


file = open("save/SAVE_3.BIN", "rb")
# print(file.read())
content = file.read()
data = content.split(
    b'\x63\x64\x31\x30\x30\x30\x00\x45\x55\x52\x65\x4b\x61\x00\x00\x00'
)
for save_byte in data:
    print(len(save_byte))  # 15152 bytes
    print(save_byte[:128])
# save = SaveStruct(file)
# save.print_name()

file.close()

# data[0xb22b] = 116
# print(data[0xb229:111].hex())

# file_write = open("save/edited/SAVE.BIN", "wb")
# file_write.write(data)
# file_write.close()
