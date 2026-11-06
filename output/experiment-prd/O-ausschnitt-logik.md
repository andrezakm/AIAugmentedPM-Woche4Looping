## High-Level Approach

An agent that, for every prospect on a rep's list, reads the public sources reps already use, picks the two or three signals that matter, and hands the rep a short, ready-to-use brief with a suggested opening line.

We chose this because the data is not missing; it is scattered and noisy. Thorne: "They're turning unstructured noise into structured talk tracks manually." The value is in the synthesis, not in more raw data. The experienced reps want to keep the interpretation (Petit: "You have to read between the lines"), so the agent does the gathering and structuring and leaves the judgment in the conversation to the rep. It is the smallest thing that removes the bottleneck and can be live in six weeks.

**Alternatives considered:**
- **Buy more data licenses (ZoomInfo, Sales Navigator)** — ruled out. More raw data adds to the noise the reps already sift through, and the Sales Ops manager already finds these tools too expensive to run on every record. It is also a purchase, not an agent build.
- **Full contact-data sync agent (LinkedIn ↔ CRM verification and write-back)** — ruled out for this engagement. It is a real need (5 of 10 interviewees, owned by Sales Ops), but it is a larger integration project with a different buyer. It is the strongest Phase 2 candidate, because signal briefs about people who have left are worthless.
- **Train reps to research faster / research playbook** — ruled out. O'Neil wants to take research out of onboarding, not teach it better: reps today are "high-priced data miners".

### Narrative

**Before.** It is 8:30 on Monday. Sarah, an SDR, has a list of 60 leads and a KPI of 50 calls. She opens the first lead and starts jumping between the company website, a news aggregator, LinkedIn and Crunchbase, looking for anything that justifies a call. Twenty minutes later she has one weak angle. By lunch she has called eight people. By five she has made 20 calls, half of them cold and generic, and she still has 40 leads she never touched. That evening, Jessica, an AE on the same team, spends four hours at her kitchen table building tomorrow's list of ten.

**After.** At 8:30 Sarah opens her list and every lead already carries a brief: "Series B closed three weeks ago. New VP Engineering started in September. Hiring four DevOps roles. Suggested opener: scaling the team after the round." She reads it in under two minutes, checks one detail on LinkedIn, adjusts the opener in her own words and dials. By lunch she has made 25 calls, each with a reason. Jessica gets her list at the end of the day and spends the evening at home.

## Goals

1. **Cut research time per prospect from 15–40 minutes to under 2 minutes** for prospects covered by a brief (O'Neil's own threshold). Baseline to be measured in Week 1.
2. **Raise SDR call volume toward the 50-calls-per-day KPI** (today around 20, per Jenkins), and increase the share of marketing leads that receive personalized outreach (today around 5 of 100, per Blunt). Target values: [Platzhalter], to be agreed with the client after baseline.
3. **Reps feel they are selling, not mining data.** The brief should feel like a colleague's prep note they trust and can use immediately, not another tab to sift.
4. **Guardrail:** reply and meeting-booked rates on personalized outreach must not drop below today's baseline. Faster research must not mean worse personalization.

## Non-Goals

1. **The agent does not write or send emails or make calls.** Reps want to keep the interpretation and their own voice. Automating outreach would remove the personalization that drives conversion.
2. **No contact-data verification or CRM data cleansing in this engagement.** That is a different skill (data clerk), a different buyer (Sales Ops) and a larger integration. Out of scope for the six-week build.
3. **No lead scoring or marketing–sales lead definition.** The conflict about what a "good lead" is was raised in interviews, but it is an organizational question, not a skill an agent replaces. Saved for a later phase, if at all.
4. **No multi-client product yet.** We build custom for this client on T&M, but modular, so the signal components can be reused if the pattern repeats at other clients.

---

# Solution Alignment

## Key Features

**Plan of record (MVP):**

1. **Signal brief per prospect** — two to three signals (funding, leadership change, hiring, recent topics/posts) from public sources, each with source link and date, plus one suggested opening angle.
2. **Batch processing of the rep's prospect list** — rep or SDR lead hands over a list (CSV or CRM export); briefs are ready by the next morning.
3. **Delivery where reps work** — brief attached to the prospect record in the CRM (or, if CRM write access is delayed, as a daily digest). Method confirmed in Week 1.
4. **Rep feedback on each brief** — one-click "useful / not useful" so the agent's signal selection can be tuned during the engagement and adoption can be measured.

**Future considerations:**

1. **Contact verification and CRM sync (Phase 2)** — detect job changes, verify emails, write updated role data back to the CRM, and turn a departed contact's successor into a new lead.
2. **Trigger-based prospecting lists (Phase 2)** — "Show me new CTOs at Series B companies" or "everyone who posted about cloud migration last week" as a standing query that generates new prospects, not just briefs for existing ones.
3. **Enterprise account map** — relationship and org mapping for Enterprise AEs, the multi-day variant of the same need.

### Key Flows

1. The rep (or SDR lead) selects tomorrow's prospect list in the CRM or uploads a CSV.
2. The agent looks up each prospect and company in the approved public sources (company website, news, funding databases, LinkedIn public data, job postings).
3. The agent filters the findings against the signal checklist (recent funding, new hiring in relevant functions, leadership changes at VP level, topic activity) and discards everything older than the freshness window or irrelevant.
4. The agent writes a brief: up to three signals, each with date and source link, and one suggested opening angle in plain language.
5. The brief lands on the prospect record in the CRM (or in the morning digest) before the rep's working day starts.
6. The rep reads the brief, verifies whatever they want via the source links, adapts the opener in their own words, and calls or emails.
7. The rep marks the brief useful or not useful. The team reviews this feedback weekly during the engagement and the signal rules are tuned.

### Key Logic

1. **What to surface:** only signals from the last 90 days ([Platzhalter] — window to be confirmed with the client), ranked by relevance to the client's offering. Funding, leadership change and hiring rank above general news. Never more than three signals.
2. **Format:** a brief must be readable in under two minutes — maximum three signals, one line each, plus one opening angle of at most two sentences. Every signal carries a date and a source link.
3. **Missing or conflicting data:** if no relevant signal is found, the brief says so explicitly ("No recent signal found") instead of padding with weak content. If sources conflict (e.g. different titles), both are shown with their dates, and the rep decides.
4. **What the agent does not touch:** it never overwrites existing CRM fields (contact data, stage, notes). It only adds the brief as a separate attachment or note. It never sends anything to a prospect.
5. **Non-functional:** a batch of [Platzhalter] prospects processed overnight; briefs available before the start of the working day; only public and client-approved sources; every run logged so source usage is traceable.

---

