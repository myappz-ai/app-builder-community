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
