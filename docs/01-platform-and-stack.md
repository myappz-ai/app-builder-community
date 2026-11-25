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
