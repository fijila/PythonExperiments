import  re
def substr(pattern,replacestr,str):
    m=re.sub(pattern,replacestr,str)
    return m

lis=['100 NORTH MAIN ROAD',
  '100 BROAD ROAD APT.',
  'SAROJINI DEVI ROAD',
  'BROAD AVENUE ROAD']
me=[]
pattern=r" ROAD"
replaceStr=' RD'
for i in lis:
  me.append(substr(pattern,replaceStr,i))
print(me)