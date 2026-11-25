# 08. UI and UX design

The bar: an app people would pay for, not a template. For a work app (dashboards, lists, forms) the work comes first: clear navigation, every state, small useful motion.

## Look and theme

- **One place for colour:** `src/index.css`, light in `:root`, dark in `.dark`. Start from a preset in `src/themes/` (neutral, signature, universe, corporate, editorial, bold, soft, night) and adjust tokens. Never put colours anywhere else; use tokens like `bg-background`, `text-muted-foreground`, `border`, `bg-primary`.
- **Pick a direction for this business** and commit: type pairing, palette (one dominant family, one accent doing real work), spacing rhythm, one signature element.
- Avoid the AI-default looks: cream + serif + terracotta, near-black + acid accent, reflex indigo/violet.
- Ads Hub: the "signature" preset. Plum primary `#7A2E5C`, gold accent `#F2A93B`, dark ink `#1A1620` for bands, Space Grotesk headings and numbers, Inter body, 16 px radius, 24 px cards.

## Components

- **shadcn/ui only.** Select, Calendar, Popover, Dialog, Sheet, Table, Tabs, Tooltip, Sidebar, Toggle group, Badge, Skeleton, Sonner. Never native selects, date inputs or raw tables; the build check refuses them.
- `Command` only inside a Popover or Dialog, never open in the page.
- **Ready blocks first** (the kit's ~200 blocks and 21 screens), your own components for the rest, eject a block only to change it.
- Icons: lucide-react. No emoji in the UI.

## Every data block has four states

1. **Loading:** a skeleton, at most about 8 seconds, then the error state. Never an endless spinner.
2. **Empty:** one friendly sentence and the next step ("No sessions yet. Upload the Zoom report after the webinar.").
3. **Error:** the platform's own words and a Try again. Keep the last numbers on screen if there are any.
4. **Content.**

## Numbers

- Compact money per currency on cards (`₹65.8K`, `₹2.07 Cr`, `$4.96M`), full value underneath in small text.
- Never a number that cannot be right (a rate over 100%, a negative count). Check the maths or leave it out.
- Never ₹0 or an empty chart when the truth is "not connected" or "failed". Show a dash and the reason.
- Never add two currencies together.
- Tabular numbers (`tabular-nums`) where numbers change in place.

## Navigation and layout (Ads Hub pattern)

- **Sidebar** with grouped navigation (Performance, Ads, Setup), collapsible to icons, a sheet on phones.
- A **badge** on the Connectors item when something needs attention.
- **Sticky header:** current page title, project tag, **date range picker defaulting to Today**, sync status and Sync now, dark mode toggle.
- A thin progress bar under the header while fresh numbers load in the background.
- Hash routes (`#/overview`) so links and back/forward work; old links redirect after pages merge (`#/event` → `#/bf`).
- Merge thin pages into tabs on one page rather than many near-empty pages.

## Feedback and motion

- Every action shows busy, success and error states. Toasts for results (`sonner`), with an action button where useful ("Copy").
- Page entrances `animate-in fade-in slide-in-from-bottom-2`; transform and opacity only; respect `prefers-reduced-motion`.
- No remount on refresh: what is on screen stays while new numbers load.
- Show save state ("Saving...", "Saved") and ask before leaving unsaved changes.

## Lists and tables

Search, status chips, sort, clickable rows, one "..." menu per row. Long names truncate with the full text in a tooltip. Wide tables scroll inside their own box. Export to CSV where the owner needs it (`14-imports-exports.md`).

## Copy

Plain words, written for this business. Say what the thing does and what to do next. No jargon, no internal tool or vendor names (always "Connector Hub"). No em dashes in materials written for the owner.

## The design check after every look

1. Spacing rhythm on a 4/8 px scale; equal gaps in a row.
2. Padding p-4 to p-6 in cards; no text near an edge.
3. Nothing cut off; no short label broken onto two lines; big numbers fit their card.
4. Contrast at least 4.5:1, also on hover and focus.
5. Dark mode reads well everywhere.
6. Every data block has its four states.
7. Motion alive but calm.
8. Phone width: nothing scrolls sideways, nothing overlaps.
