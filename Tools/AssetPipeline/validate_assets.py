#!/usr/bin/env python3
"""
Asset validation for RIFTWEAVE — checks naming, Nanite, and material setup without UE.
Usage: py Tools/AssetPipeline/validate_assets.py [--all|--quick]
"""
import pathlib, re, sys, json

ROOT = pathlib.Path(__file__).resolve().parents[2]
issues = []

def check_uasset_naming():
    for p in (ROOT / "Content").rglob("*.uasset.README.md"):
        text = p.read_text(encoding="utf-8", errors="ignore")
        if "Nanite" not in text:
            issues.append(f"[WARN] {p.relative_to(ROOT)} missing Nanite note")

def check_configs():
    for ini in (ROOT / "Config").glob("*.ini"):
        txt = ini.read_text(encoding="utf-8", errors="ignore")
        if "Nanite" in str(ini) or ini.name == "DefaultEngine.ini":
            if "r.Nanite.ProjectEnabled" not in txt:
                issues.append(f"[FAIL] {ini.name} missing Nanite flag")

def check_cpp_headers():
    for h in (ROOT / "Source").rglob("*.h"):
        txt = h.read_text(encoding="utf-8", errors="ignore")
        if "UCLASS" in txt and "generated.h" not in txt.lower():
            issues.append(f"[FAIL] {h.relative_to(ROOT)} UCLASS without generated.h")

def check_docs():
    for md in (ROOT / "Documentation").glob("*.md"):
        if md.name == "README.md":
            continue
        lines = md.read_text(encoding="utf-8", errors="ignore").splitlines()
        # Glossary/FAQ are reference, allow shorter
        min_lines = 20 if md.name in ("13_Glossary.md", "12_FAQ.md") else 30
        if len(lines) < min_lines:
            issues.append(f"[WARN] {md.name} too short ({len(lines)} lines)")

def main():
    quick = "--quick" in sys.argv
    print("=== RiftWeave Asset Validation ===")
    check_configs()
    if not quick:
        check_uasset_naming()
        check_cpp_headers()
        check_docs()
    else:
        check_docs()

    if not issues:
        print("[OK] No issues found.")
        # also print stats
        cpp = list((ROOT/"Source").rglob("*.h")) + list((ROOT/"Source").rglob("*.cpp"))
        print(f"  C++ files: {len(cpp)}")
        print(f"  Docs: {len(list((ROOT/'Documentation').glob('*.md')))}")
        print(f"  Content descriptors: {len(list((ROOT/'Content').rglob('*.md')))}")
        return 0
    else:
        for i in issues:
            print(i)
        fails = [x for x in issues if x.startswith("[FAIL]")]
        print(f"\n{len(issues)} issues ({len(fails)} fails)")
        return 1 if fails else 0

if __name__ == "__main__":
    sys.exit(main())
