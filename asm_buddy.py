#!/usr/bin/env python
from capstone import *
from keystone import *
import argparse

__author__  = "Jeff White [karttoon]"
__email__   = "karttoon@gmail.com"
__version__ = "1.0.0"
__date__    = "29SEP2016"

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
    else:
        md = Cs(CS_ARCH_X86, CS_MODE_64)

    CODE = args.input.replace("\\x", "")
    CODE = CODE.replace("0x", "")
    CODE = [CODE[x:x+2] for x in range(0, len(CODE), 2)]
    CODE = "".join([chr(int(x, 16)) for x in CODE])

    for i in md.disasm(CODE, 0x1000000):
        print "%-10s%s" % (i.mnemonic, i.op_str)

def assemble(args):
    if args.arch == "x86":
        ks = Ks(KS_ARCH_X86, KS_MODE_32)
    else:
        ks = Ks(KS_ARCH_X86, KS_MODE_64)

    CODE = args.input

    ASM = ks.asm(CODE)
    ASM = ["\\x%.2X" % x for x in ASM[0]]

    print "".join(ASM)

def main():
    parser = argparse.ArgumentParser(description="Generate ASM or disasemble bytes. ASM should be semi-colon separated (\";\").")
    parser.add_argument("-a", "--arch", help="Architecture - x86 or x64.", default="x86", choices=["x86", "x64"])
    parser.add_argument("-i", "--input", help="Your input to assemble or disassemble.", required=True)
    parser.add_argument("-f", "--func", help="Assemble [a] or Disassemble [d].", required=True, choices=["a", "d"])
    args = parser.parse_args()

    if args.func == "d":
        disassemble(args)
    if args.func == "a":
        assemble(args)

if __name__ == '__main__':
    main()
