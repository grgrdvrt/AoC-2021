input = open("16_input").read()

#value
# input = "D2FE28"
# operator
# input = "38006F45291200"
#operator2
# input = "EE00D40C823060"

def pad(data, pad, length):
    while len(data) < length:
        data = pad + data
    return data

data = "".join([pad(bin(int(c, 16))[2:], "0", 4) for c in  input.strip()])
# print(data)

def readPacket(packet):
    version, typeId = int(packet[:3], 2), int(packet[3:6], 2)
    # print("packet", len(packet), packet)
    # print("version", version, "typeId", typeId)
    if typeId == 4:
        data = packet[6:]
        groups = []
        while data[0] == "1":
            groups.append(data[1:5])
            data = data[5:]
        groups.append(data[1:5])
        value = int("".join(groups), 2)
        # print("value", value)
        return (version, typeId, value, data[5:])
    else:
        lengthTypeId = packet[6]
        # print("lengthTypeId", lengthTypeId)
        if lengthTypeId == "0":
            totalLength = int(packet[7:22], 2)
            # print("totalLength", totalLength)
            nextData = packet[22:22+totalLength]
            # print("next", len(nextData), len(packet[22:]), packet[22:])
            packets = []
            while nextData:
                subPacket = readPacket(nextData)
                # print("sub", subPacket)
                packets.append(subPacket)
                nextData = subPacket[3] if any([c == "1" for c in subPacket[3]]) else ""
            nextData = packet[22+totalLength:]
        else:
            subCount = int(packet[7:18], 2)
            # print("subCount", subCount)
            packets = []
            nextData = packet[18:]
            while len(packets) < subCount:
                subPacket = readPacket(nextData)
                packets.append(subPacket)
                nextData = subPacket[3]
        value = 0
        values = [p[2] for p in packets]
        if typeId == 0: value = sum(values)
        elif typeId == 1:
            value = 1
            for v in values: value *= v
        elif typeId == 2:
            value = min(values)
        elif typeId == 3:
            value = max(values)
        elif typeId == 5:
            value = 1 if values[0] > values[1] else 0
        elif typeId == 6:
            value = 1 if values[0] < values[1] else 0
        elif typeId == 7:
            value = 1 if values[0] == values[1] else 0

        #part1
        # return (version, typeId, packets, nextData)
        return (version, typeId, value, nextData)


packets = readPacket(data)

#part1
# result = 0
# stack = [packets]
# while stack:
#     p = stack[0]
#     stack = stack[1:]
#     result += p[0]
#     if p[1] != 4:
#         stack += p[2]
# print(result)

#part2
print(packets[2])


# x > 883

#part1 1h27
#total 1h36
