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
5. If sub-account data needs approval: nothing went live. The owner opens the app builder, Publish, approves the listed queries (and the app's permissions for outside actions), then publish again.
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
