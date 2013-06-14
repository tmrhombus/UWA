from optparse import OptionParser

p = OptionParser()
p.add_option("-f", "--file", dest="filename", help="write to FILE", metavar="FILE")

(options, args) = p.parse_args()
