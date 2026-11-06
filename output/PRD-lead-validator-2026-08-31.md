# PRD: Lead Validator AI Agent

**Prepared by:** NeoEmployee  
**Date:** 2026-08-31  
**Based on:** Interview research — 1 interview (Sarah Jenkins, SDR), 2025-10-12  
**Engagement type:** Time & Material / Custom AI Agent Build

---

# Problem Alignment

## Problem & Opportunity

Sales development reps spend 50% of their time verifying and enriching lead data instead of making sales calls. This is a direct, measurable productivity loss that prevents quota attainment.

**Evidence:**
Sarah Jenkins (SDR) reported: *"I spend half my day just trying to figure out who I'm supposed to actually call... It's zombie data. Half the emails bounce immediately, or... the person left the company three years ago."* She estimates that **if lead verification were automated, she could double her quota from 20 to 50 calls per day.** Currently, 40% of leads are outdated or incorrect, forcing manual cross-referencing across LinkedIn, company websites, Google News, and ZoomInfo—all unpaid, unproductive work.

**Who is affected:**  
Sales development reps, sales development leaders, and by extension, the entire go-to-market organization. Any company with a sales team that relies on external lead lists experiences this bottleneck.

**Why it's urgent:**  
This is happening *every day, right now.* Sarah is missing quota attainment targets due to data work, not sales skill. The cost is compounding: every day a rep spends 50% of time on verification is revenue lost and momentum damaged.

**Why now:**  
The interview was conducted near quarter-end when the pain is most acute. Lead quality problems are perennial but feel most urgent when quotas loom and reps are under pressure. There is immediate willingness to adopt a solution.

## High-Level Approach

**One sentence:** Build an AI agent that validates every lead, updates outdated contact information, flags bad data, and auto-enriches profiles—so reps get only high-confidence, verified leads ready to call.

**Why this approach:**  
This is a *before-the-rep* intervention. Rather than training reps to be better at data work, we remove the data work entirely. The agent catches problems in the funnel before they waste the rep's time. This is aligned with NeoEmployee's model of replacing inefficient skills with AI, and it's a clear, measurable win: quota impact is directly visible.

**Alternatives considered:**

- *Buy more ZoomInfo licenses* — Why we ruled it out: ZoomInfo is expensive, and reps were already avoiding it when access was rationed (see quote: *"I end up just Googling stuff half the time because the ZoomInfo login is always taken"*). Adding more licenses improves the tool, not the workflow. The problem isn't access; it's that reps are still doing manual verification work that shouldn't exist.

- *Train reps to verify leads faster* — Why we ruled it out: This addresses symptoms, not the root cause. The work itself is repetitive and automatable. Training won't scale; an agent will. And every hour spent training is an hour reps aren't selling.

- *Rebuild the lead-sourcing pipeline from marketing* — Why we ruled it out: This is valuable long-term but slow to implement and outside the scope of a sales team's control. The agent solves the immediate problem today, and once working, creates evidence that marketing's lead quality is the underlying issue—making the long-term case easier.

### Narrative

**Day before the agent:**

Sarah logs in and pulls her lead list for the day. 40 names. She opens Salesforce on one screen, LinkedIn on a second tab, and a Google search in a third. For each name, she copies the job title from LinkedIn, pastes it into Salesforce—but it comes in all caps, so she has to reformat it. She clicks the phone number to verify it's real (it often isn't). She checks if the person is still employed by searching their company's website. For 15 of the 40 leads, she discovers they've left the company or moved to a different role. She hunts for their replacement on LinkedIn or company news. One hour passes. She's made zero calls. Her anxiety rises; she needs 50 calls today to hit quota.

**Day after the agent is live:**

Sarah logs in and pulls her lead list for the day. 40 names. The agent has already run overnight. Each lead shows:
- Current job title (auto-updated from LinkedIn)
- Current employment status (verified)
- Up-to-date contact information
- A confidence score (red if stale, green if fresh)
- Auto-enriched company news or recent job change flag

The list is already clean. Sarah opens one screen (Salesforce with agent-enriched data) and starts dialing. By 10 AM, she's made 35 calls. She hits 50 by 2 PM. The quota is on track.

## Goals

1. **Primary (measurable):** Increase SDR calls-per-day from 20 to 40+ by eliminating lead verification work. Success metric: baseline call count before launch, target call count after 2 weeks of agent live.

2. **Secondary (measurable):** Reduce lead bounce rate and "wrong contact" rejections by 75%. Success metric: track call connect rate, email bounce rate, and "who?" hang-ups before and after.

3. **Qualitative (experience):** SDRs feel like salespeople, not private investigators. They spend their day on high-confidence conversations, not data hunting.

4. **Guardrail:** Do not increase false positives (flagging good leads as bad) above 5%. We're filtering junk; we must not filter good leads.

---

## Non-Goals

1. **What this agent does not do:** It does not source new leads, replace marketing, or rebuild the lead pipeline. This agent assumes leads arrive and cleans them.

2. **Out of scope for this engagement:** Building a full-scale lead-sourcing system. Integrating with all third-party data providers. Predicting lead quality or propensity-to-buy (that's a future phase).

3. **Saved for Phase 2:** Predictive lead scoring based on company signals and buyer intent. Automated outreach sequencing based on lead quality tiers. Real-time alerts when priority leads change jobs or get promoted.

---

# Solution Alignment

## Key Features

**Plan of record (MVP):**

1. **Lead Validation Engine** — For every lead in the CRM, the agent checks:
   - Is the email deliverable? (Verify format and send a test to catch bounces.)
   - Is the person still employed at that company? (Cross-check LinkedIn, company website, public records.)
   - Is the job title still current? (Fetch from LinkedIn and auto-update Salesforce.)
   - Are there recent signals of job change or promotion? (Search LinkedIn news, recent updates.)

2. **Confidence Scoring** — Every lead gets a score (High/Medium/Low/Red Flag) based on:
   - Data freshness (when was it last verified?)
   - Email deliverability
   - Employment status certainty
   - Days since last update

3. **Automatic Data Enrichment** — Update Salesforce fields:
   - Job title (auto-corrected, consistent format)
   - Email (corrected if possible)
   - Employment status flag
   - Last verified timestamp
   - Reason for flag (if Low or Red)

4. **Daily Digest & Priority Sorting** — Email SDRs (or post to Slack) a morning brief:
   - Top 20 leads ready to call (High confidence)
   - 5 leads that need manual follow-up (Medium confidence, reason flagged)
   - Leads to skip (invalid email, person gone, company dissolved)

**Future considerations:**

1. **Predictive lead scoring** — Combine validation with company intent signals (hiring, funding, tech stack changes) to predict buy-now readiness.

2. **Automated job change alerts** — Real-time notification when a champion changes jobs, along with forwarding address.

3. **Multi-touch outreach sequencing** — Route clean leads to the right rep and auto-suggest outreach timing based on lead tier.

---

## Key Flows

1. **Daily Batch Validation:**
   - SDR manager or system admin uploads lead list (CSV or Salesforce export)
   - Agent ingests and begins validation job overnight
   - By morning, all leads are scored and Salesforce is auto-updated with current data
   - SDRs see clean list ready to work

2. **Confidence Scoring & Filtering:**
   - Agent assigns score per lead
   - High-confidence leads are marked ready-to-call
   - Medium leads are flagged for manual verification (with reason)
   - Low/Red leads are set aside with explanation (wrong title, bouncing email, etc.)
   - SDR works High list first; low-bounce rate increases

3. **Continuous Refresh:**
   - Once per week, agent re-validates all leads in Salesforce
   - Auto-updates any changed data (new title, new company, email bounce patterns)
   - Keeps list fresh without manual effort

---

## Key Logic

1. **Email validation:** Test via SMTP check (is it deliverable?) + format validation (proper structure). Flag if bounce rate > 5% historically.

2. **Employment status check:** Search LinkedIn (current employer field), check company website (employee directory if public), verify against cached employment data. Source: LinkedIn API + public web search.

3. **Job title freshness:** Fetch current title from LinkedIn profile, compare to Salesforce record. If different and confidence > 90%, auto-update Salesforce. If < 90%, flag for review.

4. **Confidence scoring algorithm:**
   - 90+ points = High (ready to call)
   - 70–89 = Medium (worth manual check before calling)
   - < 70 = Low (likely bad, flag for skip)
   - Points deducted for: email bounce, employment status uncertainty, title mismatch, data age > 30 days

5. **Non-functional requirement:** Agent must process 1,000 leads within 4 hours (batch overnight). No individual lead lookup should take > 30 seconds. Error rate < 2%.

---

# Development and Launch Planning

| Milestone | Target | Description |
|-----------|--------|-------------|
| Kickoff | Week 1 | Scope confirmation, Salesforce API access, lead list sample, current baseline metrics |
| Agent v1 prototype | Week 2 | Build validation engine, test on 50 leads, show sample output to SDR team |
| Feedback round | Week 3 | SDRs test prototype, refine confidence scoring, refine field mappings |
| Salesforce integration | Week 3–4 | CRM write-back live, daily batch job scheduled, error handling built |
| QA & edge cases | Week 4–5 | Test with full lead list, handle bounces, duplicates, name variations, non-US leads |
| Soft launch | Week 5 | Live with subset of reps (5–10) and 200 leads, monitor error rate and adoption |
| Full launch | Week 6 | All reps on-boarded, full prospect list (1,000+), success metrics captured |

---

## Operational Checklist

- [ ] Salesforce API credentials and sandbox access confirmed
- [ ] Lead list format agreed (CSV template or Salesforce export)
- [ ] Current baseline metrics captured: calls/day, connect rate, email bounce rate, quota attainment
- [ ] Data sources and LinkedIn scraping permissions reviewed and approved
- [ ] Email sending and Slack integration permissions configured
- [ ] SDR team availability confirmed for feedback round and onboarding
- [ ] Monitoring and logging infrastructure in place (error tracking, success rate dashboards)
- [ ] Rollback plan documented (if confidence scoring needs adjustment, how do we revert?)

---

# Risks & Mitigation

| Risk | Impact | Mitigation |
|------|--------|-----------|
| **LinkedIn data access restricted** | Agent cannot fetch current job titles or employment status | Fallback to public web search + company websites; start with LinkedIn API and broaden sources if needed |
| **Email validation false negatives** | Agent marks good emails as bouncy, reps don't call them | Conservative threshold on email scoring; manual review for Medium confidence; iterate on signals |
| **Adoption friction** | Reps don't trust the scoring, manually verify anyway, no time savings | Show 1–2 reps the before/after metrics first; gamify adoption (leaderboard for highest-confidence calls); brief daily standup |
| **Data quality in CRM** | Many leads have incomplete data (no email, no phone, no title), agent can't work | Prioritize validation on leads with at least email or phone; flag incomplete records for cleanup; this is actually good data hygiene signal |

---

# FAQ

**Q: Why not just buy more ZoomInfo licenses?**  
A: ZoomInfo is expensive and still requires manual effort. Even with unlimited access, an SDR still has to open it, cross-reference it, and update Salesforce. The agent removes all that. And once the agent is running, the company sees the real ROI of validated data—which makes a long-term data quality investment easier to justify.

**Q: How is this different from what the SDRs are doing today?**  
A: Today, each SDR is doing the same validation work manually, in parallel, wasting time. Tomorrow, the work is done once, overnight, for the entire team. This is the difference between 1:1 inefficiency and batch automation.

**Q: What happens if the agent makes mistakes?**  
A: The confidence scoring handles this. Low-confidence leads are not removed; they're flagged for manual review. And because we measure baseline and post-launch metrics, we'll see if adoption is working or if we need to adjust.

**Q: Will this work for teams outside sales?**  
A: Yes. Any team that works with leads, prospects, or contact lists—recruiting, partnerships, account management—would benefit. This is a pattern.

---

# Appendix

- **Interview source:** `output/interview-individual-jenkins-2025-10-12.md`
- **Company context:** `context/company.md`
- **Strategy context:** `context/strategy.md`

---

# Product Summary

**Lead Validator** is an overnight batch AI agent that validates, enriches, and confidence-scores every lead in a sales team's pipeline, so reps spend their day selling instead of verifying data. It auto-updates Salesforce with current job titles, employment status, and email validity, flags low-confidence leads for manual review, and delivers a prioritized lead digest every morning. For SDRs like Sarah who currently spend 50% of their time on data cleanup, this unlocks an estimated 50% increase in sales calls per day—directly impacting quota attainment and go-to-market velocity.

