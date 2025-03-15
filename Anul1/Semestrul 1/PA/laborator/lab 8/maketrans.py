#%%
s="ana, are; mere:"
d={"a":"gigel","m":"ionel",'e':''}
tabel=str.maketrans(d)
s=s.translate(tabel)
print(s)
#%%

sep = {";":" ", ".": " ", ",":" ", ":":" "}
tabel=str.maketrans(sep)
s=s.translate(tabel)
print(s)