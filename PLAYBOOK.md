# App Builder Community: Micro App Playbook (single file)
Built 2026-11-25 from the app-builder-community repository. Upload this one file to a Claude or ChatGPT project. Each section below is one file of the repository.


---

<!-- file: README.md -->
# App Builder Community: the Micro App Playbook

The complete, end to end method for building production micro apps with an AI assistant (Claude, ChatGPT or any co-work agent) on any **AI-friendly app builder**: a platform where the AI can edit, check, preview and publish an app, and the app can reach the business's own data and outside apps. It is written from a real build, **Ads Hub** (a live Meta ads, sales and webinar dashboard), and covers everything from an empty AI account to a published, shareable app.

Anyone can pick this up with no history: create a new project in their AI assistant, upload one file, and describe the app they want in one paragraph. The assistant discovers which data sources and connectors the app needs (through the platform and the **Connector Hub**), connects them with sign-in links the person opens, builds, verifies and publishes, the same way every time. See [doc 20](docs/20-one-prompt-to-app.md).

---

## Use it in 3 minutes

| You use | Do this |
|---|---|
| **Claude (claude.ai)** | Create a Project. Upload `PLAYBOOK.md` to Project knowledge. Paste `templates/project-instructions.md` into the Project's custom instructions. Add the connectors in `docs/02-connectors.md`. Start a chat with the prompt in `docs/19-prompts.md`. |
| **ChatGPT (Projects or agent mode)** | Create a Project, upload `PLAYBOOK.md` as a file, paste `templates/project-instructions.md` into the instructions, then the starter prompt. |
| **Any co-work / browser agent** | Give it `PLAYBOOK.md` and say "Read this, then follow the starter prompt." Agents without app builder tools use the browser steps in each doc. |
| **A developer** | Read the docs in order. `docs/18-case-study-ads-hub.md` shows every decision in a real app. |

`PLAYBOOK.md` is every file in `docs/` joined into one, so a single upload carries everything. GitHub rebuilds it on every push (or run `python3 scripts/build_playbook.py`).

---

## What is inside

| # | Doc | What it covers |
|---|---|---|
| 00 | [Start here](docs/00-start-here.md) | New AI account to first app: project, files, connectors, first prompt |
| 01 | [Platform and stack](docs/01-platform-and-stack.md) | The platform model, workspaces, link types, the stack, your private platform add-on |
| 02 | [Connectors](docs/02-connectors.md) | AI-side connectors (MCP), platform integrations, Connector Hub, which one does what |
| 03 | [Build workflow](docs/03-build-workflow.md) | The build round: ask, read, small edits, build check, look, hand over, publish |
| 04 | [Product planning](docs/04-product-planning.md) | Plan like a product manager; the feature checklist that defines "done" |
| 05 | [Data layer](docs/05-data-layer.md) | Workspace data, app data, forms, platform actions, outside apps, live events |
| 06 | [Meta Ads integration](docs/06-meta-ads-integration.md) | Reading ads, leads, purchases, creatives and the account log correctly |
| 07 | [Meta token runbook](docs/07-meta-token-runbook.md) | A never-expiring Meta system user token, step by step |
| 08 | [UI and UX design](docs/08-ui-ux-design.md) | Theme, components, states, motion, numbers, navigation, header |
| 09 | [Responsive and accessible](docs/09-responsive-and-accessibility.md) | Every device, every screen size, contrast, keyboard |
| 10 | [Sign-in and access](docs/10-auth-and-access.md) | Login screen, reset, admin, roles, who sees what |
| 11 | [No duplicates, clean data](docs/11-dedup-and-data-quality.md) | Every rule that stops double counting and double records |
| 12 | [Metadata, branding, sharing](docs/12-metadata-branding-sharing.md) | Name, description, logo, favicon, WhatsApp previews, domains |
| 13 | [Sync, speed, caching](docs/13-sync-performance-caching.md) | Auto sync, instant screens, rate limits |
| 14 | [Imports and exports](docs/14-imports-exports.md) | CSV upload, CSV download in a sandbox, copy fallbacks |
| 15 | [Verify and publish](docs/15-verify-and-publish.md) | Checks before hand over, publish approvals, rollback |
| 16 | [Security and house rules](docs/16-security-and-rules.md) | Tokens, secrets, masking, what the AI must never do |
| 17 | [Troubleshooting](docs/17-troubleshooting.md) | Every problem met so far and its fix |
| 18 | [Case study: Ads Hub](docs/18-case-study-ads-hub.md) | The real app, page by page, file by file, step by step |
| 19 | [Prompts](docs/19-prompts.md) | Starter prompt and ready prompts for each stage |
| 20 | [One prompt to a finished app](docs/20-one-prompt-to-app.md) | Describe the app in one paragraph; the AI discovers and connects every source through the Connector Hub, bridges phone-only data, builds and hands over |
| 21 | [Integration routes](docs/21-integration-routes.md) | Connector Hub first (sign-in redirect and back), direct API with server-side secrets, MCP for the AI; how to choose |

Templates: [project instructions](templates/project-instructions.md), [feature checklist](templates/feature-checklist.md), [hand-over note](templates/handover-template.md), [connector check](templates/connector-check.md).

---

## The ten rules that matter most

1. **Platform first.** If the platform already has the module or action, use it. App data only for what nothing else covers.
2. **Real data only.** Never type numbers into code, never show sample numbers as real.
3. **One small change at a time.** Read the file, change exactly what is asked, let the build check pass, then the next change.
4. **Every data block has four states:** loading, empty, error with retry, content.
5. **Mobile and desktop from the start**, checked at 375 px and 1440 px.
6. **Never count twice.** Deduplicate people by email or phone, take the largest of overlapping counts, never their sum.
7. **Never handle secrets in chat.** Tokens and passwords are typed by the owner into the right box, never pasted to the AI.
8. **Ask before changing anything in a connected app** (messages, posts, deletes, settings).
9. **Publish only when asked**, and always preview first.
10. **Hand over honestly:** what works, what data it uses, what is a placeholder, what is still open.

---

## Repository layout

```
app-builder-community/
  README.md                 this page
  CONTRIBUTING.md           how to improve the playbook
  CHANGELOG.md              what changed
  PLAYBOOK.md               all docs in one file (upload this one; rebuilt automatically on every push)
  docs/                     one topic per file, read in order
  templates/                project instructions, checklists, hand-over
  assets/                   example logo mark
  scripts/build_playbook.py rebuilds PLAYBOOK.md from docs/
  scripts/check_playbook.py fails on secrets, internal names and em dashes
  .github/workflows/        runs both on every push
```

## Your platform add-on

This repository is platform-neutral. To teach the AI your own platform's tool names, domains and settings, keep a small private add-on file (described at the end of `docs/01-platform-and-stack.md`) and upload it next to `PLAYBOOK.md`. Never commit it here.

## Contributing and licence

See [CONTRIBUTING.md](CONTRIBUTING.md) and [LICENSE](LICENSE). No passwords, tokens, keys, account ids or customer data belong in this repository; a check on every push enforces it.


---

<!-- file: templates/connector-check.md -->
# Connector check: <app>, <date, time>

| # | Check | Call | Result | Fix if not OK |
|---|---|---|---|---|
| 1 | App is live, which version, unpublished changes | **live status** | | Publish when asked |
| 2 | Which workspace each AI connector points to | **integration status** (look at the links it returns) | | Rename or use the right connector |
| 3 | Connector Hub apps the app uses are active | **list Connector Hub connections** | | Owner reconnects in the workspace's Connector Hub |
| 4 | Outside app answers | one tiny read, e.g. Meta **Insights** (`GET /{ad-account}/insights`) today, account level | | Token runbook / reconnect |
| 5 | Platform integrations the app uses; required apps missing | **integration status** | | Owner connects the app |
| 6 | Workspace data readable | one `count_only` query per object the app uses | | Approve in Publish / check role |
| 7 | Syncs still fresh (e.g. Zoom latest join) | latest row query | | Reconnect or use uploads |

Summary in plain words: what works, what does not, the one-line fix for each.


---

<!-- file: templates/feature-checklist.md -->
# Feature checklist: <app name>

The definition of done. Every line ends as: **Platform** (done with a platform module), **App data** (done with app.db), or **Gap** (platform cannot do it yet, closest option named).

## People and journeys

| Person | Signs in? | Main journey | Done? |
|---|---|---|---|
| <owner> | yes | | |
| <staff> | yes | | |
| <customer / visitor> | no | | |

## Features

| # | Feature | Source (Platform / App data / Connector Hub / Gap) | States (loading, empty, error) | Mobile | Done |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |

## Around every main action

| Action | Who is told, how | Reminder | Undo / cancel | Money | Approval | Owner sees later |
|---|---|---|---|---|---|---|
| | | | | | | |

## Data sources

| Data | Source | Spec / action name | Looked at real data? | Approval needed |
|---|---|---|---|---|
| | | | | |

## Before hand-over

- [ ] Build check passes
- [ ] Every journey walked; every action has waiting, success, error
- [ ] Every link checked
- [ ] Desktop and phone pictures; design issues empty
- [ ] One or two numbers compared with the source, same timezone
- [ ] No duplicates (people, counts, actions)
- [ ] Name, description, metadata set
- [ ] Hand-over written


---

<!-- file: templates/handover-template.md -->
# <App name>: handover

**Prepared:** <date, time, timezone>   **Owner:** <name>
No passwords, tokens or keys are in this file, on purpose.

## 1. What the app is
<two or three lines: who uses it, what it shows or does>

## 2. Ids, links, accounts
| What | Value |
|---|---|
| App name / id | |
| Workspace id | |
| Live link (users) | `<app-domain>/app/<slug>` |
| Editor / preview (team) | <team-domain>/<editor-path-for-the-app> |
| Live version | |
| Outside accounts (e.g. Meta business, ad account) | (masked in shared copies) |
| Variables | |

## 3. Connectors and status (date, time)
| Connector | Where | Status | Used for |
|---|---|---|---|

AI connectors needed in a new account, and which workspace each points to.

## 4. Structure
Navigation, pages, header, what each page shows.

## 5. Data flow
Each source (workspace data, app data, Connector Hub, platform actions), the files that read it, collections and access.

## 6. Rules to keep
House rules for this app (wording, defaults, privacy, approvals).

## 7. Open items and next steps
Numbered, each with who does it.

## 8. Key numbers for sanity checks
A few numbers with date and time, to confirm a new setup reads the same data.

## 9. Starter prompt for the next chat
```
<prompt>
```


---

<!-- file: templates/project-instructions.md -->
You build and maintain micro apps on an AI-friendly app builder. PLAYBOOK.md in this project is how we work: read it before acting and follow it.

EDIT ME: Owner: <name>. Workspace: <name / id>. Apps: <names / ids>.
EDIT ME: Team preview links on `<team-domain>`. User links on `<app-domain>` or <custom domain>.
EDIT ME: Timezone for date boundaries: <e.g. Asia/Kolkata>.

One-prompt mode: when I just describe an app, follow doc 20 of PLAYBOOK.md. Discover every data source through the platform and the Connector Hub (search by need and by provider, check connection status), classify each, show me the feature checklist and connection plan, connect with sign-in links I open myself, bridge phone-only data, then build, verify and hand over.

How to work:
- Every request is one round: note the ask on the app, read files before changing them, small exact edits that pass the last-read version, fix any failed build check, look at the app (desktop and phone) only at the end, then hand over in plain words.
- Audit before building. One change at a time.
- Platform first; workspace data for the business's numbers; app data only for what nothing else covers; outside services through Connector Hub.
- Real data only. Every data block has loading, empty, error and content states. Mobile and desktop from the start.
- Never count twice: dedupe people by email/phone, take the largest of overlapping counts.
- Workspace-data query shapes stay fixed so the app can be published; tell me when Publish needs my approval.
- Publish only when I ask, and show the preview first.
- Apps with a login open on the login screen. Dashboards open on Today.

Never:
- Ask for, show, copy or store tokens, passwords or keys. I paste secrets into the right box myself.
- Send, post, delete or change settings in a connected app without asking first (unless I asked for that exact change).
- Click Revoke/Remove/Delete in Meta, turn off security settings, or create fake admins.
- Call the Connector Hub by any other name, including the vendor name a tool may show.
- Use em dashes in anything written for me.

Hand-over: what works, which data it reads, placeholders, what is still open, what I must approve.
