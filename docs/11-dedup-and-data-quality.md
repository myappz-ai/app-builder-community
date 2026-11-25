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
| Timezones | Use the sub-account's timezone for "today" and day buckets, so the app matches the platform's own dashboards. Never filter sub-account data again in UTC in the browser (it dropped midnight to 5:30 AM IST once). |

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
- Name AI connectors after the sub-account they point to.
