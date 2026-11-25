# App Builder Community: Micro App Playbook (single file)
Built 2026-11-25 from the app-builder-community repository. Upload this one file to a Claude or ChatGPT project. Each section below is one file of the repository.


---

<!-- file: README.md -->
# App Builder Community: the Micro App Playbook

The complete, end to end method for building production micro apps with an AI assistant (Claude, ChatGPT or any co-work agent) on any **AI-friendly app builder**: a platform where the AI can edit, check, preview and publish an app, and the app can reach the business's own data and outside apps. It is written from a real build, **Ads Hub** (a live Meta ads, sales and webinar dashboard), and covers everything from an empty AI account to a published, shareable app.

Anyone can pick this up with no history: create a new project in their AI assistant, upload one file, and describe the app they want in one paragraph. The assistant discovers which data sources and connectors the app needs (through the platform and the **Connector Hub**), connects them with sign-in links the person opens, builds, verifies and publishes, the same way every time. See [doc 20](docs/20-one-prompt-to-app.md).

---

## Before you start: create your account

This playbook needs a **sub-account** on a MyAppz-powered app builder. The sub-account is your business on the platform: its contacts, payments, forms, apps and connections all live there, and every app you build works inside it.

- **No account yet?** Ask the agency or partner who shared this link to create your sub-account and turn on the app builder for it.
- **Have one?** Sign in, open the app builder, and copy your two connector links (the app builder connector and your sub-account connector). Your AI needs both.

Without a sub-account an AI can still read this playbook, but it has nothing to build with.

## Which link to use

| For | Use | Why |
|---|---|---|
| **People** | This page: `https://github.com/myappz-ai/app-builder-community` | Readable docs, templates and the change history |
| **AI agents** (Claude, ChatGPT, co-work agents) | `https://raw.githubusercontent.com/myappz-ai/app-builder-community/main/PLAYBOOK.md` | One plain-text file with everything; agents read it in one go |
| **Coding agents** that clone repositories | The whole repository; start with [AGENTS.md](AGENTS.md) | Keeps docs, templates and checks together |

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
app-builder-community/
  README.md                 this page
  AGENTS.md                 where an AI agent starts
  llms.txt                  short index for AI tools
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

<!-- file: docs/05-data-layer.md -->
# 05. The data layer

An app has five data sources. Pick the right one for each feature.

| Source | Read/write | Use for | Call |
|---|---|---|---|
| **Workspace data** | Read only, live | The business's real payments, form entries, contacts, deals, staff, Zoom attendance | `useWorkspaceQuery(spec)` |
| **App data** | Read and write | What people type into the app: calling lists, notes, uploads, saved settings, caches | `app.db.collection(name)` |
| **Forms** | Write | Leads that must land in the workspace's forms and CRM | `app.forms.submit(formId, answers)` |
| **Platform actions** | Read and write | Bookings, contacts, templates, sites, payment links, integration status | `app.platform.run(action, args)` |
| **Outside apps (Connector Hub)** | Read and write | Meta Ads, Slack, Gmail, Google Drive... | a **Connector Hub read** / a **Connector Hub change** |

## Workspace data (`useWorkspaceQuery`)

### Look first

Never guess an object or field name. While building: **list workspace data** → **describe a data object** → **query workspace data**. Use the exact names and values you saw. A wrong name answers "did you mean...": use the suggestion.

### The spec

```ts
{ metric: "revenue_received", filters: { product_name: { in: PRODUCTS } }, time_grain: "day", period: "last_30_days", limit: 100 }
{ object: "form_submissions", filters: { form_name: FORM }, count_only: true }
{ object: "zoom_attendance", fields: ["join_time"], order: { field: "created_at", dir: "desc" }, limit: 1, period: "last_90_days" }
```

- `filters`: `{ field: value }` or `{ field: { gt | gte | lt | lte | neq | in | contains | is } }`.
- `group_by` / `time_grain` for charts; `count_only` or a `metric` for number cards; small `limit` (10 to 25) for tables.
- `period` presets (`today`, `yesterday`, `last_7_days`, `last_30_days`, `this_month`, `last_month`, `this_year`) use the **workspace's timezone**.
- Sorting key is `dir`, never `direction`.
- **Money comes per currency** (`{ "INR": 250000 }`). Show each currency on its own, never add two together.

### Fixed shapes, so the app can be published

A published app runs only queries the owner approved. The **shape** of every spec is fixed at build time (object or metric, fields, which filter fields, group_by, order field). **Values** may change at run time (a picked filter value, search text, limit, period preset, time_grain, cursor).

- Right: specs as top-level `const`s, spread with a runtime `period`: `{ ...EVENT_REVENUE_DAILY, period }`.
- Wrong: `{ object: picked }`, `group_by: [picked]`, `filters: { [picked]: x }`.
- A custom date range (`{ from, to }`) cannot run in a published app. Use presets, then filter rows in the browser if needed (Ads Hub does this for custom ranges).
- New shapes need the owner's approval in the app builder's Publish screen. Tell them when that happens.

### Calm screens

- One `useWorkspaceQuery` per block, so one slow read never blocks the others.
- Skeleton only while `isLoading`; small "Updating..." while `isRefreshing`.
- On error show `error.message` with Retry, keep the last numbers. `NOT_APPROVED` and `UNPUBLISHED`: show the message, no Retry.
- Live updates without polling: `useWorkspaceQuery(spec, { live: ["payment.paid"] })`. Signals available: `booking.created`, `booking.cancelled`, `form.submitted`, `payment.paid`, `contact.created`.
- Workspace data answers only for a signed-in member of the workspace. A public visitor gets a clear message, never fake numbers.

## App data (`app.db`)

1. **define the collection** (name and access) **before** code uses it. Access:
   - `owner`: each person sees only their own rows (personal caches, bookings).
   - `public`: everyone in the app reads (a shared calling list).
   - `private`: builder side only.
2. Confirm with an **app data query** that saving works.
3. Keep documents small. For large lists, split into parts (Ads Hub stores Zoom attendees 250 per document as compact arrays).

## Platform actions

- Find with **search platform actions** in plain words; use only names it returned, written out in full.
- A platform action always resolves to one of: `done`, `pending_approval` (show "Waiting for approval", never "sent"), `needs_choice` (let the person pick), `refused` (show the words).
- Ask the person in the app first ("Book this slot?"), then run once per click. Never run twice to "confirm".
- No timeouts of your own around platform calls; show loading and the platform's error.
- Who can run: staff actions only for roles `admin` or `staff`; plain users only on their own rows.

## Outside apps (Connector Hub)

```ts
// read (runs at once for staff)
const r = await hub.read("<exact action name from the hub catalogue>", {
  ad_account: AD_ACCOUNT, level: "campaign", date_preset: "today", fields: ["spend"],
});
// change (the owner approves each change action by name in the app's permissions)
await hub.change("<exact action name>", { channel, text }, { summary: "Post today's ad summary to #growth" });
```

- Find exact action names and input fields while building (**search Connector Hub actions**). Never call the search from app code.
- Write the action name out in full; never build it from a variable, and never call delete, remove or archive actions in outside apps.
- Page big lists (20 rows or fewer per call), follow `next_cursor`, show a "Load more" button for long histories.
- Read page 1 first and show it, fetch the rest in parallel, keep results in memory.
- Not connected: show a calm not-connected message (ask the owner to connect it), no button, no link, no numbers.
- `RATE_LIMITED`: show the words, never retry in a loop.
- Every change is real, even in preview. Never run one to test.

## Connecting an outside app

- **Connection status** lists every connection (platform integrations and Connector Hub) with its status and a link to its settings card.
- **Start a connection** (for one app): preview first, then confirm on the person's yes. Hub apps return a sign-in link (redirect to the provider and back); platform integrations return their settings page.
- The person signs in on the provider's page. Then check the status again and run one tiny read.
- Full flow: `21-integration-routes.md`. Device-only data: `20-one-prompt-to-app.md`.

## Which source for which Ads Hub feature

| Feature | Source |
|---|---|
| Ad spend, leads, purchases, creatives, campaigns, account log | Connector Hub, Meta Ads |
| Money received, per day and product | Workspace data, `revenue_received` metric |
| Event registrations | Workspace data, `form_submissions` |
| Callers | Workspace data, `staff_members` |
| Zoom attendance sync | Workspace data, `zoom_attendance` |
| Calling list, call log, uploaded Zoom reports, screen cache | App data collections |
| Connector status | Platform actions **integration status**, **list Connector Hub connections** |
| Share to Slack | Connector Hub, a **Connector Hub change** |


---

<!-- file: docs/06-meta-ads-integration.md -->
# 06. Meta Ads integration, done right

Meta is the hardest data source in a marketing app: big answers, rate limits, overlapping action types, and tokens that expire. These are the rules Ads Hub learned.

## Connection

- Meta Ads is read through the **Connector Hub** (a **Connector Hub read**). The app uses whatever connection is the **default** (the newest).
- Use a **system user token that never expires** (`07-meta-token-runbook.md`). Personal user tokens expire every 60 days and the dashboard then shows "Meta's login has expired".
- Keep the ad account id and business id in **public variables** (`META_AD_ACCOUNT_ID`, `META_BUSINESS_ID`), read with a fallback. Ad account ids start with `act_`.

## The actions used

| Action | For | Key arguments |
|---|---|---|
| Meta **Insights** (`GET /{ad-account}/insights`) | Spend, impressions, clicks, leads, purchases, revenue | `object_id` (act_...), `level` (account, campaign, ad), `time_range {since, until}` or `date_preset`, `time_increment` (1 for daily, `all_days` for totals), `fields`, `filtering`, `limit`, `after` |
| Meta **Campaigns** (`GET /{ad-account}/campaigns`) | Campaign list with status and budget | `ad_account_id`, `fields: [id, name, objective, effective_status, daily_budget, start_time]` |
| Meta **Ad creative** (`GET /{ad-id}?fields=creative{...}`) | One ad's picture, headline, text, button | `object_id` (ad id), `fields: "creative.thumbnail_width(480).thumbnail_height(480){thumbnail_url,title,body,call_to_action_type}"` |
| Meta **Activities** (`GET /{ad-account}/activities`) | The account's change and billing log | `object_id`, `since`, `limit: 20`, `after`, fields incl. `translated_event_type`, `actor_name`, `extra_data` |
| Meta **Ad accounts** (`GET /me/adaccounts`) | Discover which ad accounts the token sees | `fields: id, name, currency, timezone_name` |

## Correctness rules

1. **Two passes, then merge.** Read spend, impressions and link clicks in one call (filtered to `spend > 0`), and `actions` plus `action_values` in a second call (filtered to the lead and purchase action types). Merge by `date + campaign_id` (or `ad_id`). A day with spend but no lead is never dropped, and each answer stays small.
2. **Leads are the largest, never the sum.** Meta reports the same lead under several action types (`lead`, `onsite_conversion.lead_grouped`, `offsite_conversion.fb_pixel_lead`, `leadgen_grouped`). Take the maximum. Same for purchases (`purchase`, `omni_purchase`, `offsite_conversion.fb_pixel_purchase`, `onsite_web_purchase`).
3. **Results = leads + purchases.** Cost per result = spend / results.
4. **Link clicks are `inline_link_clicks`**, not `clicks` (which counts every click on the ad).
5. **Budgets and billing amounts come in the smallest unit** (paise, cents). Divide `daily_budget` and activity log amounts by 100.
6. **Dates are the ad account's timezone.** `date_start` is the day in that timezone; compare with the workspace's timezone days.
7. **A shared ad account:** filter campaigns by name to the projects this app is for, and hide the rest. Example rule: a campaign name containing the event's short code is the event project; names containing the product or brand words are the product project; anything else belongs to another business and is never shown. Keep the words in one function (or a variable the owner can edit), and where possible push the filter to Meta (`campaign.name CONTAIN "<code>"`) so fewer rows come back.

## Speed and limits

- **Windows:** read long ranges as 7-day windows, at most **3 in parallel**.
- **Totals per ad** for a whole range use `time_increment: "all_days"` in one window, so an ad is not split.
- **Shrinking pages:** start at 50 rows. If the answer is cut (`preview: true`, or `shown < total`, or a note like "Showing 96 of the 100"), halve the page size and ask again, down to 5. On a timeout retry the page smaller up to 3 times.
- **Final errors stop at once:** not connected, rate limited, not approved, role not allowed, signed out, bad args, expired token (OAuth 190). Never retry those.
- **Cache finished days:** a range that ends before today never changes, keep it in memory. Today is always read again.
- **Creatives one at a time:** reading one ad per call keeps picture links whole. Cache the cards so they stay visible when Meta is slow.
- **Account log:** 20 events per page, newest first, "Load more" per click, never a loop.
- **"All time"** starts at the project's first campaign start date, so Meta is not asked about empty months.

## What the screens show

- KPI cards: ad spend, results, cost per result, link clicks (with CTR), money received, return on ad spend, leads, active campaigns.
- "What needs attention": campaigns over a spend threshold with no results, or over 2x the average cost per result.
- Campaigns table: Running now / With spend / All, tap a row for day by day numbers.
- Creatives grid: 3 per row on desktop, picture, headline, text, spend, results, cost per result, CTR, Ads Manager link.
- Daily log: one row per day plus "Copy for WhatsApp".

## When Meta is not available

- Not connected: the kit's not-connected text, no numbers (a dash), no fake zeros.
- Read failed with saved numbers on screen: keep them and say "Couldn't refresh from Meta (reason). Showing the numbers from 3:39 pm."
- Rate limited: say "Meta limits how often the app can ask. Wait a minute and press Sync now."


---

<!-- file: docs/07-meta-token-runbook.md -->
# 07. Meta token runbook: a token that never expires

Use this when a dashboard says "Meta's login has expired", or when connecting Meta Ads to a new workspace. It can be followed by a person, or pasted into a browser-capable AI agent that does every click while the person only signs in, clicks Generate and Copy, and pastes into one box.

Background: personal Meta user tokens expire every 60 days. A **system user token** with expiry set to **Never**, made from an app that has the **Create & manage ads with Marketing API** use case, does not. Apps made for other use cases (for example an Instant Game app) can never be used and cause "No permissions available".


**How to use this file:** paste this whole file into an AI agent that can use a web browser (Claude with the browser or computer use, ChatGPT agent mode, a co‑work agent, etc.) and say **"Do this for me."** The agent does every step. You only:

1. **Log in** when a page asks (Facebook / the platform).
2. Click **Generate token** and **Copy** when the agent asks.
3. **Paste** the token into one box when the agent asks.

Takes about 10 minutes. You do it once; the token never expires.

---

## 0. Instructions for the AI agent (read fully before acting)

You are connecting a business's Meta (Facebook) ad account to its dashboard with an access token that **never expires**. Work in the user's own browser, where they are signed in to Facebook and to the platform. Do every click yourself, check each result, and only stop for the four hand-offs listed in **0.2**.

### 0.1 Values to collect first (ask the user only what you can't find)

| Name | How to get it |
|---|---|
| `BUSINESS_NAME` | Ask: *"Which Meta business portfolio owns the ad account?"* |
| `AD_ACCOUNT_NAME` | Ask: *"Which ad account should the dashboard read?"* |
| `BUSINESS_ID` | Find it yourself: open https://business.facebook.com/settings/system-users, pick `BUSINESS_NAME` in Meta's business picker, and read `business_id=` from the address bar |
| `APP_NAME` | Use **Ads Connector**, unless the user prefers another name |
| `SYSTEM_USER` | Whichever system user already exists on the System users page; if none, create one called **Connector Hub** (role Admin) |
| `PLATFORM_URL` | Your platform's admin link (the user logs in). The Connector Hub is in the workspace's settings |
| `DASHBOARD` | Ask the user which dashboard/app to check at the end, or open it from the platform after login |

Keep these values only in your working memory for this task. Don't repeat IDs or names back to the user more than needed, and never put them in files you create.

### 0.2 Hand-offs (the only times you stop and ask the user)

1. **Login / password / 2-factor code**: any login or "re-enter your password" screen. Say: *"Please sign in on the open page, then tell me 'done'."* Never ask for, read, or type a password or code.
2. **Second-admin approval** (only if Meta shows it: see step 5).
3. **Generate + Copy**: in step 5, after you have selected everything, say: *"Click the blue **Generate token** button, then click **Copy**. Don't paste it in this chat."*
4. **Paste**: in step 6, when the small window with the **Access Token** box is open, say: *"Click the Access Token box, press Ctrl+V (Mac: Cmd+V), then click **Connect Account**. Tell me 'done'."*

### 0.3 Safety rules (always)

- **Never** ask the user to paste the token into the chat. Never read it aloud, copy it, store it, screenshot it, or type it yourself.
- **Never** click **Revoke tokens**, **Remove**, **Delete**, or change anything not listed here.
- **Never** remove other people, apps, ad accounts, or other Connector Hub apps.
- Do not turn off security settings.
- If a screen doesn't match what's described, take a screenshot, describe it to the user in one line, and ask before going on.
- Meta pages load slowly. Wait 2–4 seconds after each click before reading the page.
- **Every Business Settings link must contain `?business_id=BUSINESS_ID`.** Without it Meta shows "Sorry, this content isn't available" or a business picker.

---

## 1. Check access (1 minute)

1. Open `https://business.facebook.com/latest/settings/business_users?business_id=BUSINESS_ID`.
   - Login page → hand-off 1.
2. Find the user's own row (marked **(you)**). It must say **Full access · Everything**.
   - If not, stop and tell the user: *"You need full control of BUSINESS_NAME. Ask an admin to give it to you in Business Settings → People."*
3. Note the other people with **Full access** and recent "Last active" dates. You may need one of them in step 5.

## 2. Create the ads app (3 minutes)

**First check whether a suitable app already exists:**

1. Open https://developers.facebook.com/apps/ and look for `APP_NAME` (or any app owned by `BUSINESS_NAME`).
2. If one exists, open it → **Use cases**.
   - If it lists **"Create & manage ads with Marketing API"**, reuse it and skip to step 3.
   - Apps made for something else can **never** be used. For example, "Launch an Instant Game" or "Authenticate … with Facebook Login": they produce the **"No permissions available"** error, and ads use cases can't be added to them.

**Create the app:**

1. Open https://developers.facebook.com/apps/creation/.
   - An intro pop-up "There's a new way to create apps" may appear. Its **Create app** button only closes it.
2. **App details:**
   - **App name** = `APP_NAME`.
   - Leave the email as it is.
   - Click **Next**.
3. **Use cases:**
   - Tick **Create & manage ads with Marketing API**. It's the first card; the tick is on the right.
   - Other cards turning grey is expected.
   - Click **Next**.
4. **Business:** select `BUSINESS_NAME` → **Next**.
5. **Requirements:** **Next**. It normally says "No requirements".
6. **Overview:** check it shows `APP_NAME`, the Marketing API use case and `BUSINESS_NAME` → click **Create app**.
   - Password prompt → hand-off 1.
7. You land on the app dashboard. The address is `developers.facebook.com/apps/<APP_ID>/dashboard/…`. Note `APP_ID`.
8. **Verify:** click **Customize the Create & manage ads with Marketing API use case**. These three must show **"Ready for testing"** (or "Advanced access"):
   - `ads_management`
   - `ads_read`
   - `business_management`

   If any shows **Add**, click **Add** for it.

## 3. Give the system user the app (1 minute)

1. Open `https://business.facebook.com/latest/settings/system_users?business_id=BUSINESS_ID`.
   - If there is **no system user**:
     1. Click **+ Add**.
     2. Name: **Connector Hub**. Role: **Admin**.
     3. Click **Create**. If Meta asks for approval, use the step 5 approval flow.
   - Use that system user's name as `SYSTEM_USER` below.
2. Open `https://business.facebook.com/latest/settings/apps?business_id=BUSINESS_ID` and click `APP_NAME` in the list.
3. Click **Assign people**.
4. In the dialog:
   1. Type part of `SYSTEM_USER` in the search box and tick it.
   2. On the right, under **Full access**, switch on **Manage app**.
   3. Click **Assign**, then **Done**.
5. **Verify:** the app's **People** list now shows `SYSTEM_USER` with Full access.
   - If not, repeat; the Assign didn't save.

## 4. Give the system user the ad account (1 minute)

1. Open `https://business.facebook.com/latest/settings/system_users?business_id=BUSINESS_ID` and select `SYSTEM_USER`.
2. Scroll the right panel to **Ad accounts**. If `AD_ACCOUNT_NAME` is already listed with Full access, skip to step 5.
3. Otherwise:
   1. Click **⋯** (next to Revoke tokens).
   2. Click **Assign assets**.
   3. On the left, click **Ad accounts**.
4. In the dialog:
   1. Tick `AD_ACCOUNT_NAME`.
   2. Under **Full access**, switch on **Manage ad accounts**.
   3. Click **Assign assets**, then **Done**.
5. **Verify:** the system user's **Ad accounts** section lists `AD_ACCOUNT_NAME`, and its **Apps** section lists `APP_NAME` with Full access.

## 5. Make the never-expiring token (2 minutes)

1. On the same System users page with `SYSTEM_USER` selected, click **Generate token** (top right of the panel).
2. Work through the dialog:
   1. **Select app:** open the list and choose **`APP_NAME`**, not any older app. Click **Next**.
   2. **Token expiry:** choose **Never**. Click **Next**.
   3. **Assign permissions:** open **Select permissions** and tick `ads_management`, `ads_read` and `business_management`. It should say "3 options selected".
3. **Stop → hand-off 3.** The user clicks **Generate token**, then **Copy**. Meta shows the token only once; suggest they also save it in a password manager.

**If Meta says "this request must be approved by another admin":**

- This is Meta's rule for businesses with heightened security, and it **cannot be turned off**. Do not create extra admins to get around it.
- Give the user this message to forward to one full-access admin from step 1:

  > Hi, please approve my request to generate an access token in Meta Business Suite (BUSINESS_NAME). It's in your Facebook / Business Suite notifications (or email from Meta). Check it says system user "SYSTEM_USER" and app "APP_NAME", then tap Approve. Thanks!

- When the user says it's approved:
  1. Reload the System users page and select `SYSTEM_USER`.
  2. A green box **"Access token generation approved"** appears with a **Generate token** button.
  3. Hand-off 3: the user clicks that button, then **Copy**.
  4. If it asks for app, expiry and permissions again, choose the same as above.

**If you see "No permissions available":**

- The selected app has no ads use case → go back and pick `APP_NAME`.
- Still empty → step 2's verify or step 3 was not done. Fix that, close the dialog, and try again.

## 6. Put the token into Connector Hub (2 minutes)

1. Open `PLATFORM_URL` (login → hand-off 1), then open the workspace's **Connector Hub** settings.
2. In **Search your apps**, type **Meta Ads**. If a **Meta Ads** card shows under **Connected**, click **Disconnect** on it.
   - This only switches the old (expired) connection off for this page.
   - Without this step, the new token can't be added.
3. In **Search all apps** (lower on the page), type **Meta Ads**. Point at the **Meta Ads** card and click **Connect**.
   - A small window opens with an **Access Token** box. It may open in a new tab.
   - **If your browser blocks pop-ups**, ask the user: *"Please click the green **Connect** button on the Meta Ads card yourself."*
4. **Hand-off 4:** the user pastes the token into **Access Token** and clicks **Connect Account**.
5. Back on the Connector Hub tab, click **I've connected it** (the button that replaced "Check connections").
6. **Verify:** the page says **"Meta Ads connected"**, and the **Meta Ads** card is back under **Connected** with **Active**.
   - If not, wait 10 seconds and click **Check connections**.

## 7. Check the dashboard (1 minute)

1. Open `DASHBOARD` (login → hand-off 1).
2. Click **Sync now** (top right) and wait about 20 seconds.
3. **Done when:**
   - The orange note **"Meta's login has expired"** is gone.
   - The top bar shows **Synced <time>** with a green dot.
   - **Ad spend** shows today's amount.
   - **Creatives** loads ad cards.
4. Tell the user: *"Connected with a token that never expires. Nothing else to do. Keep the token in your password manager; if it ever leaks, an admin can click **Revoke tokens** on the system user and we redo steps 5–6."*

---

## Troubleshooting

| What you see | What it means | Do this |
|---|---|---|
| "Sorry, this content isn't available" on business.facebook.com | Link is missing `business_id` | Add `?business_id=BUSINESS_ID` to the link |
| "No permissions available" when generating the token | Wrong app, or app has no Marketing API use case | Pick `APP_NAME`; check step 2 verify and step 3 |
| "Must be approved by another admin" | Meta security rule for this business | Forward the step 5 message to another full-access admin |
| "Generate token" is grey or missing | User is not an admin of the business | An admin gives them **Full control** in People |
| Dashboard: "Meta's login has expired" | The connected token has an end date or was revoked | Redo steps 5–6 with **Never** |
| Dashboard: "Meta Ads is switched off" or "not connected" | Meta Ads was disconnected in Connector Hub | Step 6.3–6.6 (Connect → paste → I've connected it) |
| Dashboard shows ₹0 / no ads, no error | System user can't see the ad account | Step 4, then redo steps 5–6 |
| Create app asks to verify the business | Wrong business picked | Pick the one marked "Business verification complete" |
| Clicking Connect does nothing | Pop-up blocked | User clicks **Connect** themselves, or allow pop-ups |

## If you (the agent) have no browser

Walk the user through these steps one at a time. Give each link as a clickable link, say exactly which button to click, and wait for "done" before the next step. Keep messages to 2–3 lines.


---

<!-- file: docs/08-ui-ux-design.md -->
# 08. UI and UX design

The bar: an app people would pay for, not a template. For a work app (dashboards, lists, forms) the work comes first: clear navigation, every state, small useful motion.

## Look and theme

- **One place for colour:** `src/index.css`, light in `:root`, dark in `.dark`. Start from a preset in `src/themes/` (neutral, signature, universe, corporate, editorial, bold, soft, night) and adjust tokens. Never put colours anywhere else; use tokens like `bg-background`, `text-muted-foreground`, `border`, `bg-primary`.
- **Pick a direction for this business** and commit: type pairing, palette (one dominant family, one accent doing real work), spacing rhythm, one signature element.
- Avoid the AI-default looks: cream + serif + terracotta, near-black + acid accent, reflex indigo/violet.
- Ads Hub: the "signature" preset. Plum primary `#7A2E5C`, gold accent `#F2A93B`, dark ink `#1A1620` for bands, Space Grotesk headings and numbers, Inter body, 16 px radius, 24 px cards.

## Components

- **shadcn/ui only.** Select, Calendar, Popover, Dialog, Sheet, Table, Tabs, Tooltip, Sidebar, Toggle group, Badge, Skeleton, Sonner. Never native selects, date inputs or raw tables; the build check refuses them.
- `Command` only inside a Popover or Dialog, never open in the page.
- **Ready blocks first** (the kit's ~200 blocks and 21 screens), your own components for the rest, eject a block only to change it.
- Icons: lucide-react. No emoji in the UI.

## Every data block has four states

1. **Loading:** a skeleton, at most about 8 seconds, then the error state. Never an endless spinner.
2. **Empty:** one friendly sentence and the next step ("No sessions yet. Upload the Zoom report after the webinar.").
3. **Error:** the platform's own words and a Try again. Keep the last numbers on screen if there are any.
4. **Content.**

## Numbers

- Compact money per currency on cards (`₹65.8K`, `₹2.07 Cr`, `$4.96M`), full value underneath in small text.
- Never a number that cannot be right (a rate over 100%, a negative count). Check the maths or leave it out.
- Never ₹0 or an empty chart when the truth is "not connected" or "failed". Show a dash and the reason.
- Never add two currencies together.
- Tabular numbers (`tabular-nums`) where numbers change in place.

## Navigation and layout (Ads Hub pattern)

- **Sidebar** with grouped navigation (Performance, Ads, Setup), collapsible to icons, a sheet on phones.
- A **badge** on the Connectors item when something needs attention.
- **Sticky header:** current page title, project tag, **date range picker defaulting to Today**, sync status and Sync now, dark mode toggle.
- A thin progress bar under the header while fresh numbers load in the background.
- Hash routes (`#/overview`) so links and back/forward work; old links redirect after pages merge (`#/event` → `#/bf`).
- Merge thin pages into tabs on one page rather than many near-empty pages.

## Feedback and motion

- Every action shows busy, success and error states. Toasts for results (`sonner`), with an action button where useful ("Copy").
- Page entrances `animate-in fade-in slide-in-from-bottom-2`; transform and opacity only; respect `prefers-reduced-motion`.
- No remount on refresh: what is on screen stays while new numbers load.
- Show save state ("Saving...", "Saved") and ask before leaving unsaved changes.

## Lists and tables

Search, status chips, sort, clickable rows, one "..." menu per row. Long names truncate with the full text in a tooltip. Wide tables scroll inside their own box. Export to CSV where the owner needs it (`14-imports-exports.md`).

## Copy

Plain words, written for this business. Say what the thing does and what to do next. No jargon, no internal tool or vendor names (always "Connector Hub"). No em dashes in materials written for the owner.

## The design check after every look

1. Spacing rhythm on a 4/8 px scale; equal gaps in a row.
2. Padding p-4 to p-6 in cards; no text near an edge.
3. Nothing cut off; no short label broken onto two lines; big numbers fit their card.
4. Contrast at least 4.5:1, also on hover and focus.
5. Dark mode reads well everywhere.
6. Every data block has its four states.
7. Motion alive but calm.
8. Phone width: nothing scrolls sideways, nothing overlaps.


---

<!-- file: docs/09-responsive-and-accessibility.md -->
# 09. Responsive on every device, accessible to everyone

Build for phone and desktop from the first line, not at the end.

## The widths that must work

| Width | Device | Check |
|---|---|---|
| 375 px | Phone | Everything stacks, no sideways scroll, touch targets 44 px |
| 768 px | Tablet | Two columns where it helps, sidebar as a sheet or icons |
| 1280 to 1440 px | Laptop, desktop | Full layout, max content width (Ads Hub: 1400 px) |

Verify at the end of the work with a phone-size and a desktop preview screenshot, and in a browser's device view.

## Layout rules

- **Fluid containers:** `max-w-[1400px] mx-auto`, padding `p-3 sm:p-5 lg:p-7`.
- **Grids collapse:** `grid gap-3 md:grid-cols-2 lg:grid-cols-4` for KPI cards; creatives 1 column on phone, 3 per row on desktop.
- **Header wraps:** `flex flex-wrap items-center justify-between gap-2`; less important text hidden on small screens (`hidden sm:inline`).
- **Sidebar** collapses to icons on desktop and becomes a sheet on phones; close it after a tap (`setOpenMobile(false)`).
- **Popovers fit the screen:** width `min(100vw - 1.5rem, 31rem)`, `max-h-[calc(100dvh-5rem)] overflow-y-auto`, `collisionPadding`. The date picker's presets become a 4-column grid on phones and a side list on desktop.
- **Tables** scroll inside their own box (`overflow-x-auto`), never the page.
- **Text** truncates with a title, never pushes the layout wider. `min-w-0` on flex children that hold text.
- Heights with `dvh`, never `vh` for full-screen roots on phones.
- **Sign-in split screen:** brand panel beside the form on desktop, a compact brand bar on top on phones.

## Accessibility

- Real elements: `<button>`, `<a href>`, `<form>`, `<label>` + input. Never click handlers on a div.
- `aria-label` on icon-only buttons ("Toggle dark mode", "Sync now", "Open menu").
- Progress indicators with `role="progressbar"` and a label while active; `role="status"` and `aria-live="polite"` on loading screens.
- Contrast 4.5:1 for text, 3:1 for large text and UI parts, also in dark mode and on hover.
- Colours that must be told apart also differ in lightness, not only hue.
- Keyboard: Tab reaches everything, Enter submits forms, focus lands on the first field of a form.
- Sign-in fields with `autocomplete="email"`, `current-password` and `new-password`, so browsers and password managers save logins.
- Respect `prefers-reduced-motion` (`motion-reduce:animate-none`, `motion-safe:`).

## The sandbox

Apps run inside a sandboxed frame. That affects:

- **Downloads:** a normal download link is blocked; see `14-imports-exports.md`.
- **Navigation:** open platform pages (a booking page, a payment link) in a new tab with `target="_blank" rel="noopener"`, never in the app frame.
- **Clipboard:** use a hidden textarea and `document.execCommand("copy")` first, then the Clipboard API.
- **Storage:** `localStorage` may be off; wrap every read and write in try/catch.


---

<!-- file: docs/10-auth-and-access.md -->
# 10. Sign-in and access

## The app opens on its login screen

Any app with accounts opens on the **login screen**, never a public page. On every load check `app.auth.user()` first and go straight in if the person is already signed in. Never make someone sign in again because they came back.

## The pieces (all ready-made, never hand-built)

| Need | Use |
|---|---|
| Email sign-in / sign-up screen | The kit's `signin-split` block (eject it to customise copy and points) |
| Forgot password | `ForgotPasswordForm` from `@/components/auth/ForgotPasswordForm` |
| Reset from the email link | `ResetPasswordForm` when `app.auth.resetToken()` returns a token |
| WhatsApp code sign-in | `WhatsAppSignIn` when `app.auth.methods()` says WhatsApp is on (the platform default for new apps) |
| Loading screen while checking | A small branded preloader with `role="status"` |

## The Ads Hub auth gate (pattern)

```tsx
const BRAND = { appName: "Ads Hub", tagline: "Know which ads bring in money.", google: false, password: true, allowSignup: true };

export function AuthGate({ children }) {
  const [user, setUser] = useState(undefined);            // undefined = still checking
  const [mode, setMode] = useState(() => app.auth.resetToken() ? "reset" : "signin");
  useEffect(() => { app.auth.user().then(u => setUser(u ?? null)).catch(() => setUser(null)); }, []);
  if (user === undefined) return <Preloader />;
  if (user) return children(user, async () => { await app.auth.signOut(); setUser(null); });
  // reset or forgot screens, else the split sign-in wired to app.auth.signIn / signUp
}
```

Rules:

- One call per button: sign-up form calls `signUp`, sign-in calls `signIn`. Never chain them to hide an error.
- Show the error text as is ("The password must be 8 to 72 characters.").
- After success, move off the form with `history.pushState` so the browser offers to save the password.
- Busy state on the button, show/hide password, Enter submits, focus on the first field.
- Never write a password, admin login or key into code. Browser code is public.

## The app's admin

An app with sign-in gets **one admin**: its first person. Ask the owner once which email the admin uses, then **create the app admin**. Never repeat or store the password. Others who sign up are normal users; the owner gives roles in the app's Dashboard, Users.

## Who sees what

- **Staff screens** check `(await app.auth.user())?.role === "admin"` (or `staff`). Use only those two role names for staff.
- **Workspace data** answers only for signed-in members of the account inside the platform.
- **Ad numbers** from Meta are visible to the app's staff by default. Opening them wider needs the owner's explicit ask (the **access roles setting**).
- **Platform actions** that touch other people's data run only for staff; plain users act on their own rows only (`NOT_YOURS`, `ROLE_NOT_ALLOWED` otherwise). Show: "Ask the app's admin to let your role do this." / "You can only change your own."
- **Outside-app actions** are approved one by one by the owner in the app's permissions. Approving one never allows another.

## Sign-up on or off

`allowSignup: true` lets the team self-register. For a closed internal tool turn it off: the screen then says "Access is by invitation. Ask your admin to add you." Change WhatsApp or email login only when the owner asks (the **app login setting**).


---

<!-- file: docs/11-dedup-and-data-quality.md -->
# 11. No duplicates, clean data

Duplicates break trust faster than anything else in a business app. Every rule below exists because a real number came out wrong without it.

## Counting rules

| Situation | Rule |
|---|---|
| Meta reports one lead under several action types | Take the **largest** value among the lead types, never the sum. Same for purchases. |
| Spend and conversions read in two calls | Merge by `date + campaign_id` (or `ad_id`) into one row; never append both lists. |
| A campaign deleted from Meta but with spend in the range | Keep its row, named from the insights answer; do not drop the spend. |
| Paged answers that come back "cut" | Re-read the page smaller; never keep a partial page and the full one. |
| Money in several currencies | Show each on its own; never add them. |
| Buyers estimated from money | Label it as an estimate ("buyers ≈ money ÷ price"). |
| Net of GST | Show as a separate line (`÷ 1.18`), keep gross visible. |
| Timezones | Use the workspace's timezone for "today" and day buckets, so the app matches the platform's own dashboards. Never filter workspace data again in UTC in the browser (it dropped midnight to 5:30 AM IST once). |

## People: one person, one row

- **Match by email or phone**, normalised: emails lower-cased and trimmed; phones digits only with country code (strip spaces, dashes, a leading 0, add +91 or the account's country code).
- **Calling list imports skip people already on a list.** "Load new leads" pulls sign-ups for a period and adds only new ones.
- **Mark existing buyers** instead of adding them as prospects (status "Paid").
- **Zoom reports:** a person who left and rejoined appears several times; **sum their minutes into one row**. Drop host, panelists and "Attended = No" rows. Fill missing phones from the CRM by email.
- **Creating contacts on the platform** with an existing phone or email reuses that contact (its old name stays). Show the name the platform returns.

## Actions: one click, one action

- Run a platform action **once per user click**. Never call it again to "confirm"; that books twice or sends twice.
- Disable the button while `isRunning`.
- `pending_approval` is not "done": show "Waiting for approval".
- Never retry a change automatically. Only reads may retry, and only for errors that can fix themselves.

## App data hygiene

- One document per logical thing; big lists split into fixed-size parts (250 attendees per part) so updates never rewrite everything.
- Every status change of a prospect is **logged** (`call_log`) with who did it and when, so performance is credited correctly and history is never lost.
- Deleting is explicit (a "Delete session" with confirmation), never a side effect.
- Personal caches in `owner` collections, shared work lists in `public` ones.

## Code hygiene: no duplicated logic

- **One place per rule:** the project split (`projectOf`), money formatting (`fmt.ts`), the Meta reader (`metaDirect.ts`), connector health (`connectorHealth.tsx`), date presets (`filters.tsx`). Pages import them; they never re-implement them.
- **One query spec per data**, as a top-level const reused across screens (same spec, same cache, same approval).
- **Merge pages instead of copying them:** Event, Webinars and Overview-of-the-event became one page with tabs; Live Now merged into Campaigns. Old links redirect.
- **One provider per live source** (`LiveAdsProvider`, `ConnectorHealthProvider`) so every page shares one read instead of each page asking Meta again.

## Connections: no duplicate connectors

- Several Connector Hub connections of one app (old 60-day Meta tokens): the newest is the default. Keep one, let the owner remove the rest. Never remove the default.
- Name AI connectors after the workspace they point to.


---

<!-- file: docs/12-metadata-branding-sharing.md -->
# 12. Metadata, branding and sharing

Everything that makes the app look like a product outside its own screens: its name, description, logo, favicon, browser tab, share previews and web address.

## Where each piece lives

| Piece | Where it is set | Notes |
|---|---|---|
| App name | the app builder, Settings, General, **Name** | Shown in the app list, editor header and browser tab title |
| Description | the app builder, Settings, General, **Description** | Internal ("only you see this") |
| In-app name | Code: sidebar header, sign-in `BRAND.appName`, preloader | Change all three together |
| Logo mark | Code (inline SVG or the sign-in block's mark) | Keep one source of truth for the mark |
| Tagline | Code: sign-in `BRAND.tagline` | Global wording; no country-only words if the product is global |
| Public variables | Settings, Advanced, App text | Editable text without code changes |
| Web address (slug) | Settings, **Web address** | Changing it breaks links already shared |
| Custom domain | Settings, Web address, Add domain (CNAME to the host the screen shows) | Verify, then test the live link |

## Renaming an app (checklist)

1. Code: sidebar name, sign-in `appName`, preloader name, logo letters or mark, quote credits.
2. Settings, General: Name, then Description.
3. Publish the code change (preview first).
4. Decide on the web address: keep the old slug so shared links keep working, or change it and tell users.
5. Update any share image and the docs.

## Share previews (WhatsApp, LinkedIn, Facebook, Slack)

Share previews are built by crawlers that read the **raw HTML** of the link. They do **not** run JavaScript. So the preview needs these tags in the HTML the server sends:

```html
<title>Ads Hub</title>
<meta name="description" content="Live Meta ads, leads, sales and webinars in one dashboard.">
<meta property="og:type" content="website">
<meta property="og:title" content="Ads Hub">
<meta property="og:description" content="Live Meta ads, leads, sales and webinars in one dashboard.">
<meta property="og:image" content="https://<public-host>/ads-hub-share-1200x630.png">
<meta property="og:url" content="https://<app-domain>/app/<slug>">
<meta name="twitter:card" content="summary_large_image">
```

- **Image:** 1200 x 630 px PNG or JPG, under 300 KB, on a public HTTPS URL. Big title, short line, logo; readable when shrunk to a phone thumbnail. Example mark: `assets/ads-hub-mark.svg` (place it on a 1200 x 630 canvas with the app name and one line).
- **Title** under 60 characters, **description** under 155.
- WhatsApp caches previews. After a change, test with a new link (`?v=2`).

### Platform status (checked on the Ads Hub build)

The platform serves `/app/<slug>` with **empty** `og:title`, `og:description`, `og:image` and an empty `<title>`; the name appears only after JavaScript runs. App code cannot fix this. The platform fix:

1. On the server, for `/app/<slug>` and custom domains, fill `<title>`, `description`, `og:*` and `twitter:*` from the app's **Name** and **Description**.
2. Add a **Share image** upload to the app's settings (General), and serve it as `og:image` (fallback: a generated image with the app name).
3. Set `twitter:card` to `summary_large_image`.

Until then: share the link with a short line of text, or share the image itself.

## Favicon and app icon

- Favicon: a simplified mark (thicker strokes, fewer details) that reads at 16 to 32 px. SVG preferred.
- App icon (home screen): the full mark on its colour square, 512 x 512 PNG.
- The platform currently serves a shared `/favicon.svg`; a per-app favicon is part of the same platform fix.

## Logo

Ads Hub's mark: a plum rounded square with a hub and spokes to ads, leads and sales; one gold spoke for "the one that paid". Wordmark in Space Grotesk. Variations: main on white with tagline, reversed on dark, app icon, favicon. Keep the mark's colours in the theme tokens so app and logo stay in step.

## Global wording

If the product is sold outside one country: no country-only phrases ("every rupee"), currency from the account's settings, dates and numbers formatted with the account's locale, tax lines only where the account has a tax setting.


---

<!-- file: docs/13-sync-performance-caching.md -->
# 13. Sync, speed and caching

Goal: the screen fills instantly with the last known numbers, fresh numbers replace them quietly, and the app never hammers an outside service.

## Stale-while-revalidate, three layers

```
cacheGet(key)  → 1. this tab's memory        (instant)
               → 2. the browser (localStorage, if allowed)
               → 3. the person's own row in app.db "screen_cache" (owner access)
                    so a fresh page load on any device starts from their last numbers
read fresh from the source in the background
cacheSet(key, value) → all three layers (server copy debounced 1.5 s,
                       newest 8 keys, under 250 KB, entries older than 7 days ignored)
```

- Keys include everything that changes the answer: `rows:<project>:<from>:<to>`, `camps`.
- On a failed refresh with saved numbers on screen: keep them and say when they are from. Never replace real numbers with zeros.
- Every storage call wrapped in try/catch (storage can be off in the sandbox).

## Automatic sync

- The dashboard reads Meta again **every 15 minutes** while open, measured from the last read **or the last attempt** (so a failure also waits 15 minutes).
- A tab hidden past the due time catches up when it becomes visible (`visibilitychange`).
- **Sync now** is always available: it bumps a `refreshKey` that every provider listens to, and rechecks connectors.
- A popover shows "Last synced" and "Next automatic sync". The header shows "Synced 3:21 pm" with a green dot, or a warning colour and the reason.
- Workspace data uses **live events**, not timers (`{ live: ["payment.paid"] }`). Use a timer only for sources with no push signal (Meta).
- After a manual sync, one toast with the outcome; automatic syncs stay quiet.

## Talking to Meta (and any rate-limited service)

- Windows of 7 days, at most 3 in parallel.
- Pages start at 50 rows and halve when the answer is cut.
- Finished days cached in memory; today always re-read.
- Final errors (not connected, rate limited, expired) stop at once, no retry loops.
- Ask Meta for fewer rows: filter by campaign name and by `spend > 0` on Meta's side.
- One provider shared by all pages, so switching pages never triggers a new read.
- Avoid rapid repeated reloads while testing; they cause "too many requests" for everyone using the app.

## Rendering

- No remount on sync: providers update state; pages re-render in place.
- A thin progress bar under the header while refreshing.
- Big lists paged ("Load more") rather than loaded whole.
- The page builder and other heavy parts load only on the screens that need them.


---

<!-- file: docs/14-imports-exports.md -->
# 14. Imports and exports

## Importing a CSV (example: Zoom attendee reports)

Ads Hub's Prospects page accepts the Zoom **webinar attendee report** or the **meeting participants** CSV.

1. **Read the file in the browser** (a file input inside a shadcn Dialog). Detect which report it is from its header rows.
2. **Parse safely:** quoted fields, commas inside quotes, a byte-order mark at the start, Windows line endings, extra header blocks Zoom adds above the table.
3. **Clean:**
   - drop host and panelist rows, and rows with "Attended = No";
   - sum minutes for the same person (rejoins), matched by email, else name;
   - fill a missing phone from the CRM by email;
   - read the topic and date from the report header.
4. **Name and tag** the session: a name, an event (Event / Workshop / Other) and a date, so it appears on the right page.
5. **Save** to app data in parts (250 attendees per document, compact arrays) so big webinars still save.
6. **Offer a sample** report to try or download, so people can test without a real file.

Alternative source: "Pull from Zoom" reads the platform's own Zoom sync (newest 2,000 joins per webinar). Show a staleness warning when the last synced join is older than 7 days, and point to the upload instead.

### Filters after import

Time watched buckets (<10, 10 to 29, 30 to 59, 60 to 119, 120+ minutes), "at least N minutes", and Bought (everyone / not bought yet / already bought, matched by email or phone against payments). Sorted by minutes. "Add N to calling list" adds the filtered people, skipping anyone already on a list.

### Pasting lists

"Name, phone" per line, or one person at a time. Normalise phones the same way as everywhere else (`11-dedup-and-data-quality.md`).

## Exporting a CSV from a sandboxed app

The app runs in a sandboxed frame without `allow-downloads`, so a normal `<a download>` is blocked. The pattern:

```ts
const body = "﻿" + csvText;                        // BOM so Excel shows ₹ and names correctly
const sandboxed = window.origin === "null" || window.self !== window.top;
if (sandboxed) window.open("data:text/csv;charset=utf-8," + encodeURIComponent(body), "_blank");
else { /* Blob + object URL + <a download> */ }
toast.success(`Downloading ${name}`, {
  description: "Nothing saved? Copy the table instead and paste it into Excel or Google Sheets.",
  action: { label: "Copy", onClick: () => copyText(csvText) },
});
```

- Always offer **Copy** as a fallback in the toast.
- Quote fields that contain commas, quotes or newlines.
- Confirm with a real user that the file arrives on their computer; browsers differ.

## Copy for WhatsApp

The Daily log has "Copy for WhatsApp": a short text summary of the day (spend, results, cost per result, leads, purchases, clicks, money) using WhatsApp's `*bold*` and line breaks. Copy uses the hidden-textarea method so it works inside the sandbox.

## Share to Slack

Connectors page: a preview of the message, a channel field, and a confirm dialog ("This sends a real message as the connected Slack account"). Runs Slack **send message** through a **Connector Hub change**, shown only when Slack is connected. Handles done, waiting for approval and refused.


---

<!-- file: docs/15-verify-and-publish.md -->
# 15. Verify, publish, roll back

## Before the hand-over

1. **Build check passes** on the last save.
2. **Every journey walked through the code:** each action has waiting, success and error states.
3. **Every link** the app sends people to passes a **link check** in this round.
4. **Pictures at the end:** preview screenshots on desktop, then phone size, for every page and tab people use, with a test user behind the sign-in. Fix every design issue, look again until none are left.
5. **Feature checklist** gone through item by item: done with a platform module, done with app data, or a named platform gap.
6. **Numbers sanity:** compare one or two numbers on screen with the source (for example today's Meta spend from a direct Meta **Insights** (`GET /{ad-account}/insights`) read, today's registrations from `form_submissions`). Same timezone, same filters.

## Publish

1. User says publish.
2. **live status**: which version is live, is the new one ready.
3. **publish** without confirm: the preview of what goes live. Show it.
4. On yes: **publish** again with confirm.
5. If workspace data needs approval: nothing went live. The owner opens the app builder, Publish, approves the listed queries (and the app's permissions for outside actions), then publish again.
6. Open the live link in a browser and confirm the change. A sign-in is needed, so ask the owner to sign in in the browser pane if the AI is checking.

## After publishing

- Users get the live link on the client domain.
- Note the live version in the project's handover doc.
- Watch the Connectors page for a day for anything red.

## Roll back

- **version history**, then **restore a version** to bring an older version back as a new version; check it in preview; publish.
- Settings changes (name, description, variables, domain) are not versioned with code: write down the old value before changing.

## Approvals the owner must know about

| Thing | Where the owner approves |
|---|---|
| A new account-data query shape | the app builder, Publish |
| An outside-app action (Meta, Slack...) | the app's permissions (also listed in the Publish dialog) |
| Messages, money, bulk changes run from the app | the platform's approvals inbox (they arrive as `pending_approval`) |
| WhatsApp login template | Meta approves it (minutes); status via the **template status** check |


---

<!-- file: docs/16-security-and-rules.md -->
# 16. Security and house rules

These apply to every person and every AI working on a micro app.

## Secrets

- **Never generate, copy, display or store tokens, passwords or API keys in chat**, files, code, variables or screenshots.
- Never ask anyone to paste a token into a chat. The owner pastes it straight into the right box (Connector Hub's Access Token field).
- Passwords and 2-factor codes are typed by the person, always.
- Keys an app needs go in **Secrets** (owner only), never in code or public variables.
- If a token leaks, an admin clicks **Revoke tokens** on the Meta system user and the token runbook (steps 5 to 6) is redone.

## Changing things outside the app

- **Ask before** sending a message, replying, posting, deleting, or changing settings in any connected app (Meta, Slack, Gmail, Google Drive...). One exception: a change the owner explicitly asked for.
- Never click Revoke, Remove or Delete in Meta. Never remove people, apps, ad accounts or other Connector Hub apps.
- Never turn off security protections. Never create extra or fake admins to get around an approval rule (Meta's "approved by another admin" cannot be turned off; another real admin approves).
- Apps never delete data in outside apps (the build check refuses delete, remove and archive actions).

## Privacy and masking

- In anything public or shareable (guides, screenshots, share images, docs like this one): **blank out**, do not blur, names, ids, emails, phone numbers, keys and ad account names.
- Phones are masked in in-app lists of buyers.
- Only use Slack or email conversations the requesting person is part of or tagged in. If a connected account belongs to someone else (for example the founder), ignore their private conversations.

## Wording users see

- Always "Connector Hub". Never use the name of the company behind it, even when a tool name or tool answer shows it. "Connect Meta", not "connect to <vendor>".
- Never name the platform vendor inside a white-labelled app; use the agency's brand only when given.
- Plain words; no em dashes in materials written for the owner.

## Links

- Team preview links: `<team-domain>`. User links: `<app-domain>` or the custom domain.
- Never send app users to the platform dashboard or an editor .
- Never build platform links by hand; use the `public_url` a tool returns.

## Data use

- An app works for one workspace and never reads or guesses another's data.
- Never copy numbers from the account into code; the app reads them live.
- Workspace data in apps is read-only; what users type goes into app data.


---

<!-- file: docs/17-troubleshooting.md -->
# 17. Troubleshooting

Every problem met while building and running Ads Hub, with its cause and fix.

## Meta and Connector Hub

| What you see | Cause | Fix |
|---|---|---|
| "Meta's login has expired" on the dashboard | The connected token had an end date or was revoked | Make a never-expiring system user token (`07-meta-token-runbook.md`), connect it in Connector Hub |
| "No permissions available" when generating a token | Wrong Meta app (no Marketing API use case, e.g. an Instant Game app) | Pick the app with "Create & manage ads with Marketing API"; check it has ads_read, ads_management, business_management |
| "This request must be approved by another admin" | Meta's heightened-security rule for the business | Another full-access admin approves in their Facebook notifications; it cannot be turned off |
| "Sorry, this content isn't available" on business.facebook.com | Link missing `?business_id=` or signed in to the wrong profile | Add the business id; switch to the admin's profile |
| "Couldn't refresh from Meta (Too many requests)" | Meta's rate limit, often from many reloads in a few minutes | Wait a minute, then Sync now; avoid rapid reloads |
| Ad spend shows ₹0 with no error | The system user cannot see the ad account | Assign the ad account to the system user (Manage ad accounts), then regenerate the token |
| Leads look doubled | Summing several lead action types | Take the largest, never the sum |
| Spend for a day missing | Reading spend and conversions in one filtered call | Two calls (spend, conversions), merged by date and id |
| Numbers from other businesses appear | Shared ad account | Filter campaigns by name to this app's projects |
| "Connector Hub is not reachable: the action could not run" | A one-off failure of the status check | Press Check again; only act if it repeats |
| "no key" from **list Connector Hub connections** | That workspace has no Connector Hub set up | Add the key in that workspace's settings, or use the connector for the right workspace |

## Platform and the app builder

| What you see | Cause | Fix |
|---|---|---|
| Tools that change the app are refused | No **note the request** this round | Call **note the request** with the user's words first |
| Save refused | Someone else changed the app | Read the file again, redo the edit, save with the new version |
| **hand over** refused | No the **preview screenshot** tool of the latest version yet, or design issues open | Look, fix the issues, look again |
| Publish says queries need approval | A new account-data query shape | Owner approves in the app builder, Publish, then publish again |
| Account-data card shows `NOT_APPROVED` | The live app runs a query that was not approved | Approve it in Publish; no Retry button for this code |
| Numbers differ from the platform's dashboard by a few hours | Browser filtering in UTC | Use the account's timezone and period presets |
| Download CSV does nothing | Sandboxed frame blocks downloads | Open via a new window with a data URL; offer Copy |
| A platform page renders white inside the app | Opened inside the sandboxed frame | Open in a new tab (`target="_blank"`) |
| Toasts never appear | No `<Toaster />` | Render it once in App |
| Tooltip crash | No `<TooltipProvider>` | Wrap the app once |

## Sharing and domains

| What you see | Cause | Fix |
|---|---|---|
| WhatsApp shows no title, description or thumbnail | Server sends empty OG tags; crawlers do not run JavaScript | Platform must fill OG tags server-side (`12-metadata-branding-sharing.md`) |
| Custom domain shows "403 Not Available" though Settings says Verified | Domain not routed to the app by the host | Check the domain is attached to this app and the CNAME target matches; ask the platform team |
| Old name still in the browser tab | App name in Settings not changed | Settings, General, Name |

## Data sources

| What you see | Cause | Fix |
|---|---|---|
| Zoom sessions stop appearing | Platform Zoom sync stopped | Reconnect Zoom in the workspace's integrations, or upload the attendee report CSV |
| A connector named for one business shows another's data | Connector points to a different workspace | Check `connect_url` in **integration status**; rename connectors |


---

<!-- file: docs/18-case-study-ads-hub.md -->
# 18. Case study: Ads Hub, end to end

Ads Hub is a live dashboard for a business running Meta ads for two projects: a **seasonal event** (free registrations, a small paid upgrade, webinars) and a **subscription product** (workshops and plan sales). Names, numbers and brands are generalised; the lessons are real. It joins ad spend, leads, payments, webinar attendance and a team calling list in one place.

Identifiers below are placeholders. Real values belong in the app's variables and a private handover note, never in this repository.

## 1. The brief, as given

"One place for our ads, webinars, calls and sales. Live Meta numbers, money received, who registered, who attended, who to call next. Opens on today. Works on my phone."

## 2. What was decided (product plan)

| Decision | Why |
|---|---|
| Staff-only app with its own login, opening on the sign-in screen | Ad numbers and buyer lists are internal |
| Meta through Connector Hub, not the platform's built-in ads module | Outside apps are the default; built-in ads module only on explicit request |
| Payments, form entries, staff, Zoom attendance from workspace data | They already live in the platform's modules |
| Calling list, call log, uploaded Zoom reports, screen cache in app data | Nothing in the platform covers them |
| Date range opens on **Today** | The team checks the day's numbers first |
| One project shown at a time; campaigns of other businesses hidden | The ad account is shared |
| Older history from a one-time export | Some history (pixels, older attribution) is not available live |

## 3. Pages

**Performance**
- **Overview:** event live block (registrations, upgrade money, upgrade buyers ≈ money ÷ price, ad spend per registration); KPIs (ad spend, results, cost per result, link clicks, money received, ROAS, leads, active campaigns); spend and results chart; top campaigns; "what needs attention"; spend by offer; click-to-sale funnel.
- **Sales:** successful payments per project, by day and by product, net of GST, ROAS, payments table.
- **Event** (three tabs): Event so far; Webinar sessions (from uploaded Zoom reports tagged to the event: attended, average minutes, 30+ and 60+, bought); Buyers and sources (registrations by UTM source, latest 50 buyers with phones masked, latest 50 registrations).
- **Prospects:** Calling list (pick "I am", statuses Not called yet, Spoke: interested, Spoke: call back later, Did not answer, Not interested, Wrong or no number, Paid; every change logged and credited); Zoom attendees (upload or pull, filters, add filtered people to the calling list); Performance per caller.

**Ads**
- **Creatives:** every ad that spent, 3 per row, picture, headline, text, spend, results, cost per result, CTR, Ads Manager link, sort and search, cached cards.
- **Campaigns:** running now, spend, per result, by day; table filters Running now / With spend / All; tap a row for day by day.
- **Daily log:** one row per day; Copy for WhatsApp.

**Setup**
- **Account log:** Meta's change and billing history (7, 30 or 90 days, 20 per page, Load more), money converted from the smallest unit.
- **Connectors:** only what the app uses (Payment gateway, Zoom, Meta Ads, Slack), the workspace data it reads with live counts, a Zoom staleness warning, Share to Slack.

**Header on every page:** project tag, date range (Today by default), sync status and Sync now, dark mode.

## 4. Files

```
src/App.tsx                    providers, hash routes, redirects for merged pages
src/components/AppShell.tsx    sidebar navigation, header, date picker, refresh bar
src/components/AuthGate.tsx    login gate, reset/forgot, BRAND (name, tagline)
src/blocks/custom/signin-split.tsx  ejected split sign-in screen
src/components/Preloader.tsx   branded loading screen
src/components/SyncButton.tsx  "Synced 3:21 pm", popover with last/next sync
src/components/LivePanel.tsx   sync notes, Meta-expired note, AdsGate wrapper
src/components/ConnectorAlerts.tsx, ConnectionList.tsx   connector banner and list
src/components/ZoomAttendees.tsx   Zoom upload, pull, filters, add to calling list
src/components/DataTable.tsx   search, sort, CSV export
src/components/{Charts,Kpi,Section,States,DateRangePicker,BfLive}.tsx
src/lib/metaDirect.ts          every Meta read (insights, campaigns, ad looks, activities)
src/lib/liveAds.tsx            live ads provider, 15-minute auto sync, project split, revenue
src/lib/connectorHealth.tsx    Platform integrations + Connector Hub status, only the used connectors
src/lib/cache.ts               3-layer stale-while-revalidate cache
src/lib/filters.tsx            presets, Today default, refresh key
src/lib/fmt.ts                 money, numbers, dates, CSV download, copy
src/lib/zoom.ts                Zoom CSV parser, sync puller, storage, payers, sample
src/lib/snapshot.ts, src/data/snapA|B|C.ts   one-time export for older history
src/pages/*.tsx                Overview, Sales, BlackFriday, Prospects, Creatives,
                               Campaigns, Daily, AccountLog, Connectors
src/index.css                  theme tokens (signature preset, plum and gold)
```

## 5. App data collections

| Collection | Access | Holds |
|---|---|---|
| `prospects` | public | The calling list |
| `call_log` | public | Every status change, who and when |
| `zoom_sessions` | public | One document per session part, attendees as compact arrays, 250 per part |
| `screen_cache` | owner | Each person's last Meta answers, so screens paint at once |

## 6. Variables

`META_AD_ACCOUNT_ID`, `META_BUSINESS_ID`, `APP_STORE_URL`. No secrets in the app.

## 7. How it was built, in order

1. **Connector check:** the app builder live, Connector Hub Meta Ads active, platform integrations, a direct Meta read for today.
2. **Looked at the real data:** payments (product names), form submissions (form name), staff, Zoom attendance; Meta campaign names to design the project split.
3. **Plan and checklist** written into the app's request note.
4. **Backend first:** collections defined; account-data specs written as fixed consts; Meta reader built and proven with one real read per action.
5. **Shell:** providers (filters, connector health, live ads), sidebar, header, date picker defaulting to Today, sync button.
6. **Pages one by one**, each with its four states, each on data that already worked.
7. **Hard problems solved along the way:** doubled leads (largest, not sum), missing spend days (two-pass merge), slow long ranges (7-day windows, 3 at a time, shrinking pages), UTC filter dropping early-morning payments (removed; account timezone), downloads blocked by the sandbox (new-window data URL plus Copy), Meta token expiring every 60 days (system user token that never expires).
8. **Merged thin pages** (Event and Webinars into one Event page; Live Now into Campaigns) with redirects for old links.
9. **Connectors page trimmed** to only what the app uses, with "Connector Hub" wording.
10. **Pictures at the end**, desktop and phone; design issues fixed.
11. **Published**, queries approved by the owner.
12. **Handover** written so another AI account could continue with nothing lost.
13. **Rebrand to Ads Hub:** in-app name, logo mark, sign-in tagline made global, the app builder name and description, share image, logo canvas.

## 8. Open items at the time of writing

- Platform: server-side OG tags and a share image setting (WhatsApp previews).
- Custom domain answering 403 although marked verified.
- Zoom platform sync stopped; uploads used meanwhile.
- A real user to confirm CSV downloads save a file.
- Money in one currency with Indian formatting and GST; a global version needs per-account currency, locale and tax settings, and configurable projects and campaign rules instead of fixed names.


---

<!-- file: docs/19-prompts.md -->
# 19. Prompts

Copy these into a chat in the project. Replace anything in `<angle brackets>`.

## Starter prompt (first chat in a new project)

```
Read PLAYBOOK.md in this project fully before doing anything. Follow it as the way we work.

Context:
- Workspace: <workspace id or name>
- App (if it exists): <app id or name>. If it does not exist yet, say so and wait for my brief.
- Team preview links on `<team-domain>`; user links on `<app-domain>` or our domain.

First task: run the connector check from docs/02-connectors.md (the app builder live status, Connector Hub
connections, one tiny read from each outside app the app uses, platform integrations, and which
workspace each connector points to). Tell me in plain words what works and what needs fixing.
Then ask me what to build or change.
```

## One prompt: just describe the app

```
Build this app: <one paragraph, e.g. "a personal health tracker where everyone in my family tracks
their steps, connected to the Health app on their iPhones">.

Follow PLAYBOOK.md doc 20: discover every source through the platform and the Connector Hub,
classify each one, show me the feature checklist and connection plan, connect what is needed
with sign-in links I open myself, use a device bridge for phone-only data, then build, verify
and hand over. Ask at most one question.
```

## Build a new app (step by step)

```
New app: <one-paragraph brief: who uses it, what they need to see or do>.
Follow docs/04-product-planning.md: explore the platform first, look at the real data, then show me
the plan and the feature checklist before building screens. Build backend first, then screens,
mobile and desktop from the start. Open on the login screen. Hand over when the checklist is done.
```

## Change something small

```
In <app>, change <exact thing> to <new thing>. One change only. Read the file first, keep everything
else as it is, show me the preview link. Do not publish.
```

## Add a data source

```
Add <source, e.g. Google Ads spend> to <page>. Check whether it is a platform module, workspace data,
or a Connector Hub app. Look at a real answer first, then wire it with all four states and a
not-connected message. Tell me which approvals I need to give.
```

## Fix wrong numbers

```
<Card/number> on <page> shows <x> but <source> shows <y> for <period>. Audit before changing:
read the code that computes it, read the source directly for the same period in the account's
timezone, explain the difference, then fix it with the smallest change.
```

## Responsive and design pass

```
Do a design pass on <app>: look at every page on desktop and phone, list what fails the design
check in docs/08-ui-ux-design.md, fix them one by one, and show me before/after.
```

## Publish

```
Publish <app>. Show me the preview of what goes live first.
```

## Rename or rebrand

```
Rename <app> to <new name> everywhere: in-app name, logo letters, sign-in, preloader, the app builder
name and description. Keep the web address unless I say otherwise. Update the share image.
```

## Reconnect Meta (expired token)

```
The dashboard says Meta's login has expired. Follow docs/07-meta-token-runbook.md in my browser.
I will only sign in, click Generate and Copy, and paste into the box. Never ask me for the token.
```

## Handover to a new chat or account

```
Write a complete handover for <app> following templates/handover-template.md: ids and links,
connectors and their status, structure, data flow, rules, open items, key numbers for sanity
checks, and a starter prompt. No secrets.
```


---

<!-- file: docs/20-one-prompt-to-app.md -->
# 20. One prompt to a finished app

The goal: a person writes one paragraph ("I want a family step tracker connected to our iPhones' Health app") and the AI works out everything else itself: which data sources exist, which connectors are needed, how to connect them, what to build, and what each user must do once. The person only answers a question when a wrong guess would break the app, signs in where a provider asks, and approves.

**Wording rule:** the place where outside apps are connected is the **Connector Hub** (in the workspace's settings). Users never see the name of the company behind it. Tool answers may mention that vendor name; never repeat it.

---

## The pipeline

```
1. Read the brief        people, data, actions, devices, privacy
2. Discover              platform actions, Connector Hub actions, connection status
3. Classify each source  connected / connectable / device-only / none
4. Plan                  feature checklist + connection plan, shown before building
5. Connect               sign-in link per app, person signs in, status confirmed, one real read
6. Build                 backend first, then screens (docs 03 to 15)
7. Verify                every journey, every device, numbers against the source
8. Hand over             what works, setup each user does once, approvals, gaps
```

### 1. Read the brief

Write down, from the brief alone:

| Question | Family step tracker example |
|---|---|
| Who uses it, and do they sign in? | Every family member, each with their own login |
| What data comes in, from where? | Daily steps, from each person's iPhone Health app |
| What do people do in the app? | See their own steps, the family's totals, a weekly leaderboard, goals |
| On which devices? | iPhones mostly, sometimes a laptop |
| What is private? | Health data: each person's detail is theirs; only agreed totals are shared |
| What must happen automatically? | Steps arrive daily without anyone typing them |

### 2. Discover through connectors

Run all of these before deciding anything:

1. **Platform:** **search platform actions** with plain words for each job ("send a reminder", "create a group", "payment link").
2. **Connector Hub, by need:** **search Connector Hub actions** with plain words for each outside data source ("read daily step count", "list workouts", "sleep score"). The answer lists actions of connected **and not-connected** apps, so it shows what is possible, not only what is on now.
3. **Connector Hub, by name:** **search Connector Hub actions** with `app` set to likely providers (for health: fitbit, oura, garmin, withings, whoop, strava, google_fit). "No matching actions" means that provider is not in the hub.
4. **Status:** **connection status** lists every connection of the account (platform integrations and Connector Hub) as connected, needs attention or not connected, each with a `connect_url`.
5. **Workspace data:** **list workspace data** if the brief touches business data already in the platform.

Never decide a source "can't be done" before these searches.

### 3. Classify each source

| Class | Meaning | What to do |
|---|---|---|
| **A. Connected** | Action exists and the app is connected | Prove it with one tiny read, then build |
| **B. Connectable** | Action exists, app not connected yet | Connect it (step 5). Build with it anyway; until connected the app shows the not-connected text |
| **C. Platform integration** | Meta pages, WhatsApp Business, SMTP, Zoom, Slack, payment gateways, Google Calendar | a **connect link** or **start a connection** gives the connect page |
| **D. Device-only** | The data lives only on a phone with no online API (Apple Health, Android Health Connect, phone contacts, local files) | Use a **device bridge** (below) |
| **E. Nothing exists** | No action, no API, no device route | Manual entry or CSV upload in the app, named as a gap |

### 4. Plan, and show it before building

Two tables, in plain words, in one message:

- **Feature checklist** (`templates/feature-checklist.md`).
- **Connection plan:** each source, its class, how it connects, who must do what, once.

Ask at most one question, and only if the answer changes the build. Otherwise state the assumptions and continue.

### 5. Connect

For each source of class B or C:

1. **start a connection** (for one app) **without** confirm: a preview of what will happen. Show it.
2. On the person's yes: confirm it. Connector Hub apps return a **sign-in link** (the provider's page, then back); platform integrations return a **settings page** link.
3. Give the person the link. **They** sign in on the provider's page. Never ask for a password, code or token in chat.
4. **connection status** (for that app) until it shows connected.
5. One tiny real read (a **Connector Hub read**) to prove it.
6. Note it in the hand-over: which account was connected, by whom.

Inside the app itself there is **never** a connect button or link of your own. When something is not connected, the app shows the kit's not-connected text (not-connected message), which tells people to ask the owner. Connecting is the owner's job, done through the steps above or in the workspace's Connector Hub settings.

### 6 to 8. Build, verify, hand over

Exactly as docs 03 to 15. The hand-over adds a **"Setup each person does once"** section when a device bridge is used.

---

## Device bridges: getting phone-only data in

Some data never leaves the phone unless the phone sends it. The app can receive it in three ways, from most to least automatic:

| Bridge | How | Good for |
|---|---|---|
| **Phone automation opens the app with the data** | An iOS Shortcut (or Android automation app) reads the value, then opens the app's link with the value in it. The signed-in app saves it. | Daily numbers: steps, sleep hours, weight |
| **Export and upload** | The person exports a file (Apple Health export, CSV) and uploads it in the app; the app parses it | History, one-time imports |
| **Manual entry** | A quick "Add today" form, one tap per value | Fallback, people without the automation |

### Worked example: family step tracker on iPhone

**Why a bridge:** Apple Health (HealthKit) data stays on the iPhone. There is no web API and no Connector Hub app for it, so no server can read it. The iPhone itself must send it. (Checked 25 Nov 2026: the Connector Hub had no Apple Health, Fitbit, Oura, Garmin, Withings, Whoop, Strava or Google Fit actions for this account. Search again before each build; the catalogue grows.)

**The app**

- Sign-in: every family member has their own login (WhatsApp code or email). Opens on the login screen.
- Collections:
  - `steps_daily` (**owner**): one row per person per day `{ date, steps, source, synced_at }`. Each person sees only their own detail.
  - `families` (**public**): `{ name, invite_code, members: [{ user_id, display_name }] }`.
  - `family_totals` (**public**): one row per person per day with only the shared number `{ family_id, user_id, display_name, date, steps }`, written by the app when a person syncs, and only if they turned "share my steps with family" on.
- Screens: Today (my steps, goal ring), Week (my chart), Family (leaderboard and totals, this week), Settings (goal, share toggle, family invite code, "Set up iPhone sync").
- **No duplicates:** a sync for a date that already has a row **updates** that row (upsert by person and date), never adds a second one. Steps for a day only go up during the day; keep the larger value if two syncs disagree.

**The iPhone Shortcut (each person, once)**

1. Shortcuts app, new shortcut "Sync steps to <app name>".
2. Action **Find Health Samples**: type Steps, start date is today.
3. Action **Calculate Statistics**: Sum of the Health Samples.
4. Action **Open URLs**: `<live app link>#/sync?steps=<Statistics>&date=<Current Date, format yyyy-MM-dd>`.
5. Automation tab, **Personal Automation**, Time of Day 9:00 PM daily, run the shortcut, **Run Immediately**.
6. Run it once by hand; the app shows "Synced today, 9:00 PM, 8,412 steps".

The app's Settings page shows these steps with the person's own link filled in, so nobody types a URL.

**In the app code**

- On load, after sign-in, read `#/sync?steps=&date=` from the hash, validate (whole number 0 to 100,000, a real date not in the future), upsert the row, write the family total if sharing is on, show a toast, then clear the hash so a reload does not save again.
- If the person is signed out when the shortcut opens the link, keep the values, show the sign-in screen, save right after sign-in.

**Test before rolling out:** confirm on one iPhone that the hash reaches the app on the live link and that the session survives in Safari. Note the result in the hand-over.

**Honest limits to tell the family**

- Data arrives once a day (or whenever the shortcut runs), not live.
- iPhone only; Android needs Health Connect with an automation app, or manual entry.
- **Privacy:** app collections have three access levels (owner, public, private). There is no "family-only" level yet, so anything in a public collection can be read by any signed-in user of the app. Keep detail in owner collections, share only agreed totals, and run **one app per family** if families must not see each other. A family-scoped access level is a platform gap to raise.
- Health data is sensitive: ask before sharing anything, let people delete their data, never send it to other apps.

---

## The same pipeline, other briefs

| Brief | Sources found through connectors | Class | Bridge or gap |
|---|---|---|---|
| "Team inbox for client emails with a weekly digest" | Gmail (Connector Hub), platform contacts | A or B | None |
| "Post our blog to LinkedIn and Instagram" | LinkedIn, Instagram (Connector Hub) | A or B | Posting is a change: owner approves each action |
| "Book site visits with WhatsApp reminders" | Calendar booking, WhatsApp template (platform) | Platform | Template approval by Meta |
| "Track our Stripe revenue against ad spend" | Stripe, Meta Ads (Connector Hub) | A or B | Currencies shown separately |
| "Kids' screen time across our phones" | None (phone-only) | D | Device bridge, or a gap |

---

## The one-prompt starter (paste with any brief)

```
Build this app: <one paragraph brief>.

Work from PLAYBOOK.md, doc 20 "One prompt to a finished app":
read the brief, discover every source through the platform and the Connector Hub (search by need
and by provider name, check connection status), classify each source, then show me the feature
checklist and the connection plan in one message. Connect what is needed with sign-in links I
open myself (never ask me for passwords, codes or tokens). Use a device bridge for phone-only
data. Then build, verify on phone and desktop, and hand over with the setup each user does once.
Ask me at most one question, only if a wrong guess would break the app.
```


---

<!-- file: docs/21-integration-routes.md -->
# 21. Integration routes: Connector Hub, direct API, MCP

Every outside app an app talks to (ads, CRM, email, chat, payments, files, wearables) goes through one of three routes. **The Connector Hub is the default.** The other two exist for what the hub cannot do.

## The three routes

| Route | What it is | Who signs in | Where the credential lives | Use when |
|---|---|---|---|---|
| **1. Connector Hub** (default) | The workspace's hub holds one connection per outside app; apps call it for reads and changes | The owner, once, on the provider's own page (redirect and back) | Inside the hub, never visible to the app, the AI or chat | The provider is in the hub's catalogue |
| **2. Direct API** | The app (on the server side) calls the provider's API itself | The owner, through the provider's OAuth page, or by creating a key | A **server-side secret**, never in browser code | The provider is not in the hub, or the hub lacks an endpoint you need |
| **3. MCP server** | An AI-side connector to the provider (official MCP if one exists) | The person using the AI, in their AI account | In the AI account's connector settings | The **AI** needs the provider while building: reading docs, testing a call, checking an account, diagnosing |

Route 3 is for building, not for the running app. A live app never depends on someone's AI session.

## Route 1: Connector Hub, the redirect flow

```
Owner asks to connect  →  start a connection (preview, then confirm)
        →  the hub returns a sign-in link for the provider
        →  owner opens it, signs in ON THE PROVIDER'S PAGE, grants access
        →  provider redirects back to the hub; the hub stores the connection
        →  connection status shows "connected"
        →  one tiny real read proves it
```

Rules:

- **Redirect, never collect.** People sign in on the provider's page. Nobody types a password, code or key into chat, the app, or a form you built.
- **Apps never show their own connect button or link.** When a hub app is not connected, the app shows a calm "not connected" message telling people to ask the owner. Connecting is the owner's job, in the workspace settings or through the flow above.
- **Build with the hub action even before it is connected.** Search the hub's catalogue for the exact action and its fields, write the call, and let the not-connected message show until the owner connects.
- **Reads run directly; changes need approval.** The owner approves each change action by name (send, post, update). Approving one never allows another. Apps never delete in outside apps.
- **One default per provider.** Several connections of one provider: the newest is the default; old ones are removed by the owner.
- **Rate limits are real.** Page results (20 rows or fewer), cache, never loop.

## Route 2: Direct API

Use only when the hub cannot do the job. Checklist:

1. **Search the hub first** (by need and by provider name). Note in the plan why the hub is not enough.
2. **Prefer OAuth** with the provider's own consent page (same redirect pattern as the hub). Use an API key only when the provider offers nothing else.
3. **Credentials as server-side secrets**, added by the owner. Browser code never sees them. If your platform has no server-side code for apps yet, this route is a **platform gap**: say so and use route 1 or a device bridge instead.
4. **Least privilege:** request only the scopes the features need (read-only when possible).
5. **Token refresh:** store refresh tokens server-side; handle expiry with a clear "reconnect" message for the owner.
6. **Webhooks in, not polling:** when the provider can push events, receive them on a server endpoint and verify the signature.
7. **Same rules as the hub** for paging, rate limits, no deletes, approvals for changes, and the not-connected state.

## Route 3: MCP for the AI

- Add the provider's **official MCP server** (or a trusted one) to the AI account when building needs it: reading API docs, testing a query, listing accounts, checking a webhook.
- Sign in through the MCP's own flow. Never paste keys into chat.
- Anything the AI learns there becomes code that uses route 1 or 2. The live app never calls the AI's MCP.

## Choosing a route

| Question | Answer → route |
|---|---|
| Is the provider in the Connector Hub with the action you need? | Yes → **1** |
| Not in the hub, has OAuth or keys, and your platform runs server-side code for apps? | Yes → **2** |
| Not in the hub and no server-side code? | **Platform gap**; offer upload, manual entry or a device bridge |
| Data only on a phone (Apple Health, Health Connect, phone contacts)? | **Device bridge** (`20-one-prompt-to-app.md`) |
| The AI needs it only while building? | **3** |

## Integration plan table (put it in every plan)

| Provider | Data or action | Route | Connected? | Who connects, how | Approvals | Fallback if missing |
|---|---|---|---|---|---|---|
| Meta Ads | Spend, leads, creatives | 1 | Yes | Owner, hub sign-in | None (reads) | Not-connected message |
| Slack | Post daily summary | 1 | Yes | Owner, hub sign-in | "Send message" approved | Copy text instead |
| Apple Health | Daily steps | Device bridge | n/a | Each person, iPhone Shortcut once | None | Manual entry |


---

<!-- file: templates/connector-check.md -->
# Connector check: <app>, <date, time>

| # | Check | Call | Result | Fix if not OK |
|---|---|---|---|---|
| 1 | App is live, which version, unpublished changes | **live status** | | Publish when asked |
| 2 | Which sub-account each AI connector points to | **integration status** (look at the links it returns) | | Rename or use the right connector |
| 3 | Connector Hub apps the app uses are active | **list Connector Hub connections** | | Owner reconnects in the sub-account's Connector Hub |
| 4 | Outside app answers | one tiny read, e.g. Meta **Insights** (`GET /{ad-account}/insights`) today, account level | | Token runbook / reconnect |
| 5 | Platform integrations the app uses; required apps missing | **integration status** | | Owner connects the app |
| 6 | Sub-account data readable | one `count_only` query per object the app uses | | Approve in Publish / check role |
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
| Sub-account id | |
| Live link (users) | `<app-domain>/app/<slug>` |
| Editor / preview (team) | <team-domain>/<editor-path-for-the-app> |
| Live version | |
| Outside accounts (e.g. Meta business, ad account) | (masked in shared copies) |
| Variables | |

## 3. Connectors and status (date, time)
| Connector | Where | Status | Used for |
|---|---|---|---|

AI connectors needed in a new account, and which sub-account each points to.

## 4. Structure
Navigation, pages, header, what each page shows.

## 5. Data flow
Each source (sub-account data, app data, Connector Hub, platform actions), the files that read it, collections and access.

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

EDIT ME: Owner: <name>. Sub-account: <name / id>. Apps: <names / ids>.
EDIT ME: Team preview links on `<team-domain>`. User links on `<app-domain>` or <custom domain>.
EDIT ME: Timezone for date boundaries: <e.g. Asia/Kolkata>.

One-prompt mode: when I just describe an app, follow doc 20 of PLAYBOOK.md. Discover every data source through the platform and the Connector Hub (search by need and by provider, check connection status), classify each, show me the feature checklist and connection plan, connect with sign-in links I open myself, bridge phone-only data, then build, verify and hand over.

How to work:
- Every request is one round: note the ask on the app, read files before changing them, small exact edits that pass the last-read version, fix any failed build check, look at the app (desktop and phone) only at the end, then hand over in plain words.
- Audit before building. One change at a time.
- Platform first; sub-account data for the business's numbers; app data only for what nothing else covers; outside services through Connector Hub.
- Real data only. Every data block has loading, empty, error and content states. Mobile and desktop from the start.
- Never count twice: dedupe people by email/phone, take the largest of overlapping counts.
- Sub-account-data query shapes stay fixed so the app can be published; tell me when Publish needs my approval.
- Publish only when I ask, and show the preview first.
- Apps with a login open on the login screen. Dashboards open on Today.

Never:
- Ask for, show, copy or store tokens, passwords or keys. I paste secrets into the right box myself.
- Send, post, delete or change settings in a connected app without asking first (unless I asked for that exact change).
- Click Revoke/Remove/Delete in Meta, turn off security settings, or create fake admins.
- Call the Connector Hub by any other name, including the vendor name a tool may show.
- Use em dashes in anything written for me.

Hand-over: what works, which data it reads, placeholders, what is still open, what I must approve.
