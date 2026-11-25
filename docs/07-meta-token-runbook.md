# 07. Meta token runbook: a token that never expires

Use this when a dashboard says "Meta's login has expired", or when connecting Meta Ads to a new workspace. It can be followed by a person, or pasted into a browser-capable AI agent that does every click while the person only signs in, clicks Generate and Copy, and pastes into one box.

Background: personal Meta user tokens expire every 60 days. A **system user token** with expiry set to **Never**, made from an app that has the **Create & manage ads with Marketing API** use case, does not. Apps made for other use cases (for example an Instant Game app) can never be used and cause "No permissions available".


**How to use this file:** paste this whole file into an AI agent that can use a web browser (Claude with the browser or computer use, ChatGPT agent mode, a co‑work agent, etc.) and say **"Do this for me."** The agent does every step. You only:

1. **Log in** when a page asks (Facebook / the platform).
2. Click **Generate token** and **Copy** when the agent asks.
3. **Paste** the token into one box when the agent asks.

Takes about 10 minutes. You do it once; the token never expires.

---

## 0. Instructions for the AI agent (read fully before acting)

You are connecting a business's Meta (Facebook) ad account to its dashboard with an access token that **never expires**. Work in the user's own browser, where they are signed in to Facebook and to the platform. Do every click yourself, check each result, and only stop for the four hand-offs listed in **0.2**.

### 0.1 Values to collect first (ask the user only what you can't find)

| Name | How to get it |
|---|---|
| `BUSINESS_NAME` | Ask: *"Which Meta business portfolio owns the ad account?"* |
| `AD_ACCOUNT_NAME` | Ask: *"Which ad account should the dashboard read?"* |
| `BUSINESS_ID` | Find it yourself: open https://business.facebook.com/settings/system-users, pick `BUSINESS_NAME` in Meta's business picker, and read `business_id=` from the address bar |
| `APP_NAME` | Use **Ads Connector**, unless the user prefers another name |
| `SYSTEM_USER` | Whichever system user already exists on the System users page; if none, create one called **Connector Hub** (role Admin) |
| `PLATFORM_URL` | Your platform's admin link (the user logs in). The Connector Hub is in the workspace's settings |
| `DASHBOARD` | Ask the user which dashboard/app to check at the end, or open it from the platform after login |

Keep these values only in your working memory for this task. Don't repeat IDs or names back to the user more than needed, and never put them in files you create.

### 0.2 Hand-offs (the only times you stop and ask the user)

1. **Login / password / 2-factor code**: any login or "re-enter your password" screen. Say: *"Please sign in on the open page, then tell me 'done'."* Never ask for, read, or type a password or code.
2. **Second-admin approval** (only if Meta shows it: see step 5).
3. **Generate + Copy**: in step 5, after you have selected everything, say: *"Click the blue **Generate token** button, then click **Copy**. Don't paste it in this chat."*
4. **Paste**: in step 6, when the small window with the **Access Token** box is open, say: *"Click the Access Token box, press Ctrl+V (Mac: Cmd+V), then click **Connect Account**. Tell me 'done'."*

### 0.3 Safety rules (always)

- **Never** ask the user to paste the token into the chat. Never read it aloud, copy it, store it, screenshot it, or type it yourself.
- **Never** click **Revoke tokens**, **Remove**, **Delete**, or change anything not listed here.
- **Never** remove other people, apps, ad accounts, or other Connector Hub apps.
- Do not turn off security settings.
- If a screen doesn't match what's described, take a screenshot, describe it to the user in one line, and ask before going on.
- Meta pages load slowly. Wait 2–4 seconds after each click before reading the page.
- **Every Business Settings link must contain `?business_id=BUSINESS_ID`.** Without it Meta shows "Sorry, this content isn't available" or a business picker.

---

## 1. Check access (1 minute)

1. Open `https://business.facebook.com/latest/settings/business_users?business_id=BUSINESS_ID`.
   - Login page → hand-off 1.
2. Find the user's own row (marked **(you)**). It must say **Full access · Everything**.
   - If not, stop and tell the user: *"You need full control of BUSINESS_NAME. Ask an admin to give it to you in Business Settings → People."*
3. Note the other people with **Full access** and recent "Last active" dates. You may need one of them in step 5.

## 2. Create the ads app (3 minutes)

**First check whether a suitable app already exists:**

1. Open https://developers.facebook.com/apps/ and look for `APP_NAME` (or any app owned by `BUSINESS_NAME`).
2. If one exists, open it → **Use cases**.
   - If it lists **"Create & manage ads with Marketing API"**, reuse it and skip to step 3.
   - Apps made for something else can **never** be used. For example, "Launch an Instant Game" or "Authenticate … with Facebook Login": they produce the **"No permissions available"** error, and ads use cases can't be added to them.

**Create the app:**

1. Open https://developers.facebook.com/apps/creation/.
   - An intro pop-up "There's a new way to create apps" may appear. Its **Create app** button only closes it.
2. **App details:**
   - **App name** = `APP_NAME`.
   - Leave the email as it is.
   - Click **Next**.
3. **Use cases:**
   - Tick **Create & manage ads with Marketing API**. It's the first card; the tick is on the right.
   - Other cards turning grey is expected.
   - Click **Next**.
4. **Business:** select `BUSINESS_NAME` → **Next**.
5. **Requirements:** **Next**. It normally says "No requirements".
6. **Overview:** check it shows `APP_NAME`, the Marketing API use case and `BUSINESS_NAME` → click **Create app**.
   - Password prompt → hand-off 1.
7. You land on the app dashboard. The address is `developers.facebook.com/apps/<APP_ID>/dashboard/…`. Note `APP_ID`.
8. **Verify:** click **Customize the Create & manage ads with Marketing API use case**. These three must show **"Ready for testing"** (or "Advanced access"):
   - `ads_management`
   - `ads_read`
   - `business_management`

   If any shows **Add**, click **Add** for it.

## 3. Give the system user the app (1 minute)

1. Open `https://business.facebook.com/latest/settings/system_users?business_id=BUSINESS_ID`.
   - If there is **no system user**:
     1. Click **+ Add**.
     2. Name: **Connector Hub**. Role: **Admin**.
     3. Click **Create**. If Meta asks for approval, use the step 5 approval flow.
   - Use that system user's name as `SYSTEM_USER` below.
2. Open `https://business.facebook.com/latest/settings/apps?business_id=BUSINESS_ID` and click `APP_NAME` in the list.
3. Click **Assign people**.
4. In the dialog:
   1. Type part of `SYSTEM_USER` in the search box and tick it.
   2. On the right, under **Full access**, switch on **Manage app**.
   3. Click **Assign**, then **Done**.
5. **Verify:** the app's **People** list now shows `SYSTEM_USER` with Full access.
   - If not, repeat; the Assign didn't save.

## 4. Give the system user the ad account (1 minute)

1. Open `https://business.facebook.com/latest/settings/system_users?business_id=BUSINESS_ID` and select `SYSTEM_USER`.
2. Scroll the right panel to **Ad accounts**. If `AD_ACCOUNT_NAME` is already listed with Full access, skip to step 5.
3. Otherwise:
   1. Click **⋯** (next to Revoke tokens).
   2. Click **Assign assets**.
   3. On the left, click **Ad accounts**.
4. In the dialog:
   1. Tick `AD_ACCOUNT_NAME`.
   2. Under **Full access**, switch on **Manage ad accounts**.
   3. Click **Assign assets**, then **Done**.
5. **Verify:** the system user's **Ad accounts** section lists `AD_ACCOUNT_NAME`, and its **Apps** section lists `APP_NAME` with Full access.

## 5. Make the never-expiring token (2 minutes)

1. On the same System users page with `SYSTEM_USER` selected, click **Generate token** (top right of the panel).
2. Work through the dialog:
   1. **Select app:** open the list and choose **`APP_NAME`**, not any older app. Click **Next**.
   2. **Token expiry:** choose **Never**. Click **Next**.
   3. **Assign permissions:** open **Select permissions** and tick `ads_management`, `ads_read` and `business_management`. It should say "3 options selected".
3. **Stop → hand-off 3.** The user clicks **Generate token**, then **Copy**. Meta shows the token only once; suggest they also save it in a password manager.

**If Meta says "this request must be approved by another admin":**

- This is Meta's rule for businesses with heightened security, and it **cannot be turned off**. Do not create extra admins to get around it.
- Give the user this message to forward to one full-access admin from step 1:

  > Hi, please approve my request to generate an access token in Meta Business Suite (BUSINESS_NAME). It's in your Facebook / Business Suite notifications (or email from Meta). Check it says system user "SYSTEM_USER" and app "APP_NAME", then tap Approve. Thanks!

- When the user says it's approved:
  1. Reload the System users page and select `SYSTEM_USER`.
  2. A green box **"Access token generation approved"** appears with a **Generate token** button.
  3. Hand-off 3: the user clicks that button, then **Copy**.
  4. If it asks for app, expiry and permissions again, choose the same as above.

**If you see "No permissions available":**

- The selected app has no ads use case → go back and pick `APP_NAME`.
- Still empty → step 2's verify or step 3 was not done. Fix that, close the dialog, and try again.

## 6. Put the token into Connector Hub (2 minutes)

1. Open `PLATFORM_URL` (login → hand-off 1), then open the workspace's **Connector Hub** settings.
2. In **Search your apps**, type **Meta Ads**. If a **Meta Ads** card shows under **Connected**, click **Disconnect** on it.
   - This only switches the old (expired) connection off for this page.
   - Without this step, the new token can't be added.
3. In **Search all apps** (lower on the page), type **Meta Ads**. Point at the **Meta Ads** card and click **Connect**.
   - A small window opens with an **Access Token** box. It may open in a new tab.
   - **If your browser blocks pop-ups**, ask the user: *"Please click the green **Connect** button on the Meta Ads card yourself."*
4. **Hand-off 4:** the user pastes the token into **Access Token** and clicks **Connect Account**.
5. Back on the Connector Hub tab, click **I've connected it** (the button that replaced "Check connections").
6. **Verify:** the page says **"Meta Ads connected"**, and the **Meta Ads** card is back under **Connected** with **Active**.
   - If not, wait 10 seconds and click **Check connections**.

## 7. Check the dashboard (1 minute)

1. Open `DASHBOARD` (login → hand-off 1).
2. Click **Sync now** (top right) and wait about 20 seconds.
3. **Done when:**
   - The orange note **"Meta's login has expired"** is gone.
   - The top bar shows **Synced <time>** with a green dot.
   - **Ad spend** shows today's amount.
   - **Creatives** loads ad cards.
4. Tell the user: *"Connected with a token that never expires. Nothing else to do. Keep the token in your password manager; if it ever leaks, an admin can click **Revoke tokens** on the system user and we redo steps 5–6."*

---

## Troubleshooting

| What you see | What it means | Do this |
|---|---|---|
| "Sorry, this content isn't available" on business.facebook.com | Link is missing `business_id` | Add `?business_id=BUSINESS_ID` to the link |
| "No permissions available" when generating the token | Wrong app, or app has no Marketing API use case | Pick `APP_NAME`; check step 2 verify and step 3 |
| "Must be approved by another admin" | Meta security rule for this business | Forward the step 5 message to another full-access admin |
| "Generate token" is grey or missing | User is not an admin of the business | An admin gives them **Full control** in People |
| Dashboard: "Meta's login has expired" | The connected token has an end date or was revoked | Redo steps 5–6 with **Never** |
| Dashboard: "Meta Ads is switched off" or "not connected" | Meta Ads was disconnected in Connector Hub | Step 6.3–6.6 (Connect → paste → I've connected it) |
| Dashboard shows ₹0 / no ads, no error | System user can't see the ad account | Step 4, then redo steps 5–6 |
| Create app asks to verify the business | Wrong business picked | Pick the one marked "Business verification complete" |
| Clicking Connect does nothing | Pop-up blocked | User clicks **Connect** themselves, or allow pop-ups |

## If you (the agent) have no browser

Walk the user through these steps one at a time. Give each link as a clickable link, say exactly which button to click, and wait for "done" before the next step. Keep messages to 2–3 lines.
