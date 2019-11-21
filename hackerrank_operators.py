import sys

xlines = sys.stdin
line2 = ''
for line in xlines:
    line2=line2+','+line.split('\n')[0]
j = line2.split(",")[1]
k = int(j)
e = line2.split(",")[2]
f = float(e)
t = line2.split(",")[3]

# Print the sum of both integer variables on a new line.
print int(i + k)
# Print the sum of the double variables on a new line.
print float(f + d)
# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
print s+t