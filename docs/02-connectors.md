# 02. Connectors: what connects to what

Three different kinds of connection are involved. Mixing them up is the most common source of confusion.

| Layer | Lives in | Used by | Examples |
|---|---|---|---|
| **AI connectors (MCP)** | Your AI account (Settings, Connectors) | The AI, while building | App builder connector, workspace connector, provider MCPs (ads, docs, GitHub), email, chat |
| **Platform integrations** | The workspace's settings | The platform and apps | Payment gateway, video meetings, email sending, WhatsApp Business, social pages, AI models |
| **Connector Hub** | The workspace's settings | Apps and the AI | Ads accounts, Slack, Gmail, Google Drive, Stripe, GitHub, CRMs... |

> Naming rule: always call it the **Connector Hub**. Some tool names and tool answers carry the name of the company behind a hub; never repeat that name to anyone. Say "Connect Meta", not "connect to <vendor>".

How an app integration should be done (Connector Hub, direct API or MCP) is in `21-integration-routes.md`.

## AI connectors to add

| Connector | Needed for | Priority |
|---|---|---|
| **App builder connector** | List apps, read and edit files, build check, preview screenshot, versions, variables, publish | Essential |
| **Workspace connector** (one per workspace) | Integration status, Connector Hub connections and reads, workspace data (payments, forms, contacts) | Essential |
| **Connector Hub manager** | Managing hub connections (list, add, set default) | Useful |
| Provider MCPs (ads platforms, developer tools) | Direct reads and diagnostics while building | Optional |
| Email, files, calendar, chat | General work around the project | Optional |

Add each in your AI account's connector settings with the server URL your platform gives you, then sign in. Never paste a key into chat to "add" a connector.

## Find out where a connector points

Connector names are chosen by people and can mislead. Before trusting one:

1. Ask it for the workspace's **integration status**. The links in the answer contain the workspace id and domain. That is the workspace it reads.
2. Ask it to **list Connector Hub connections**. "No key" means that workspace has no hub set up, so no outside apps can run there.
3. Compare with the app's workspace (shown in the app builder).

Real example: a connector named after one business pointed at a different workspace with no hub key, while a connector with a generic name was the app's real workspace. Rename connectors so the name matches where they point.

## Connector check (start of every new chat)

1. **Live status:** is the app live, which version, unpublished changes?
2. **Hub connections:** is every hub app the app uses active?
3. **One tiny read** from each outside app (for ads: today's spend at account level).
4. **Integration status:** platform integrations connected; any **required** one missing.
5. Report in plain words: what works, what does not, the one-line fix for each.

Template: `templates/connector-check.md`.

## Several connections of one app

One hub app (for example an ads account) can hold several connections. Usually **the newest becomes the default**, and apps use the default. Old ones (expired tokens) can be removed by the owner, but never remove the default.

## When a check fails

- "Hub not reachable" on a status check: usually a one-off. Check again before assuming anything is broken.
- "No key": set up the Connector Hub in that workspace's settings, or use the connector for the right workspace.
- Ads "login has expired" or OAuth error 190: the token expired. Follow `07-meta-token-runbook.md`.
- "Rate limited" or "too many requests": wait a minute; never retry in a loop.
