# 09. Responsive on every device, accessible to everyone

Build for phone and desktop from the first line, not at the end.

## The widths that must work

| Width | Device | Check |
|---|---|---|
| 375 px | Phone | Everything stacks, no sideways scroll, touch targets 44 px |
| 768 px | Tablet | Two columns where it helps, sidebar as a sheet or icons |
| 1280 to 1440 px | Laptop, desktop | Full layout, max content width (Ads Hub: 1400 px) |

Verify at the end of the work with a phone-size and a desktop preview screenshot, and in a browser's device view.

## Layout rules

- **Fluid containers:** `max-w-[1400px] mx-auto`, padding `p-3 sm:p-5 lg:p-7`.
- **Grids collapse:** `grid gap-3 md:grid-cols-2 lg:grid-cols-4` for KPI cards; creatives 1 column on phone, 3 per row on desktop.
- **Header wraps:** `flex flex-wrap items-center justify-between gap-2`; less important text hidden on small screens (`hidden sm:inline`).
- **Sidebar** collapses to icons on desktop and becomes a sheet on phones; close it after a tap (`setOpenMobile(false)`).
- **Popovers fit the screen:** width `min(100vw - 1.5rem, 31rem)`, `max-h-[calc(100dvh-5rem)] overflow-y-auto`, `collisionPadding`. The date picker's presets become a 4-column grid on phones and a side list on desktop.
- **Tables** scroll inside their own box (`overflow-x-auto`), never the page.
- **Text** truncates with a title, never pushes the layout wider. `min-w-0` on flex children that hold text.
- Heights with `dvh`, never `vh` for full-screen roots on phones.
- **Sign-in split screen:** brand panel beside the form on desktop, a compact brand bar on top on phones.

## Accessibility

- Real elements: `<button>`, `<a href>`, `<form>`, `<label>` + input. Never click handlers on a div.
- `aria-label` on icon-only buttons ("Toggle dark mode", "Sync now", "Open menu").
- Progress indicators with `role="progressbar"` and a label while active; `role="status"` and `aria-live="polite"` on loading screens.
- Contrast 4.5:1 for text, 3:1 for large text and UI parts, also in dark mode and on hover.
- Colours that must be told apart also differ in lightness, not only hue.
- Keyboard: Tab reaches everything, Enter submits forms, focus lands on the first field of a form.
- Sign-in fields with `autocomplete="email"`, `current-password` and `new-password`, so browsers and password managers save logins.
- Respect `prefers-reduced-motion` (`motion-reduce:animate-none`, `motion-safe:`).

## The sandbox

Apps run inside a sandboxed frame. That affects:

- **Downloads:** a normal download link is blocked; see `14-imports-exports.md`.
- **Navigation:** open platform pages (a booking page, a payment link) in a new tab with `target="_blank" rel="noopener"`, never in the app frame.
- **Clipboard:** use a hidden textarea and `document.execCommand("copy")` first, then the Clipboard API.
- **Storage:** `localStorage` may be off; wrap every read and write in try/catch.
