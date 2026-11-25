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
