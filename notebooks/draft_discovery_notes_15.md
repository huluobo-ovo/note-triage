# Draft discovery notes (15)

Fictional IT-delivery scraps for informal NoteTriage tests. No real client, person, employer, mailbox, or system id.

This file is an assistant draft. It is not the frozen holdout. `data/raw` asks for notes the project author writes, and these sentences should be rewritten in the author's own wording before any gold file is committed.

Label rule used here, same idea as the portal example:

- `fact`: the sentence records a settled client statement or something the client showed on the call, and the sentence does not mark that point as unsure.
- `assumption`: the sentence lets the team plan on a guess, a colleague's view, a hedge (`probably`, `might`, `sounds fine`, a nod), silence, or a number nobody counted.
- `open_question`: the sentence leaves a gap, a conflict, or a follow-up. A later sentence that fills the gap anyway stays an assumption.

Counts: 117 sentences — fact 26, assumption 50, open_question 41.

Character offsets are into the `text` field of each JSON record, including the title line.

## N01 — Discovery note: staff portal sign-in

Style: close to a tidy discovery scribble, one buried hedge

```text
Discovery note: staff portal sign-in

Client confirmed that staff sign in to the portal with the corporate directory.
Priya thinks the same directory login can cover the new mobile app.
Need to ask whether weekend contractors get a directory account.
The client said the pilot group is the north warehouse team.
Assume the directory team can add the app registration before month end.
Client said MFA is probably already on for every account, but nobody opened the policy.
Kiosk PCs, domain-joined or not, still unknown.
```

| # | label | sentence |
|---|---|---|
| 1 | fact | Client confirmed that staff sign in to the portal with the corporate directory. |
| 2 | assumption | Priya thinks the same directory login can cover the new mobile app. |
| 3 | open_question | Need to ask whether weekend contractors get a directory account. |
| 4 | fact | The client said the pilot group is the north warehouse team. |
| 5 | assumption | Assume the directory team can add the app registration before month end. |
| 6 | assumption | Client said MFA is probably already on for every account, but nobody opened the policy. |
| 7 | open_question | Kiosk PCs, domain-joined or not, still unknown. |

## N02 — Vendor file drop — scratch from the call

Style: telegraphic, missed details at the end

```text
Vendor file drop — scratch from the call

Client confirmed the nightly file lands in an SFTP folder, and they opened that folder on the call.
Jules reckons the site-to-site tunnel can take the new feed.
Client said that tunnel was for another vendor and might be pinned to the old destination.
Firewall change Tuesday night.
Owen put that slot in; their network lead never said it.
Who signs a new destination, network lead or the vendor?
Sponsor said the pilot should start in November.
Nothing dated, so 18 Nov is just the placeholder in my head.
Folder path and the login name: missed them.
```

| # | label | sentence |
|---|---|---|
| 1 | fact | Client confirmed the nightly file lands in an SFTP folder, and they opened that folder on the call. |
| 2 | assumption | Jules reckons the site-to-site tunnel can take the new feed. |
| 3 | assumption | Client said that tunnel was for another vendor and might be pinned to the old destination. |
| 4 | assumption | Firewall change Tuesday night. |
| 5 | assumption | Owen put that slot in; their network lead never said it. |
| 6 | open_question | Who signs a new destination, network lead or the vendor? |
| 7 | fact | Sponsor said the pilot should start in November. |
| 8 | assumption | Nothing dated, so 18 Nov is just the placeholder in my head. |
| 9 | open_question | Folder path and the login name: missed them. |

## N03 — OA leave path, after the workshop

Style: silence treated as agreement

```text
OA leave path, after the workshop

Client confirmed the leave form is still paper, then scanned into a shared drive.
Supervisor, then HR, then finance — wrote that down and they did not object, so using it as the path.
What amount sends a form to finance?
Client said finance joins only when the claim is "large".
Mei thinks large means over 500, currency not stated.
Need to ask if audit still wants a wet-signature scan.
The client said they want the new flow in before the year-end shutdown.
Assume HR can freeze the old form the same weekend.
```

| # | label | sentence |
|---|---|---|
| 1 | fact | Client confirmed the leave form is still paper, then scanned into a shared drive. |
| 2 | assumption | Supervisor, then HR, then finance — wrote that down and they did not object, so using it as the path. |
| 3 | open_question | What amount sends a form to finance? |
| 4 | fact | Client said finance joins only when the claim is "large". |
| 5 | assumption | Mei thinks large means over 500, currency not stated. |
| 6 | open_question | Need to ask if audit still wants a wet-signature scan. |
| 7 | fact | The client said they want the new flow in before the year-end shutdown. |
| 8 | assumption | Assume HR can freeze the old form the same weekend. |

## N04 — Case-tracker move, two people talking

Style: estimate plus a contradiction

```text
Case-tracker move, two people talking

Client confirmed the live tracker is a shared workbook on the department drive.
About 4,000 open rows, give or take, from their admin.
Not a counted export.
Ari thinks the history can move in one weekend.
Client said closed cases older than three years can be left behind.
Later the same admin said legal might want seven years, so the cutoff is not settled.
Do we get a read-only copy of the workbook, or only a csv they prepare?
Column names in row 1 stay as they are, and I'm taking that as given.
Priya says the ids look unique.
Blanks were not tested.
```

| # | label | sentence |
|---|---|---|
| 1 | fact | Client confirmed the live tracker is a shared workbook on the department drive. |
| 2 | assumption | About 4,000 open rows, give or take, from their admin. |
| 3 | assumption | Not a counted export. |
| 4 | assumption | Ari thinks the history can move in one weekend. |
| 5 | fact | Client said closed cases older than three years can be left behind. |
| 6 | open_question | Later the same admin said legal might want seven years, so the cutoff is not settled. |
| 7 | open_question | Do we get a read-only copy of the workbook, or only a csv they prepare? |
| 8 | assumption | Column names in row 1 stay as they are, and I'm taking that as given. |
| 9 | assumption | Priya says the ids look unique. |
| 10 | open_question | Blanks were not tested. |

## N05 — Billing rekey, ten minutes left

Style: short and blunt

```text
Billing rekey, ten minutes left

Client confirmed orders get created in the inventory app, then someone types them into billing again.
They said there is no API today.
Nightly csv is enough for phase 1, in Sam's view.
Whether a clerk still has to check every file — need to ask.
Order number joins the two sides, and I'm taking that as given.
```

| # | label | sentence |
|---|---|---|
| 1 | fact | Client confirmed orders get created in the inventory app, then someone types them into billing again. |
| 2 | fact | They said there is no API today. |
| 3 | assumption | Nightly csv is enough for phase 1, in Sam's view. |
| 4 | open_question | Whether a clerk still has to check every file — need to ask. |
| 5 | assumption | Order number joins the two sides, and I'm taking that as given. |

## N06 — Field-app roles, rough

Style: missing subjects, nod treated as a decision

```text
Field-app roles, rough

Tech, dispatcher, read-only auditor.
Those three got mentioned, not locked.
Client confirmed techs only see their own jobs.
Whole region for the dispatcher?
They nodded, I think, and it never made the recap.
Export rights for the auditor still need to be asked.
Region lives as a column on the job.
Directory login, probably, and the client had already left by then.
Owen will just mirror the web roles, which was us talking, not them.
```

| # | label | sentence |
|---|---|---|
| 1 | assumption | Tech, dispatcher, read-only auditor. |
| 2 | assumption | Those three got mentioned, not locked. |
| 3 | fact | Client confirmed techs only see their own jobs. |
| 4 | open_question | Whole region for the dispatcher? |
| 5 | assumption | They nodded, I think, and it never made the recap. |
| 6 | open_question | Export rights for the auditor still need to be asked. |
| 7 | assumption | Region lives as a column on the job. |
| 8 | assumption | Directory login, probably, and the client had already left by then. |
| 9 | assumption | Owen will just mirror the web roles, which was us talking, not them. |

## N07 — Shared mailbox cutover

Style: several missing lists

```text
Shared mailbox cutover

Client confirmed the public address is a shared mailbox, not a licensed user.
Who is allowed to send as that mailbox?
The send-as list was not provided.
Retention on the old mailbox is unclear, and their admin will check.
Jules thinks forwarding can stay on for two weeks.
The client said they do not want auto-replies during the cutover weekend.
They said there are "a few" aliases and then stopped, so the list is still needed.
DNS sits with central IT, not with the mailbox host.
```

| # | label | sentence |
|---|---|---|
| 1 | fact | Client confirmed the public address is a shared mailbox, not a licensed user. |
| 2 | open_question | Who is allowed to send as that mailbox? |
| 3 | open_question | The send-as list was not provided. |
| 4 | open_question | Retention on the old mailbox is unclear, and their admin will check. |
| 5 | assumption | Jules thinks forwarding can stay on for two weeks. |
| 6 | fact | The client said they do not want auto-replies during the cutover weekend. |
| 7 | open_question | They said there are "a few" aliases and then stopped, so the list is still needed. |
| 8 | assumption | DNS sits with central IT, not with the mailbox host. |

## N08 — Test copy

Style: an open gap, then the team fills it

```text
Test copy

Separate test tenant was never confirmed.
Working as if they will mask a copy taken from the live system.
Blank the emails and the mobile numbers — Mei's guess.
Client said a copy can come after the audit.
No month was named.
Attachments in or out?
Ten cases is enough to rehearse, decided on our side.
Their security person was out, and the note still treats no live names in test as agreed.
```

| # | label | sentence |
|---|---|---|
| 1 | open_question | Separate test tenant was never confirmed. |
| 2 | assumption | Working as if they will mask a copy taken from the live system. |
| 3 | assumption | Blank the emails and the mobile numbers — Mei's guess. |
| 4 | fact | Client said a copy can come after the audit. |
| 5 | open_question | No month was named. |
| 6 | open_question | Attachments in or out? |
| 7 | assumption | Ten cases is enough to rehearse, decided on our side. |
| 8 | assumption | Their security person was out, and the note still treats no live names in test as agreed. |

## N09 — Contractor access

Style: confirmation from the wrong person

```text
Contractor access

Leo walked through the guest-account steps, but Leo is on our team and their admin was not on the call.
Client confirmed staff use the corporate directory.
On contractors, the client said "sometimes a spreadsheet of names", and sounded unsure.
Need to ask whether those accounts expire.
Using a 90-day expiry because that is what we used last time, on a different job.
Client said the sponsor wants contractors in the pilot, but the sponsor was absent and nothing was decided.
Whether contractor devices are managed is still open.
```

| # | label | sentence |
|---|---|---|
| 1 | assumption | Leo walked through the guest-account steps, but Leo is on our team and their admin was not on the call. |
| 2 | fact | Client confirmed staff use the corporate directory. |
| 3 | assumption | On contractors, the client said "sometimes a spreadsheet of names", and sounded unsure. |
| 4 | open_question | Need to ask whether those accounts expire. |
| 5 | assumption | Using a 90-day expiry because that is what we used last time, on a different job. |
| 6 | assumption | Client said the sponsor wants contractors in the pilot, but the sponsor was absent and nothing was decided. |
| 7 | open_question | Whether contractor devices are managed is still open. |

## N10 — Nightly extract, clocks disagree

Style: same call, two times

```text
Nightly extract, clocks disagree

Client confirmed a csv extract runs after midnight.
Ops lead said 01:00, the analyst later said 03:30, and nobody picked one.
Which clock is the business-date cut-off?
Jules thinks the warehouse can take a late file until 06:00.
Putting our job at 04:00 so both of their times are covered, which is us stitching the gap.
Holiday calendar still to be sent before the schedule is locked.
Client said weekends are included, then someone said maybe not public holidays, and it was left open.
```

| # | label | sentence |
|---|---|---|
| 1 | fact | Client confirmed a csv extract runs after midnight. |
| 2 | open_question | Ops lead said 01:00, the analyst later said 03:30, and nobody picked one. |
| 3 | open_question | Which clock is the business-date cut-off? |
| 4 | assumption | Jules thinks the warehouse can take a late file until 06:00. |
| 5 | assumption | Putting our job at 04:00 so both of their times are covered, which is us stitching the gap. |
| 6 | open_question | Holiday calendar still to be sent before the schedule is locked. |
| 7 | open_question | Client said weekends are included, then someone said maybe not public holidays, and it was left open. |

## N11 — Order status back to the shop floor

Style: opinion sitting next to an unasked question

```text
Order status back to the shop floor

Client confirmed they poll order status every five minutes today.
A webhook would be cleaner.
Nobody has asked the gateway owner yet.
Client said the gateway can probably do callbacks.
Timeouts and retries were not discussed and need a follow-up.
Status values are only open, packed, shipped.
Partial shipment: blank in the notes.
```

| # | label | sentence |
|---|---|---|
| 1 | fact | Client confirmed they poll order status every five minutes today. |
| 2 | assumption | A webhook would be cleaner. |
| 3 | open_question | Nobody has asked the gateway owner yet. |
| 4 | assumption | Client said the gateway can probably do callbacks. |
| 5 | open_question | Timeouts and retries were not discussed and need a follow-up. |
| 6 | assumption | Status values are only open, packed, shipped. |
| 7 | open_question | Partial shipment: blank in the notes. |

## N12 — Cutover weekend

Style: soft acceptance recorded as a plan

```text
Cutover weekend

Client confirmed the cutover window is Saturday 22:00 to Sunday 06:00 local.
Rollback would be last night's backup, which was our suggestion, and they only said "sounds fine" before moving on.
Mei thinks the backup finishes before 21:00.
If the restore overruns the window, who calls the stop is still not named.
Writing down one environment and no second copy to switch to, even though that was not discussed.
The client said they will staff someone overnight.
Name of that person still to come.
```

| # | label | sentence |
|---|---|---|
| 1 | fact | Client confirmed the cutover window is Saturday 22:00 to Sunday 06:00 local. |
| 2 | assumption | Rollback would be last night's backup, which was our suggestion, and they only said "sounds fine" before moving on. |
| 3 | assumption | Mei thinks the backup finishes before 21:00. |
| 4 | open_question | If the restore overruns the window, who calls the stop is still not named. |
| 5 | assumption | Writing down one environment and no second copy to switch to, even though that was not discussed. |
| 6 | fact | The client said they will staff someone overnight. |
| 7 | open_question | Name of that person still to come. |

## N13 — IDs. Messy.

Style: fragments, screen-pointing

```text
IDs. Messy.

Client put the sales customer number and the billing account code side by side, and they are not the same field.
They pointed at "the short code" as the join key, then were not sure.
Short code is unique.
Keeping the leading zeros because the billing screen looked like it had them, without going back to check.
Ten-row sample from each side, still need it in writing.
Client said deleted customers stay in billing as inactive.
Saw two rows with the same display name.
Did not ask if that is allowed.
```

| # | label | sentence |
|---|---|---|
| 1 | fact | Client put the sales customer number and the billing account code side by side, and they are not the same field. |
| 2 | open_question | They pointed at "the short code" as the join key, then were not sure. |
| 3 | assumption | Short code is unique. |
| 4 | assumption | Keeping the leading zeros because the billing screen looked like it had them, without going back to check. |
| 5 | open_question | Ten-row sample from each side, still need it in writing. |
| 6 | fact | Client said deleted customers stay in billing as inactive. |
| 7 | fact | Saw two rows with the same display name. |
| 8 | open_question | Did not ask if that is allowed. |

## N14 — change window, corridor chat after

Style: informal, dates inferred

```text
change window, corridor chat after

No change window written down.
Client said avoid the first week of the month, finance close.
Priya reads that as the 10th being fine.
The infra calendar was not shared, so ask again.
Two hours is enough.
A duration never came up.
Someone mentioned a freeze near "the festival week", and which festival was not captured.
Dates stay unbooked on our side until that calendar shows up.
```

| # | label | sentence |
|---|---|---|
| 1 | open_question | No change window written down. |
| 2 | fact | Client said avoid the first week of the month, finance close. |
| 3 | assumption | Priya reads that as the 10th being fine. |
| 4 | open_question | The infra calendar was not shared, so ask again. |
| 5 | assumption | Two hours is enough. |
| 6 | open_question | A duration never came up. |
| 7 | open_question | Someone mentioned a freeze near "the festival week", and which festival was not captured. |
| 8 | assumption | Dates stay unbooked on our side until that calendar shows up. |

## N15 — Audit export, then a scribble

Style: starts neat, ends with a parked side question

```text
Audit export, then a scribble

Client confirmed the app writes an audit row on login, on edit, and on export.
Compliance lead said retention is "about a year", off the top of the head.
Who can download the full log?
Lena thinks only compliance, not the project team.
Export file is csv.
The client said a regulator can ask for the log.
How that request actually arrives was not described.
They shrugged when asked if a delete is itself an audited event.
Unclear whether this is the same security reviewer as the network change, so parked.
```

| # | label | sentence |
|---|---|---|
| 1 | fact | Client confirmed the app writes an audit row on login, on edit, and on export. |
| 2 | assumption | Compliance lead said retention is "about a year", off the top of the head. |
| 3 | open_question | Who can download the full log? |
| 4 | assumption | Lena thinks only compliance, not the project team. |
| 5 | assumption | Export file is csv. |
| 6 | fact | The client said a regulator can ask for the log. |
| 7 | open_question | How that request actually arrives was not described. |
| 8 | open_question | They shrugged when asked if a delete is itself an audited event. |
| 9 | open_question | Unclear whether this is the same security reviewer as the network change, so parked. |
