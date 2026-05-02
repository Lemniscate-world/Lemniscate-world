# AGENTS.md - Kuro Rules (Compact Master)
# Full rules: ~/Documents/kuro-rules/rules/
# Last updated: 2026-04-29 | Rules: R1-R79

---

## STARTUP SEQUENCE (every session, in order)

1. Confirm aloud: "I have read AGENTS.md and will enforce all rules."
2. Classify project: client-requested | verified-problem | personal | startup
3. Check LINEAR: verify connection, pull pending tasks (R29, R36)
4. Check git: verify branch exists, never work on main (R30)
5. Read SESSION_SUMMARY.md if resuming ("on continue" = always read it first) (R73)

---

## ALWAYS-ON BEHAVIOUR (active every session, no trigger needed)

| Rule | Directive |
|------|-----------|
| R1   | Read this file first. Confirm to user. |
| R3.5 | Deadlines in hours/days only. MVP = 2-4 weeks, not months. |
| R7   | Never ignore failures. Report + retry. Ask if still failing. |
| R8   | Push back on bad ideas. Ask: Does it help users? Simpler way? What breaks? |
| R9   | Zero emojis. Anywhere. No exceptions. |
| R11  | Any rule change -> sync to ~/Documents/kuro-rules/ immediately. |
| R27  | Ask or detect persona (CEO / DevOps / Dev). Adapt depth and vocabulary. |
| R34  | Filter all tools (Linear, GitHub) to active project only. Ask if ambiguous. |
| R41  | UTF-8 only. No mojibake. Reject commits with encoding errors. |
| R61  | No glassmorphism, gradients, neon, particles, generic AI imagery. |
| R62  | Never commit PLAN.md, ROADMAP.md, PRD.md, ideas.md to public repo. |
| R65  | Instructor mode: decompose into 10 sub-tasks, explain What/Why/How for every new concept, just-in-time. |
| R66  | Windows first: test .exe formats via GH Actions. Always update sync_summary.py at session end. |
| R67  | KISS + Single Responsibility + Clean Code + Thin Interfaces. Refactor on friction. |
| R68  | Every project needs explicit visibility decision (public/private) documented in README. |
| R69  | Same as R21 - Intelligence Harvester at each milestone. 3+ external sources. |
| R70  | Landing page via v0.dev - use prompt template in rule_65_66_67_68_70_71_72.md. |
| R71  | "Cry Test" at session end: log % of users who would lose value if deleted. If 0% x3 -> STRATEGIC REVIEW. |
| R72  | All UI follows Impeccable Skitt design system (github.com/pbakaus/impeccable). |
---

## STARTUP PROJECT GATES (R2 applies; skip if client/verified/personal)

| Rule | Gate | Trigger |
|------|------|---------|
| R2   | Mom Test: 5 interviews OR equivalent before ANY prod code | Project classified as startup |
| R14  | Periodic validation (Mom Test + Marketing) | At 25/50/75/90/95% |
| R14.5| 5-risk failure mode table | Before first code |
| R20  | Hard lock: no code if milestone hit without VALIDATION_PASSED | Auto-check at each milestone |
| R48  | Market Gravity Test: Evidence Matrix + Scorecard | Before L2 |
| R49  | Adversarial Mom Test simulation | Before L2 |
| R57  | Activate parallel validation tracks | At L2 |
| R60  | PRD must exist before implementation | Before 25% |
| R63  | moat.md required | Before 50% |
| R64  | Negative Mom Test -> Deep Verification before declaring dead | On rejection |
| R77  | L2 validated -> auto-execute full distribution pipeline | On "L2 VALIDATED" in decision-memo.md |

---

## CODE QUALITY (trigger: any code written)

| Rule | Directive |
|------|-----------|
| R5   | Backend test coverage >= 60%. STOP new features if below. |
| R6   | Security scan before commit: bandit+safety (Py), cargo audit+clippy (Rust), npm audit (JS) |
| R18  | After any change: run full test suite. Fix regressions before new work. |
| R19  | SemVer tag at each milestone: vX.Y.Z-kuro |
| R38  | Code review (Qode/CodeRabbit/GitHub PR) AFTER commit, BEFORE continuing. |
| R46  | GUI/web bugs: follow Web-Debug-7 protocol (console->network->state->backend->DOM->auth->regression). 80% coverage before phase transition. |
| R54  | After every PR review: generate corrections list + one learning rule for the contributor. |
| R55  | PR author fixes their own code. Reviewer deposits feedback only. |
| R58  | Frontend/GUI coverage >= 90% (views, components, services). |
| R59  | Integration + E2E coverage >= 90% on critical flows. |

---

## SESSION LIFECYCLE

| Rule | Directive |
|------|-----------|
| R4   | SESSION_SUMMARY.md at end of every session (EN + FR). |
| R36  | Status report at START: branch, Linear tasks, progress %, blockers. |
| R42  | Never overwrite SESSION_SUMMARY.md history. Prepend only. |
| R43  | .docx backup at end of session (sync_summary.py). |
| R74  | New rules added this session? Sync to kuro-rules before closing. |
| R79  | Compact summary in SESSION_SUMMARY.md: <=150 words, plain language, EN+FR. |
---

## LINEAR & TEAM

| Rule | Directive |
|------|-----------|
| R25  | When working with DevOps/MLOps engineer: shift focus to infra, pipelines, reproducibility. |
| R26  | At each milestone: generate 5 DevOps/MLOps tasks -> Linear issues. |
| R28  | Assign tasks to DevOps engineer (penielteko02@gmail.com). Review their PRs. |
| R29  | Verify Linear connection at session start. Block work if unavailable. |
| R30  | Create branch before any work. Convention: scope/issue-id-description |
| R31  | Every Linear issue must include Codebase Context section (file map, entry point, key concepts). |
| R32  | Verify team stack at session start: Git, Linear, Python, pytest, bandit all configured. |
| R33  | Rule parity: all branches must carry current AGENTS.md. Only ceo/ branch can modify rules. |
| R35  | CEO tasks must be visible in Linear at all times. |
| R37  | Sync CEO activity to Linear at session end (rule-sync.yml). |
| R40  | Zero manual Linear updates. All via automation. |

---

## PLANNING & ROADMAP

| Rule | Directive |
|------|-----------|
| R3   | Progress = (Weight * Multiplier) - Penalties. Pessimistic. Never inflate. |
| R12  | PLAN.md or ROADMAP.md must exist. No code without a plan. |
| R13  | Roadmap minimum 4 weeks, weekly milestones. |
| R17  | Before phase transition: explain mechanism, 2nd/3rd order effects, teach 1 concept. |
| R22  | One feature per validation cycle. Depth over breadth. |

---

## RESEARCH & VALIDATION

| Rule | Directive |
|------|-----------|
| R15  | Rule files synced across all branches. |
| R21  | At each milestone: 3+ external sources, 2+ competitor complaints documented. |
| R23  | Pivot/failure -> post-mortem in kuro-rules/KNOWLEDGE_BASE/. |
| R39  | Before marketing: run Perplexity + Grok research. 5 signals, 2025-2026 sources. |
| R75  | Desk research = 5 dimensions: Personas, Competitors, Market Size, Risk, Gaps. |

---

## MARKETING & LAUNCH

| Rule | Directive |
|------|-----------|
| R16  | 2 working demos before each milestone. |
| R24  | Before launch: 3 communities ID'd, feedback channel live, templates drafted. |
| R44  | Research -> kuro-rules/MARKETING_MEMORY/ |
| R45  | Mom Test data -> kuro-rules/KNOWLEDGE_BASE/mom_tests/ |
| R47  | At each milestone: generate X/vlog draft for Build In Public. |
| R50  | Generate Google Doc summary block at session end. |
| R56  | Landing page via v0.dev prompt (docs/v0_landing_page_prompt.md). |

---

## SECURITY & GITIGNORE

| Rule | Directive |
|------|-----------|
| R10  | Protected files never committed: .env, mom_test_results.md, decision.md, PRD.md, PLAN.md |
| R76  | .gitignore must cover: *.pem, *.key, .env*, secrets/, data/, logs/, dist/ |

---

## PROFILE & VISIBILITY

| Rule | Directive |
|------|-----------|
| R51  | Update GitHub profile README with new project metrics at each milestone. |
| R52  | Update skill percentages in profile README. |
---

## LOAD ON DEMAND (full details in kuro-rules/rules/)

| File | Load when |
|------|-----------|
| rule_02_mom_test.md                                      | Startup project - Mom Test gate active |
| rule_03_progress.md                                      | Calculating progress % |
| rule_03_5_ai_time.md                                     | Proposing any deadline |
| rule_04_36_42_43_47_50_51_52.md                          | Session lifecycle - summary, backup, vlog, Google Doc |
| rule_05_06_18_19_38_58_59.md                             | Any code written - tests, security, coverage, versioning |
| rule_07_08_09_10_11_12_13_15_16_17.md                    | Core behaviour - failures, thinking, emojis, roadmap, demos |
| rule_14_5_failure_mode.md                                | Starting a new project |
| rule_14_73.md                                            | Milestone validation OR session resume |
| rule_20_21_22_23_24_25_26_27_29_31_32_33_34_35_37_40.md  | Linear, team, milestones, personas |
| rule_28_linear_review.md                                 | DevOps engineer submits PR |
| rule_30_branching.md                                     | Creating any branch |
| rule_39_41_44_45_54_55_60_61_62_63_74_76.md              | Marketing, encoding, security, PR policy, PRD, moat |
| rule_46_48_49.md                                         | GUI/web bug OR B2C validation OR Mom Test simulation |
| rule_56_57.md                                            | Landing page needed OR L2 validated |
| rule_64_mom_deep.md                                      | Negative Mom Test signals |
| rule_65_66_67_68_70_71_72.md                             | Pedagogy, code design, UI, repo visibility, Cry Test |
| rule_75_desk_research.md                                 | Running desk research |
| rule_77_79.md                                            | L2 VALIDATED in decision-memo.md OR writing SESSION_SUMMARY.md |
| rule_80_epingle.md                                       | Any project progress % changes |
| rule_81_research.md                                      | Before any feature/architecture decision |

---

---

## PORTFOLIO & SCIENCE (always-on)

| Rule | Directive |
|------|-----------|
| R80  | After any session changing a project % or status: update Epingle_Projets.md in kuro-rules/. -> rule_80_epingle.md |
| R81  | Before any feature/architecture decision: search arXiv/Semantic Scholar for relevant papers. Summarize in kuro-rules/RESEARCH_MEMORY/. -> rule_81_research.md |


## COMPLIANCE CHECK (when user asks "Did you follow AGENTS.md?")

Respond with one line per rule: [DONE / N/A / PENDING / VIOLATED]
Format: "R1: DONE | R2: N/A (client) | R5: DONE (67%) | ..."
Full compliance checklist in: kuro-rules/rules/COMPLIANCE_CHECKLIST.md
