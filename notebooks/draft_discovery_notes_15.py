"""Draft discovery notes for smoke tests.

These strings are an assistant draft for informal testing. They are not the
frozen holdout: data/raw requires notes the project author writes by hand.
"""

from __future__ import annotations

import json
from pathlib import Path

NOTES = [
    {
        "id": "N01",
        "title": "Discovery note: staff portal sign-in",
        "style": "close to a tidy discovery scribble, one buried hedge",
        "sentences": [
            ("Client confirmed that staff sign in to the portal with the corporate directory.", "fact"),
            ("Priya thinks the same directory login can cover the new mobile app.", "assumption"),
            ("Need to ask whether weekend contractors get a directory account.", "open_question"),
            ("The client said the pilot group is the north warehouse team.", "fact"),
            ("Assume the directory team can add the app registration before month end.", "assumption"),
            ("Client said MFA is probably already on for every account, but nobody opened the policy.", "assumption"),
            ("Kiosk PCs, domain-joined or not, still unknown.", "open_question"),
        ],
    },
    {
        "id": "N02",
        "title": "Vendor file drop — scratch from the call",
        "style": "telegraphic, missed details at the end",
        "sentences": [
            ("Client confirmed the nightly file lands in an SFTP folder, and they opened that folder on the call.", "fact"),
            ("Jules reckons the site-to-site tunnel can take the new feed.", "assumption"),
            ("Client said that tunnel was for another vendor and might be pinned to the old destination.", "assumption"),
            ("Firewall change Tuesday night.", "assumption"),
            ("Owen put that slot in; their network lead never said it.", "assumption"),
            ("Who signs a new destination, network lead or the vendor?", "open_question"),
            ("Sponsor said the pilot should start in November.", "fact"),
            ("Nothing dated, so 18 Nov is just the placeholder in my head.", "assumption"),
            ("Folder path and the login name: missed them.", "open_question"),
        ],
    },
    {
        "id": "N03",
        "title": "OA leave path, after the workshop",
        "style": "silence treated as agreement",
        "sentences": [
            ("Client confirmed the leave form is still paper, then scanned into a shared drive.", "fact"),
            ("Supervisor, then HR, then finance — wrote that down and they did not object, so using it as the path.", "assumption"),
            ("What amount sends a form to finance?", "open_question"),
            ('Client said finance joins only when the claim is "large".', "fact"),
            ("Mei thinks large means over 500, currency not stated.", "assumption"),
            ("Need to ask if audit still wants a wet-signature scan.", "open_question"),
            ("The client said they want the new flow in before the year-end shutdown.", "fact"),
            ("Assume HR can freeze the old form the same weekend.", "assumption"),
        ],
    },
    {
        "id": "N04",
        "title": "Case-tracker move, two people talking",
        "style": "estimate plus a contradiction",
        "sentences": [
            ("Client confirmed the live tracker is a shared workbook on the department drive.", "fact"),
            ("About 4,000 open rows, give or take, from their admin.", "assumption"),
            ("Not a counted export.", "assumption"),
            ("Ari thinks the history can move in one weekend.", "assumption"),
            ("Client said closed cases older than three years can be left behind.", "fact"),
            ("Later the same admin said legal might want seven years, so the cutoff is not settled.", "open_question"),
            ("Do we get a read-only copy of the workbook, or only a csv they prepare?", "open_question"),
            ("Column names in row 1 stay as they are, and I'm taking that as given.", "assumption"),
            ("Priya says the ids look unique.", "assumption"),
            ("Blanks were not tested.", "open_question"),
        ],
    },
    {
        "id": "N05",
        "title": "Billing rekey, ten minutes left",
        "style": "short and blunt",
        "sentences": [
            ("Client confirmed orders get created in the inventory app, then someone types them into billing again.", "fact"),
            ("They said there is no API today.", "fact"),
            ("Nightly csv is enough for phase 1, in Sam's view.", "assumption"),
            ("Whether a clerk still has to check every file — need to ask.", "open_question"),
            ("Order number joins the two sides, and I'm taking that as given.", "assumption"),
        ],
    },
    {
        "id": "N06",
        "title": "Field-app roles, rough",
        "style": "missing subjects, nod treated as a decision",
        "sentences": [
            ("Tech, dispatcher, read-only auditor.", "assumption"),
            ("Those three got mentioned, not locked.", "assumption"),
            ("Client confirmed techs only see their own jobs.", "fact"),
            ("Whole region for the dispatcher?", "open_question"),
            ("They nodded, I think, and it never made the recap.", "assumption"),
            ("Export rights for the auditor still need to be asked.", "open_question"),
            ("Region lives as a column on the job.", "assumption"),
            ("Directory login, probably, and the client had already left by then.", "assumption"),
            ("Owen will just mirror the web roles, which was us talking, not them.", "assumption"),
        ],
    },
    {
        "id": "N07",
        "title": "Shared mailbox cutover",
        "style": "several missing lists",
        "sentences": [
            ("Client confirmed the public address is a shared mailbox, not a licensed user.", "fact"),
            ("Who is allowed to send as that mailbox?", "open_question"),
            ("The send-as list was not provided.", "open_question"),
            ("Retention on the old mailbox is unclear, and their admin will check.", "open_question"),
            ("Jules thinks forwarding can stay on for two weeks.", "assumption"),
            ("The client said they do not want auto-replies during the cutover weekend.", "fact"),
            ('They said there are "a few" aliases and then stopped, so the list is still needed.', "open_question"),
            ("DNS sits with central IT, not with the mailbox host.", "assumption"),
        ],
    },
    {
        "id": "N08",
        "title": "Test copy",
        "style": "an open gap, then the team fills it",
        "sentences": [
            ("Separate test tenant was never confirmed.", "open_question"),
            ("Working as if they will mask a copy taken from the live system.", "assumption"),
            ("Blank the emails and the mobile numbers — Mei's guess.", "assumption"),
            ("Client said a copy can come after the audit.", "fact"),
            ("No month was named.", "open_question"),
            ("Attachments in or out?", "open_question"),
            ("Ten cases is enough to rehearse, decided on our side.", "assumption"),
            ("Their security person was out, and the note still treats no live names in test as agreed.", "assumption"),
        ],
    },
    {
        "id": "N09",
        "title": "Contractor access",
        "style": "confirmation from the wrong person",
        "sentences": [
            ("Leo walked through the guest-account steps, but Leo is on our team and their admin was not on the call.", "assumption"),
            ("Client confirmed staff use the corporate directory.", "fact"),
            ('On contractors, the client said "sometimes a spreadsheet of names", and sounded unsure.', "assumption"),
            ("Need to ask whether those accounts expire.", "open_question"),
            ("Using a 90-day expiry because that is what we used last time, on a different job.", "assumption"),
            ("Client said the sponsor wants contractors in the pilot, but the sponsor was absent and nothing was decided.", "assumption"),
            ("Whether contractor devices are managed is still open.", "open_question"),
        ],
    },
    {
        "id": "N10",
        "title": "Nightly extract, clocks disagree",
        "style": "same call, two times",
        "sentences": [
            ("Client confirmed a csv extract runs after midnight.", "fact"),
            ("Ops lead said 01:00, the analyst later said 03:30, and nobody picked one.", "open_question"),
            ("Which clock is the business-date cut-off?", "open_question"),
            ("Jules thinks the warehouse can take a late file until 06:00.", "assumption"),
            ("Putting our job at 04:00 so both of their times are covered, which is us stitching the gap.", "assumption"),
            ("Holiday calendar still to be sent before the schedule is locked.", "open_question"),
            ("Client said weekends are included, then someone said maybe not public holidays, and it was left open.", "open_question"),
        ],
    },
    {
        "id": "N11",
        "title": "Order status back to the shop floor",
        "style": "opinion sitting next to an unasked question",
        "sentences": [
            ("Client confirmed they poll order status every five minutes today.", "fact"),
            ("A webhook would be cleaner.", "assumption"),
            ("Nobody has asked the gateway owner yet.", "open_question"),
            ("Client said the gateway can probably do callbacks.", "assumption"),
            ("Timeouts and retries were not discussed and need a follow-up.", "open_question"),
            ("Status values are only open, packed, shipped.", "assumption"),
            ("Partial shipment: blank in the notes.", "open_question"),
        ],
    },
    {
        "id": "N12",
        "title": "Cutover weekend",
        "style": "soft acceptance recorded as a plan",
        "sentences": [
            ("Client confirmed the cutover window is Saturday 22:00 to Sunday 06:00 local.", "fact"),
            ('Rollback would be last night\'s backup, which was our suggestion, and they only said "sounds fine" before moving on.', "assumption"),
            ("Mei thinks the backup finishes before 21:00.", "assumption"),
            ("If the restore overruns the window, who calls the stop is still not named.", "open_question"),
            ("Writing down one environment and no second copy to switch to, even though that was not discussed.", "assumption"),
            ("The client said they will staff someone overnight.", "fact"),
            ("Name of that person still to come.", "open_question"),
        ],
    },
    {
        "id": "N13",
        "title": "IDs. Messy.",
        "style": "fragments, screen-pointing",
        "sentences": [
            ("Client put the sales customer number and the billing account code side by side, and they are not the same field.", "fact"),
            ('They pointed at "the short code" as the join key, then were not sure.', "open_question"),
            ("Short code is unique.", "assumption"),
            ("Keeping the leading zeros because the billing screen looked like it had them, without going back to check.", "assumption"),
            ("Ten-row sample from each side, still need it in writing.", "open_question"),
            ("Client said deleted customers stay in billing as inactive.", "fact"),
            ("Saw two rows with the same display name.", "fact"),
            ("Did not ask if that is allowed.", "open_question"),
        ],
    },
    {
        "id": "N14",
        "title": "change window, corridor chat after",
        "style": "informal, dates inferred",
        "sentences": [
            ("No change window written down.", "open_question"),
            ("Client said avoid the first week of the month, finance close.", "fact"),
            ("Priya reads that as the 10th being fine.", "assumption"),
            ("The infra calendar was not shared, so ask again.", "open_question"),
            ("Two hours is enough.", "assumption"),
            ("A duration never came up.", "open_question"),
            ('Someone mentioned a freeze near "the festival week", and which festival was not captured.', "open_question"),
            ("Dates stay unbooked on our side until that calendar shows up.", "assumption"),
        ],
    },
    {
        "id": "N15",
        "title": "Audit export, then a scribble",
        "style": "starts neat, ends with a parked side question",
        "sentences": [
            ("Client confirmed the app writes an audit row on login, on edit, and on export.", "fact"),
            ('Compliance lead said retention is "about a year", off the top of the head.', "assumption"),
            ("Who can download the full log?", "open_question"),
            ("Lena thinks only compliance, not the project team.", "assumption"),
            ("Export file is csv.", "assumption"),
            ("The client said a regulator can ask for the log.", "fact"),
            ("How that request actually arrives was not described.", "open_question"),
            ("They shrugged when asked if a delete is itself an audited event.", "open_question"),
            ("Unclear whether this is the same security reviewer as the network change, so parked.", "open_question"),
        ],
    },
]


def note_text(note: dict) -> str:
    body = "\n".join(sentence for sentence, _ in note["sentences"])
    return f"{note['title']}\n\n{body}\n"


def build_records() -> list[dict]:
    records = []
    for note in NOTES:
        text = note_text(note)
        cursor = text.index("\n\n") + 2
        labeled = []
        for index, (sentence, label) in enumerate(note["sentences"], start=1):
            start = text.find(sentence, cursor)
            if start < 0:
                raise SystemExit(f"{note['id']} sentence {index} not found: {sentence}")
            end = start + len(sentence)
            if text[start:end] != sentence:
                raise SystemExit(f"{note['id']} span mismatch at {index}")
            labeled.append(
                {
                    "n": index,
                    "label": label,
                    "text": sentence,
                    "start": start,
                    "end": end,
                }
            )
            cursor = end
        records.append(
            {
                "id": note["id"],
                "title": note["title"],
                "style": note["style"],
                "text": text,
                "sentences": labeled,
            }
        )
    return records


def render_markdown(records: list[dict]) -> str:
    counts = {"fact": 0, "assumption": 0, "open_question": 0}
    for record in records:
        for sentence in record["sentences"]:
            counts[sentence["label"]] += 1
    total = sum(counts.values())
    lines = [
        "# Draft discovery notes (15)",
        "",
        "Fictional IT-delivery scraps for informal NoteTriage tests. No real client, person, employer, mailbox, or system id.",
        "",
        "This file is an assistant draft. It is not the frozen holdout. `data/raw` asks for notes the project author writes, and these sentences should be rewritten in the author's own wording before any gold file is committed.",
        "",
        "Label rule used here, same idea as the portal example:",
        "",
        "- `fact`: the sentence records a settled client statement or something the client showed on the call, and the sentence does not mark that point as unsure.",
        "- `assumption`: the sentence lets the team plan on a guess, a colleague's view, a hedge (`probably`, `might`, `sounds fine`, a nod), silence, or a number nobody counted.",
        "- `open_question`: the sentence leaves a gap, a conflict, or a follow-up. A later sentence that fills the gap anyway stays an assumption.",
        "",
        f"Counts: {total} sentences — fact {counts['fact']}, assumption {counts['assumption']}, open_question {counts['open_question']}.",
        "",
        "Character offsets are into the `text` field of each JSON record, including the title line.",
        "",
    ]
    for record in records:
        lines.append(f"## {record['id']} — {record['title']}")
        lines.append("")
        lines.append(f"Style: {record['style']}")
        lines.append("")
        lines.append("```text")
        lines.append(record["text"].rstrip("\n"))
        lines.append("```")
        lines.append("")
        lines.append("| # | label | sentence |")
        lines.append("|---|---|---|")
        for sentence in record["sentences"]:
            shown = sentence["text"].replace("|", "\\|")
            lines.append(f"| {sentence['n']} | {sentence['label']} | {shown} |")
        lines.append("")
    return "\n".join(lines)


def main() -> None:
    records = build_records()
    root = Path(__file__).resolve().parent
    jsonl_path = root / "draft_discovery_notes_15.jsonl"
    md_path = root / "draft_discovery_notes_15.md"
    with jsonl_path.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")
    md_path.write_text(render_markdown(records), encoding="utf-8")
    print(f"wrote {len(records)} notes")
    print(md_path)
    print(jsonl_path)


if __name__ == "__main__":
    main()
