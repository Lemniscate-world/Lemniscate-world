# DESIGN.md — lambda-Section portfolio

> Contexte design (R72 / R108 / Impeccable). Source de verite.
> Le detecteur `npx impeccable detect` est le gate — 0 issue obligatoire.

## Surface
brand (portfolio public et dashboard de pilotage).

## Direction retenue : **Quiet Precision** (R108.1 — remplace Ledger Brutal)
- Neutre chaleureux, dense mais respirant.
- Radius structurel : 6px sur conteneurs, cartes, filtres, badges et barres.
- Ombres douces en blur (`box-shadow: 0 1px 3px rgba(0,0,0,0.04), 0 1px 2px rgba(0,0,0,0.02)`).
- Bordures structurelles fines 1px (`--hair: #e5e3dc`).
- La couleur est reservee a la donnee uniquement (badges de statut et etats CI).
- Historique : Initié en "Ledger Brutal" (commit b5ad526 / 7488759 du 2026-08-21), puis unifié sous "Quiet Precision" (R108 du 2026-08-22) pour adoucir la rigidité sans perdre la sobriété éditoriale.

## Tokens (source : generate_portfolio.py)
| Token | Valeur | Usage |
|---|---|---|
| --paper | #faf9f6 | Fond principal (papier neutre chaleureux) |
| --surface | #ffffff | Cartes, conteneurs et panneaux isolés |
| --ink | #141312 | Texte principal (contraste élevé > 10:1) |
| --muted | #57534e | Métadonnées et labels secondaires (contraste ≥ 4.5:1) |
| --subtle | #78716c | Détails tertiaires et séparateurs discrets |
| --hair | #e5e3dc | Bordures 1px structurelles |
| --zebra | #f4f2ec | Zébrure de table et fonds secondaires |
| --hover | #eeece5 | États survol |
| serif | Georgia stack | Titres éditoriaux |
| mono | ui-monospace / Cascadia Mono | Chiffres, statuts, navigation, quickstart |
| sans | system stack / Segoe UI | Corps de texte et descriptions |

## Règles dures (Anti-AI Slop)
- Radius : 6px structurel (`border-radius: 6px`).
- Aucune border-left épaisse "side-tab" (interdite par R108.2, tell #1 détecté par Impeccable). Remplacée par bordure fine 1px ou ombre inset.
- Contraste AA 4.5:1 minimum obligatoire partout.
- Pas de gradients décoratifs, glassmorphism, néon, ou cartes imbriquées superflues (R61).
- Easing standard ≤ 180ms (`cubic-bezier(0.2, 0, 0, 1)`).

## Composants Clés
- Quickstart : Cartes 1px border avec radius 6px, titre discret, commandes copiables.
- Intégration Continue (`.ci-box`) : Panneau structuré sur fond blanc/surface, indicateurs de santé discrets.
- Tableau des Projets : Lignes zebra avec transitions douces, badges de statut tintés selon la donnée.

## Gate
`npx -y impeccable detect --no-config index.html sections/s-1/index.html` → 0 issue.

