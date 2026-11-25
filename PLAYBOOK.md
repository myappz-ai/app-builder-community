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

<!-- file: docs/00-start-here.md -->
# 00. Start here: from a new AI account to your first app

This page assumes nothing. You have a fresh Claude (or ChatGPT) account and access to a workspace on your platform. By the end you have a project that knows this whole playbook and can build, fix and publish micro apps.

## What you need before you start

| Need | Why | Where to get it |
|---|---|---|
| A login to your app platform with access to the workspace the app will live in | The app, its data and its connections live in one workspace | Your agency or super admin |
| Owner or admin role in that workspace | Publishing, approving data reads and connecting apps need it | Ask the account owner |
| A Claude Pro/Team/Enterprise account (or ChatGPT with Projects) | Projects, files and connectors | claude.ai |
| The **app builder connector** URL for your account | Lets the AI read and edit app code, check it, preview and publish | Your platform team (see 02-connectors) |
| Optional: the Claude desktop app | Lets the AI use a browser on your computer (sign-in pages, Meta Business Settings) | claude.ai/download |

## Step 1. Create the project

1. In Claude, open **Projects** and click **New project**.
2. Name it after the app or the work, for example `Micro apps` or `Ads Hub`.
3. Upload **`PLAYBOOK.md`** to the project's knowledge. This one file is the whole playbook.
4. Open the project's **custom instructions** and paste everything in `templates/project-instructions.md`. Fill the lines marked `EDIT ME` (your name, your workspace, your link domains).
5. Optional but recommended: upload your **platform add-on** file (see `01-platform-and-stack.md`, last section) so the AI knows your platform's own tool names and settings.

## Step 2. Add the connectors

Go to **Settings, Connectors** and add the ones in `docs/02-connectors.md`. At minimum:

- **App builder connector** (essential): reads and edits app code, compiles, takes pictures, publishes.
- **Your workspace connector**: reads the account's data and integration status, and runs Connector Hub actions (Meta, Slack, Gmail and more).

Sign in to each one when Claude asks. Then, in a chat, ask:

> List my connectors and tell me which workspace each one points to.

This matters. Two connectors can have similar names and point at different workspaces. The check is in `docs/02-connectors.md`, section "Find out where a connector points".

## Step 3. Start the first chat

Either describe the app you want in one paragraph (one-prompt mode, `docs/20-one-prompt-to-app.md`), or paste the **starter prompt** from `docs/19-prompts.md`. It tells the AI to:

1. Read the playbook.
2. Check every connector and report, in plain words, what works.
3. Ask you what to build (or what to change), then follow the build workflow in `docs/03-build-workflow.md`.

## Step 4. Build in rounds

Every request is one **round**:

1. You say what you want in plain words.
2. The AI notes your ask on the app, reads the files it will change, makes small exact edits, and fixes anything the build check reports.
3. At the end it looks at the app (desktop and phone), fixes what looks wrong, and writes a short hand-over: what works, what data it uses, what is still open.
4. You check the **preview link** (always on the `<team-domain>` domain for the team).
5. When you are happy, say **"publish"**. The AI shows what will go live, then publishes.

## Step 5. Share it

- Give users the **live link** on the client-facing domain (`<app-domain>/app/<slug>` or your own domain).
- Set the app's name and description in the app's settings.
- For WhatsApp previews see `docs/12-metadata-branding-sharing.md`.

## If you are not using Claude

The same files work in ChatGPT Projects and co-work agents. Where a doc names a tool (for example the **preview screenshot** tool), an agent without that tool does the same step in the browser: open the preview link, look at the page, and report. Every doc says what the outcome must be, not only which tool to call.

## How to read the rest

Read 01 to 05 once; they explain the platform and the method. Then use the others as reference while building. `18-case-study-ads-hub.md` is the real example that ties it all together.


---

<!-- file: docs/01-platform-and-stack.md -->
# 01. The platform model and the stack

This playbook works on any **AI-friendly app builder**: a platform where an AI assistant can read and edit an app's code, check it, take a preview screenshot and publish it, and where the app can reach a business's own data and outside apps. Names below are generic. If your platform uses other names, keep a short private "platform add-on" file that maps them (see "Your platform add-on" at the end).

## The model in one picture

```
Platform
  └── Workspace  = ONE business: its own contacts, deals, payments, forms,
        │          staff, brand, domain and connections
        └── Apps
              ├── App data           the app's own store (collections)
              ├── App users          the app's own sign-in
              ├── Forms              leads into the workspace's real forms and CRM
              ├── Workspace data     live, read-only data of the business
              ├── Platform actions   book, add a contact, send a template, publish a page...
              └── Connector Hub      outside apps (ads, chat, email, files, payments...)
```

- A **workspace is one business**. An app always works for one workspace, with only its data. Never mix workspaces.
- People in a workspace: owner, admin, staff. An app also has its **own** users, separate from workspace users.

## Three kinds of link

| Link | For | Rule |
|---|---|---|
| **Editor / preview link** (`<team-domain>`) | The team building the app | Never sent to users |
| **Live link** (`<app-domain>/app/<slug>`) | Users | The one people bookmark; changing the slug breaks shared links |
| **Custom domain** | Users, branded | Connected in the app's settings with a DNS record; test it after verifying |

Never send app users to an editor or an admin dashboard.

## The stack this playbook assumes

Any modern stack works; these choices kept Ads Hub fast to build and easy for an AI to edit:

- React + TypeScript, Tailwind CSS.
- **shadcn/ui** for every control (select, calendar, dialog, sheet, table, tabs, tooltip, sidebar, toast). No native selects, date inputs or raw tables.
- lucide icons, recharts (inside a chart container), sonner toasts, a motion library for small transitions, date-fns, zod, react-hook-form, TanStack Table, react-day-picker.
- Folders: `src/components/` (one component per file), `src/pages/`, `src/lib/` (helpers and data providers).
- If your builder ships a component kit or block library, import it and never edit its files. Copy ("eject") a block into your own folder only when you must change it.

### Must-know wiring (shadcn)

- Wrap the app once in `<TooltipProvider>`.
- `<Sidebar>` only inside `<SidebarProvider>`.
- Render `<Toaster />` once, or toasts never show.
- Colours live in **one** place: the theme stylesheet (light and dark tokens). Never hard-code colours elsewhere.

## The app's backend, in neutral terms

Code samples in this playbook use this neutral pseudo-API. Map each line to your platform's real calls in your add-on file.

| Pseudo-API | What it does |
|---|---|
| `app.db.collection(name)` | The app's own store: insert, list, get, update, remove |
| `app.forms.submit(formId, answers)` | Sends a lead into the workspace's forms and CRM |
| `app.auth.signUp / signIn / signOut / user()` | The app's own users |
| `useWorkspaceQuery(spec)` / `app.workspace.query(spec)` | Live, read-only workspace data (payments, form entries, contacts, staff...) |
| `app.platform.run(action, args)` | A platform action (book, add contact, send template...) |
| `hub.read(action, args)` / `hub.change(action, args)` | A Connector Hub read or change in an outside app |
| `app.track(event)` | Analytics |

Every call can fail; show the platform's own error message to people as is.

## Variables and secrets

- **Public variables:** editable, non-secret values (an ad account id, a headline, a support email), read with a fallback in code.
- **Secrets:** keys and passwords, added by the owner only, readable only on the server. Never in browser code, never in a public variable, never in chat.

## Versions

Every save should create a version with a build check. Restoring an old version must be possible without touching what is live; the live link changes only when you publish.

## Your platform add-on

Keep one private file, for example `platforms/<your-platform>.md`, that lists:

- your domains for preview and live links;
- the real names of the builder tools (note the request, read files, edit, check, preview screenshot, hand over, publish, version history);
- the real names of the data calls (workspace data, app data, forms, platform actions, Connector Hub read and change, start a connection, connection status);
- where settings live (name, description, variables, secrets, permissions, domains, approvals).

Upload it to the same AI project as `PLAYBOOK.md`. The public playbook stays the same for everyone; the add-on teaches the AI your platform's words.


---

<!-- file: docs/02-connectors.md -->
# 02. Connectors: what connects to what

Three different kinds of connection are involved. Mixing them up is the most common source of confusion.

| Layer | Lives in | Used by | Examples |
|---|---|---|---|
| **AI connectors (MCP)** | Your AI account (Settings, Connectors) | The AI, while building | App builder connector, workspace connector, provider MCPs (ads, docs, GitHub), email, chat |
| **Platform integrations** | The workspace's settings | The platform and apps | Payment gateway, video meetings, email sending, WhatsApp Business, social pages, AI models |
| **Connector Hub** | The workspace's settings | Apps and the AI | Ads accounts, Slack, Gmail, Google Drive, Stripe, GitHub, CRMs... |

> Naming rule: always call it the **Connector Hub**. Some tool names and tool answers carry the name of the company behind a hub; never repeat that name to anyone. Say "Connect Meta", not "connect to <vendor>".

How an app integration should be done (Connector Hub, direct API or MCP) is in `21-integration-routes.md`.

## AI connectors to add

| Connector | Needed for | Priority |
|---|---|---|
| **App builder connector** | List apps, read and edit files, build check, preview screenshot, versions, variables, publish | Essential |
| **Workspace connector** (one per workspace) | Integration status, Connector Hub connections and reads, workspace data (payments, forms, contacts) | Essential |
| **Connector Hub manager** | Managing hub connections (list, add, set default) | Useful |
| Provider MCPs (ads platforms, developer tools) | Direct reads and diagnostics while building | Optional |
| Email, files, calendar, chat | General work around the project | Optional |

Add each in your AI account's connector settings with the server URL your platform gives you, then sign in. Never paste a key into chat to "add" a connector.

## Find out where a connector points

Connector names are chosen by people and can mislead. Before trusting one:

1. Ask it for the workspace's **integration status**. The links in the answer contain the workspace id and domain. That is the workspace it reads.
2. Ask it to **list Connector Hub connections**. "No key" means that workspace has no hub set up, so no outside apps can run there.
3. Compare with the app's workspace (shown in the app builder).

Real example: a connector named after one business pointed at a different workspace with no hub key, while a connector with a generic name was the app's real workspace. Rename connectors so the name matches where they point.

## Connector check (start of every new chat)

1. **Live status:** is the app live, which version, unpublished changes?
2. **Hub connections:** is every hub app the app uses active?
3. **One tiny read** from each outside app (for ads: today's spend at account level).
4. **Integration status:** platform integrations connected; any **required** one missing.
5. Report in plain words: what works, what does not, the one-line fix for each.

Template: `templates/connector-check.md`.

## Several connections of one app

One hub app (for example an ads account) can hold several connections. Usually **the newest becomes the default**, and apps use the default. Old ones (expired tokens) can be removed by the owner, but never remove the default.

## When a check fails

- "Hub not reachable" on a status check: usually a one-off. Check again before assuming anything is broken.
- "No key": set up the Connector Hub in that workspace's settings, or use the connector for the right workspace.
- Ads "login has expired" or OAuth error 190: the token expired. Follow `07-meta-token-runbook.md`.
- "Rate limited" or "too many requests": wait a minute; never retry in a loop.


---

<!-- file: docs/03-build-workflow.md -->
# 03. The build workflow: one round, every time

Every request, small or large, is one **round**. The round keeps the app safe, the history readable and the owner informed.

## The round

```
1. find the app        list apps (or create one)
2. note the ask        record the user's own words on the app, and which AI is working
3. read                list files, then read EVERY file you will change
4. change              a small exact edit, or write a new / fully replaced file
                       always pass the version you last read
5. build check         every save returns a new version and a check; a failure is the next job
6. look                preview screenshot at the END only (desktop, then phone, each journey)
7. fix                 what looks wrong; look again until no design issues are left
8. hand over           a short plain summary, always the last step, also when stopping early
9. publish             only when the user says so: preview first, then confirm
```

Good builders refuse changes until the request is noted for that app in this round; follow that even where the platform does not enforce it. A new request is a new round.

## Rules inside a round

- **Audit before building.** Read what exists before deciding what to change. Never write over a file you have not read.
- **One change at a time.** Small exact edits (replace one exact piece of text). Rewrite a whole file only when it is new or truly replaced.
- **The last-read version on every save.** If someone else changed the app, the save is refused and you read again. Nothing is overwritten silently.
- **A failed build check comes first.** Fix exactly what it names and save again. Never say "it works" while the check fails.
- **Pictures at the end, not during.** The preview screenshot is slow. Take it once the work is finished: walk each person's main journey, check the phone size where layout matters, fix every design issue, look again.
- **Behind a sign-in:** use a test user (for example an admin role that exists only in the screenshot) rather than a real account.
- **Links:** every link the app sends people to is checked with a **link check** in the same round.
- **Code belongs in files, not in chat.** Give the user the preview link.

## The hand-over note

Short, plain words. In this order:

1. What now works (screens, saved data, forms).
2. Which workspace data it reads.
3. Anything invented as a placeholder.
4. What is still open, and what the owner must do (approve a query, connect an app, publish).

Template: `templates/handover-template.md`.

## Publishing

- Publish **only when the user asks** in this conversation, never because work is finished.
- **live status** says what is live and whether there are unpublished changes.
- **publish** **without** confirm shows a preview (nothing changes). Show it, get a yes, then **publish** again with confirm.
- If the answer says workspace data needs approval, nothing went live: the owner approves the listed queries in the app builder's Publish screen, then you publish again.
- After publishing, open the live link and confirm the change is there.

## Rollback

**version history** shows history; **restore a version** brings an older version back as a new version. Publishing is separate, so a restore is safe to try in preview first.

## Working with someone else in the app

The owner (or another AI) may change the app between your rounds. That is why every round re-reads files and passes the last-read version. If a save is refused, read again, redo your change on the new text, and continue.

## When the AI has no app builder tools

Do the same steps in the app builder's editor: the **Code** tab to read and edit, **Versions** to go back, **Preview** to look, **Publish** to go live, **Settings** for name, description, variables, web address and permissions. The rules do not change.


---

<!-- file: docs/04-product-planning.md -->
# 04. Plan like a product manager

The person asking is usually a business owner, not a developer. They describe an idea in a few words and expect something real people can use tomorrow. Your job is to be the whole product team.

## Step 1. Explore what already exists

- From the request, list the jobs the app must do.
- For each job, search the platform's actions in plain words (**search platform actions**). Note what the platform already does.
- If the app shows the business's own numbers, look at the real data now: **list workspace data** (module), **describe a data object** (object fields, real values), **query workspace data** (one real answer).

## Step 2. Plan the product

1. **Who uses it**, and who must sign in. Who never does.
2. **Each person's journey**, from first visit to coming back.
3. **The bar:** which well-loved products already do this, and what makes them good (flows, few steps, how they handle mistakes). Meet that bar and beat it. Never copy their name, brand or text.
4. **Around every main action ask:** who needs to be told, and how? Does anyone need a reminder? Can it be changed, cancelled or undone? Does money move? Does someone approve it? What does the owner need to see later (lists, totals, reports, export)? Each "yes" is a feature.
5. **Where each feature lives**, in this order:
   1. the platform (default, so data lands in real modules),
   2. `app.db` only for data no module covers,
   3. a platform gap, said plainly, with the closest honest option.
6. Write it as a **feature checklist** (`templates/feature-checklist.md`). It is the definition of done.

Do not stall on a thin brief. Decide like an expert, state what you assumed, and continue. Ask only when a wrong guess would break the app or the business.

## Step 3. Backend before screens

Define every collection, connect forms, wire every platform action. Prove each with one real call (one read per data source, one preview per write). Fix failures before any screen depends on them.

## Step 4. Screens

Build every screen on data that already works: real copy, one design system, every state, mobile first, accessible. See `08-ui-ux-design.md` and `09-responsive-and-accessibility.md`.

## Step 5. Verify and hand over

Walk the checklist item by item. Each item is: done with a platform module, done with app data, or a named platform gap. See `15-verify-and-publish.md`.

## Standing decisions that save time

| Question | Default |
|---|---|
| Does the app open on a public page or the login? | **Login screen**, for any app with accounts |
| Default date range on dashboards | **Today** |
| Timezone for date boundaries | **The workspace's own timezone** (IST for Indian tenants), so numbers match the platform's dashboards |
| Where do settings the owner may change live? | Public variables, with a fallback in code |
| Outside services (Meta, Gmail, Slack) | Connector Hub through a **Connector Hub read**, connected or not; show a not-connected message until it is |
| The platform's built-in ads module | Only when the user explicitly asks for it |
| Sending messages from an app | Approved templates or workflows only, never an unofficial linked phone |
| Taking money | Payment links or invoices through platform actions; ask once if the request did not say |
| "Later" jobs (reminders, follow-ups) | Platform workflows, not app timers |


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
