#!/usr/bin/env python3
"""Smali Safari — real mini-challenge (smali-safari)."""
import base64, hashlib, json, os, struct, sys, zlib, wave, io, math, random, re, textwrap
sys.path.insert(0, "/challenge/_shared")
from fetch_material import fetch_material

CHALLENGE_KEY = os.environ.get("CHALLENGE_KEY", 'dex-decompile')


def main():
    mat = fetch_material()
    with open("/challenge/flag.enc", "w") as f:
        f.write(mat["delivery_blob"])
    key = CHALLENGE_KEY or "dex-key"
    smali = f""".class public LMain;
.super Ljava/lang/Object;

.method public static main([Ljava/lang/String;)V
    const-string v0, "{key}"
    sget-object v1, Ljava/lang/System;->out:Ljava/io/PrintStream;
    invoke-virtual {{v1, v0}}, Ljava/io/PrintStream;->println(Ljava/lang/String;)V
    return-void
.end method
"""
    with open("/challenge/Main.smali", "w") as f:
        f.write(smali)
    print("Smali Safari: const-string in Main.smali holds key; decrypt flag.enc.")


if __name__ == "__main__":
    main()
