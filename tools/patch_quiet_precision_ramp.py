#!/usr/bin/env python3
"""patch_quiet_precision_ramp.py — Corrige la rampe typographique Quiet Precision.

Cause racine des warnings Impeccable (undersized-ui-text / all-caps-body) :
les tailles CSS descendaient sous le plancher de lisibilite (0.62-0.68rem
= 9.92-10.88px). Ce script introduit une rampe tokenisee dans :root et
remplace les valeurs fautives, au bon endroit : le generateur de source
(kuro-rules/scripts/generate_portfolio.py), pas index.html qui est ecrase.

Idempotent : relancer le script ne casse rien (PATCHED / ALREADY PATCHED /
ANCHOR NOT FOUND).
"""
from pathlib import Path

GEN = Path(r"C:\Users\Utilisateur\Documents\kuro-rules\scripts\generate_portfolio.py")

# --- 1. Rampe typographique tokenisee (plancheres : 11px fonctionnel, 12px meta) ---
ROOT_OLD = (
    "    --sans: -apple-system, BlinkMacSystemFont, 'Segoe UI', Inter, Helvetica, Arial, sans-serif;\n"
    "  }"
)
ROOT_NEW = (
    "    --sans: -apple-system, BlinkMacSystemFont, 'Segoe UI', Inter, Helvetica, Arial, sans-serif;\n"
    "    /* R108 rampe typographique : planchere anti-slop (>=11px fonctionnel, >=12px meta) */\n"
    "    --fs-micro: 0.8125rem; /* 13px - titres de micro-blocs, labels */\n"
    "    --fs-meta: 0.75rem;    /* 12px - colophon, footer, meta, badges */\n"
    "    --fs-body: 0.875rem;   /* 14px - corps secondaire */\n"
    "  }"
)

# --- 2. Ajustement de la rampe : valeurs en rem sous le plancher -> tokens ---
RAMPS = [
    # .over : 0.68rem -> meta, uppercase retire (label long possible)
    (
        ".over { font-family: var(--mono); font-size: 0.68rem; letter-spacing: 0.18em; text-transform: uppercase; color: var(--muted); }",
        ".over { font-family: var(--mono); font-size: var(--fs-meta); letter-spacing: 0.14em; color: var(--muted); }",
    ),
    # .colophon : 0.68rem -> meta
    (
        ".colophon { font-family: var(--mono); font-size: 0.68rem; color: var(--muted); }",
        ".colophon { font-family: var(--mono); font-size: var(--fs-meta); color: var(--muted); }",
    ),
    # .stat-label : 0.62rem (9.92px FAIL) -> meta, uppercase retire
    (
        ".stat-label { font-family: var(--mono); font-size: 0.62rem; letter-spacing: 0.14em; text-transform: uppercase; color: var(--muted); }",
        ".stat-label { font-family: var(--mono); font-size: var(--fs-meta); letter-spacing: 0.1em; color: var(--muted); }",
    ),
    # .ci-head : 0.68rem -> meta, uppercase retire
    (
        ".ci-head { font-family: var(--mono); font-size: 0.68rem; font-weight: 600; letter-spacing: 0.12em; text-transform: uppercase; color: var(--muted); margin-bottom: 0.4rem; }",
        ".ci-head { font-family: var(--mono); font-size: var(--fs-meta); font-weight: 600; letter-spacing: 0.1em; color: var(--muted); margin-bottom: 0.4rem; }",
    ),
    # .ci-box p : 0.76rem -> body
    (
        ".ci-box p { font-family: var(--mono); font-size: 0.76rem; color: var(--muted); margin: 0.2rem 0; }",
        ".ci-box p { font-family: var(--mono); font-size: var(--fs-body); color: var(--muted); margin: 0.2rem 0; }",
    ),
    # th : 0.62rem (9.92px FAIL) -> meta, uppercase conserve (en-tete court legitime)
    (
        "th { font-family: var(--mono); font-weight: 600; text-align: left; font-size: 0.62rem; letter-spacing: 0.16em; text-transform: uppercase;",
        "th { font-family: var(--mono); font-weight: 600; text-align: left; font-size: var(--fs-meta); letter-spacing: 0.12em; text-transform: uppercase;",
    ),
    # .badge : 0.64rem (10.24px FAIL) -> meta, uppercase conserve (badge court legitime)
    (
        ".badge { display: inline-block; font-family: var(--mono); font-size: 0.64rem; font-weight: 500; letter-spacing: 0.08em; text-transform: uppercase;",
        ".badge { display: inline-block; font-family: var(--mono); font-size: var(--fs-meta); font-weight: 500; letter-spacing: 0.06em; text-transform: uppercase;",
    ),
    # .proj-desc : 0.8rem -> body
    (
        ".proj-desc { color: var(--muted); font-size: 0.8rem; max-width: 440px; }",
        ".proj-desc { color: var(--muted); font-size: var(--fs-body); max-width: 440px; }",
    ),
    # .footer : 0.68rem -> meta
    (
        "gap: 0.5rem; font-family: var(--mono); font-size: 0.68rem; color: var(--muted); }",
        "gap: 0.5rem; font-family: var(--mono); font-size: var(--fs-meta); color: var(--muted); }",
    ),
    # .quickstart .qs-title : 0.66rem (10.56px FAIL) -> meta, uppercase retire
    (
        ".quickstart .qs-title { display: block; color: var(--muted); font-size: 0.66rem; letter-spacing: 0.12em; text-transform: uppercase; margin-bottom: 0.35rem; font-weight: 600; }",
        ".quickstart .qs-title { display: block; color: var(--muted); font-size: var(--fs-meta); letter-spacing: 0.08em; margin-bottom: 0.35rem; font-weight: 600; }",
    ),
    # .quickstart code : 0.76rem -> body (contexte code : exempte, mais on harmonise)
    (
        ".quickstart code { background: var(--zebra); padding: 0.15rem 0.4rem; border-radius: 4px; border: 1px solid var(--hair); font-size: 0.76rem; }",
        ".quickstart code { background: var(--zebra); padding: 0.15rem 0.4rem; border-radius: 4px; border: 1px solid var(--hair); font-size: var(--fs-body); }",
    ),
    # h2 .count / .pct : 0.72rem -> meta (eviter le borderline 11.52px)
    (
        "h2 .count { font-family: var(--mono); font-size: 0.72rem; color: var(--muted); font-weight: 400; }",
        "h2 .count { font-family: var(--mono); font-size: var(--fs-meta); color: var(--muted); font-weight: 400; }",
    ),
    # .pct : 0.72rem -> meta
    (
        ".pct { font-family: var(--mono); font-size: 0.72rem; margin-left: 0.5rem; color: var(--muted); display: inline-block; min-width: 2.4rem; }",
        ".pct { font-family: var(--mono); font-size: var(--fs-meta); margin-left: 0.5rem; color: var(--muted); display: inline-block; min-width: 2.4rem; }",
    ),
    # index des mondes : S-x 0.68rem -> meta
    (
        "font-family:var(--mono);font-size:0.68rem;color:var(--muted);letter-spacing:0.14em;",
        "font-family:var(--mono);font-size:var(--fs-meta);color:var(--muted);letter-spacing:0.12em;",
    ),
    # index des mondes : tagline 0.78rem -> body
    (
        "color:var(--muted);font-size:0.78rem;font-style:italic;",
        "color:var(--muted);font-size:var(--fs-body);font-style:italic;",
    ),
    # --- Vague 2 : wide-tracking (gate Impeccable, 3 issues) ---
    # .over : tracking 0.14em sur texte sans uppercase -> 0.05em
    (
        ".over { font-family: var(--mono); font-size: var(--fs-meta); letter-spacing: 0.14em; color: var(--muted); }",
        ".over { font-family: var(--mono); font-size: var(--fs-meta); letter-spacing: 0.05em; color: var(--muted); }",
    ),
    # h2 .no : tracking 0.08em -> 0.05em
    (
        "h2 .no { font-family: var(--mono); font-size: 0.75rem; color: var(--muted); letter-spacing: 0.08em; }",
        "h2 .no { font-family: var(--mono); font-size: 0.75rem; color: var(--muted); letter-spacing: 0.05em; }",
    ),
    # .qs-title : tracking 0.08em -> 0.05em
    (
        ".quickstart .qs-title { display: block; color: var(--muted); font-size: var(--fs-meta); letter-spacing: 0.08em; margin-bottom: 0.35rem; font-weight: 600; }",
        ".quickstart .qs-title { display: block; color: var(--muted); font-size: var(--fs-meta); letter-spacing: 0.05em; margin-bottom: 0.35rem; font-weight: 600; }",
    ),
]


def main():
    if not GEN.is_file():
        print(f"ANCHOR NOT FOUND: generateur introuvable a {GEN}")
        return 1

    c = GEN.read_text(encoding="utf-8")
    original = c
    applied, missing = 0, []

    # 1. Tokens de rampe dans :root
    if ROOT_NEW in c:
        print("SKIP: rampe deja injectee dans :root.")
    elif ROOT_OLD in c:
        c = c.replace(ROOT_OLD, ROOT_NEW, 1)
        applied += 1
    else:
        missing.append(":root (bloc --sans)")

    # 2. Remplacements de rampe
    for old, new in RAMPS:
        if new in c:
            continue  # deja patche
        if old in c:
            c = c.replace(old, new, 1)
            applied += 1
        else:
            missing.append(old[:60] + "...")

    # 3. Unification : hauteur de ligne mini sur les tokens fonctionnels
    meta_rule = (
        "  /* R108 : plancher de lisibilite applique aux tokens fonctionnels. */\n"
        "  .badge, th, .stat-label, .ci-head, .qs-title, .footer { line-height: 1.35; }\n"
    )
    if meta_rule not in c and "  * { margin: 0; padding: 0; box-sizing: border-box; }" in c:
        c = c.replace(
            "  * { margin: 0; padding: 0; box-sizing: border-box; }",
            "  * { margin: 0; padding: 0; box-sizing: border-box; }\n" + meta_rule,
            1,
        )
        applied += 1

    if c != original:
        GEN.write_text(c, encoding="utf-8")
        print(f"PATCHED: {applied} modification(s) appliquee(s).")
    else:
        print("ALREADY PATCHED: aucune modification necessaire.")

    if missing:
        print(f"ATTENTION: {len(missing)} ancre(s) non trouvee(s) :")
        for m in missing:
            print(f"  - {m}")
        return 2

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
