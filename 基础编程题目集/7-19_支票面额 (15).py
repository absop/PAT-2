isOk = False
n = int(raw_input())
for f in xrange(100):
    for y in xrange(201):
        if 98 * f - 199 * y == n:
            isOk = True
            print '%d.%d' % (y, f)
if not isOk:
    print 'No Solution'
            
