#conf binaire
o a.out~prevent_display
e asm.arch = msp430
#e asm.bits = 16
e asm.esil = true

# conf esil
aei
aeim 0x2000 0xffff
aeip 0x4400
e io.cache=true
"e cmd.esil.intr=#!pipe python handlers.py"
e esil.gotolimit=0xffff
aec
