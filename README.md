# Smali Safari (`smali-safari`)

**Category:** reverse engineering · **Difficulty:** medium · **Points:** 300

An Android DEX method builds the seed at runtime; reverse the smali to recover it.

## Run it

```bash
docker build -t sparflag/smali-safari .
# `deca-ai start smali-safari` (or the web UI) prints the docker run line with your
# SPARFLAG_SERVER + SPARFLAG_INSTANCE_TOKEN
```

## Recover the flag

The delivery blob is Fernet ciphertext. Discover the key seed, derive the Fernet key, then decrypt.

The plaintext flag is never written to disk or served — only the encoded delivery blob
is. When you have it:

```bash
deca-ai submit smali-safari 'sparflag{...}'
```

## Hints

- Decompile the DEX to smali or Java.
- Trace how the seed string is assembled.
