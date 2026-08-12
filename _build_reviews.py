from _helpers import page, sec, intro, sidebar

CB = [("Home", "/"), ("Reviews", "/reviews/"), (None, None)]


def crumb(label):
    return [("Home", "/"), ("Reviews", "/reviews/"), (label, "")]


# ---------------------------------------------------------------- 1
page(
    "reviews/nec4-programme-acceptance-review.html",
    "NEC4 Programme Acceptance Review | Clause 31 Support | Planned Ltd",
    "Independent review of a contractor programme against NEC4 clause 31.2, tested before it is submitted or before you accept it. Fixed scope, written recommendation with reasons.",
    "NEC4 clause 31, programme acceptance, accepted programme, NEC4 programme review, clause 31.3 reasons",
    "reviews/nec4-programme-acceptance-review", 1,
    crumb("NEC4 Programme Acceptance Review"),
    "NEC4 Programme Acceptance Review",
    "Test a programme against clause 31.2 before it is submitted, or before you accept it",
    intro([
        "Under NEC4 clause 31.3 the Project Manager has two weeks to accept a programme or state reasons for not accepting it. Miss that window and the programme is treated as accepted. State a reason that does not sit within clause 31.3 and the rejection is exposed.",
        "The NEC4 Programme Acceptance Review is a fixed scope, independent assessment of a programme against the four grounds in clause 31.3 and the content requirements of clause 31.2, delivered inside the reply period with a written recommendation and the reasons that support it.",
    ]) +
    sec("Who it is for", [
        "<strong>Clients, project managers and their advisers</strong> who receive contractor programmes and have to accept or reject them on a defensible basis, inside a two week reply period, often without an in-house planner.",
        "<strong>Contractors and subcontractors</strong> who want a programme tested before submission, so that it is accepted first time rather than rejected and resubmitted, and so that the Accepted Programme they will later assess compensation events against is one they can actually rely on.",
    ]) +
    sec("What the review covers", [
        "Every element the contract requires, checked against clause 31.2 rather than against general good practice:"
    ], [
        "The starting date, access dates, Key Dates, Sectional Completion dates and Completion Date, and whether the programme is consistent with them",
        "Planned Completion, and the float shown between planned Completion and the Completion Date",
        "Total float, terminal float and time risk allowance, shown separately as the contract requires rather than hidden inside durations",
        "The order and timing of the operations the Contractor plans to do, and of the work of the Client and Others",
        "Provisions for float, time risk allowance, health and safety requirements and the procedures set out in the contract",
        "Statements of how the Contractor plans to do the work, and the resources assumed",
        "Logic, critical path and sequencing, including open ends, negative lag, constraints and out of sequence progress",
        "Consistency between the narrative, the programme and the contract documents",
    ]) +
    sec("What you receive", [
        "A written report stating, for each ground in clause 31.3, whether the programme complies and why. Where it does not, the report states the reason in language that can be used directly in a notice of non acceptance.",
        "Where the recommendation is acceptance, the report records the basis of that recommendation, which matters later when the Accepted Programme becomes the baseline against which every compensation event is assessed.",
        "A marked up schedule of findings ranked by significance, so that the issues that would change the outcome are separated from the ones that are merely untidy.",
    ]) +
    sec("How we work", [
        "Desktop review of the programme file, the narrative and the relevant contract documents. Where progress is claimed and the engagement allows for it, we verify progress on site rather than accepting the update, because a programme reporting progress that has not happened understates delay and corrupts every later assessment against the Accepted Programme.",
        "Delivery is inside the reply period. Our standard turnaround and the terms that sit behind it are published at <a href=\"/how-we-work\">How We Work</a>.",
    ]),
    sidebar("Programme due for reply?",
            "Send us the file and the contract particulars and we will tell you whether the review fits inside your reply period.",
            "Request this review", "At a glance", [
                "Fixed scope, fixed fee",
                "Delivered inside the clause 31.3 reply period",
                "Written reasons, notice ready",
                "Optional site verification",
                "Independent of both parties",
                "Remote UK wide",
            ]),
    "Programme sitting on your desk with the clock running?",
    "Send us the file and the contract particulars. We will confirm scope and turnaround before you commit to anything.",
    "Request a programme review"
)

# ---------------------------------------------------------------- 2
page(
    "reviews/independent-schedule-assurance-review.html",
    "Independent Schedule Assurance Review | DCMA 14 Point | Planned Ltd",
    "An independent, evidence based assessment of whether a schedule can be relied on to manage a project. DCMA 14 point checks, logic and critical path integrity, and a ranked list of what to fix.",
    "schedule assurance, DCMA 14 point assessment, schedule health check, independent schedule review, schedule quality",
    "reviews/independent-schedule-assurance-review", 1,
    crumb("Independent Schedule Assurance Review"),
    "Independent Schedule Assurance Review",
    "Find out whether the schedule you are reporting against can actually be relied on",
    intro([
        "Most schedules pass visual inspection and fail structural inspection. Dangling activities, constraints doing the work that logic should be doing, and float that is an artefact of the network rather than a property of the project are common, and none of them are visible in a printed bar chart.",
        "The Independent Schedule Assurance Review is a fixed scope assessment of whether a schedule is structurally sound enough to manage a project, forecast a completion date and support a claim if one becomes necessary.",
    ]) +
    sec("Who it is for", [
        "<strong>Boards, sponsors and funders</strong> who are being told a date and want to know how much confidence to place in it.",
        "<strong>Project managers</strong> who inherited a schedule and need to know what they have before they start reporting against it.",
        "<strong>Contractors</strong> preparing a baseline for submission, who would rather find the problems themselves than have them found by the other side.",
    ]) +
    sec("What the review covers", [
        "The DCMA 14 point assessment in full, plus the checks that matter beyond it:"
    ], [
        "Logic: missing predecessors and successors, dangling activities, and whether the network actually drives",
        "Leads and lags, and negative lag used to force a date",
        "Relationship types, and over reliance on start to start and finish to finish",
        "Hard constraints and whether the critical path is real or manufactured",
        "High float, negative float and long duration activities",
        "Invalid dates, resource assignment, missed tasks and the critical path test",
        "Critical path integrity and float erosion between updates",
        "Baseline execution index and whether progress is being reported honestly",
        "Calendar setup, exclusions and whether the working pattern reflects reality",
        "Whether the schedule supports the contract it sits under",
    ]) +
    sec("What you receive", [
        "A written report giving a pass or fail against each check, with the specific activities at fault named, so the findings can be acted on rather than merely noted.",
        "A ranked list of remedial actions separating what would change the forecast completion date from what is cosmetic. Most schedule review reports fail here, and hand over two hundred findings of equal weight.",
        "A plain English statement of how much confidence the schedule currently supports, written for a reader who is not a planner.",
    ]) +
    sec("Start with the free check", [
        "If you want an indication before commissioning anything, our <a href=\"/tools/schedule-health-check\">free schedule health check</a> runs a subset of these tests in your browser. No file leaves your machine and there is nothing to install.",
    ]),
    sidebar("Not sure what you have?",
            "Run the free check first. If it flags something, we will tell you whether a full review is worth the money.",
            "Try the free check", "At a glance", [
                "Full DCMA 14 point assessment",
                "Named activities, not generic findings",
                "Findings ranked by impact on the date",
                "Written for non planners",
                "Primavera P6, Oracle Primavera Cloud, MS Project",
                "Remote UK wide",
            ], cta_href="/tools/schedule-health-check"),
    "Find out what your schedule is actually telling you",
    "Start with the free browser based check, or send us the file for the full review.",
    "Request a schedule review"
)

# ---------------------------------------------------------------- 3
page(
    "reviews/delay-and-eot-position-review.html",
    "Delay and Extension of Time Position Review | Planned Ltd",
    "An independent assessment of your delay position before you spend money on a claim or a defence. What the records support, which method fits, and whether the case is worth running.",
    "extension of time, delay analysis, EOT claim, time impact analysis, delay position review, compensation event",
    "reviews/delay-and-eot-position-review", 1,
    crumb("Delay and Extension of Time Position Review"),
    "Delay and Extension of Time Position Review",
    "Know what your delay position is worth before you spend money proving it",
    intro([
        "Extension of time disputes are usually lost on records rather than on merit. A party with a good entitlement and poor contemporaneous evidence will lose to a party with a weaker entitlement and better evidence, and most organisations do not find that out until they have already committed to a claim or a defence.",
        "The Delay and Extension of Time Position Review is a fixed scope, independent assessment of where you actually stand, delivered before you commit to a course of action.",
    ]) +
    sec("Who it is for", [
        "<strong>Contractors and subcontractors</strong> considering whether to pursue an extension of time, and needing to know whether the records will carry it.",
        "<strong>Clients and project managers</strong> facing a claim, who need an independent view of it before responding.",
        "<strong>Anyone in a compensation event assessment</strong> where the parties disagree on the programme impact and both are asserting rather than demonstrating.",
    ]) +
    sec("What the review covers", [
        "The review answers four questions and stops there. It is deliberately not a full forensic report:"
    ], [
        "What do the contemporaneous records actually support, as distinct from what is being asserted",
        "Which delay analysis method fits the available records, the contract and the stage the project is at, and which methods are not available to you",
        "Whether the events being relied on are on the critical path, and whether concurrency is present",
        "Whether the notices required by the contract were given, when, and what the consequences of any failure are",
    ]) +
    sec("What you receive", [
        "A written opinion on the strength of the position, stated plainly, including where it is weak. A review that tells you what you want to hear is worth nothing.",
        "A recommended method, with the reason it fits and the reasons the alternatives do not.",
        "A record gap list, identifying what is missing and what could still be gathered while it is gatherable, which is often the single most valuable output when a project is still running.",
        "A view on whether a full forensic analysis is justified by the sums at stake.",
    ]) +
    sec("Why this comes first", [
        "A full forensic delay analysis is an expensive document. Commissioning one before knowing whether the records support it is the most common way organisations spend money on a case they were never going to win. This review is designed to be the cheap step that decides whether the expensive step is worth taking.",
    ]),
    sidebar("Before you commit to a claim",
            "Send us the contract particulars and a description of the events. We will tell you what the review would cover and what it would cost.",
            "Request this review", "At a glance", [
                "Fixed scope, fixed fee",
                "Independent and candid",
                "Method selection with reasons",
                "Record gap list while records are still gatherable",
                "NEC and JCT",
                "Remote UK wide",
            ]),
    "Find out where you stand before you spend money proving it",
    "A short, candid assessment of your delay position, including where it is weak.",
    "Request a position review"
)

# ---------------------------------------------------------------- 4
page(
    "reviews/primavera-cloud-migration-readiness-assessment.html",
    "Oracle Primavera Cloud Migration Readiness Assessment | Planned Ltd",
    "An independent assessment of whether your P6 estate, data and processes are ready to move to Oracle Primavera Cloud, what will not carry across, and what it will cost you to find out later.",
    "Oracle Primavera Cloud migration, P6 to OPC, Primavera Cloud readiness, P6 migration assessment",
    "reviews/primavera-cloud-migration-readiness-assessment", 1,
    crumb("Primavera Cloud Migration Readiness Assessment"),
    "Primavera Cloud Migration Readiness Assessment",
    "Find out what will and will not survive the move from P6 before you commit to it",
    intro([
        "Oracle Primavera Cloud is not Primavera P6 in a browser. The data model, the way codes and structures behave, the reporting approach and the administration model all differ, and organisations routinely discover this partway through a migration rather than before it.",
        "This assessment establishes what your current estate contains, what carries across cleanly, what has to be rebuilt, and what should be retired rather than migrated.",
    ]) +
    sec("Who it is for", [
        "Organisations running Primavera P6, whether EPPM or Professional, who are considering Oracle Primavera Cloud, have been told to move by a client or a parent company, or are being asked to price a migration and have no basis for the number.",
    ]) +
    sec("What the assessment covers", [], [
        "The current estate: projects, users, calendars, codes, layouts, resource structures and how much of it is actually in use",
        "Data quality, and what should be archived or retired rather than carried across",
        "Structural differences that will require rework, including code and structure behaviour, resource and role modelling, and baseline handling",
        "Reporting and integrations, and what breaks when the source system changes",
        "Administration and governance: who currently has rights, what they do with them, and what the equivalent looks like afterwards",
        "The people question, which is usually the real constraint: who needs to be retrained, on what, and when",
    ]) +
    sec("What you receive", [
        "A written readiness assessment stating plainly whether you are ready, partly ready or not ready, and what would have to change.",
        "A migration scope with the work broken down, so a credible cost and duration can be built from it rather than guessed at.",
        "A retire list, which is frequently the most valuable output. Most estates carry a substantial volume of data that nobody has opened in years and that nobody should pay to migrate.",
        "A risk list of the things that commonly surface halfway through and cause a migration to stall.",
    ]) +
    sec("Independence", [
        "We do not resell Oracle licences and we take no commission on software. If the assessment concludes that you should stay where you are for now, that is what it will say.",
    ]),
    sidebar("Considering the move?",
            "Tell us roughly what your estate looks like and we will confirm what the assessment would cover.",
            "Request this assessment", "At a glance", [
                "P6 EPPM and P6 Professional",
                "Independent, no software commission",
                "Costable migration scope",
                "Retire list as well as a migrate list",
                "Training and capability view",
                "Remote UK wide",
            ]),
    "Do not find out midway through",
    "A short assessment now is cheaper than a stalled migration later.",
    "Request the assessment"
)

print("4 review pages built")
