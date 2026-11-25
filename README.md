# Micro App Builder: the Micro App Playbook

The complete, end to end method for building production micro apps with an AI assistant (Claude, ChatGPT or any co-work agent) on any **AI-friendly app builder**: a platform where the AI can edit, check, preview and publish an app, and the app can reach the business's own data and outside apps. It is written from a real build, **Ads Hub** (a live Meta ads, sales and webinar dashboard), and covers everything from an empty AI account to a published, shareable app.

Anyone can pick this up with no history: create a new project in their AI assistant, upload one file, and describe the app they want in one paragraph. The assistant discovers which data sources and connectors the app needs (through the platform and the **Connector Hub**), connects them with sign-in links the person opens, builds, verifies and publishes, the same way every time. See [doc 20](docs/20-one-prompt-to-app.md).

---

## Before you start: create your account

This playbook needs a **sub-account** on a MyAppz-powered app builder. The sub-account is your business on the platform: its contacts, payments, forms, apps and connections all live there, and every app you build works inside it.

- **No account yet?** Ask the agency or partner who shared this link to create your sub-account and turn on the app builder for it.
- **Have one?** Sign in, open the app builder, and copy your two connector links (the app builder connector and your sub-account connector). Your AI needs both.

Without a sub-account an AI can still read this playbook, but it has nothing to build with.

## The one link to share

**https://github.com/myappz-ai/micro-app-builder/raw/main/App-Builder-Playbook.pdf**

It downloads the whole playbook as one PDF, always the latest version (rebuilt on every change). People read it; to build, they upload it to a Claude or ChatGPT project and describe the app. Coding agents that clone repositories can start at [AGENTS.md](AGENTS.md).

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
| 01 | [Platform and stack](docs/01-platform-and-stack.md) | The platform model, sub-accounts, link types, the stack, your private platform add-on |
| 02 | [Connectors](docs/02-connectors.md) | AI-side connectors (MCP), platform integrations, Connector Hub, which one does what |
| 03 | [Build workflow](docs/03-build-workflow.md) | The build round: ask, read, small edits, build check, look, hand over, publish |
| 04 | [Product planning](docs/04-product-planning.md) | Plan like a product manager; the feature checklist that defines "done" |
| 05 | [Data layer](docs/05-data-layer.md) | Sub-account data, app data, forms, platform actions, outside apps, live events |
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
micro-app-builder/
  README.md                 this page
  AGENTS.md                 where an AI agent starts
  llms.txt                  short index for AI tools
  CONTRIBUTING.md           how to improve the playbook
  CHANGELOG.md              what changed
  App-Builder-Playbook.pdf  everything in one PDF (the link to share; rebuilt on every push)
  PLAYBOOK.md               everything in one text file (same content, for agents)
  docs/                     one topic per file, read in order
  templates/                project instructions, checklists, hand-over
  assets/                   example logo mark
  scripts/build_playbook.py rebuilds PLAYBOOK.md from docs/
  scripts/build_pdf.py      rebuilds App-Builder-Playbook.pdf
  scripts/check_playbook.py fails on secrets, internal names and em dashes
  .github/workflows/        runs both on every push
```

## Your platform add-on

This repository is platform-neutral. To teach the AI your own platform's tool names, domains and settings, keep a small private add-on file (described at the end of `docs/01-platform-and-stack.md`) and upload it next to `PLAYBOOK.md`. Never commit it here.

## Contributing and licence

See [CONTRIBUTING.md](CONTRIBUTING.md) and [LICENSE](LICENSE). No passwords, tokens, keys, account ids or customer data belong in this repository; a check on every push enforces it.
