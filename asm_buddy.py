#!/usr/bin/env python
from capstone import *
from keystone import *
import argparse

__author__  = "Jeff White [karttoon] @noottrak"
__email__   = "karttoon@gmail.com"
__version__ = "1.0.1"
__date__    = "13OCT2016"

"""
asma() {
    python ~/Scripts/OneOffs/asm_buddy.py -f a -i "$@"
}

asmd() {
    python ~/Scripts/OneOffs/asm_buddy.py -f d -i "$@"
}
"""

def disassemble(args):

    if args.arch == "x86":
        md = Cs(CS_ARCH_X86, CS_MODE_32)
    if args.arch == "x64":
        md = Cs(CS_ARCH_X86, CS_MODE_64)
    if args.arch == "arm":
        md = Cs(CS_ARCH_ARM, CS_MODE_ARM)

    CODE = args.input
    CODE = [CODE[x:x+2] for x in range(0, len(CODE), 2)]
    CODE = "".join([chr(int(x, 16)) for x in CODE])

    for i in md.disasm(CODE, 0):
        print "%-10s%s" % (i.mnemonic, i.op_str)

def assemble(args):

    if args.arch == "x86":
        ks = Ks(KS_ARCH_X86, KS_MODE_32)
    if args.arch == "x64:":
        ks = Ks(KS_ARCH_X86, KS_MODE_64)
    if args.arch == "arm":
        ks = Ks(KS_ARCH_ARM, KS_MODE_ARM)

    CODE = args.input

    ASM = ks.asm(CODE)
    ASM = ["\\x%.2X" % x for x in ASM[0]]

    print "".join(ASM)

def main():
    parser = argparse.ArgumentParser(description="Generate ASM or disasemble bytes. ASM should be semi-colon separated (\";\").")
    parser.add_argument("-a", "--arch", help="Architecture - x86 or x64.", default="x86", choices=["x86",
                                                                                                   "x64",
                                                                                                   "arm"])
    parser.add_argument("-i", "--input", help="Your input to assemble or disassemble.", required=True)
    parser.add_argument("-f", "--func", help="Assemble [a] or Disassemble [d].", required=True, choices=["a", "d"])
    args = parser.parse_args()

    if args.func == "d":

        args.input = args.input.replace("0x","")
        args.input = args.input.replace("\\x", "")
        args.input = args.input.replace(",", "")
        args.input = args.input.replace(";", "")
        args.input = args.input.replace("+", "")
        args.input = args.input.replace(":", "")
        args.input = args.input.replace(" ", "")

        disassemble(args)

    if args.func == "a":

        assemble(args)

if __name__ == '__main__':
    main()
