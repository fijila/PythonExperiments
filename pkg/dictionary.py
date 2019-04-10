def group_by_owners(files):
   dinv = {}
   for k, v in files.items():
        if v in dinv:
            dinv[v].append(k)
        else:
            dinv[v] = [k]
   return dinv
files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}
print(group_by_owners(files))