# Meeting Notes

Fifteen raw call write‑ups, some points left hanging from discussion, no final sign‑off on several items.

# 01 Warehouse handheld device rollout

表格

| Topic | When | Who was there | Status |
| --- | --- | --- | --- |
| Warehouse handheld device rollout | not logged | attendee list missing | follow‑up required |

• Client side: warehouse team will get new handheld units, target site is south distribution hub.
• Mentioned existing device inventory is roughly 112 units, exact count not tabled in call.
• Sam said existing corporate directory auth should work for handheld login.
• Some guy from client side mumbled MFA might not be rolled out to warehouse floor staff yet — never pulled up policy doc to verify.
• Weekend shift staff? Not sure if they get assigned dedicated device or share kiosk hardware.
• Kiosk hardware OS version, nobody brought up.
• Need to circle back: can temp workers reuse old retired handhelds?

# 02 Supplier API payload handover

表格

| Topic | When | Who was there | Status |
| --- | --- | --- | --- |
| Supplier API payload handover | — | participants not captured | consensus not reached |

• Night‑time API push sends supplier order payloads, hitting their staging endpoint right now.
• Business sponsor wants pilot kicking off December.
• Jake thought existing site‑to‑site VPN can carry this new API traffic.
• Client pushed back — that VPN was built for another vendor, IP whitelist locked down to old destination IP.
• Firewall tweak pencilled in for Wednesday evening slot.
• Mark added calendar slot, but client network lead never acknowledged the invite.
• No firm date locked, mid‑Dec floating as rough mental marker only.
• Unclear: who formally approves new target IP? Network lead or supplier contact?
• API basic auth credentials, folder path got skipped in call, forgot to write those down.

# 03 Travel claim workflow refresh post‑workshop

表格

| Topic | When | Who was there | Status |
| --- | --- | --- | --- |
| Travel claim workflow refresh post‑workshop | TBC | — | item open |

• Client still running physical paper travel claim forms, scan and dump to shared drive afterwards.
• Finance team only gets looped in for bigger value submissions.
• They want new digital workflow live before year‑end system freeze.
• Flow talked through: submitter → line manager → HR → finance. No pushback during call, going with that sequence for now.
• Ling guessed high‑value threshold sits above 750, currency not specified in conversation.
• Hoping HR can cut over old paper forms same weekend we go‑live.
• Need to clarify exact monetary threshold triggering finance review.
• Audit team still requesting physical wet‑signature scans? Never got clear yes/no.

# 04 Incident tracker data migration

表格

| Topic | When | Who was there | Status |
| --- | --- | --- | --- |
| Incident tracker data migration | call date unrecorded | names absent | needs verification |

• Live incident tracker lives as shared excel workbook on department network drive.
• Client comment: closed incidents older than 4 years can stay on legacy drive, no need to migrate across.
• Client admin approximate number: ~3200 open active incident rows, ballpark figure, not formal exported stat.
• Zoe said full history migration doable within single cutover weekend window.
• Keep original header column names on row one, everyone seemed okay with that.
• Row ID fields look unique on quick spot check.
• Later same admin chimed‑in, legal team might demand 8‑year retention instead. Cutoff age totally unresolved.
• Are we getting read‑only copy of full workbook, or only pre‑prepared CSV export from their side?
• Empty field handling hasn’t been tested at all.

# 05 Manual invoice re‑key workaround

表格

| Topic | When | Who was there | Status |
| --- | --- | --- | --- |
| Manual invoice re‑key workaround | not noted | not noted | need follow‑up |

• Order records created inside inventory application, then finance staff manually re‑type everything over to invoicing tool.
• No production API integration available today.
• Our side take: nightly CSV dump should satisfy phase one requirements.
• Order number will act as join key between two datasets, proceeding under that premise.
• Still ambiguous: does finance clerk still need full manual line‑by‑line check for every incoming CSV file? Must ask client.

# 06 Mobile field technician permission sets

表格

| Topic | When | Who was there | Status |
| --- | --- | --- | --- |
| Mobile field technician permission sets | — | participants not captured | full agreement missing |

• Client confirm: field techs can only view jobs assigned directly to themselves.
• Roles tossed around in discussion: field tech, job dispatcher, read‑only compliance auditor.
• Those three role names mentioned verbally, nothing formally documented.
• Client nodded along verbally but this didn’t make call recap minutes afterwards.
• Job dataset contains region column stored as field value.
• Expect corporate directory authentication, client rep left call before we could lock that down.
• Ryan’s idea: mirror existing web portal role structure for mobile app, that was internal team talk, client never weighed‑in.
• Dispatcher permission: can dispatcher see every job across entire region? Not resolved.
• Auditor role — is export functionality granted? Still need raise this question.

# 07 Service desk shared mailbox migration

表格

| Topic | When | Who was there | Status |
| --- | --- | --- | --- |
| Service desk shared mailbox migration | TBC | — | open action |

• Public incoming service‑desk address runs off shared mailbox resource, not licensed user account.
• Client hard ask: no auto‑reply messages active during migration weekend.
• Our suggestion: keep email forwarding active for three weeks post‑cutover.
• DNS records managed by central corporate IT group, not the mailbox hosting vendor.
• Who holds send‑as permissions for this shared mailbox? List never handed over.
• Retention policy applied against old mailbox instance, their admin will go check internally.
• Client mentioned handful of email aliases exist, then conversation shifted topic, alias inventory still outstanding.

# 08 Non‑production test dataset provision

表格

| Topic | When | Who was there | Status |
| --- | --- | --- | --- |
| Non‑production test dataset provision | no call date logged | attendee names missing | needs checking |

• Client perspective: test data extract can only happen once audit cycle completes.
• Working off idea they will supply masked copy taken directly from live production environment.
• Kelly’s best guess: scrub all customer email addresses plus phone numbers out of dataset.
• Team internal call: 15 sample records enough for rehearsal testing.
• Client security lead absent from meeting; we operate assumption no real‑person PII inside test data.
• Questions hanging: separate dedicated test tenant environment approved?
• No calendar month given for data hand‑over.
• What about embedded file attachments, include or drop them from test set? No answer.

# 09 Third‑party vendor contractor directory access

表格

| Topic | When | Who was there | Status |
| --- | --- | --- | --- |
| Third‑party vendor contractor directory access | not noted | not noted | follow‑up item |

• Full‑time internal staff authenticate via corporate directory service.
• Tony walked through guest account provision workflow, but client system admin wasn’t present for that part of call.
• Client response re contractors: sometimes they maintain name spreadsheet, sounded unsure of formal process.
• Reuse expiry setting 60 days, same config we implemented for different project previously.
• Project sponsor wants contractors included within early pilot wave, sponsor themselves didn’t join call so no binding decision made.
• Need clarify: guest directory accounts auto expire or manually disabled?
• Contractor end‑user devices under corporate MDM management? Topic left open‑ended.

# 10 Scheduled nightly data extract timing drift

表格

| Topic | When | Who was there | Status |
| --- | --- | --- | --- |
| Scheduled nightly data extract timing drift | — | participants not captured | agreement incomplete |

• Client system runs CSV extract job post‑midnight each day.
• Warehouse downstream system can accept late arriving files up to 07:00 according to Rob.
• We proposed schedule our transformation job for 04:30 to bridge conflicting timings.
• Conflicting times surfaced: operations lead stated 01:30, business analyst later quoted 03:00, nobody picked final agreed time.
• Which system clock defines official business date cutoff? Not settled.
• Public holiday calendar file still awaiting client hand‑over before schedule finalised.
• Client first said include weekend runs, then someone added public holidays should maybe skip. Topic unresolved.

# 11 Order status push notification to production floor

表格

| Topic | When | Who was there | Status |
| --- | --- | --- | --- |
| Order status push notification to production floor | TBC | — | open topic |

• Current integration setup: shop floor system polls order status every four minutes.
• Webhook callback would be cleaner architecture‑wise.
• Client comment: existing integration gateway might support callback functionality.
• Limited status values in scope: open, packed, dispatched.
• Haven’t yet reached out to gateway system owner to validate capability.
• Retry logic and connection timeout behaviour never got discussed, need circle back.
• Partial shipment scenarios, nothing written down about handling logic.

# 12 Major system cutover weekend window

表格

| Topic | When | Who was there | Status |
| --- | --- | --- | --- |
| Major system cutover weekend window | call date missing | participant names absent | needs validation |

• Confirmed change window Saturday 21:00 local time through Sunday 05:00.
• Client commit: onsite resource on‑call overnight for cutover event.
• Rollback strategy: restore from previous night backup, we floated suggestion, client replied “that should work” then moved onto next agenda.
• Amy’s estimate: backup job normally completes before 20:30.
• Only single production environment available; no standby failover instance, this was our reading, never explicitly confirmed by them.
• If restore procedure overruns hard cut‑off window — who triggers abort? Named contact not supplied.

# 13 Inconsistent customer identifier mapping

表格

| Topic | When | Who was there | Status |
| --- | --- | --- | --- |
| Inconsistent customer identifier mapping | not noted | not noted | follow‑up needed |

• Customer sales reference number and billing account code shown side‑by‑side during screen share; they are different fields.
• Deleted customer entries persist inside billing database marked inactive status.
• Observed duplicate display‑name values across different customer rows.
• Short reference code appears unique on spot check.
• Preserve leading zero characters, observed on billing UI screen, didn’t dig deeper to validate backend behaviour.
• Client gestured toward short code as potential join key, then second‑guessed themselves mid‑sentence.
• Request written sample dataset, ten rows pulled each from sales and billing side, still pending.
• Not yet asked whether joining on that field is formally allowed by data governance rules.

# 14 Maintenance change window hallway conversation

表格

| Topic | When | Who was there | Status |
| --- | --- | --- | --- |
| Maintenance change window hallway conversation | — | participants not captured | no final agreement |

• Client ask: avoid first week of every month due finance month‑end close activities.
• Bella’s take: 11th of month should be safe slot.
• Two‑hour maintenance slot should suffice for most deployments.
• We won’t lock calendar until client shares infrastructure change calendar.
• No official change window documented anywhere yet.
• Their infra calendar hasn’t been shared, send another reminder.
• Somebody mentioned freeze period around festival week, which festival exactly? Nobody clarified.

# 15 Compliance audit log requirements

表格

| Topic | When | Who was there | Status |
| --- | --- | --- | --- |
| Compliance audit log requirements | TBC | — | open item |

• Application writes audit event entries for login actions, record edits and data export operations.
• Regulator bodies can demand full log dataset as part of compliance checks.
• Compliance lead off‑the‑cuff comment: log retention roughly 12 months.
• Our side thought only compliance team permitted access; project team shouldn’t touch raw audit logs.
• Audit exports delivered out as CSV formatted files.
• Who possesses permission to download complete full audit log set? Unclear.
• Process how formal log requests get submitted, not explained in meeting.
• Question: does record‑delete operation itself trigger an audit log entry? Client team just shrugged.
• Can’t tell if same security reviewer handles network change work and audit log reviews, parked topic for later.