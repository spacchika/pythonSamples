import ipaddress
import json
import re

ipAddress = "x.x.x.x"
f = open(r"PATH_TO_FILE_HERE","r")
contents = f.read()
f.close()

config_lines = re.findall("gtm((.|\n)*?)}\n}",contents)

for line in config_lines:
    #print(line)
    if ipAddress in str(line):
        line = (((str(line)).replace("('","")).replace("', ' ')","")).replace("\\n","\n")
        line = "gtm "+line+"}\n}"
        f = open(ipAddress,"x")
        f.write(line)
        f.close()
