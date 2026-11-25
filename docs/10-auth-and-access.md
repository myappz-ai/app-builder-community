# 10. Sign-in and access

## The app opens on its login screen

Any app with accounts opens on the **login screen**, never a public page. On every load check `app.auth.user()` first and go straight in if the person is already signed in. Never make someone sign in again because they came back.

## The pieces (all ready-made, never hand-built)

| Need | Use |
|---|---|
| Email sign-in / sign-up screen | The kit's `signin-split` block (eject it to customise copy and points) |
| Forgot password | `ForgotPasswordForm` from `@/components/auth/ForgotPasswordForm` |
| Reset from the email link | `ResetPasswordForm` when `app.auth.resetToken()` returns a token |
| WhatsApp code sign-in | `WhatsAppSignIn` when `app.auth.methods()` says WhatsApp is on (the platform default for new apps) |
| Loading screen while checking | A small branded preloader with `role="status"` |

## The Ads Hub auth gate (pattern)

```tsx
const BRAND = { appName: "Ads Hub", tagline: "Know which ads bring in money.", google: false, password: true, allowSignup: true };

export function AuthGate({ children }) {
  const [user, setUser] = useState(undefined);            // undefined = still checking
  const [mode, setMode] = useState(() => app.auth.resetToken() ? "reset" : "signin");
  useEffect(() => { app.auth.user().then(u => setUser(u ?? null)).catch(() => setUser(null)); }, []);
  if (user === undefined) return <Preloader />;
  if (user) return children(user, async () => { await app.auth.signOut(); setUser(null); });
  // reset or forgot screens, else the split sign-in wired to app.auth.signIn / signUp
}
```

Rules:

- One call per button: sign-up form calls `signUp`, sign-in calls `signIn`. Never chain them to hide an error.
- Show the error text as is ("The password must be 8 to 72 characters.").
- After success, move off the form with `history.pushState` so the browser offers to save the password.
- Busy state on the button, show/hide password, Enter submits, focus on the first field.
- Never write a password, admin login or key into code. Browser code is public.

## The app's admin

An app with sign-in gets **one admin**: its first person. Ask the owner once which email the admin uses, then **create the app admin**. Never repeat or store the password. Others who sign up are normal users; the owner gives roles in the app's Dashboard, Users.

## Who sees what

- **Staff screens** check `(await app.auth.user())?.role === "admin"` (or `staff`). Use only those two role names for staff.
- **Sub-account data** answers only for signed-in members of the account inside the platform.
- **Ad numbers** from Meta are visible to the app's staff by default. Opening them wider needs the owner's explicit ask (the **access roles setting**).
- **Platform actions** that touch other people's data run only for staff; plain users act on their own rows only (`NOT_YOURS`, `ROLE_NOT_ALLOWED` otherwise). Show: "Ask the app's admin to let your role do this." / "You can only change your own."
- **Outside-app actions** are approved one by one by the owner in the app's permissions. Approving one never allows another.

## Sign-up on or off

`allowSignup: true` lets the team self-register. For a closed internal tool turn it off: the screen then says "Access is by invitation. Ask your admin to add you." Change WhatsApp or email login only when the owner asks (the **app login setting**).
