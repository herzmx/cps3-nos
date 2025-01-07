# -*- coding: utf-8 -*-
import argparse
from argparse import RawTextHelpFormatter

bios_patch = [
    (0x00000000, 0xD23F420B),
    (0x00000014, 0x0009D33D),
    (0x00000020, 0xA0180009),
    (0x00000060, 0xD227420B),
    (0x00000068, 0x000963E2),
    (0x0000006C, 0xD2300009),
    (0x00000070, 0x33208905),
    (0x00000074, 0x000961E2),
    (0x00000078, 0xD02F0009),
    (0x0000007C, 0x31008B2D),
    (0x00000084, 0xD221420B),
    (0x0000008C, 0x0009A021),
    (0x00000090, 0x000963F1),
    (0x00000124, 0x01007E22),
    (0x00000130, 0x89007E22),
    (0x00000138, 0x0089227E),
    (0x000001EC, 0x8B06D21B),
    (0x00000210, 0x8903D01E),
    (0x00000214, 0x61E23100),
    (0x00000218, 0x8B06D210),
    (0x0000027C, 0x01000100),
    (0x00000280, 0x7E227E22),
    (0x00000288, 0x89008900),
    (0x0000028C, 0x00890089),
]

bios_multi_nomenu_patch = [(0x0000405C, 0x00020730), (0x00020744, 0xC8108904)]

bios_patch_text = [
    (0x00000000, 0x5350414E),
    (0x00000004, 0x53494F4E),
    (0x00000008, 0x20202000),
    (0x0000000C, 0x4D494352),
    (0x00000010, 0x4F4E2020),
    (0x00000014, 0x20202000),
    (0x0000091C, 0x5350414E),
    (0x00000920, 0x53494F4E),
    (0x00000924, 0x20202020),
    (0x00000930, 0x4D494352),
    (0x00000934, 0x4F4E2020),
    (0x00000938, 0x20202020),
]

bios_patch_text_redearth = [
    (0x00000000, 0x5350414E),
    (0x00000004, 0x53494F4E),
    (0x00000008, 0x20202000),
    (0x0000000C, 0x4D494352),
    (0x00000010, 0x4F4E2020),
    (0x00000014, 0x20202000),
    (0x00001D30, 0x5350414E),
    (0x00001D34, 0x53494F4E),
    (0x00001D38, 0x20202020),
    (0x00001D44, 0x4D494352),
    (0x00001D48, 0x4F4E2020),
    (0x00001D4C, 0x20202020),
]


game_keys = {
    "jojo": {
        "key1": 0x02203EE3,
        "key2": 0x01301972,
        "is_special": 0,
        "patch_offset": 0xA690,
        "patch_text_offset": 0x170A8,
        "region_offset": 0x1FEC8,
        "cdnocd_offset": 0x1FECC,
    },
    "jojoba": {
        "key1": 0x23323EE3,
        "key2": 0x03021972,
        "is_special": 0,
        "patch_offset": 0xA6B4,
        "patch_text_offset": 0x17120,
        "region_offset": 0x1FEC8,
        "cdnocd_offset": 0x1FECC,
    },
    "sfiii": {
        "key1": 0xB5FE053E,
        "key2": 0xFC03925A,
        "is_special": 0,
        "patch_offset": 0x121B0,
        "region_offset": 0x1FEC8,
        "cdnocd_offset": 0x1FECC,
    },
    "sfiiin": {
        "key1": 0xB5FE053E,
        "key2": 0xFC03925A,
        "is_special": 0,
        "patch_offset": 0x12228,
        "region_offset": 0x1FEC8,
    },
    "sfiii2": {
        "key1": 0x00000000,
        "key2": 0x00000000,
        "is_special": 1,
        "patch_offset": 0x12278,
        "region_offset": 0x1FEC8,
        "cdnocd_offset": 0x1FECC,
    },
    "sfiii3": {
        "key1": 0xA55432B4,
        "key2": 0x0C129981,
        "is_special": 0,
        "patch_offset": 0xA6A8,
        "patch_text_offset": 0x170C4,
        "region_offset": 0x1FEC8,
        "cdnocd_offset": 0x1FECC,
    },
    "warzard": {
        "key1": 0x9E300AB1,
        "key2": 0xA175B82C,
        "is_special": 0,
        "patch_offset": 0x11DD0,
        "patch_text_offset": 0x1B1C4,
        "region_offset": 0x1FED8,
    },
    "redearth": {
        "key1": 0x9E300AB1,
        "key2": 0xA175B82C,
        "is_special": 0,
        "patch_offset": 0x11DD0,
        "patch_text_offset": 0x1B1C4,
        "region_offset": 0x1FED8,
    },
    "redearthn": {
        "key1": 0x9E300AB1,
        "key2": 0xA175B82C,
        "is_special": 0,
        "patch_offset": 0x11C50,
        "patch_text_offset": 0x1B1C4,
        "region_offset": 0x1FED8,
    },
    "cps3boot": {
        "key1": 0x00000000,
        "key2": 0x00000000,
        "is_special": 1,
        "patch_offset": 0xA6A8,
        "patch_text_offset": 0x170C4,
        "region_offset": 0x20730,
        "cdnocd_offset": 0x1FECC,
    },
    "cps3boota": {
        "key1": 0x00000000,
        "key2": 0x00000000,
        "is_special": 1,
        "patch_offset": 0xA6A8,
        "patch_text_offset": 0x170C4,
        "region_offset": 0x20730,
        "cdnocd_offset": 0x1FECC,
    },
}

parser = argparse.ArgumentParser(
    description="Apply a patch to enable NOS compatibility on CPS3 BIOS.",
    formatter_class=RawTextHelpFormatter,
)
parser.add_argument("-f", "--file", help="BIOS file path")
parser.add_argument(
    "-g",
    "--game",
    help="""\
jojo
jojoba
sfiii
sfiii2
sfiii3
redearth
cps3boot  (Standard SH2)
cps3boota (Custom SH2)
sfiiin    (Asia NCD)
redearthn (Asia NCD)
""",
)
parser.add_argument(
    "-r",
    "--region",
    type=int,
    default=0,
    help="""\
1: JAPAN
2: ASIA
3: EURO
4: USA
5: HISPANIC
6: BRAZIL
7: OCEANIA
8: ASIA NCD
""",
)
parser.add_argument("-t", "--togflecdnocd", action="store_true", help="Toggle CD/NCD")
args = parser.parse_args()


def rotate_left(value, n):
    value &= 0xFFFF
    aux = value >> (16 - n)
    return ((value << n) | aux) % 0x10000


def rotxor(val, xor):
    val &= 0xFFFF
    res = val + rotate_left(val, 2)
    res = rotate_left(res, 4) ^ (res & (val ^ xor))

    return res


def cps3_mask(addr, key1, key2):
    addr ^= key1
    val = (addr & 0xFFFF) ^ 0xFFFF
    val = rotxor(val, key2 & 0xFFFF)
    val ^= (addr >> 16) ^ 0xFFFF
    val = rotxor(val, key2 >> 16)
    val ^= (addr & 0xFFFF) ^ (key2 & 0xFFFF)

    return val | (val << 16)


def cps3_patch_bios(game, filename, ext="patched", offset=0):
    bios_patches = []
    for patch in bios_patch:
        offset = patch[0] + game_keys[game]["patch_offset"]
        xormask = cps3_mask(offset, game_keys[game]["key1"], game_keys[game]["key2"])
        dword = patch[1]
        if game != "cps3boot":
            dword ^= xormask
        bios_patches.append((offset, dword.to_bytes(4, "big")))
    if game_keys[game].get("patch_text_offset"):
        patch_text = bios_patch_text
        if game in ["redearth", "redearthn", "warzard"]:
            patch_text = bios_patch_text_redearth
        for patch in patch_text:
            offset = patch[0] + game_keys[game]["patch_text_offset"]
            xormask = cps3_mask(
                offset, game_keys[game]["key1"], game_keys[game]["key2"]
            )
            dword = patch[1]
            if game != "cps3boot":
                dword ^= xormask
            bios_patches.append((offset, dword.to_bytes(4, "big")))
    if game in ["cps3boot", "cps3boota"] and args.region > 0:
        for patch in bios_multi_nomenu_patch:
            offset = patch[0]
            xormask = cps3_mask(
                patch[0], game_keys[game]["key1"], game_keys[game]["key2"]
            )
            dword = patch[1]
            if game != "cps3boot":
                dword ^= xormask
            bios_patches.append((offset, dword.to_bytes(4, "big")))

    bios_patches.sort(key=lambda tup: tup[0])

    with open(filename, "rb") as r, open(f"{filename}.{ext}", "wb") as w:
        i = 0
        pi = 0
        while dword := r.read(4):
            if pi < len(bios_patches) and i == bios_patches[pi][0]:
                dword = bios_patches[pi][1]
                pi += 1
            if (
                args.togflecdnocd
                and game_keys[game].get("cdnocd_offset")
                and game_keys[game].get("cdnocd_offset") == i
            ):
                xormask = cps3_mask(i, game_keys[game]["key1"], game_keys[game]["key2"])
                dword = int.from_bytes(dword, "big")
                if game != "cps3boot":
                    dword ^= xormask
                dword ^= 0x01000000
                if game != "cps3boot":
                    dword ^= xormask
                dword = dword.to_bytes(4, "big")
            if (
                args.region > 0
                and game_keys[game].get("region_offset")
                and game_keys[game].get("region_offset") == i
            ):
                xormask = cps3_mask(i, game_keys[game]["key1"], game_keys[game]["key2"])
                dword = int.from_bytes(dword, "big")
                if game != "cps3boot":
                    dword ^= xormask
                dword ^= dword & 0x000000FF
                dword ^= args.region
                if game != "cps3boot":
                    dword ^= xormask
                dword = dword.to_bytes(4, "big")
            w.write(dword)
            i += 4


if not args.file or not args.game:
    parser.print_help()
    exit()

cps3_patch_bios(args.game, args.file)
