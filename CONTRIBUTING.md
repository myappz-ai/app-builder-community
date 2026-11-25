# Contributing

Thank you for improving the playbook. It is used by people and by AI assistants, so clarity matters more than length.

## How to change something

1. Edit the doc in `docs/` (or a template in `templates/`). Never commit `PLAYBOOK.md` or the PDF: CI builds them and attaches them to each release.
2. Optional: rebuild the single file locally with `python3 scripts/build_playbook.py`. CI checks that it builds on every push and pull request.
3. Run the check: `python3 scripts/check_playbook.py`.
4. Add a line to `CHANGELOG.md`.
5. Open a pull request saying what problem the change solves, ideally with the real situation that showed it.

## Writing rules

- Plain words. Say what to do and what the result must be, not only which tool to call.
- Keep it platform-neutral. Platform-specific names, domains, tool names and settings paths go in your **private platform add-on**, never here.
- No secrets, account ids, emails, phone numbers, customer data or screenshots that show them. Blank them out, do not blur.
- Always call the integration layer the **Connector Hub**. Never use the name of a vendor behind it.
- No em dashes.
- Use `[Your Platform]` where you would name a specific platform.
- Follow the [Code of Conduct](CODE_OF_CONDUCT.md). Report security problems privately (see [SECURITY.md](SECURITY.md)).

By contributing you agree that your contribution is licensed under the MIT License of this repository.
- One topic per doc. If a doc grows past about 250 lines, split it.
- When you add a lesson, add the troubleshooting row too (`docs/17-troubleshooting.md`).

## Private words check

To stop your own internal words slipping in, create `.playbook-banned` (one regex per line) in your local copy. It is listed in `.gitignore` and the check reads it.
