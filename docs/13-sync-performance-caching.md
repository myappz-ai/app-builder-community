# 13. Sync, speed and caching

Goal: the screen fills instantly with the last known numbers, fresh numbers replace them quietly, and the app never hammers an outside service.

## Stale-while-revalidate, three layers

```
cacheGet(key)  → 1. this tab's memory        (instant)
               → 2. the browser (localStorage, if allowed)
               → 3. the person's own row in app.db "screen_cache" (owner access)
                    so a fresh page load on any device starts from their last numbers
read fresh from the source in the background
cacheSet(key, value) → all three layers (server copy debounced 1.5 s,
                       newest 8 keys, under 250 KB, entries older than 7 days ignored)
```

- Keys include everything that changes the answer: `rows:<project>:<from>:<to>`, `camps`.
- On a failed refresh with saved numbers on screen: keep them and say when they are from. Never replace real numbers with zeros.
- Every storage call wrapped in try/catch (storage can be off in the sandbox).

## Automatic sync

- The dashboard reads Meta again **every 15 minutes** while open, measured from the last read **or the last attempt** (so a failure also waits 15 minutes).
- A tab hidden past the due time catches up when it becomes visible (`visibilitychange`).
- **Sync now** is always available: it bumps a `refreshKey` that every provider listens to, and rechecks connectors.
- A popover shows "Last synced" and "Next automatic sync". The header shows "Synced 3:21 pm" with a green dot, or a warning colour and the reason.
- Sub-account data uses **live events**, not timers (`{ live: ["payment.paid"] }`). Use a timer only for sources with no push signal (Meta).
- After a manual sync, one toast with the outcome; automatic syncs stay quiet.

## Talking to Meta (and any rate-limited service)

- Windows of 7 days, at most 3 in parallel.
- Pages start at 50 rows and halve when the answer is cut.
- Finished days cached in memory; today always re-read.
- Final errors (not connected, rate limited, expired) stop at once, no retry loops.
- Ask Meta for fewer rows: filter by campaign name and by `spend > 0` on Meta's side.
- One provider shared by all pages, so switching pages never triggers a new read.
- Avoid rapid repeated reloads while testing; they cause "too many requests" for everyone using the app.

## Rendering

- No remount on sync: providers update state; pages re-render in place.
- A thin progress bar under the header while refreshing.
- Big lists paged ("Load more") rather than loaded whole.
- The page builder and other heavy parts load only on the screens that need them.
