# Individual Interview Analysis: David Kim

## 1. Interviewee Profile

- **Name:** David Kim
- **Role:** Sales Operations Manager
- **Date of interview:** 2025-10-19
- **Topic:** The Stack and Data Hygiene

David owns the CRM and the wider sales tech stack. He is the person who gets paged when integrations fail ("The API sync broke again at 3 AM. Woke me up."). He sees the sales organization as a data system, and he judges it by data integrity, cost efficiency, and what the logs show rather than by what people say. He is quick to trust telemetry over testimony: he checks the reps' claims about their research habits against web traffic logs. To him the sales team is a source of unreliable input, and the CRM is supposed to be the system of record but has failed at that job. He is also aware of the economics: he frames rep time in salary terms and enrichment tools in per-record cost. His core belief is that the organization's real database has moved outside its walls, to LinkedIn, and that internal systems now only record outcomes after the fact.

## 2. Sentiment

- **Dominant emotional tone:** Sardonic, exasperated contempt for an irrational system. This is not helpless frustration. It is the irritation of a systems person who sees an obvious inefficiency nobody has fixed. He uses dark, vivid metaphors ("feral", "graveyard", "Swiss cheese") and sounds incredulous at the waste ("It makes no sense.", "It's backwards."). Underneath is a sense of being personally burdened by fragility he did not design.
- **Energy level:** Worn down but combative. He is clearly sleep-deprived and in firefighting mode ("fighting fires all morning"), yet he is engaged and opinionated, not resigned. He has a clear diagnosis and wants it acted on.
- **Trust level:**
  - *Tools:* Low. Enrichment tools (ZoomInfo, Clearbit) "break, or they're too expensive". The API sync breaks repeatedly ("again"). The databases are "feral".
  - *Colleagues (sales reps):* Low. He sees them as error-prone ("Fat fingers, lazy entries") and not fully honest about their workflow. He trusts the logs over their accounts ("I see the web traffic logs. I know the truth."). There is some sympathy, though, since he grants that they hate the admin work.
  - *Leadership:* Not mentioned directly. The implied criticism is about how resources are allocated (paying humans to copy-paste), which suggests some distance from whoever designed or tolerates the current setup.
- **Quote that captures his emotional state:**
  > "Why do I have a human being paid $80k a year acting as a copy-paste machine? It makes no sense."

## 3. Problems They Described

| # | Problem | How he described it | Pain level |
|---|---|---|---|
| 1 | **Fragile integrations / API sync failures** | "The API sync broke again at 3 AM. Woke me up." "Again" means it keeps happening. | **High (personal).** It costs him sleep and leaves him firefighting all morning. |
| 2 | **Poor CRM data integrity** | "Data integrity. 100%. No doubt about it. Our CRM is a graveyard... of outdated info." "It's Swiss cheese." | **Very high.** He named it his biggest operational headache, with absolute certainty. |
| 3 | **Error-prone manual data entry by reps** | "Reps enter stuff manually, and they make mistakes. Fat fingers, lazy entries, or they just don't enter it at all." | **High.** He sees it as the direct cause of data decay. |
| 4 | **The CRM is no longer the source of truth** | "the source of truth isn't the CRM anymore. It's the internet. Specifically, it's LinkedIn." | **High (structural).** The system of record has been displaced. |
| 5 | **Rep updates are optional and often skipped** | "maybe they update Salesforce, maybe they don't. Usually they don't." | **High.** Data goes stale as soon as the outside world changes. |
| 6 | **Enrichment tools are unreliable or too expensive** | "ZoomInfo, Clearbit—that are supposed to sync this auto-magically, but they break, or they're too expensive to run on every single contact record. So we rely on humans." | **Medium-high.** The automation that should solve this fails on reliability and cost. |
| 7 | **Wasted rep time on admin** | Reps "claim they spend 2 hours a day just updating contact fields based on what they see online." They call it "admin time" or "overhead". | **High (economic).** He frames it as an expensive misuse of $80k employees. |
| 8 | **Rep resentment of data maintenance** | "And they hate it. They despise it." | **Medium.** A morale and compliance issue that feeds problem 5. |
| 9 | **Gap between what reps say and what they do** | Reps claim to check "Crunchbase... the news... the stock ticker," but "It's 90% LinkedIn." | **Medium.** It erodes trust and hides the true workflow. |
| 10 | **Inverted system architecture** | LinkedIn is "their real database. Ours is just where they log the result so they get paid commissions. It's backwards." | **High (conceptual).** The CRM has shrunk to a commission ledger instead of a working tool. |

## 4. Urgency Signals

- **Recurring overnight outages, happening right now:** "The API sync broke again at 3 AM." "I've been fighting fires all morning." This is his immediate, lived pain on the day of the interview.
- **Daily time drain, quantified:** "2 hours a day" per rep spent updating contact fields. That is a measurable, ongoing cost. Note that it is the reps' claim ("They claim"), so David is relaying it rather than vouching for it, but he does not dispute the scale.
- **Cost framing:** "$80k a year", a person used as "a copy-paste machine". He ties the waste directly to salary dollars.
- **Concentration metric:** "It's 90% LinkedIn." This is a data point from logs that shows where the work actually happens.
- **Certainty and intensity spikes:** "Data integrity. 100%. No doubt about it." "They despise it." "It makes no sense." "It's backwards."
- **Ongoing decay:** "Usually they don't [update]." Data quality gets worse continuously, not occasionally.

**Most urgent by his own framing:** CRM data integrity (his number-one headache) and the fragile sync infrastructure that is disrupting him today.

## 5. Underlying Needs

**What he said he wants (stated):**
- A clean CRM with accurate, current contact data.
- Automatic syncing of public information ("auto-magically") instead of relying on humans.
- Reps to stop wasting time on copy-paste work.

**What he actually needs:**
- **This person needs** contact and company changes (title changes, promotions, acquisitions) to flow from LinkedIn into the CRM automatically, **so that** the CRM stops decaying and becomes a trustworthy system of record again.
- **This person needs** the integration layer to be reliable and observable, failing gracefully rather than catastrophically, **so that** he stops being woken at 3 AM and can spend his time on improvements instead of firefighting.
- **This person needs** data enrichment whose cost scales sensibly, for example triggered by detected changes rather than a full refresh of every record, **so that** automation is affordable across the whole database rather than only part of it.
- **This person needs** to meet reps where they already work (the LinkedIn tab) instead of asking them to change behavior, **so that** data capture happens as a by-product of their real workflow, not as resented "overhead".
- **This person needs** to remove humans from mechanical data transfer entirely, **so that** expensive sales time goes to selling and the error sources (fat fingers, skipped updates) go away.
- **This person needs** visibility into the real data sources and data freshness, **so that** he can manage data quality based on facts rather than on rep self-reports.

**Stated vs. actual:** He frames the problem as "data hygiene" and rep sloppiness. The deeper need is architectural. The organization's real source of truth sits outside its systems, and he needs a reliable bridge from LinkedIn to the CRM that does not depend on human discipline or on fragile, expensive bulk-enrichment tools. Cleaning the CRM once would not solve it. The flow itself has to change.

## 6. Notable Quotes

1. > "'Behaving'? That implies they have manners. They're feral."
2. > "Our CRM is a graveyard. It's a graveyard of outdated info."
3. > "Why do I have a human being paid $80k a year acting as a copy-paste machine? It makes no sense."
4. > "But I see the web traffic logs. I know the truth. It's 90% LinkedIn. They just keep that tab open all day. It's their real database."
5. > "Ours is just where they log the result so they get paid commissions. It's backwards."
