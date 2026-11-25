# 12. Metadata, branding and sharing

Everything that makes the app look like a product outside its own screens: its name, description, logo, favicon, browser tab, share previews and web address.

## Where each piece lives

| Piece | Where it is set | Notes |
|---|---|---|
| App name | the app builder, Settings, General, **Name** | Shown in the app list, editor header and browser tab title |
| Description | the app builder, Settings, General, **Description** | Internal ("only you see this") |
| In-app name | Code: sidebar header, sign-in `BRAND.appName`, preloader | Change all three together |
| Logo mark | Code (inline SVG or the sign-in block's mark) | Keep one source of truth for the mark |
| Tagline | Code: sign-in `BRAND.tagline` | Global wording; no country-only words if the product is global |
| Public variables | Settings, Advanced, App text | Editable text without code changes |
| Web address (slug) | Settings, **Web address** | Changing it breaks links already shared |
| Custom domain | Settings, Web address, Add domain (CNAME to the host the screen shows) | Verify, then test the live link |

## Renaming an app (checklist)

1. Code: sidebar name, sign-in `appName`, preloader name, logo letters or mark, quote credits.
2. Settings, General: Name, then Description.
3. Publish the code change (preview first).
4. Decide on the web address: keep the old slug so shared links keep working, or change it and tell users.
5. Update any share image and the docs.

## Share previews (WhatsApp, LinkedIn, Facebook, Slack)

Share previews are built by crawlers that read the **raw HTML** of the link. They do **not** run JavaScript. So the preview needs these tags in the HTML the server sends:

```html
<title>Ads Hub</title>
<meta name="description" content="Live Meta ads, leads, sales and webinars in one dashboard.">
<meta property="og:type" content="website">
<meta property="og:title" content="Ads Hub">
<meta property="og:description" content="Live Meta ads, leads, sales and webinars in one dashboard.">
<meta property="og:image" content="https://<public-host>/ads-hub-share-1200x630.png">
<meta property="og:url" content="https://<app-domain>/app/<slug>">
<meta name="twitter:card" content="summary_large_image">
```

- **Image:** 1200 x 630 px PNG or JPG, under 300 KB, on a public HTTPS URL. Big title, short line, logo; readable when shrunk to a phone thumbnail. Example mark: `assets/ads-hub-mark.svg` (place it on a 1200 x 630 canvas with the app name and one line).
- **Title** under 60 characters, **description** under 155.
- WhatsApp caches previews. After a change, test with a new link (`?v=2`).

### Platform status (checked on the Ads Hub build)

The platform serves `/app/<slug>` with **empty** `og:title`, `og:description`, `og:image` and an empty `<title>`; the name appears only after JavaScript runs. App code cannot fix this. The platform fix:

1. On the server, for `/app/<slug>` and custom domains, fill `<title>`, `description`, `og:*` and `twitter:*` from the app's **Name** and **Description**.
2. Add a **Share image** upload to the app's settings (General), and serve it as `og:image` (fallback: a generated image with the app name).
3. Set `twitter:card` to `summary_large_image`.

Until then: share the link with a short line of text, or share the image itself.

## Favicon and app icon

- Favicon: a simplified mark (thicker strokes, fewer details) that reads at 16 to 32 px. SVG preferred.
- App icon (home screen): the full mark on its colour square, 512 x 512 PNG.
- The platform currently serves a shared `/favicon.svg`; a per-app favicon is part of the same platform fix.

## Logo

Ads Hub's mark: a plum rounded square with a hub and spokes to ads, leads and sales; one gold spoke for "the one that paid". Wordmark in Space Grotesk. Variations: main on white with tagline, reversed on dark, app icon, favicon. Keep the mark's colours in the theme tokens so app and logo stay in step.

## Global wording

If the product is sold outside one country: no country-only phrases ("every rupee"), currency from the account's settings, dates and numbers formatted with the account's locale, tax lines only where the account has a tax setting.
