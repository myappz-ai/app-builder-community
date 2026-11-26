# 22. Use the platform, not the app

The app builder already has preview, versions, storage, secrets, connections, permissions and custom domains. The sub-account already has payments, invoices, email sending and workflows. Build only what those cannot do. This lesson comes from a live shop: online checkout worked, but the order still looked unpaid, and the app had started to grow its own domain, payment-key and email screens.

## Do not rebuild the app builder

| The app builder already has | Do not build in the app | Do this instead |
|---|---|---|
| Publish, Connect a domain | A Domain tab, or a domain field saved in app data | Point the owner to Publish, Connect a domain. Show the live link as read-only, with Copy |
| Versions and restore | A change history or undo of the code | Versions in the app builder |
| Preview | A preview-mode toggle | The app builder preview |
| Storage | A file bucket of your own | Platform storage. Keep large images out of app data rows where you can |
| Variables and Secrets | API keys in app data or a settings screen the storefront can read | Secrets in the app builder (for example a courier API password). Never put them in a collection the public app can list |
| Plugins, marketplace, connections | "Connect the payment gateway / email / WhatsApp" forms | Sub-account connections. The app can read connection status and tell the owner to connect; it never collects a key |
| App settings, Permissions | A role editor for platform actions | The Permissions screen (who may start a checkout, send email, and so on) |

Custom domains are a platform action (add, show the DNS records, verify, attach). Never store the domain only in app data and never send people to a dashboard link you invented.

## Payments go through the platform

- What you sell online are the sub-account's payment products. The app maps each shop item to a product id and never sends a price, amount or total. Keep the prices shown in the app the same as the product prices, because the server charges the product price.
- Save the app's own order first (lines, contact, unpaid). Then start the platform's in-app checkout for that order, with the product lines, the customer, and a link to the order row. A delivery charge is its own product line, not a fee the app adds.
- When the payment succeeds, the platform is supposed to mark that order row itself. Show "Paid" from that mark, never from a field the app sets, and never give staff a "Mark paid" button for online payments.
- Keep the checkout's payment reference on the order. Without it you cannot read the payment status again if the shopper closed the app, or if the mark did not land.
- One helper should decide the status for every screen (admin list, customer orders, confirmation, tracking, receipt): the platform mark first, then a signed staff link to a matching successful payment in sub-account transactions, then a live status read. Shoppers and staff must see the same words, including the gateway name and the payment reference when you have them.

### If the mark never arrives

This happened on a real one-item checkout: the payment succeeded in the sub-account's transactions, but the order row was not marked paid, so the admin list said "pending" and the thank-you page asked the shopper to pay again. Multi-item checkouts on the same app kept the link. Treat a missing mark as a platform gap and report it, but do not leave the shop broken:

- Staff (only) may read successful payments from sub-account data and match them to unpaid online orders: exact payment reference first, otherwise the same amount paid shortly after the order was placed. Save the link as a signed staff event, not as a field the browser invents.
- Until that link is saved, a live status read on the stored payment reference (and the `payment.paid` signal) can still show Paid on the confirmation page.

### Unpaid online orders are not sales

An abandoned checkout is not revenue and is not ready to ship. Exclude unpaid online orders from revenue, "to ship" and dashboard totals. Hold their stock only for a short window (for example one hour), then release it.

If the app uses hash routes (`#/order/...`), read the checkout result from the hash query (`#/order/ID?pay=paid`), not from `window.location.search`. The page search string is empty on a hash route, so a thank-you page that reads it will miss a successful payment.

## Receipts

- Give every order a receipt route in the app, styled for print (hide on-screen buttons when printing). The person uses Print, Save as PDF. Do not open a blank window and write HTML into it: sandboxed previews block it, and it will not match the store theme.
- One HTML body with inline styles can feed both the printed receipt and an email.
- Successful platform payments often already create an invoice in the sub-account. Sending that invoice, or a receipt email, is a platform action. It may come back as `pending_approval`: show "Waiting for approval", never "sent".

## Email after a payment

- Check the sub-account's email-sending connection first (list its SMTP or email connections).
- Automatic customer emails belong in a platform workflow (a payment-received or invoice-paid trigger, then a send-email step), not in app code that runs only while someone has the shop open.
- A payment-received trigger is usually account-wide. Create the workflow as a draft and let the owner publish it, after they have confirmed it should run for every such payment in the sub-account, not only for this app.
- Owner alerts ("invoice paid") live in the sub-account's notification settings, not in the app.

## Customer details when collections are only owner, public or private

Staff must see every order, so the orders collection is often `public`. That would leave names, phones, emails and addresses readable to anyone who can load the app. Until the platform offers a staff-only collection access level, seal those details in the shopper's browser with a store key, and sign staff changes so the storefront can trust them. Explain this in plain words (a Security tab, not a "data lock" that sounds like a block). Set the key up once. Do not block checkout after it exists. Say in the hand-over that a staff-only access level would let this layer go.

## Checklist (add these to the feature checklist)

- [ ] No Domain, Versions, Secrets or Connections screens that copy the app builder
- [ ] Online pay: product ids only (no prices sent); payment reference saved; Paid comes from one helper; unpaid online orders excluded from revenue, to-ship and stock
- [ ] Receipt route that prints or saves as PDF; email goes through a platform action, with "Waiting for approval" when needed
- [ ] Payment emails via a platform workflow (draft first); email-sending connection checked
- [ ] Keep "start a checkout" on in Permissions if guests may pay

## See also

- Data sources and live payment events: `05-data-layer.md`
- Custom domains and sharing: `12-metadata-branding-sharing.md`
- Secrets and what the AI must never do: `16-security-and-rules.md`
- Troubleshooting rows for a missing payment mark, a hash-route thank-you page, and a duplicated Domain tab: `17-troubleshooting.md`
- Connector Hub vs direct API vs MCP: `21-integration-routes.md`
