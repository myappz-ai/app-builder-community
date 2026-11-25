# 16. Security and house rules

These apply to every person and every AI working on a micro app.

## Secrets

- **Never generate, copy, display or store tokens, passwords or API keys in chat**, files, code, variables or screenshots.
- Never ask anyone to paste a token into a chat. The owner pastes it straight into the right box (Connector Hub's Access Token field).
- Passwords and 2-factor codes are typed by the person, always.
- Keys an app needs go in **Secrets** (owner only), never in code or public variables.
- If a token leaks, an admin clicks **Revoke tokens** on the Meta system user and the token runbook (steps 5 to 6) is redone.

## Changing things outside the app

- **Ask before** sending a message, replying, posting, deleting, or changing settings in any connected app (Meta, Slack, Gmail, Google Drive...). One exception: a change the owner explicitly asked for.
- Never click Revoke, Remove or Delete in Meta. Never remove people, apps, ad accounts or other Connector Hub apps.
- Never turn off security protections. Never create extra or fake admins to get around an approval rule (Meta's "approved by another admin" cannot be turned off; another real admin approves).
- Apps never delete data in outside apps (the build check refuses delete, remove and archive actions).

## Privacy and masking

- In anything public or shareable (guides, screenshots, share images, docs like this one): **blank out**, do not blur, names, ids, emails, phone numbers, keys and ad account names.
- Phones are masked in in-app lists of buyers.
- Only use Slack or email conversations the requesting person is part of or tagged in. If a connected account belongs to someone else (for example the founder), ignore their private conversations.

## Wording users see

- Always "Connector Hub". Never use the name of the company behind it, even when a tool name or tool answer shows it. "Connect Meta", not "connect to <vendor>".
- Never name the platform vendor inside a white-labelled app; use the agency's brand only when given.
- Plain words; no em dashes in materials written for the owner.

## Links

- Team preview links: `<team-domain>`. User links: `<app-domain>` or the custom domain.
- Never send app users to the platform dashboard or an editor .
- Never build platform links by hand; use the `public_url` a tool returns.

## Data use

- An app works for one sub-account and never reads or guesses another's data.
- Never copy numbers from the account into code; the app reads them live.
- Sub-account data in apps is read-only; what users type goes into app data.
