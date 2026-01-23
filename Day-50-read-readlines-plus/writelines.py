f = open('file-for-writelines.txt', 'w')

n = '\n'
lines = ['line 1' + n, 'line 2' + n, 'line 3' + n]

f.writelines(lines)