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
