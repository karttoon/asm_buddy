# asm_buddy
Small script using [Capstone](http://capstone-engine.org)/[Keystone](http://keystone-engine.org) to assemble/disassemble x86/x64 instructions from the command line.

Add the below functions into your .bashrc or .bash_profile for daily usage.

```
asma() {
    python ~/Scripts/OneOffs/asm_buddy.py -f a -i "$@"
}

asmd() {
    python ~/Scripts/OneOffs/asm_buddy.py -f d -i "$@"
}
```

### Usage

Using the functions above, it's pretty straight forward.

For assembling -

```
$ asma 'jmp esp; inc ecx; call 0x400100'
\xFF\xE4\x41\xE8\xF8\x00\x40\x00
```

For disassembling -

```
$ asmd 'ffe441e8f8004000'
jmp       esp
inc       ecx
call      0x1400100
```

A couple of other options if you need some more control over architecture.

```
usage: asm_buddy.py [-h] [-a {x86,x64,arm}] -i INPUT -f {a,d}

Generate ASM or disasemble bytes. ASM should be semi-colon separated (";").

optional arguments:
  -h, --help            show this help message and exit
  -a {x86,x64,arm}, --arch {x86,x64,arm}
                        Architecture choice.
  -i INPUT, --input INPUT
                        Your input to assemble or disassemble.
  -f {a,d}, --func {a,d}
                        Assemble [a] or Disassemble [d].
```
