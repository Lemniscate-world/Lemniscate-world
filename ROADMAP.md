# ROADMAP — Lemniscate-world
# Studio Portfolio & Architecture Hub

> Vitrine publique et registre temps reel des 60 projets et 15 mondes du studio lambda-Section.
> Synchronise automatiquement depuis l'activite Git reelle.

---

## 1. Vision & Architecture

Lemniscate-world sert de console centrale pour l'ensemble des initiatives du studio :
- **Portfolio Principal (`index.html`)** : Vue d'ensemble du registre, filtres multicriteres, suivi CI en direct, metriques globales.
- **Index des Mondes (`sections/`)** : Pages dediees pour chacune des 15 sections organisationnelles (AI, Quant, Biohacking, Fintech, etc.).
- **Journal & Blog (`blog/`)** : Flux d'actualites et rapports d'avancement factuels auto-generes.
- **Identite Visuelle** : Design "Quiet Precision" (R108) base sur une palette neutre chaleureuse, typographie soignee et densite d'information lisible.

---

## 2. Feuille de Route des Versions

### v1.0 — Socle & Registre Initial
- [x] Compilation statique multi-projets depuis `Epingle_Projets.md`.
- [x] Generation automatique des sous-sections organisationnelles `sections/s-*/`.
- [x] Integration de flux RSS et meta-tags SEO (OpenGraph, sitemap, robots.txt).
- [x] Panneau d'integration continue en direct depuis `ci-status.json`.

### v1.1 — Modernisation Visuelle & Quiet Precision (En cours)
- [x] Application du systeme de design R108 (Quiet Precision).
- [x] Elimination des bordures agressives et harmonisation des rayons de courbure (radius 6px).
- [x] Correction et stylisation complete du panneau d'integration continue (`.ci-box`).
- [x] Optimisation de la structure des blocs Quickstart.
- [ ] Integration du badge d'etat des audits hebdomadaires.
- [ ] Recherche instantanee amelioree avec filtres par section.

### v1.2 — Automatisation & Temps Reel
- [ ] Visualisation interactive des dependances inter-projets via graphe de donnees.
- [ ] Historique de velocite et graphiques de progression temporelle.
- [ ] Flux de syndication automatique vers les canaux communautaires.

---

## 3. Utilisation & Generation Locale

Le portfolio est auto-genere par le script dedie de `kuro-rules` :

```powershell
# Generation complete (index, sections, meta)
python ~/Documents/kuro-rules/scripts/generate_portfolio.py
```

Le detecteur de qualite UI Impeccable verifie la conformite des contrastes :
```bash
npx -y impeccable detect index.html sections/s-1/index.html
```

---

## 4. Licence
MIT License. © 2026 lambda-Section.
