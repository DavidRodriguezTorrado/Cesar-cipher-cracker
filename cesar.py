# Developed by David Rodriguez
# ATTENTION: ONLY WORKS with English dictionary

# Modify the next variable. Introduce text to decode:
Text_to_decode = 'HPCXS PSEXH PTAPR TATGP SDGEP GPPBE AXPGA PATNP CIXIP QPRDP THEPR XDHPA PXGTA XQGT'

def cesar(decode):
    text = decode.replace(" ", "").lower()

    dictionary = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                   'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    string_result = ''
    for rot in range(26):
        for i in range(len(text)):
            search_index = dictionary.index(text[i])+rot
            if search_index > 25:
                search_index = search_index-26
            string_result = string_result + dictionary[search_index]
        print('Rotational: {} {}'.format(rot, string_result))
        string_result = ''

if __name__ == '__main__':
    print('Printing all rotational posibilities')
    cesar(Text_to_decode)

