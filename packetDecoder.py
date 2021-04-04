def xor_key_data(key,data):  # XORs two bytes of data
    xored_bits = ''
    for i,j in zip(key,data):
        xored_bits += str(int(i) ^ int(j))
    return xored_bits  
  
def decodePacket(packet_data):
    key = packet_data[:8]    # first byte is key 
    data_length = int(packet_data[8:16],2) # second byte is data length, converted Binary to decimal for length
    data = textwrap.wrap(packet_data[16:], 8) # All the bytes after 2nd is data

    if data_length != len(data):
        return "Invalid packet"  # edge case

    xored_res = []
    for byte in data:
        xored_res.append(xor_key_data(key,byte)) # call XOR bytes function for each byte in data 

    decoded_str = ''
    for char in xored_res:
        decoded_str += chr(int(char,2))  # convert string result to ascii (string -> int -> ascii)
        
    return decoded_str
  
# Demo invocation 
# decodePacket('10101010000001011110001011001111110001101100011011000101') #returns hello
# decodePacket('1010101000000101111000101100111111000110110001101100010100') #returns Invalid packet
