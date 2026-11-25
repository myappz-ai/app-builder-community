# For AI agents

You are helping someone build a micro app on [Your Platform] (any AI-friendly app builder with sub-accounts). Read in this order:

1. **PLAYBOOK.md**: the whole playbook in one file, attached to the latest release: `https://github.com/myappz-ai/micro-app-builder/releases/latest/download/PLAYBOOK.md`. Read it fully before acting. If you cloned the repository, read the files in `docs/` in order instead (same content).
2. **[templates/project-instructions.md](templates/project-instructions.md)**: the working rules to follow in every chat.
3. If the person describes an app in one paragraph, follow **[docs/20-one-prompt-to-app.md](docs/20-one-prompt-to-app.md)**.

Before building anything:

- Check that you have the **app builder connector** and the **sub-account connector**. If either is missing, tell the person they need a sub-account and both connector links, and stop there. Never ask for passwords, tokens or keys.
- Address the person's business as their **sub-account**. Each app works inside one sub-account only.
- Call the outside-app connection layer the **Connector Hub**. Never use any other vendor or platform name for it.
- Ask before sending, posting, deleting or changing anything in a connected app. Publish only when the person asks.
