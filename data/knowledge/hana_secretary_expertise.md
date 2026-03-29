# Hana (Secretary Agent) -- Knowledge Base
## ComInc. | Inbound Tourism Business, Joetsu/Myoko, Niigata, Japan
### Last Updated: 2026-03-29

---

## 1. Notion Workspace Best Practices for Small Businesses

### 1.1 Core Design Principles

- **Start simple**: Do not build dozens of pages on Day 1. Begin with a dashboard and add only what you actually use.
- **Central Dashboard**: Create one main dashboard as your home base -- the first page anyone opens. It should answer "What matters right now?"
- **Consolidate**: A single Business Hub (clients, finances, projects, documents) is better than scattered pages.
- **Performance awareness**: Notion performance degrades noticeably above 5,000 records per database (3-5 second load times). Plan to archive or split large datasets.

### 1.2 Database Design

**Recommended Core Databases for ComInc.**:

| Database | Purpose | Key Properties |
|---|---|---|
| Projects | Track all active initiatives | Name, Status, Owner (Agent), Priority, Due Date, Category |
| Tasks | Individual work items | Name, Status, Assignee, Due Date, Project (Relation), Priority |
| Proposals | Business proposals pipeline | Title, Score, Status, Submitted By, Evaluated Date |
| Customers | Tourist/client records | Name, Nationality, Service Used, Date, Satisfaction Score |
| Knowledge Base | Reference materials | Title, Category, Agent, Last Updated |
| Meetings & Decisions | Decision log | Date, Attendees, Decisions Made, Action Items |

**Relations & Rollups**:
- Use the **Relation** property to connect databases (e.g., Tasks -> Projects, Proposals -> Projects).
- Use **Rollup** properties to aggregate data from related items (e.g., count of open tasks per project, average proposal score).
- When relating a database to itself, toggle off "Two-way relation" to avoid duplication.
- Give relations and rollups clear, descriptive names (e.g., "Related Tasks" not "Relation 1").

**Views**:
- **Table**: Default for data entry and bulk editing.
- **Board (Kanban)**: Best for tracking status workflows (To Do -> In Progress -> Done).
- **Calendar**: Use for deadline-driven views (proposal due dates, event schedules).
- **Timeline (Gantt)**: Use for project planning with start/end dates.
- **List**: Clean, minimal view for reference databases like Knowledge Base.
- Create **filtered views** per agent (e.g., "Fin's Tasks", "Hana's Review Queue").

### 1.3 Automations

- **Database automations**: Trigger actions when a property changes (e.g., when Status changes to "Ready for Review", notify Hana).
- **Template buttons**: Create buttons that auto-populate new pages with standard structure (e.g., "New Proposal" template, "Weekly Report" template).
- **Recurring tasks**: Use automations or template buttons to generate recurring items (daily standups, weekly reports).
- **Linked Database views**: Embed filtered views of one database inside another page for context (e.g., show a project's tasks inside the project page).

### 1.4 Templates to Create

1. **Proposal Evaluation Template**: Pre-filled scoring rubric, standard fields.
2. **Meeting Notes Template**: Date, attendees, agenda, decisions, action items.
3. **Weekly Report Template**: Accomplishments, blockers, next week priorities.
4. **Project Brief Template**: Objective, scope, timeline, success metrics.
5. **Customer Feedback Template**: Service used, date, rating, comments, follow-up actions.

### 1.5 Wiki and Knowledge Management

- Use the "Turn into Wiki" feature on key pages to enable verification badges indicating content freshness.
- Set verification periods: 30 days for rapidly changing info (pricing, availability), 90 days for stable content (SOPs, policies).
- Assign page owners who are responsible for keeping content current.
- Use tags consistently across all databases for cross-referencing (e.g., "winter", "marketing", "minpaku").
- Link related pages using @-mentions and relation properties to build a connected knowledge graph.
- Create a "Getting Started" page for onboarding new team members or AI agents.
- Use Notion AI Q&A to enable natural-language search across the entire workspace.

### 1.6 Access Control and Maintenance

- Limit modification rights to designated teams/individuals to prevent unauthorized changes.
- Schedule quarterly reviews to refresh outdated content.
- Use the "Last Edited" property to identify stale pages that need attention.
- Archive completed projects and outdated content rather than deleting them.

---

## 2. Project Management for AI Agent Teams

### 2.1 Multi-Agent Task Tracking

ComInc. operates with multiple AI agents (Hana, Fin, and potentially others). Coordination requires:

**Task Assignment Framework**:
- Every task must have a single **Owner** (the agent responsible).
- Use a **Status** property with standardized values: `Backlog`, `To Do`, `In Progress`, `In Review`, `Done`, `Blocked`.
- Add a **Requester** field to track who initiated the task.
- Use **Dependencies** (relation to other tasks) to track what blocks what.

**Agent Handoff Protocol**:
1. When Agent A completes work that Agent B needs, change status to "In Review" and tag Agent B.
2. Agent B reviews, either approves (moves to Done) or returns with comments.
3. All handoffs should include a brief **handoff note** explaining what was done and what's needed next.

**Status Reporting**:
- Each agent updates their task statuses daily.
- Hana (Secretary) aggregates a daily summary for CEO review.
- Use rollup properties to auto-calculate: tasks completed this week, tasks overdue, tasks blocked.

### 2.2 Coordination Best Practices

- **Single source of truth**: All task tracking happens in one Notion workspace, not in chat or email.
- **Async-first**: Agents communicate through Notion comments and status updates, not real-time meetings (unless escalation needed).
- **Escalation path**: Blocked -> Comment with details -> If unresolved in 24h -> Flag to Hana -> If still unresolved -> Escalate to CEO.
- **Cross-agent visibility**: Each agent can see all tasks (not just their own) to understand context and dependencies.

### 2.3 Progress Dashboards

Build a **CEO Dashboard** in Notion with:
- Active projects count and status breakdown (Board view).
- Overdue tasks (filtered Table view, sorted by days overdue).
- This week's completed items.
- Upcoming deadlines (Calendar view, next 2 weeks).
- Proposal pipeline (Board view by stage).

---

## 3. Proposal Evaluation Framework

### 3.1 Scoring Rubric

Use a weighted scoring system. Each criterion is scored 1-5 and multiplied by its weight.

| Criterion | Weight | 1 (Poor) | 3 (Adequate) | 5 (Excellent) |
|---|---|---|---|---|
| **Feasibility** | 25% | Requires resources/skills we don't have | Achievable with significant effort | Clearly achievable with current resources |
| **User Value** | 25% | Minimal benefit to tourists | Moderate improvement to experience | Transformative experience improvement |
| **ROI Potential** | 20% | Negative or break-even | Modest returns within 12 months | Strong returns within 6 months |
| **Strategic Alignment** | 15% | Doesn't fit ComInc. mission | Partially aligned | Directly advances core mission |
| **Urgency** | 15% | Can wait 6+ months | Should act within 3 months | Immediate opportunity, time-sensitive |

**Total Score** = Sum of (Score x Weight) for all criteria. Maximum = 5.00.

### 3.2 Score Interpretation

| Score Range | Action |
|---|---|
| 4.0 - 5.0 | **Priority**: Implement immediately. Allocate resources. |
| 3.0 - 3.9 | **Approve**: Schedule for implementation within current quarter. |
| 2.0 - 2.9 | **Conditional**: Revise proposal to address weak areas, then re-evaluate. |
| 1.0 - 1.9 | **Decline**: Does not meet minimum threshold. Archive with feedback. |

### 3.3 Evaluation Process

1. **Submission**: Proposal submitted to Notion Proposals database with all required fields.
2. **Completeness Check**: Hana verifies all required information is present (see QA Checklist, Section 5).
3. **Financial Review**: Fin reviews financial projections and budget.
4. **Scoring**: Hana applies the scoring rubric.
5. **Summary**: Hana writes a 3-5 sentence executive summary with recommendation.
6. **CEO Decision**: Present top proposals (score >= 3.0) with summaries for CEO decision.

### 3.4 Required Proposal Fields

- Title and one-paragraph summary
- Problem/opportunity description
- Proposed solution
- Target customer segment
- Estimated cost (initial + ongoing)
- Expected revenue or value
- Timeline to implement
- Risks and mitigations
- Success metrics (how to measure if it worked)

---

## 4. Tourism Customer Experience Evaluation

### 4.1 What Inbound Tourists Value (Japan-Specific Research)

**Top Activities by Participation**:
- Japanese food: 96.6% of visitors
- Shopping: 77.2% of visitors

**Highest Satisfaction Drivers**:
- Experiences of Japan's lifestyle: 70.0% satisfaction
- History and traditional culture: 67.9% satisfaction
- Authentic, locale-specific experiences that require effort
- Interaction with locals and deeper cultural understanding

**Cultural Differences in Preferences**:
- Western tourists: Prioritize hospitality and staff behavior.
- Asian tourists (e.g., Chinese): Prioritize room/facility quality, food culture, and cleanliness.
- All segments: Value experiences they cannot get at home.

### 4.2 Key UX Signals for ComInc. (Joetsu/Myoko Context)

**Snow/Outdoor Experiences**:
- Myoko receives 13-16 meters of snowfall annually -- world-class powder.
- Growing international popularity as an authentic alternative to Niseko.
- English-speaking ski guides and backcountry experiences are in high demand.
- Private guiding sessions (1-4 people) command premium pricing.

**Service Quality Indicators**:
1. **Responsiveness**: Speed of booking confirmation, pre-arrival communication.
2. **Personalization**: Tailored itinerary based on guest preferences, ability level.
3. **Cultural Authenticity**: Local food, onsen experience, interaction with community.
4. **Communication**: Multilingual support (English minimum; Chinese, Korean, Thai are growing).
5. **Safety**: Clear safety briefings, proper equipment, emergency protocols.
6. **Surprise & Delight**: Small unexpected touches (welcome gift, local treat, photo service).

### 4.3 Customer Feedback Collection

- **Post-experience survey**: 5-question max, send within 24 hours.
- **Review encouragement**: Guide guests to leave Google/TripAdvisor reviews.
- **Net Promoter Score (NPS)**: "How likely are you to recommend us?" (0-10 scale).
- **Track by segment**: Nationality, season, service type, group size.
- **Sentiment analysis**: Monitor online reviews for recurring themes (positive and negative).

---

## 5. Quality Assurance Checklist

### 5.1 Before Presenting Proposals to CEO

Use this checklist before any proposal, report, or recommendation goes to the CEO.

**Completeness**:
- [ ] All required fields are filled (see Section 3.4).
- [ ] Financial projections reviewed by Fin.
- [ ] Scoring rubric applied with all 5 criteria rated.
- [ ] Executive summary written (3-5 sentences).
- [ ] Risks identified with at least one mitigation per risk.
- [ ] Success metrics defined and measurable.

**Accuracy**:
- [ ] Financial numbers verified (no calculation errors).
- [ ] Market data cited with sources and dates.
- [ ] No conflicting information between sections.
- [ ] Timeline is realistic (checked against current resource availability).
- [ ] Legal/regulatory requirements noted (e.g., minpaku 180-day limit, guide licensing).

**Brand Consistency**:
- [ ] Tone is professional but approachable (matches ComInc. voice).
- [ ] Terminology is consistent throughout the document.
- [ ] All content is in the correct language (Japanese for internal, English for international-facing).
- [ ] No placeholder text or "[TBD]" markers remaining.
- [ ] Formatting is clean: headings, bullet points, tables used appropriately.

**Strategic Fit**:
- [ ] Aligns with ComInc.'s mission (inbound tourism in Joetsu/Myoko).
- [ ] Does not conflict with existing active projects.
- [ ] Considers seasonal timing (ski season Nov-Apr, green season May-Oct).
- [ ] Target customer segment is clearly identified.

### 5.2 Before Publishing Any External Content

- [ ] Grammar and spelling checked.
- [ ] Contact information is current.
- [ ] Pricing is accurate and up to date.
- [ ] Images have proper rights/licensing.
- [ ] Links are functional (no broken URLs).
- [ ] Mobile-friendly formatting.

---

## 6. Meeting/Summary Templates

### 6.1 Daily Standup Format

**Duration**: 15 minutes maximum.
**Frequency**: Every business day, same time.
**Format**: Each agent reports (2-3 minutes each).

```
## Daily Standup -- [YYYY-MM-DD]

### Hana (Secretary)
- **Yesterday**: [What was completed]
- **Today**: [What is planned]
- **Blockers**: [Any obstacles, or "None"]

### Fin (Finance)
- **Yesterday**: [What was completed]
- **Today**: [What is planned]
- **Blockers**: [Any obstacles, or "None"]

### [Other Agents as added]

---
### Action Items from Standup
- [ ] [Action] -- Owner: [Agent] -- Due: [Date]
```

**Rules**:
- Stick to the three questions. Deep discussions go to a separate follow-up.
- If blocked, state what you need and from whom.
- Hana facilitates and ensures no one dominates the standup.

### 6.2 Weekly Report Format

**Submitted by**: Hana (on behalf of all agents)
**Due**: Every Friday end of day
**Audience**: CEO

```
## Weekly Report -- Week of [YYYY-MM-DD]

### Highlights
- [Top 1-3 accomplishments this week]

### Key Metrics
| Metric | This Week | Last Week | Trend |
|---|---|---|---|
| Tasks Completed | X | Y | Up/Down/Flat |
| Proposals Evaluated | X | Y | |
| Customer Inquiries | X | Y | |
| Revenue (if applicable) | X | Y | |

### Active Projects Status
| Project | Status | Owner | Next Milestone |
|---|---|---|---|
| [Project Name] | On Track / At Risk / Blocked | [Agent] | [Milestone + Date] |

### Issues & Risks
- [Issue 1]: [Brief description + proposed action]
- [Issue 2]: [Brief description + proposed action]

### Next Week Priorities
1. [Priority 1]
2. [Priority 2]
3. [Priority 3]

### Decisions Needed from CEO
- [Decision 1]: [Context + options + recommendation]
```

### 6.3 Decision Log Format

Track all significant decisions in a dedicated Notion database.

**Database Properties**:
- **Decision Date**: Date
- **Decision**: Short title (e.g., "Approved winter package pricing")
- **Context**: Why was this decision needed?
- **Options Considered**: What alternatives were evaluated?
- **Decision Made**: What was chosen and why?
- **Decided By**: CEO / Agent name
- **Impact**: What changes as a result?
- **Review Date**: When to revisit this decision (optional)

**Why This Matters**:
- Prevents re-litigating old decisions.
- Provides context for new team members or agents.
- Creates accountability and traceability.
- Helps identify patterns in decision-making over time.

### 6.4 Meeting Notes Template

```
## Meeting Notes -- [Meeting Title]
**Date**: [YYYY-MM-DD]
**Attendees**: [Names/Agents]
**Facilitator**: [Name]

### Agenda
1. [Topic 1]
2. [Topic 2]
3. [Topic 3]

### Discussion Notes
#### [Topic 1]
- [Key points discussed]
- [Different perspectives raised]

#### [Topic 2]
- [Key points discussed]

### Decisions Made
- [Decision 1]: [Details]
- [Decision 2]: [Details]

### Action Items
| Action | Owner | Due Date | Status |
|---|---|---|---|
| [Action 1] | [Agent] | [Date] | To Do |
| [Action 2] | [Agent] | [Date] | To Do |

### Next Meeting
- **Date**: [Date]
- **Agenda items to carry forward**: [Items]
```

---

---

## 7. Executive Assistant Communication Best Practices

### 7.1 The BLUF Method (Bottom Line Up Front)

When presenting information to Sho, always lead with the conclusion:

```
Subject: [Topic]
Priority: [High/Medium/Low]
Decision Needed: [Yes/No - if Yes, state the decision]
BLUF: [1-2 sentence summary of the key point]
Key Points:
- [Point 1]
- [Point 2]
- [Point 3]
Recommended Action: [What Hana recommends]
Deadline: [If applicable]
```

### 7.2 Calendar Management Principles

1. **Know the executive's preferences**: Learn Sho's peak productivity hours, preferred meeting lengths, and buffer time needs.
2. **Color-code by category**: Internal meetings, external meetings, travel, focused work, personal time.
3. **Protect deep work time**: Block at least 2-3 hours daily for strategic thinking.
4. **Buffer between meetings**: Add 15-minute buffers for context switching.
5. **Batch similar meetings**: Group similar meeting types on the same day.
6. **Evening prep**: Send next-day summary highlighting early meetings, preparation needed, and key decisions.

### 7.3 Priority Matrix (Adapted for ComInc.)

| | Urgent | Not Urgent |
|---|---|---|
| **Important** | Handle immediately, notify Sho | Schedule for review, add to weekly agenda |
| **Not Important** | Delegate or batch process | Archive, low-priority queue |

**Priority Classifications:**
- **P0 (Immediate)**: Safety issues, legal deadlines, major partner/client problems, revenue-threatening situations
- **P1 (Same Day)**: Client bookings requiring response, partner communications with time sensitivity, financial deadlines
- **P2 (This Week)**: Proposals from departments, non-urgent partner updates, planning items
- **P3 (When Available)**: Industry news, nice-to-have improvements, long-term planning ideas

### 7.4 Communication Filtering

- Screen incoming messages and categorize by priority.
- Create daily digest of non-urgent items.
- Flag items that need Sho's personal attention vs. items that can be handled independently.
- Track response deadlines and send reminders.
- Maintain a "Waiting For" list for items pending external responses.

---

## 8. Cross-Department Proposal Coordination

### 8.1 Department-Specific Review Questions

**Marketing Department Proposals:**
- Does this reach our target audience (inbound tourists interested in Joetsu/Myoko)?
- Is the messaging culturally appropriate for international visitors?
- What is the expected ROI? Is a measurement plan defined?
- Does it align with current brand positioning?
- Are there seasonal timing considerations?

**Web Department Proposals:**
- Does this improve the user booking/discovery experience?
- Is it mobile-friendly (critical for travelers)?
- Does it support multiple languages (at minimum EN/JP)?
- What is the maintenance burden after launch?
- Does it integrate with existing systems?

**Operations Department Proposals:**
- Does this improve the guest experience on the ground?
- Is it operationally feasible with current staff/resources?
- What are the safety and liability considerations?
- Does it account for seasonal variations?
- Are required partnerships secured?

### 8.2 Cross-Department Alignment Checklist

Before any proposal moves to approval:
- [ ] Budget impact reviewed (coordinate with Fin agent)
- [ ] Timeline is realistic and doesn't conflict with other department initiatives
- [ ] User/customer impact assessed (Hana's primary responsibility)
- [ ] Dependencies on other departments identified
- [ ] Success metrics defined and measurable
- [ ] Risk assessment completed
- [ ] Alignment with ComInc.'s overall mission confirmed

### 8.3 Coordination Practices

- Maintain a shared project timeline visible to all departments.
- Hold weekly cross-department sync (15-20 min max).
- Use a shared Notion database for all proposals so status is transparent.
- Assign a single point of contact per department for each initiative.
- Document decisions and rationale so institutional knowledge is preserved.

---

## 9. Information Quality Control (Deep Dive)

### 9.1 Fact-Checking Framework

Before presenting any information to Sho, verify across four dimensions:

**Source Reliability:**
- Is the source official (government website, established platform)?
- When was the information last updated?
- Are there multiple sources confirming the same fact?

**Numerical Accuracy:**
- Do the numbers add up? (Cross-check all calculations)
- Are units consistent (yen vs. dollars, per night vs. per month)?
- Are percentages based on the correct denominator?

**Temporal Relevance:**
- Is this data current enough for the decision being made?
- Have regulations or conditions changed since publication?
- For seasonal tourism data, is the correct season being referenced?

**Contextual Accuracy:**
- Does the information apply to Joetsu/Myoko specifically, or is it national/general?
- Are comparisons fair (similar market size, season, region)?
- Are there local exceptions or special conditions?

### 9.2 Gap Detection in Proposals

Common gaps to actively look for:
1. **Missing user perspective** -- Who is the target customer? How does this benefit them?
2. **Missing measurement plan** -- How will success be measured?
3. **Missing risk assessment** -- What could go wrong?
4. **Missing budget details** -- What will this cost? What is the ROI?
5. **Missing timeline** -- When will this be done? Are there milestones?
6. **Missing dependencies** -- What else needs to happen first?
7. **Missing competitive context** -- What are competitors doing?
8. **Missing seasonal considerations** -- How does this vary by season?
9. **Missing language/cultural considerations** -- Is this appropriate for international visitors?
10. **Missing legal/regulatory check** -- Are there permits, licenses, or regulations?

### 9.3 Asking the Right Questions

For any proposal or piece of information, always ask:
- "Who specifically benefits from this?" (Reject vague answers like "everyone")
- "What evidence supports this assumption?"
- "What happens if this doesn't work?"
- "Have we done something similar before? What did we learn?"
- "What would a tourist from [specific country] think of this?"
- "Is there a simpler/cheaper way to achieve the same goal?"
- "What are we NOT doing if we commit resources to this?"

---

## 10. User-Perspective Review and Scoring Framework (Hana's Key Responsibility)

### 10.1 Hana's Primary Role: The Customer Advocate

Hana serves as the voice of the customer/user within ComInc. Every proposal, idea, or initiative from any department must pass through Hana's user-centric evaluation before being presented to Sho. This ensures that business decisions remain grounded in what actually matters to ComInc.'s customers: inbound tourists visiting the Joetsu/Myoko region.

**Why this matters:**
- Departments naturally optimize for their own metrics (marketing for impressions, web for traffic, operations for efficiency).
- Without a dedicated user advocate, customer needs can be lost in internal priorities.
- Hana bridges the gap between business goals and tourist satisfaction.

### 10.2 Target User Personas

When evaluating from a user perspective, consider these primary personas:

**Persona 1: Adventure Seeker (Winter Focus)**
- International visitor, typically from Australia, SE Asia, or North America
- Primarily interested in skiing/snowboarding at Myoko resorts
- Values: powder snow quality, accommodation proximity to slopes, English-language support, authentic cultural experiences after skiing
- Budget: Mid to high range
- Pain points: Language barriers, transportation from airport, booking complexity

**Persona 2: Cultural Explorer (Year-round)**
- International or domestic visitor interested in Japanese culture
- Interested in: sake breweries, temples, local food, onsen, historical sites in Joetsu
- Values: Authenticity, local knowledge, unique experiences not found in guidebooks
- Budget: Mid range
- Pain points: Limited English information, difficulty finding non-mainstream attractions

**Persona 3: Family/Group Traveler**
- Families with children or friend groups
- Looking for: Safe activities, accommodation for groups, variety of experiences
- Values: Convenience, safety, good value, memorable experiences
- Budget: Value-conscious but willing to pay for quality
- Pain points: Planning complexity, accommodation size limitations, child-friendly options

**Persona 4: Digital Nomad / Extended Stay**
- Remote worker spending 1-4 weeks in the area
- Interested in: Reliable WiFi, comfortable workspace, local community, affordable accommodation
- Values: Work-life balance, authentic living experience, community connection
- Budget: Budget to mid range for long stays
- Pain points: Monthly accommodation availability, co-working spaces, social isolation

### 10.3 The ComInc. User-Centric Scoring System (100-Point Scale)

Each proposal is evaluated across 10 dimensions, each worth up to 10 points:

#### Dimension 1: User Need Alignment (0-10 points)
Does this address a real, validated need of our target users?
- **9-10**: Directly addresses a top-3 pain point identified through user feedback/data
- **7-8**: Addresses a known user need with some supporting evidence
- **5-6**: Addresses a plausible user need but lacking direct evidence
- **3-4**: Loosely connected to user needs; more business-driven
- **0-2**: No clear connection to user needs; internally motivated

#### Dimension 2: User Experience Impact (0-10 points)
How significantly does this improve the tourist's experience?
- **9-10**: Transformative improvement; removes major friction or creates delight
- **7-8**: Significant improvement to a key touchpoint in the user journey
- **5-6**: Moderate improvement; nice to have but not critical
- **3-4**: Minor improvement; most users would not notice
- **0-2**: No meaningful impact on user experience; may even worsen it

#### Dimension 3: Accessibility and Inclusivity (0-10 points)
Is this accessible to our diverse international audience?
- **9-10**: Fully multilingual, culturally sensitive, accessible to all ability levels
- **7-8**: Available in English and Japanese, culturally appropriate
- **5-6**: Available in one language with plans for expansion
- **3-4**: Language or cultural barriers exist that limit reach
- **0-2**: Only accessible to a narrow audience; excludes key segments

#### Dimension 4: Ease of Discovery and Use (0-10 points)
How easy is it for a tourist to find and use this?
- **9-10**: Intuitive, zero-friction; tourist encounters it naturally in their journey
- **7-8**: Easy to find with minimal effort; clear instructions
- **5-6**: Requires some searching or explanation
- **3-4**: Difficult to discover; requires insider knowledge
- **0-2**: Confusing or hidden; tourists would struggle to access

#### Dimension 5: Trust and Safety (0-10 points)
Does this build trust and ensure safety for international visitors?
- **9-10**: Exceeds safety standards; builds strong trust through transparency
- **7-8**: Meets all safety standards; clear policies and communications
- **5-6**: Adequate safety measures; some trust-building elements present
- **3-4**: Safety or trust concerns not fully addressed
- **0-2**: Potential safety issues or trust-damaging elements

#### Dimension 6: Value for Money (0-10 points)
Does the tourist receive fair value relative to what they pay?
- **9-10**: Exceptional value; tourists would rave about the price-quality ratio
- **7-8**: Good value; competitive with similar offerings elsewhere
- **5-6**: Fair value; meets expectations without exceeding them
- **3-4**: Somewhat overpriced for what is delivered
- **0-2**: Poor value; likely to generate negative reviews

#### Dimension 7: Memorable and Shareable (0-10 points)
Will tourists remember this and want to share it with others?
- **9-10**: Creates "wow" moments; tourists will definitely post on social media and tell friends
- **7-8**: Memorable experience that tourists would recommend
- **5-6**: Pleasant but not particularly noteworthy
- **3-4**: Forgettable; blends in with other travel experiences
- **0-2**: Negative or bland; would not be mentioned to others

#### Dimension 8: Seasonal Resilience (0-10 points)
Does this work across seasons or only during peak periods?
- **9-10**: Works year-round with equal effectiveness
- **7-8**: Works well in 3 seasons or has clear seasonal adaptation plan
- **5-6**: Works well in 2 seasons
- **3-4**: Primarily single-season with limited off-season value
- **0-2**: Only viable in one brief period; idle most of the year

#### Dimension 9: Local Authenticity (0-10 points)
Does this reflect genuine Joetsu/Myoko character and culture?
- **9-10**: Deeply rooted in local culture; could only exist in this specific region
- **7-8**: Strong local elements; clearly connected to the area
- **5-6**: Some local flavor but could be replicated elsewhere
- **3-4**: Generic tourism offering with minimal local character
- **0-2**: Feels artificial or disconnected from the local community

#### Dimension 10: Repeat Visit Potential (0-10 points)
Does this encourage tourists to return or extend their stay?
- **9-10**: Creates strong emotional connection; tourists will plan return trips
- **7-8**: Offers enough depth that repeat visits would reveal new experiences
- **5-6**: Some repeat potential; tourists might come back if in the area
- **3-4**: Limited repeat appeal; one-time experience
- **0-2**: No repeat visit incentive

### 10.4 Score Interpretation and Action

| Score Range | Rating | Action |
|------------|--------|--------|
| 85-100 | Excellent | Strong recommend for approval. Minimal revisions needed. |
| 70-84 | Good | Recommend with specific improvements. Address weak dimensions. |
| 55-69 | Moderate | Needs significant revision. Identify top 3 dimensions to improve. |
| 40-54 | Below Average | Major rethinking needed. Consider if the core concept is viable. |
| 0-39 | Poor | Recommend rejection or complete redesign from user perspective. |

### 10.5 User-Perspective Scoring Report Template

```
## User-Perspective Evaluation Report

**Proposal:** [Title]
**Department:** [Marketing / Web / Operations]
**Evaluated by:** Hana (Secretary Agent)
**Date:** [Date]

### Overall Score: [X]/100 -- [Rating]

### Dimension Breakdown
| Dimension | Score | Key Reasoning |
|-----------|-------|---------------|
| User Need Alignment | X/10 | [Brief justification] |
| User Experience Impact | X/10 | [Brief justification] |
| Accessibility & Inclusivity | X/10 | [Brief justification] |
| Ease of Discovery & Use | X/10 | [Brief justification] |
| Trust & Safety | X/10 | [Brief justification] |
| Value for Money | X/10 | [Brief justification] |
| Memorable & Shareable | X/10 | [Brief justification] |
| Seasonal Resilience | X/10 | [Brief justification] |
| Local Authenticity | X/10 | [Brief justification] |
| Repeat Visit Potential | X/10 | [Brief justification] |

### Top Strengths
1. [Strongest dimension and why]
2. [Second strongest and why]

### Key Concerns
1. [Weakest dimension and what needs to change]
2. [Second weakest and what needs to change]

### User Persona Impact
- Adventure Seeker: [How this affects them]
- Cultural Explorer: [How this affects them]
- Family/Group: [How this affects them]
- Digital Nomad: [How this affects them]

### Recommendation
[Approve / Approve with Revisions / Revise and Resubmit / Reject]

### Specific Improvement Suggestions
1. [Actionable suggestion tied to a specific dimension]
2. [Actionable suggestion tied to a specific dimension]
3. [Actionable suggestion tied to a specific dimension]
```

### 10.6 Quick Evaluation Checklist (For Rapid Reviews)

When a full 100-point evaluation is not needed, use this checklist:

- [ ] Does a real tourist actually want or need this?
- [ ] Can a non-Japanese-speaking visitor easily use this?
- [ ] Would I recommend this to a friend visiting Myoko/Joetsu?
- [ ] Does this create a moment worth sharing on social media?
- [ ] Is the pricing fair compared to similar offerings?
- [ ] Does this work in more than one season?
- [ ] Does this feel authentically local, not generic?
- [ ] Is there a clear way to measure if tourists like this?

### 10.7 Comparative Evaluation (When Multiple Proposals Compete)

```
## Comparative Evaluation -- [Resource/Budget Being Allocated]

| Dimension | Proposal A | Proposal B | Proposal C |
|-----------|-----------|-----------|-----------|
| User Need Alignment | X/10 | X/10 | X/10 |
| User Experience Impact | X/10 | X/10 | X/10 |
| Accessibility & Inclusivity | X/10 | X/10 | X/10 |
| Ease of Discovery & Use | X/10 | X/10 | X/10 |
| Trust & Safety | X/10 | X/10 | X/10 |
| Value for Money | X/10 | X/10 | X/10 |
| Memorable & Shareable | X/10 | X/10 | X/10 |
| Seasonal Resilience | X/10 | X/10 | X/10 |
| Local Authenticity | X/10 | X/10 | X/10 |
| Repeat Visit Potential | X/10 | X/10 | X/10 |
| **Total** | **X/100** | **X/100** | **X/100** |
| Budget Required | JPY X | JPY X | JPY X |
| Score per JPY 10K spent | X | X | X |

### Recommendation: [Proposal X] because [clear reasoning]
```

### 10.8 Integrating the Two Scoring Systems

Hana uses TWO scoring systems depending on context:

**System A: Weighted 5-Point Rubric (Section 3.1)**
- Best for: Quick evaluations, internal feasibility checks, business-priority decisions
- Dimensions: Feasibility, User Value, ROI Potential, Strategic Alignment, Urgency
- Max score: 5.00
- Use when: Sho needs a fast go/no-go recommendation

**System B: 100-Point User-Centric Score (Section 10.3)**
- Best for: Deep user-perspective analysis, comparing competing proposals, major decisions
- Dimensions: 10 user-focused criteria
- Max score: 100
- Use when: The proposal significantly affects the tourist experience or involves substantial investment

**When to use which:**
- Simple internal process changes -> System A only
- Customer-facing features, new services, marketing campaigns -> System B required
- Major strategic decisions -> Both systems, presented side by side

### 10.9 Ongoing User Insight Collection

To keep the user-perspective evaluation grounded in reality:

1. **Review Monitoring**: Regularly check Google Reviews, TripAdvisor, Booking.com reviews for Myoko/Joetsu area businesses (competitors and partners).
2. **Social Media Listening**: Monitor hashtags like #Myoko, #Joetsu, #MyokoKogen, #NiigataPowder, #Japow.
3. **Competitor Analysis**: Track what other inbound tourism companies in Japanese ski regions (Niseko, Hakuba, Nozawa) offer.
4. **Direct Feedback**: When available, collect and categorize tourist feedback from ComInc. experiences.
5. **Trend Tracking**: Monitor Japan inbound tourism trends from JTA (Japan Tourism Agency), JNTO (Japan National Tourism Organization), and tourism research reports.
6. **Review Sentiment Themes**: Identify recurring positive/negative themes across platforms to inform scoring calibration.

---

## Appendix A: Hana's Daily Workflow

1. **Morning**: Run daily standup, collect updates from all agents.
2. **Mid-morning**: Review new proposals and submissions for completeness.
3. **Midday**: Update Notion databases, check task statuses, flag overdue items.
4. **Afternoon**: Evaluate proposals (scoring with System A and/or System B), draft summaries, QA check outputs.
5. **End of day**: Update CEO dashboard, prepare next day's priorities, send evening summary to Sho.
6. **Friday**: Compile weekly report, update decision log, archive completed items.

## Appendix B: Key Tourism Context for User-Perspective Evaluation

### Regional Assets
- **Myoko Kogen**: Multiple ski resorts (Akakura Onsen, Myoko Suginohara, Seki Onsen, Ikenotaira). 13-16m annual snowfall.
- **Joetsu City**: Takada Castle, Takada Cherry Blossom Road, historical districts, sake breweries.
- **Local culture**: Sake brewing, onsen, local cuisine (sasa-dango, hegi-soba), rice farming.
- **Access**: Joetsu-Myoko Shinkansen station (approx. 2 hours from Tokyo).

### Current Market Context (2025-2026)
- Niigata Prefecture recorded 55% year-on-year increase in foreign guest nights.
- Myoko attracting significant international investment (Patience Capital Group $1.4B mega-resort project).
- Growing tension between development and community preservation -- some foreign operators do not join local tourism association.
- Season pass sales (4-resort pass at 115,000 yen) increased 1.5x over previous year.
- Japan Tourism Agency considering dual pricing for tourists vs. locals (panel launched March 2026).
- International Tourist Tax increasing from 1,000 to 3,000 yen per traveler (July 2026).

### Seasonal Calendar
| Month | Season | Tourism Focus |
|-------|--------|---------------|
| Dec-Mar | Winter (Peak) | Skiing, snowboarding, onsen, snow activities |
| Apr-May | Spring | Cherry blossoms, rice planting experiences, hiking |
| Jun-Aug | Summer | Mountain hiking, outdoor activities, festivals |
| Sep-Nov | Autumn | Foliage viewing, harvest experiences, cultural tours |
