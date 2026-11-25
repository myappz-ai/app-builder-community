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
6. **Dates are the ad account's timezone.** `date_start` is the day in that timezone; compare with the sub-account's timezone days.
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
