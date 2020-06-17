class Solution:
    def validIPAddress(self, IP: str) -> str:
        if len(IP) != 0:
            if IP[0] == '.' or IP[0] == ':':
                return 'Neither'
            last_ind = 0
            if IP[0] != '0':
                # avoiding 1st leading zeros
                isIPv4 = True
                countDot = 0
                for i in range(len(IP)):
                    c = IP[i]
                    if c == '-' or (c == '.' and i==len(IP)-1) or (c.isalpha()) or (i==len(IP)-1 and i - last_ind >= 3):
                        isIPv4 = False
                        break
                    if c == '.':
                        countDot += 1
                        if i - last_ind > 3 or (i+2<len(IP) and IP[i+1] == '0' and IP[i+2].isdigit()) or int(IP[last_ind:i])>255 or int(IP[last_ind:i])<0 or IP[i+1] == '.':
                            # more than 3 char or leading zero in between or Out of range
                            isIPv4 = False
                            break
                        last_ind = i + 1
                if isIPv4 and countDot == 3:
                    return 'IPv4'
            # checking for IPv6 as not IPv4
            last_ind = 0
            isIPv6 = True
            countColon = 0
            if IP[0] != ":":
                # avoiding 1st char to be ":"
                for i in range(len(IP)):
                    c = IP[i]
                    if c == '-' or (c.isalpha() and ord(c.lower())>102) or (c==':' and i==len(IP)-1) or (i==len(IP)-1 and i - last_ind >= 4):
                        isIPv6 = False
                        break
                    if c == ':':
                        countColon += 1
                        if i - last_ind > 4 or IP[i+1] == ':':
                            # more than 4 char Or c is char & higher than 'F/f' or 2 consecutive ": :"
                            isIPv6 = False
                            break
                        last_ind = i + 1
                if isIPv6 and countColon == 7:
                    return 'IPv6'
        return 'Neither'
