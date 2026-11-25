# Connector check: <app>, <date, time>

| # | Check | Call | Result | Fix if not OK |
|---|---|---|---|---|
| 1 | App is live, which version, unpublished changes | **live status** | | Publish when asked |
| 2 | Which workspace each AI connector points to | **integration status** (look at the links it returns) | | Rename or use the right connector |
| 3 | Connector Hub apps the app uses are active | **list Connector Hub connections** | | Owner reconnects in the workspace's Connector Hub |
| 4 | Outside app answers | one tiny read, e.g. Meta **Insights** (`GET /{ad-account}/insights`) today, account level | | Token runbook / reconnect |
| 5 | Platform integrations the app uses; required apps missing | **integration status** | | Owner connects the app |
| 6 | Workspace data readable | one `count_only` query per object the app uses | | Approve in Publish / check role |
| 7 | Syncs still fresh (e.g. Zoom latest join) | latest row query | | Reconnect or use uploads |

Summary in plain words: what works, what does not, the one-line fix for each.
