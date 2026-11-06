# PRD: Signal Brief Agent

**Prepared by:** NeoEmployee
**Date:** 2026-11-05
**Based on:** Interview research — 10 interviews, 2025-10-12 to 2025-10-23
**Engagement type:** Time & Material / Custom AI Agent Build

---

# Problem Alignment

## Problem & Opportunity

The client's sales team spends 15 minutes to several days per prospect manually turning scattered public information into a reason to call, so reps reach a fraction of their target volume and most paid-for leads are never worked. An agent that delivers the two or three relevant signals per prospect, ready to use, gives that time back to selling.

- **Why it matters to the customer:** Research is the bottleneck in front of every call and email. The VP of Sales puts it plainly: "That's the bottleneck. It's the 'manual' part that kills me." Closing capacity sits idle because too little reaches the top of the funnel: "They are starving for good meetings." (Mike Ross, Sales Director). Marketing sees its leads go unworked: "They can't do that for 100 leads a day. So they do it for 5 and ignore the rest." (Emily Blunt, Marketing Manager).
- **Why it matters to NeoEmployee:** It replaces a clearly bounded employee skill, the prospect researcher, which is exactly our vision filter. The buyers (VP Sales, Sales Director, Sales Enablement) have budget and board pressure, so it sells as a T&M engagement now. And the signal types (funding, leadership change, hiring, topics) are generic across B2B sales organizations, which makes this a candidate for the pattern-recognition team and a future product.
- **Evidence from the interviews (9 of 10 interviewees describe this problem):**
  - Marcus Thorne, VP of Sales: "But does it really take 15 minutes per prospect? 15 minutes! If you do the math, that's only 4 prospects an hour. That's a joke."
  - Linda O'Neil, Director Sales Enablement: "It's not just "is the data there?" — it's "can you find it in under two minutes?"" Today it takes her new hires around 40 minutes.
  - Sarah Jenkins, SDR: "I'm supposed to be making 50 calls a day. That's the KPI. But I'm lucky if I get to 20…"
  - Jessica Chen, Account Executive: "I spend maybe 4 hours a night just building a list of 10 people to email the next day. 4 hours!"
  - Rachel Green, Junior SDR: "But that took me 30 minutes to find. 30 minutes for one email!"
  - Sam Petit, Enterprise AE: "I spend days—literal days—just mapping an account before I even send the first 'hello' email."
  - Tom Baker, Senior Sales Rep: "It feels like half the job is just staring at a screen trying to find an angle."
- **Most affected roles:** SDRs and junior SDRs (volume KPI), Account Executives (unpaid evening research), Enterprise AEs (account mapping), Sales Enablement (ramp time), and the VP of Sales and Sales Director, who own the pipeline number.
- **What is lost every day:** Roughly 30 calls per SDR per day against KPI (20 instead of 50), about 4 prospects per hour instead of a full working list, and 95 of every 100 marketing leads left untouched. Two reps independently estimate they would double their numbers without the research load (Chen: "I'd double my numbers.").
- **Why now:** The buyers have already named the solution themselves. Thorne: "If we could automate that 'intel gathering' piece—just hand them the dossier—we'd be unstoppable." O'Neil: "If we could just hand them the "signals" on a platter…". The VP of Sales is under board pressure on exactly this metric. Demand, budget owner and pain are aligned today.

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

# Development and Launch Planning

| Milestone | Target | Description |
|-----------|--------|-------------|
| Kickoff | Week 1 | Scope confirmation, data source access, CRM credentials, baseline of research time and call volume |
| Agent prototype | Week 2–3 | First working version on 20 test prospects |
| Client feedback round | Week 3 | Rep team tests prototype, feedback collected |
| Integration complete | Week 4–5 | CRM write-back of briefs, delivery mechanism live |
| QA & edge case hardening | Week 5–6 | Edge cases, formatting, error handling |
| Launch | Week 6 | Full prospect list live, all reps onboarded |

All dates are relative and must be confirmed with the client at kickoff.

## Operational Checklist

- [ ] CRM credentials and API access confirmed
- [ ] Prospect list format agreed (CSV / CRM export / live sync)
- [ ] Output delivery method confirmed (email digest / CRM attachment / Slack)
- [ ] Data sources and scraping permissions reviewed
- [ ] Rep team onboarding session scheduled
- [ ] Success metrics baseline captured before launch
- [ ] Rollback / pause plan documented

---

## Other

### Risks

1. **Data source reliability or access** — LinkedIn and other sources restrict automated access. Mitigation: agree on permitted sources in Week 1, design the agent to work on a source mix rather than depend on one.
2. **CRM integration complexity** — write access may be slow to obtain or the CRM data model may be complex. Mitigation: start with the daily digest as fallback, so value is delivered even before integration is complete.
3. **Rep adoption** — senior reps may not trust a machine's angle (Baker values relationships; Chen wants to "know *everything*" about a prospect). Mitigation: briefs show sources and leave the judgment to the rep; involve senior reps in the Week 3 feedback round.
4. **Stale contact data undermines briefs** — a brief about someone who left the company is worthless, and around 40 % of contacts are outdated according to Jenkins. Mitigation: flag obvious job changes in the brief; address properly in Phase 2.

### FAQ

**Q: Why not just buy more ZoomInfo licenses?**
A: More licenses give reps more raw data, but the problem is not missing data. O'Neil: "The problem isn't that the data is missing; it's that they have to sift through so much irrelevant noise to find those three specific things." The Sales Ops manager also reports that tools like ZoomInfo and Clearbit "break, or they're too expensive to run on every single contact record." The agent delivers the finished synthesis, which no license provides.

**Q: How is this different from what the SDRs are doing today?**
A: Today the SDRs do the same work by hand: "They're jumping between five different tabs. Corporate website, some news aggregator, LinkedIn, maybe Crunchbase." (Ross). The agent does the gathering and structuring for every prospect on the list, every day, in the format reps need. The rep keeps the part they are good at: reading the situation and having the conversation.

### Appendix

- Interview synthesis: `output/interview-synthesis-2026-11-03.md`
- Individual interview analyses: `output/interview-individual-*-2025-10-*.md`
- Interviews: `input/Interview_Gen_01.md` to `input/Interview_Gen_10.md`
- Company context: `context/company.md`
- Strategy context: `context/strategy.md`

---

## Product Summary

The Signal Brief Agent is a custom AI agent for the client's sales team that replaces the manual prospect research reps do today across five or more browser tabs. Every morning, each prospect on a rep's list comes with a short brief: two or three dated signals, such as a funding round, a new executive or a hiring push, each with its source, plus a suggested opening angle. It takes research from 15–40 minutes per prospect down to the two minutes it takes to read the brief. Reps spend their day on calls and conversations instead of data mining, and the team can personalize outreach for far more than 5 of every 100 leads. It is built in six weeks on a time-and-material basis, modular enough that its signal components can become the seed of a reusable NeoEmployee product.
