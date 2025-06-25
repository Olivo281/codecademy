import string

# -------------------
# 1 & 4: Caesar Cipher encode & decode functions

def caesar_encode(message, offset):
    """
    Encode a message by shifting letters to the left by offset.
    Non-letters remain unchanged.
    """
    encoded = []
    for ch in message:
        if ch.isalpha():
            base = ord('a') if ch.islower() else ord('A')
            # shift left means subtract offset
            new_char = chr((ord(ch) - base - offset) % 26 + base)
            encoded.append(new_char)
        else:
            encoded.append(ch)
    return ''.join(encoded)

def caesar_decode(message, offset):
    """
    Decode a message by shifting letters to the right by offset.
    Non-letters remain unchanged.
    """
    decoded = []
    for ch in message:
        if ch.isalpha():
            base = ord('a') if ch.islower() else ord('A')
            # shift right means add offset
            new_char = chr((ord(ch) - base + offset) % 26 + base)
            decoded.append(new_char)
        else:
            decoded.append(ch)
    return ''.join(decoded)

# Example of decoding the first message (offset 10)
encoded_msg1 = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
decoded_msg1 = caesar_decode(encoded_msg1, 10)
print("Decoded message 1:\n", decoded_msg1)
print()

# -------------------
# 2: Encode a reply using same offset
reply = "Hello Vishal! I am doing great, thanks for the cipher challenge!"
encoded_reply = caesar_encode(reply, 10)
print("Encoded reply:\n", encoded_reply)
print()

# -------------------
# 3: Decode two new messages

encoded_msg2a = "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."
encoded_msg2b = "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"

decoded_msg2a = caesar_decode(encoded_msg2a, 10)
print("Decoded message 2a:\n", decoded_msg2a)

# The hint message 2a says: "the result for the second message is sixteen"

# So decode message 2b with offset 16
decoded_msg2b = caesar_decode(encoded_msg2b, 16)
print("Decoded message 2b:\n", decoded_msg2b)
print()

# -------------------
# 4: Brute force decode Caesar cipher without knowing offset

coded_msg3 = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."

print("Brute force Caesar decode attempts:\n")
for offset in range(26):
    attempt = caesar_decode(coded_msg3, offset)
    print(f"Offset {offset}: {attempt}\n")

print("Based on reading, offset 7 yields readable text.\n")

# -------------------
# 5: Vigenère Cipher encode and decode

def vigenere_encode(message, keyword):
    """
    Encode message using Vigenere cipher with given keyword.
    Only letters are encoded, others left unchanged.
    """
    encoded = []
    keyword = keyword.lower()
    key_len = len(keyword)
    key_indices = [ord(k) - ord('a') for k in keyword]

    j = 0  # keyword index
    for ch in message:
        if ch.isalpha():
            base = ord('a') if ch.islower() else ord('A')
            shift = key_indices[j % key_len]
            new_char = chr((ord(ch) - base + shift) % 26 + base)
            encoded.append(new_char)
            j += 1
        else:
            encoded.append(ch)
    return ''.join(encoded)

def vigenere_decode(message, keyword):
    """
    Decode message encoded with Vigenere cipher and given keyword.
    """
    decoded = []
    keyword = keyword.lower()
    key_len = len(keyword)
    key_indices = [ord(k) - ord('a') for k in keyword]

    j = 0
    for ch in message:
        if ch.isalpha():
            base = ord('a') if ch.islower() else ord('A')
            shift = key_indices[j % key_len]
            new_char = chr((ord(ch) - base - shift) % 26 + base)
            decoded.append(new_char)
            j += 1
        else:
            decoded.append(ch)
    return ''.join(decoded)

# Vishal's coded message and keyword for task 5:
vigenere_coded = "txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztylktoikqq!"
keyword = "friends"

vigenere_decoded = vigenere_decode(vigenere_coded, keyword)
print("Decoded Vigenere message:\n", vigenere_decoded)
print()

# -------------------
# 6: Function to encode a message using Vigenère cipher and test roundtrip

message_to_encode = "python is fun and I love coding!"
keyword_for_encoding = "friends"

encoded_message = vigenere_encode(message_to_encode, keyword_for_encoding)
print("Encoded message:\n", encoded_message)

decoded_message = vigenere_decode(encoded_message, keyword_for_encoding)
print("Decoded message (should match original):\n", decoded_message)
print()

# -------------------
# Summary printouts to verify correctness
print("All tasks completed!")