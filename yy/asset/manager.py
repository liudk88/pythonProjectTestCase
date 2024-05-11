import sys
sys.path.append("../..")
import common as c

def list():
    c.pget("/view/AssetView-BS/view?flag=1&current=1&size=10");

def delete():
    c.pget("/view/AssetView-BS/data/1173683241375236096?delFlag=flag");

def toAdd():
    c.pget("/asset/main/init?entryKey=AssetForm-ES")

args=c.args()

args.append("5")

if len(args) == 0:
    args.append("0")
    # args.append("commitList")

if len(args)==0 or args[0]=='0':
    list()
elif args[0]=='5':
    toAdd()

