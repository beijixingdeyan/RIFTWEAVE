#!/usr/bin/env python3
"""Batch import helper (stub) - integrates Quixel Bridge export."""
import json, pathlib
cfg = json.load(open(pathlib.Path(__file__).parent / "AssetImport.json", encoding="utf-8"))
print(f"Import policies: {len(cfg['policies'])}")
for p in cfg["policies"]:
    print(f"  {p['path']} nanite={p['nanite']}")
print("Stub: run via UE Python (unreal.AssetTools) in editor.")
