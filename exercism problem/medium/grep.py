#copy-pasted the solution...

def grep(pattern, flags, files):
    n, l, i, v, x = "-n" in flags, "-l" in flags, "-i" in flags, "-v" in flags, "-x" in flags
    pattern = pattern.lower() if i else pattern
    m = len(files) > 1
    res = ""
    for file in files:
        for ln_num, line in enumerate(open(file).readlines()):
            line_i = line.lower() if i else line
            if v ^ (not x and pattern in line_i or pattern + '\n' == line_i):
                if l:
                    res += file + "\n"
                    break
                res += (f"{file}:" if m else '') + \
                    (f"{ln_num+1}:" if n else '') + line
    return res
