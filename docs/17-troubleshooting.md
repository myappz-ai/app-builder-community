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
| "no key" from **list Connector Hub connections** | That sub-account has no Connector Hub set up | Add the key in that sub-account's settings, or use the connector for the right sub-account |

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
| Zoom sessions stop appearing | Platform Zoom sync stopped | Reconnect Zoom in the sub-account's integrations, or upload the attendee report CSV |
| A connector named for one business shows another's data | Connector points to a different sub-account | Check `connect_url` in **integration status**; rename connectors |

## Payments, receipts and settings

| What you see | Cause | Fix |
|---|---|---|
| Payment succeeded in sub-account transactions, but the order still says pending | The platform did not write its payment mark on the linked app-data row (seen on a one-item checkout; a multi-item cart on the same app kept the link) | Show Paid from the platform mark first, then a staff match to the successful transaction, then a live status read on the stored payment reference. Report the missing mark as a platform gap (`22-use-the-platform-not-the-app.md`) |
| Thank-you page never shows "Paid" after checkout | The app uses hash routes and read `window.location.search`, which is empty | Read the checkout result from the hash query (`#/order/ID?pay=paid`) and keep the payment reference on the order |
| Unpaid online attempts appear in revenue or "to ship", or they hold stock forever | Abandoned checkouts were treated as placed orders | Exclude unpaid online orders from revenue and to-ship; release their stock after a short window |
| The app has its own Domain, Secrets or Connect payment screens | Those already exist in the app builder and the sub-account | Remove the duplicate screens and point the owner to Publish (domain), Secrets, and sub-account connections |
| Receipt email or invoice is shown as "sent" at once | Sending mail is a platform action that may wait for the owner | Show "Waiting for approval" until the status is `done` |
| Automatic payment emails never go out | The app tried to send them itself, or the workflow was published too widely without a check | Use a platform workflow (draft first). Confirm the email-sending connection, and that the trigger should run for the whole sub-account |
