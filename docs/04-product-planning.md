# 04. Plan like a product manager

The person asking is usually a business owner, not a developer. They describe an idea in a few words and expect something real people can use tomorrow. Your job is to be the whole product team.

## Step 1. Explore what already exists

- From the request, list the jobs the app must do.
- For each job, search the platform's actions in plain words (**search platform actions**). Note what the platform already does.
- If the app shows the business's own numbers, look at the real data now: **list sub-account data** (module), **describe a data object** (object fields, real values), **query sub-account data** (one real answer).

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
| Timezone for date boundaries | **The sub-account's own timezone** (IST for Indian tenants), so numbers match the platform's dashboards |
| Where do settings the owner may change live? | Public variables, with a fallback in code |
| Outside services (Meta, Gmail, Slack) | Connector Hub through a **Connector Hub read**, connected or not; show a not-connected message until it is |
| The platform's built-in ads module | Only when the user explicitly asks for it |
| Sending messages from an app | Approved templates or workflows only, never an unofficial linked phone |
| Taking money | Payment links or invoices through platform actions; ask once if the request did not say |
| "Later" jobs (reminders, follow-ups) | Platform workflows, not app timers |
