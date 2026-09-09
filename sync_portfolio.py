#!/usr/bin/env python3
"""sync_portfolio.py — Passerelle locale directe entre kuro-rules et Lemniscate-world.

Met a jour le dashboard portfolio, le panneau CI et les mondes
directement depuis la source de verite kuro-rules.
"""
import shutil
import subprocess
import sys
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parent
KURO_RULES = WORKSPACE.parent / "kuro-rules"


def main():
    print("[Kuro-Bridge] Verification du lien kuro-rules <-> Lemniscate-world...")
    if not KURO_RULES.is_dir():
        print(f"[Erreur] Repertoire kuro-rules introuvable a {KURO_RULES}")
        sys.exit(1)

    epingle = KURO_RULES / "Epingle_Projets.md"
    generator = KURO_RULES / "scripts" / "generate_portfolio.py"
    ci_source = KURO_RULES / "ci-status.json"

    if not epingle.is_file():
        print(f"[Erreur] Epingle_Projets.md introuvable a {epingle}")
        sys.exit(1)

    # 1. Copie du statut CI le plus recent si disponible
    if ci_source.is_file():
        ci_dest = WORKSPACE / "ci-status.json"
        shutil.copy2(ci_source, ci_dest)
        print("[Kuro-Bridge] ci-status.json synchronise.")

    # 2. Execution de generate_portfolio.py
    print("[Kuro-Bridge] Regeneration du portfolio et des 14 mondes...")
    cmd = [
        sys.executable,
        str(generator),
        "--epingle", str(epingle),
        "--output", str(WORKSPACE / "index.html"),
    ]
    res = subprocess.run(cmd, cwd=str(WORKSPACE))
    if res.returncode == 0:
        print("[Kuro-Bridge] Portfolio genere avec succes selon Quiet Precision (R108).")
    else:
        print(f"[Erreur] Echec generation portfolio (code {res.returncode})")
        sys.exit(res.returncode)


if __name__ == "__main__":
    main()
