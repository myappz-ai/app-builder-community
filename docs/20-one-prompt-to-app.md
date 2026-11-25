# 20. One prompt to a finished app

The goal: a person writes one paragraph ("I want a family step tracker connected to our iPhones' Health app") and the AI works out everything else itself: which data sources exist, which connectors are needed, how to connect them, what to build, and what each user must do once. The person only answers a question when a wrong guess would break the app, signs in where a provider asks, and approves.

**Wording rule:** the place where outside apps are connected is the **Connector Hub** (in the sub-account's settings). Users never see the name of the company behind it. Tool answers may mention that vendor name; never repeat it.

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
5. **Sub-account data:** **list sub-account data** if the brief touches business data already in the platform.

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

Inside the app itself there is **never** a connect button or link of your own. When something is not connected, the app shows the kit's not-connected text (not-connected message), which tells people to ask the owner. Connecting is the owner's job, done through the steps above or in the sub-account's Connector Hub settings.

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
