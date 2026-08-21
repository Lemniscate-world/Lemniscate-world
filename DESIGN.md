# DESIGN.md — lambda-Section portfolio

> Contexte design (R72 / Impeccable). Source de vérité. Le détecteur `npx impeccable detect` est le gate — 0 issue obligatoire.

## Surface
brand (portfolio public).

## Direction retenue : **Ledger Brutal** (papier/encre)
Registre comptable éditorial : papier chaud, encre noire, hairlines, radius 0, zébrures.
Pourquoi : distinctif (anti dark-AI-slop), sérieux, lisible, imprimable. Validé par commit b5ad526.

## Tokens (source : CSS generate_portfolio.py)
| Token | Valeur |
|---|---|
| --paper | #faf9f5 |
| --ink | #161513 |
| --muted | #5f5b52 (≥4.5:1 sur paper et hover) |
| --hair | #d9d6cc |
| --zebra | #f1efe8 |
| --hover | #eae7dd |
| serif | Georgia stack (titres) |
| mono | ui-monospace/Cascadia (data, nav, colophon) |

## Règles dures
- radius: 0 partout (`border-radius: 0 !important`)
- contraste AA 4.5:1 minimum — vérifié par détecteur, pas à l'œil
- easing standard ≤160ms ; hover = bordure/couleur uniquement
- pas de gradients/glassmorphism/néon/emoji-tiles/cards-imbriquées (R61 + Impeccable)
- ligne ≤ 72ch corps

## Utilité avant crédibilité (règle maison)
Chaque page répond en <10s : Quoi → Prouvé comment → Je l'essaie comment.
Blocs quickstart copiables sur flagship (pip install neuraldbg / Releases LifeTrack).
Chiffres uniquement depuis TRUTH_DAILY / git log — jamais d'intentions.

## SEO/partage
og:image assets/og.png (1200x630, généré Pillow style Ledger depuis stats réelles),
twitter:card large, sitemap.xml + robots.txt auto, blog/feed.xml RSS.

## Gate
`npx -y impeccable detect --no-config index.html sections/s-1/index.html` → 0 low-contrast.
À intégrer en step CI non-bloquant puis bloquant après stabilisation.
