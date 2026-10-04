#!/usr/bin/env python3
"""Convert length-prefixed RTP (G.729) .dat recordings to WAV.

Usage: python3 dat_to_wav.py file1.dat [file2.dat ...]
Requires ffmpeg on your PATH for the final decode step.
"""
import struct
import subprocess
import sys
from pathlib import Path


def extract_payload(data: bytes) -> bytes:
    """Return the concatenated RTP payloads from a .dat byte string."""
    out, i = [], 0
    while i + 2 <= len(data):
        # Each record: 2-byte big-endian length, then an RTP packet.
        (length,) = struct.unpack(">H", data[i:i + 2])
        i += 2
        if length == 0:          # zero-length padding between records
            continue
        pkt = data[i:i + length]
        i += length
        if len(pkt) < 12 or pkt[0] >> 6 != 2:   # RTP version must be 2
            raise ValueError(f"Not an RTP packet at offset {i - length}")
        csrc_count = pkt[0] & 0x0F
        header_len = 12 + 4 * csrc_count         # fixed header + CSRC list
        if pkt[0] & 0x10:                        # header extension present
            ext_words = struct.unpack(">H", pkt[header_len + 2:header_len + 4])[0]
            header_len += 4 + 4 * ext_words
        out.append(pkt[header_len:])             # payload (20 bytes = 2x G.729 frames)
    return b"".join(out)


def main(paths):
    for p in map(Path, paths):
        payload = extract_payload(p.read_bytes())
        raw = p.with_suffix(".g729")
        raw.write_bytes(payload)
        wav = p.with_suffix(".wav")
        subprocess.run(
            ["ffmpeg", "-v", "error", "-y", "-f", "g729", "-i", str(raw), str(wav)],
            check=True,
        )
        print(f"{p.name}: {len(payload)} bytes of G.729 -> {wav.name}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    main(sys.argv[1:])
