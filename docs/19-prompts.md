# 19. Prompts

Copy these into a chat in the project. Replace anything in `<angle brackets>`.

## Starter prompt (first chat in a new project)

```
Read PLAYBOOK.md in this project fully before doing anything. Follow it as the way we work.

Context:
- Sub-account: <sub-account id or name>
- App (if it exists): <app id or name>. If it does not exist yet, say so and wait for my brief.
- Team preview links on `<team-domain>`; user links on `<app-domain>` or our domain.

First task: run the connector check from docs/02-connectors.md (the app builder live status, Connector Hub
connections, one tiny read from each outside app the app uses, platform integrations, and which
sub-account each connector points to). Tell me in plain words what works and what needs fixing.
Then ask me what to build or change.
```

## One prompt: just describe the app

```
Build this app: <one paragraph, e.g. "a personal health tracker where everyone in my family tracks
their steps, connected to the Health app on their iPhones">.

Follow PLAYBOOK.md doc 20: discover every source through the platform and the Connector Hub,
classify each one, show me the feature checklist and connection plan, connect what is needed
with sign-in links I open myself, use a device bridge for phone-only data, then build, verify
and hand over. Ask at most one question.
```

## Build a new app (step by step)

```
New app: <one-paragraph brief: who uses it, what they need to see or do>.
Follow docs/04-product-planning.md: explore the platform first, look at the real data, then show me
the plan and the feature checklist before building screens. Build backend first, then screens,
mobile and desktop from the start. Open on the login screen. Hand over when the checklist is done.
```

## Change something small

```
In <app>, change <exact thing> to <new thing>. One change only. Read the file first, keep everything
else as it is, show me the preview link. Do not publish.
```

## Add a data source

```
Add <source, e.g. Google Ads spend> to <page>. Check whether it is a platform module, sub-account data,
or a Connector Hub app. Look at a real answer first, then wire it with all four states and a
not-connected message. Tell me which approvals I need to give.
```

## Fix wrong numbers

```
<Card/number> on <page> shows <x> but <source> shows <y> for <period>. Audit before changing:
read the code that computes it, read the source directly for the same period in the account's
timezone, explain the difference, then fix it with the smallest change.
```

## Responsive and design pass

```
Do a design pass on <app>: look at every page on desktop and phone, list what fails the design
check in docs/08-ui-ux-design.md, fix them one by one, and show me before/after.
```

## Publish

```
Publish <app>. Show me the preview of what goes live first.
```

## Rename or rebrand

```
Rename <app> to <new name> everywhere: in-app name, logo letters, sign-in, preloader, the app builder
name and description. Keep the web address unless I say otherwise. Update the share image.
```

## Reconnect Meta (expired token)

```
The dashboard says Meta's login has expired. Follow docs/07-meta-token-runbook.md in my browser.
I will only sign in, click Generate and Copy, and paste into the box. Never ask me for the token.
```

## Handover to a new chat or account

```
Write a complete handover for <app> following templates/handover-template.md: ids and links,
connectors and their status, structure, data flow, rules, open items, key numbers for sanity
checks, and a starter prompt. No secrets.
```
