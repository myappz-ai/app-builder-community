# 03. The build workflow: one round, every time

Every request, small or large, is one **round**. The round keeps the app safe, the history readable and the owner informed.

## The round

```
1. find the app        list apps (or create one)
2. note the ask        record the user's own words on the app, and which AI is working
3. read                list files, then read EVERY file you will change
4. change              a small exact edit, or write a new / fully replaced file
                       always pass the version you last read
5. build check         every save returns a new version and a check; a failure is the next job
6. look                preview screenshot at the END only (desktop, then phone, each journey)
7. fix                 what looks wrong; look again until no design issues are left
8. hand over           a short plain summary, always the last step, also when stopping early
9. publish             only when the user says so: preview first, then confirm
```

Good builders refuse changes until the request is noted for that app in this round; follow that even where the platform does not enforce it. A new request is a new round.

## Rules inside a round

- **Audit before building.** Read what exists before deciding what to change. Never write over a file you have not read.
- **One change at a time.** Small exact edits (replace one exact piece of text). Rewrite a whole file only when it is new or truly replaced.
- **The last-read version on every save.** If someone else changed the app, the save is refused and you read again. Nothing is overwritten silently.
- **A failed build check comes first.** Fix exactly what it names and save again. Never say "it works" while the check fails.
- **Pictures at the end, not during.** The preview screenshot is slow. Take it once the work is finished: walk each person's main journey, check the phone size where layout matters, fix every design issue, look again.
- **Behind a sign-in:** use a test user (for example an admin role that exists only in the screenshot) rather than a real account.
- **Links:** every link the app sends people to is checked with a **link check** in the same round.
- **Code belongs in files, not in chat.** Give the user the preview link.

## The hand-over note

Short, plain words. In this order:

1. What now works (screens, saved data, forms).
2. Which workspace data it reads.
3. Anything invented as a placeholder.
4. What is still open, and what the owner must do (approve a query, connect an app, publish).

Template: `templates/handover-template.md`.

## Publishing

- Publish **only when the user asks** in this conversation, never because work is finished.
- **live status** says what is live and whether there are unpublished changes.
- **publish** **without** confirm shows a preview (nothing changes). Show it, get a yes, then **publish** again with confirm.
- If the answer says workspace data needs approval, nothing went live: the owner approves the listed queries in the app builder's Publish screen, then you publish again.
- After publishing, open the live link and confirm the change is there.

## Rollback

**version history** shows history; **restore a version** brings an older version back as a new version. Publishing is separate, so a restore is safe to try in preview first.

## Working with someone else in the app

The owner (or another AI) may change the app between your rounds. That is why every round re-reads files and passes the last-read version. If a save is refused, read again, redo your change on the new text, and continue.

## When the AI has no app builder tools

Do the same steps in the app builder's editor: the **Code** tab to read and edit, **Versions** to go back, **Preview** to look, **Publish** to go live, **Settings** for name, description, variables, web address and permissions. The rules do not change.
