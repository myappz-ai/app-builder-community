# 21. Integration routes: Connector Hub, direct API, MCP

Every outside app an app talks to (ads, CRM, email, chat, payments, files, wearables) goes through one of three routes. **The Connector Hub is the default.** The other two exist for what the hub cannot do.

## The three routes

| Route | What it is | Who signs in | Where the credential lives | Use when |
|---|---|---|---|---|
| **1. Connector Hub** (default) | The sub-account's hub holds one connection per outside app; apps call it for reads and changes | The owner, once, on the provider's own page (redirect and back) | Inside the hub, never visible to the app, the AI or chat | The provider is in the hub's catalogue |
| **2. Direct API** | The app (on the server side) calls the provider's API itself | The owner, through the provider's OAuth page, or by creating a key | A **server-side secret**, never in browser code | The provider is not in the hub, or the hub lacks an endpoint you need |
| **3. MCP server** | An AI-side connector to the provider (official MCP if one exists) | The person using the AI, in their AI account | In the AI account's connector settings | The **AI** needs the provider while building: reading docs, testing a call, checking an account, diagnosing |

Route 3 is for building, not for the running app. A live app never depends on someone's AI session.

## Route 1: Connector Hub, the redirect flow

```
Owner asks to connect  →  start a connection (preview, then confirm)
        →  the hub returns a sign-in link for the provider
        →  owner opens it, signs in ON THE PROVIDER'S PAGE, grants access
        →  provider redirects back to the hub; the hub stores the connection
        →  connection status shows "connected"
        →  one tiny real read proves it
```

Rules:

- **Redirect, never collect.** People sign in on the provider's page. Nobody types a password, code or key into chat, the app, or a form you built.
- **Apps never show their own connect button or link.** When a hub app is not connected, the app shows a calm "not connected" message telling people to ask the owner. Connecting is the owner's job, in the sub-account settings or through the flow above.
- **Build with the hub action even before it is connected.** Search the hub's catalogue for the exact action and its fields, write the call, and let the not-connected message show until the owner connects.
- **Reads run directly; changes need approval.** The owner approves each change action by name (send, post, update). Approving one never allows another. Apps never delete in outside apps.
- **One default per provider.** Several connections of one provider: the newest is the default; old ones are removed by the owner.
- **Rate limits are real.** Page results (20 rows or fewer), cache, never loop.

## Route 2: Direct API

Use only when the hub cannot do the job. Checklist:

1. **Search the hub first** (by need and by provider name). Note in the plan why the hub is not enough.
2. **Prefer OAuth** with the provider's own consent page (same redirect pattern as the hub). Use an API key only when the provider offers nothing else.
3. **Credentials as server-side secrets**, added by the owner. Browser code never sees them. If your platform has no server-side code for apps yet, this route is a **platform gap**: say so and use route 1 or a device bridge instead.
4. **Least privilege:** request only the scopes the features need (read-only when possible).
5. **Token refresh:** store refresh tokens server-side; handle expiry with a clear "reconnect" message for the owner.
6. **Webhooks in, not polling:** when the provider can push events, receive them on a server endpoint and verify the signature.
7. **Same rules as the hub** for paging, rate limits, no deletes, approvals for changes, and the not-connected state.

## Route 3: MCP for the AI

- Add the provider's **official MCP server** (or a trusted one) to the AI account when building needs it: reading API docs, testing a query, listing accounts, checking a webhook.
- Sign in through the MCP's own flow. Never paste keys into chat.
- Anything the AI learns there becomes code that uses route 1 or 2. The live app never calls the AI's MCP.

## Choosing a route

| Question | Answer → route |
|---|---|
| Is the provider in the Connector Hub with the action you need? | Yes → **1** |
| Not in the hub, has OAuth or keys, and your platform runs server-side code for apps? | Yes → **2** |
| Not in the hub and no server-side code? | **Platform gap**; offer upload, manual entry or a device bridge |
| Data only on a phone (Apple Health, Health Connect, phone contacts)? | **Device bridge** (`20-one-prompt-to-app.md`) |
| The AI needs it only while building? | **3** |

## Integration plan table (put it in every plan)

| Provider | Data or action | Route | Connected? | Who connects, how | Approvals | Fallback if missing |
|---|---|---|---|---|---|---|
| Meta Ads | Spend, leads, creatives | 1 | Yes | Owner, hub sign-in | None (reads) | Not-connected message |
| Slack | Post daily summary | 1 | Yes | Owner, hub sign-in | "Send message" approved | Copy text instead |
| Apple Health | Daily steps | Device bridge | n/a | Each person, iPhone Shortcut once | None | Manual entry |
