# -*- coding: utf-8 -*-

def ds2nos_64(filea, fileb, filec):
    result_patch = []
    with open(filea, "rb") as ra, open(fileb, "rb") as rb, open(filec, "wb") as w:
        i = 0
        while dworda := ra.read(4):
            dwordb = rb.read(4)
            w.write(dworda[:2][::-1])
            w.write(dwordb[:2][::-1])
            w.write(dworda[2:][::-1])
            w.write(dwordb[2:][::-1])


def ds2nos_128(filea, fileb):
    result_patch = []
    with open(filea, "rb") as r, open(fileb, "wb") as w:
        i = 0
        for game in range(8):
            for bank in range(4)[::-1]:
                rseek = (game * 0x1000000) + (bank * 0x400000)
                r.seek(rseek)
                i = 0
                while i < 0x400000:
                    dword = r.read(2)
                    w.write(dword[::-1])
                    i += 2


ds2nos_64(
    "SIMM 1-2/Custom SH2/SIMM1_Jumper_U9_CustomSH2_WarzardFIX.bin", 
    "SIMM 1-2/Custom SH2/SIMM1_Jumper_U10_CustomSH2.bin",
    "NOS10_Custom")

ds2nos_64(
    "SIMM 1-2/Custom SH2/SIMM2_Jumper_U9_CustomSH2.bin", 
    "SIMM 1-2/Custom SH2/SIMM2_Jumper_U10_CustomSH2.bin",
    "NOS20_Custom")

ds2nos_64(
    "SIMM 1-2/Standard SH2/SIMM1_Jumper_U9_CustomSH2_WarzardFIX.bin", 
    "SIMM 1-2/Standard SH2/SIMM1_Jumper_U10_CustomSH2.bin",
    "NOS10_Standard")

ds2nos_64(
    "SIMM 1-2/Standard SH2/SIMM2_Jumper_U9_CustomSH2.bin", 
    "SIMM 1-2/Standard SH2/SIMM2_Jumper_U10_CustomSH2.bin",
    "NOS20_Standard")

ds2nos_128(
    "SIMM 3-6/SIMM3_Final.bin", 
    "NOS30")

ds2nos_128(
    "SIMM 3-6/SIMM4_Final.bin", 
    "NOS40")

ds2nos_128(
    "SIMM 3-6/SIMM5_Final_MakotoFIX.bin", 
    "NOS50_MakotoFIX")

ds2nos_128(
    "SIMM 3-6/SIMM5_Final_reTHIRD.bin", 
    "NOS50_reTHIRD")

ds2nos_128(
    "SIMM 3-6/SIMM6_Final.bin", 
    "NOS60")
