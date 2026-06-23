from ciphers.atbash import atbash_cipher
from ciphers.caesers import brute_force_caesar
from ciphers.morse_code import decode_morse, encode_morse
from ciphers.bacon import decode_bacon, encode_bacon
from analysis.frequency_analysis import frequency_analysis_tool

print("type 1 for Ceaser Cipher")
print("type 2 for Atbash Cipher")
print("type 3 for Morse Code Decoder or Encoder")
print("type 4 for Baconian Code Decoder or Encoder")
print("type 5 for Frequency Analysis Tool")
init = input()
if init == "1":
    brute_force_caesar()
elif init == "2":
    atbash_cipher()
elif init == "3":
    print("type 1 for Morse Code Decoder")
    print("type 2 for Morse Code Encoder")
    morse_init = input()
    if morse_init == "1":
        decode_morse()
    elif morse_init == "2":
        encode_morse()
elif init == "4":
    print("type 1 for Baconian Code Decoder")
    print("type 2 for Baconian Code Encoder")
    bacon_init = input()
    if bacon_init == "1":
        decode_bacon()
    elif bacon_init == "2":
        encode_bacon()
elif init == "5":
    frequency_analysis_tool()
