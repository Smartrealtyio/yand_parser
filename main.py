from parser import Yandex_Parser
import sys

parser = Yandex_Parser()
parser.parse(**sys.argv)
