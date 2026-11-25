# 00. Start here: from a new AI account to your first app

This page assumes nothing. You have a fresh Claude (or ChatGPT) account and access to a sub-account on your platform. By the end you have a project that knows this whole playbook and can build, fix and publish micro apps.

## What you need before you start

| Need | Why | Where to get it |
|---|---|---|
| A login to your app platform with access to the sub-account the app will live in | The app, its data and its connections live in one sub-account | Your agency or super admin |
| Owner or admin role in that sub-account | Publishing, approving data reads and connecting apps need it | Ask the account owner |
| A Claude Pro/Team/Enterprise account (or ChatGPT with Projects) | Projects, files and connectors | claude.ai |
| The **app builder connector** URL for your account | Lets the AI read and edit app code, check it, preview and publish | Your platform team (see 02-connectors) |
| Optional: the Claude desktop app | Lets the AI use a browser on your computer (sign-in pages, Meta Business Settings) | claude.ai/download |

## Step 1. Create the project

1. In Claude, open **Projects** and click **New project**.
2. Name it after the app or the work, for example `Micro apps` or `Ads Hub`.
3. Upload **`PLAYBOOK.md`** to the project's knowledge. This one file is the whole playbook.
4. Open the project's **custom instructions** and paste everything in `templates/project-instructions.md`. Fill the lines marked `EDIT ME` (your name, your sub-account, your link domains).
5. Optional but recommended: upload your **platform add-on** file (see `01-platform-and-stack.md`, last section) so the AI knows your platform's own tool names and settings.

## Step 2. Add the connectors

Go to **Settings, Connectors** and add the ones in `docs/02-connectors.md`. At minimum:

- **App builder connector** (essential): reads and edits app code, compiles, takes pictures, publishes.
- **Your sub-account connector**: reads the account's data and integration status, and runs Connector Hub actions (Meta, Slack, Gmail and more).

Sign in to each one when Claude asks. Then, in a chat, ask:

> List my connectors and tell me which sub-account each one points to.

This matters. Two connectors can have similar names and point at different sub-accounts. The check is in `docs/02-connectors.md`, section "Find out where a connector points".

## Step 3. Start the first chat

Either describe the app you want in one paragraph (one-prompt mode, `docs/20-one-prompt-to-app.md`), or paste the **starter prompt** from `docs/19-prompts.md`. It tells the AI to:

1. Read the playbook.
2. Check every connector and report, in plain words, what works.
3. Ask you what to build (or what to change), then follow the build workflow in `docs/03-build-workflow.md`.

## Step 4. Build in rounds

Every request is one **round**:

1. You say what you want in plain words.
2. The AI notes your ask on the app, reads the files it will change, makes small exact edits, and fixes anything the build check reports.
3. At the end it looks at the app (desktop and phone), fixes what looks wrong, and writes a short hand-over: what works, what data it uses, what is still open.
4. You check the **preview link** (always on the `<team-domain>` domain for the team).
5. When you are happy, say **"publish"**. The AI shows what will go live, then publishes.

## Step 5. Share it

- Give users the **live link** on the client-facing domain (`<app-domain>/app/<slug>` or your own domain).
- Set the app's name and description in the app's settings.
- For WhatsApp previews see `docs/12-metadata-branding-sharing.md`.

## If you are not using Claude

The same files work in ChatGPT Projects and co-work agents. Where a doc names a tool (for example the **preview screenshot** tool), an agent without that tool does the same step in the browser: open the preview link, look at the page, and report. Every doc says what the outcome must be, not only which tool to call.

## How to read the rest

Read 01 to 05 once; they explain the platform and the method. Then use the others as reference while building. `18-case-study-ads-hub.md` is the real example that ties it all together.
