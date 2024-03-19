import sys
sys.path.append("../..")
import common as c

def count():
    req=c.pget(url='/operator/perspective/workList?type=1')

count()
