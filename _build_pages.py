from _helpers import page, sec, intro, sidebar

# ============================================================ reviews index
page(
    "reviews/index.html",
    "Fixed Scope Reviews and Assessments | Planned Ltd",
    "Four named, fixed scope reviews: NEC4 programme acceptance, independent schedule assurance, delay and extension of time position, and Primavera Cloud migration readiness.",
    "schedule review, NEC4 programme review, delay analysis, schedule assurance, Primavera Cloud migration",
    "reviews/", 1,
    [("Home", "/"), ("Reviews", "")],
    "Fixed Scope Reviews",
    "Four defined pieces of work with a clear scope, a clear output and a fixed fee",
    intro([
        "Most consultancy is sold by the day, which means the buyer carries the risk of how many days it takes. These four reviews are sold as defined pieces of work instead. You know what is covered, what you get and what it costs before it starts.",
        "Each one is independent of both parties, delivered remotely, and written so that a reader who is not a planner can act on it.",
    ]) +
    sec("NEC4 Programme Acceptance Review", [
        "Test a contractor programme against clause 31.2 before it is submitted, or before you accept it. Delivered inside the two week reply period at clause 31.3, with written reasons that can be used directly in a notice.",
        "<a href=\"/reviews/nec4-programme-acceptance-review\">Read more about the NEC4 Programme Acceptance Review</a>",
    ]) +
    sec("Independent Schedule Assurance Review", [
        "A full DCMA 14 point assessment plus logic, critical path and float integrity checks, with the failing activities named and the findings ranked by whether they would change the completion date.",
        "<a href=\"/reviews/independent-schedule-assurance-review\">Read more about the Independent Schedule Assurance Review</a>",
    ]) +
    sec("Delay and Extension of Time Position Review", [
        "A candid assessment of where you stand before you commit money to a claim or a defence: what the records support, which method fits, and what is still gatherable.",
        "<a href=\"/reviews/delay-and-eot-position-review\">Read more about the Delay and Extension of Time Position Review</a>",
    ]) +
    sec("Primavera Cloud Migration Readiness Assessment", [
        "What carries across from Primavera P6, what has to be rebuilt, what should be retired rather than migrated, and a scope a credible cost can be built from.",
        "<a href=\"/reviews/primavera-cloud-migration-readiness-assessment\">Read more about the Primavera Cloud Migration Readiness Assessment</a>",
    ]) +
    sec("How these are priced and delivered", [
        "Fees depend on the size of the programme and whether site verification is included, and are confirmed in writing before anything starts. The terms that sit behind every engagement, including the working day, travel, insurance and response times, are published at <a href=\"/how-we-work\">How We Work</a>.",
    ]),
    sidebar("Not sure which one you need?",
            "Describe the situation in a sentence or two and we will tell you which review fits, or tell you that none of them does.",
            "Ask us", "The four reviews", [
                "NEC4 Programme Acceptance Review",
                "Independent Schedule Assurance Review",
                "Delay and EOT Position Review",
                "Primavera Cloud Migration Readiness Assessment",
            ]),
    "Defined work, defined output, agreed fee",
    "Tell us what you are dealing with and we will confirm scope and price in writing.",
    "Start a conversation",
    cta_text="See the four reviews"
)

# ============================================================ how we work
page(
    "how-we-work.html",
    "How We Work | Terms, Response Times and Standards | Planned Ltd",
    "The standards behind every Planned Limited engagement: working day, working week, travel and subsistence, insurance, response times, independence, confidentiality and data protection.",
    "consultancy terms, project controls consultant terms, day rate terms, response times",
    "how-we-work", 0,
    [("Home", "/"), ("How We Work", "")],
    "How We Work",
    "The standards behind every engagement, published so you do not have to ask",
    intro([
        "Most consultancies make you get to a phone call before you can find out how they actually operate. These are the terms that sit behind every Planned Limited engagement. They are published because they are the questions buyers ask first, and because a firm that has thought about them has usually thought about the rest.",
        "Fees are not published. They depend on the size and complexity of the programme and they are confirmed in writing before any work starts.",
    ]) +
    sec("The working day and week", [], [
        "<strong>A consultant day is eight hours</strong>, exclusive of travel and lunch.",
        "<strong>The working week is Monday to Friday</strong>, excluding public holidays in England and Wales.",
        "<strong>Core hours are 09:00 to 17:00</strong>, flexed to client requirements where a programme, a site or a time zone needs it.",
        "<strong>Part days are charged in half day units.</strong> We do not bill in six minute increments.",
        "Work outside these hours is agreed in advance, in writing, before it is done.",
    ]) +
    sec("Travel and subsistence", [], [
        "<strong>Included in the fee within 30 miles of central London.</strong> No travel charge, no mileage, no parking.",
        "Beyond 30 miles, travel and subsistence is charged at cost and at the client's own expenses policy where one exists.",
        "Travel time is not charged as consultancy time.",
        "Most work is delivered remotely. Site attendance is arranged where it adds something, and we will say so if we think it does not.",
    ]) +
    sec("Insurance", [
        "Professional indemnity cover is included in the fee and is not charged as a separate line. Current cover:",
    ], [
        "<strong>Professional Indemnity: £2,000,000</strong> each and every claim",
        "<strong>Public Liability: £10,000,000</strong> any one event",
        "<strong>Employers' Liability: £10,000,000</strong>",
        "Certificates are provided on request. See also our <a href=\"/credentials\">credentials</a>.",
    ]) +
    sec("Response times", [
        "These are commitments, not aspirations.",
    ], [
        "<strong>Enquiries are acknowledged within one working day.</strong>",
        "<strong>A written proposal follows within two working days</strong> of the scope being agreed.",
        "<strong>NEC4 programme reviews are delivered inside the reply period</strong> at clause 31.3, provided the file reaches us with at least five working days remaining.",
        "During an engagement, correspondence is answered within one working day.",
    ]) +
    sec("Independence", [
        "We do not resell software, we hold no reseller agreement with any vendor, and we take no commission on any licence, tool or platform we recommend.",
        "Where a review concerns work carried out by another party, we say what the evidence supports, including where that is unwelcome. A review that tells a client what it wants to hear has no value to the client and none to us.",
        "Where we cannot act independently because of an existing relationship, we say so and decline.",
    ]) +
    sec("Confidentiality and data protection", [], [
        "We sign client non disclosure agreements as a matter of course, and we do not name clients or projects publicly without written permission. That is why our <a href=\"/case-studies\">case studies</a> and <a href=\"/credentials\">credentials</a> describe work without naming the parties.",
        "<strong>Cyber Essentials certified</strong>, whole organisation, and registered with the Information Commissioner's Office.",
        "Project data is held only for as long as the engagement and our record keeping obligations require, and is returned or destroyed on request. See our <a href=\"/privacy\">privacy policy</a>.",
        "Where a client requires data to remain on their own systems, we work inside their environment rather than taking copies.",
    ]) +
    sec("People", [
        "Work is carried out by the named individual set out in the proposal. We do not sell a senior consultant and deliver with a junior one.",
        "Where a sub-consultant is engaged, they are named to the client in advance, they work to our <a href=\"/human-rights\">human rights</a> and health and safety policies, and they must evidence their own arrangements and any site qualification the work requires before they are engaged.",
    ]) +
    sec("Invoicing", [], [
        "Fixed scope reviews are invoiced on delivery.",
        "Ongoing engagements are invoiced monthly in arrears.",
        "Payment terms are 30 days from invoice date.",
        "Expenses are invoiced at cost with receipts attached.",
    ]) +
    sec("Raising a concern", [
        "If something is wrong with the work or the conduct of it, tell us directly and it will be dealt with by the director. Anyone affected by our work can raise a concern through the channel published in our <a href=\"/human-rights\">human rights policy</a>, including anonymously.",
    ]),
    sidebar("Ready to talk?",
            "Tell us what you are dealing with. You will get an acknowledgement the same or next working day.",
            "Get in touch", "In short", [
                "8 hour day, no six minute billing",
                "Travel included within 30 miles of London",
                "PI insurance included in the fee",
                "Acknowledged in 1 working day",
                "Proposal in 2 working days",
                "No software commission, ever",
            ]),
    "Terms you can read before you call",
    "If anything here does not fit how you need to work, say so and we will tell you whether we can accommodate it.",
    "Get in touch",
    cta_text="Get in touch"
)

# ============================================================ academy
page(
    "academy.html",
    "Planned Academy | Primavera P6 and Project Controls Training | Planned Ltd",
    "Planned Academy delivers practitioner led training in Primavera P6, Oracle Primavera Cloud, NEC4 programme management, schedule quality and delay analysis. Onsite, live online and one to one.",
    "Primavera P6 training, project controls training, NEC4 training, planning training UK, P6 course",
    "academy", 0,
    [("Home", "/"), ("Planned Academy", "")],
    "Planned Academy",
    "Practitioner led training in planning, scheduling and project controls",
    intro([
        "Planned Academy is the training arm of Planned Limited. Every course is written and delivered by a practising planner who does the work on live infrastructure programmes, not by a trainer who last used the software in a classroom.",
        "Courses are modular. Take one, or work through several. Each is available onsite, live online, or one to one.",
    ]) +
    sec("Courses", [
        "<strong>Primavera P6 Foundation.</strong> Building a schedule that works: structures, calendars, activity types, logic, and the settings that quietly determine whether a schedule behaves. For new users and for experienced users who inherited their habits from someone else.",
        "<strong>Primavera P6 Advanced Scheduling.</strong> Resource and cost loading, baselines, progress and update discipline, multi project working, layouts, filters and reporting that people actually read.",
        "<strong>Schedule Quality and the DCMA 14 Point Assessment.</strong> What each of the fourteen checks is testing, why it matters, how to fix a failing schedule, and how to tell a cosmetic finding from one that moves the completion date.",
        "<strong>NEC4 Programme Management.</strong> Clause 31 and 32 in practice: what a programme must contain, the four grounds for non acceptance, the reply period, and how the Accepted Programme drives every later compensation event assessment.",
        "<strong>Delay Analysis Fundamentals.</strong> The recognised methods, which records each one needs, how concurrency works, and why most extension of time cases are decided on records rather than on merit.",
        "<strong>Oracle Primavera Cloud Transition.</strong> For teams moving from P6: what is different, what breaks, and how to work in the new model rather than fighting it.",
    ]) +
    sec("How it is delivered", [], [
        "<strong>Onsite</strong> at your offices or on site, for a whole team",
        "<strong>Live online</strong>, delivered in sessions rather than as a recorded course, so questions get answered",
        "<strong>One to one</strong>, for a single planner who needs to get to a standard quickly",
        "Course material is built around your own programmes where you want it to be, so what people learn on Tuesday is usable on Wednesday",
        "Every course issues a certificate of completion recording the CPD hours",
    ]) +
    sec("Who it is for", [
        "<strong>Planners and schedulers</strong> who want to close a specific gap rather than sit through a general course.",
        "<strong>Project managers, commercial managers and engineers</strong> who have to read, challenge or accept a programme without being planners themselves. This is the largest untrained group in the industry and the one where training pays back fastest.",
        "<strong>Career changers and new entrants</strong> moving into planning from engineering, construction management or commercial roles.",
        "<strong>Service leavers.</strong> Planned Limited is a signatory to the Armed Forces Covenant, and project controls is one of the closest civilian equivalents to military planning. If you are leaving the forces and considering this route, get in touch.",
    ]) +
    sec("Next cohort", [
        "Public course dates are released to the waiting list first. Tell us which course and which format suits you and we will let you know when the next cohort opens, or arrange a dedicated session for your team.",
        "Planned Limited is an <a href=\"/credentials\">APM Corporate Affiliate</a> and a Disability Confident Committed employer. If you need any adjustment to take part in a course, tell us and we will make it.",
    ]),
    sidebar("Join the waiting list",
            "Tell us the course and format you want and we will contact you when the next cohort opens.",
            "Register your interest", "Formats", [
                "Onsite, whole team",
                "Live online",
                "One to one",
                "Built around your own programmes",
                "Certificate with CPD hours",
                "Adjustments made on request",
            ]),
    "Train the people who have to read the programme, not just the ones who build it",
    "Tell us the course and the format and we will come back with dates and a price.",
    "Register your interest",
    cta_text="Register your interest"
)

print("reviews index, how-we-work and academy built")
