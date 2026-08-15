from _helpers import page, sec, intro, sidebar

CB = [("Home", "/"), ("Reviews", "/reviews/"), (None, None)]


def crumb(label):
    return [("Home", "/"), ("Reviews", "/reviews/"), (label, "")]


# ---------------------------------------------------------------- 1
page(
    "reviews/nec4-programme-acceptance-review.html",
    "NEC4 Programme Acceptance Review | Clause 31 | Planned Ltd",
    "Independent review of a contractor programme against NEC4 clause 31.2, before it is submitted or before you accept it. Fixed scope, written reasons.",
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
    "Request a programme review",
    extra_ld='    <script type="application/ld+json">\n    {\n      "@context": "https://schema.org",\n      "@type": "Service",\n      "name": "NEC4 Programme Acceptance Review",\n      "serviceType": "NEC4 programme review and acceptance support",\n      "description": "Independent review of a contractor programme against NEC4 clause 31.2 and the grounds in clause 31.3, before submission or before acceptance, delivered inside the reply period with a written recommendation and reasons.",\n      "provider": {\n        "@type": "Organization",\n        "name": "Planned Limited",\n        "url": "https://plannedltd.co.uk"\n      },\n      "areaServed": [\n        "GB",\n        "EMEA"\n      ],\n      "availableLanguage": "en",\n      "url": "https://plannedltd.co.uk/reviews/nec4-programme-acceptance-review"\n    }\n    </script>\n    <script type="application/ld+json">\n    {\n      "@context": "https://schema.org",\n      "@type": "BreadcrumbList",\n      "itemListElement": [\n        {\n          "@type": "ListItem",\n          "position": 1,\n          "name": "Home",\n          "item": "https://plannedltd.co.uk/"\n        },\n        {\n          "@type": "ListItem",\n          "position": 2,\n          "name": "Reviews",\n          "item": "https://plannedltd.co.uk/reviews/"\n        },\n        {\n          "@type": "ListItem",\n          "position": 3,\n          "name": "NEC4 Programme Acceptance Review",\n          "item": "https://plannedltd.co.uk/reviews/nec4-programme-acceptance-review"\n        }\n      ]\n    }\n    </script>\n'
)

# ---------------------------------------------------------------- 2
page(
    "reviews/independent-schedule-assurance-review.html",
    "Independent Schedule Assurance Review | DCMA 14 Point",
    "Independent, evidence based assessment of whether a schedule can be relied on: DCMA 14 point checks, logic and critical path integrity, what to fix first.",
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
    "Request a schedule review",
    extra_ld='    <script type="application/ld+json">\n    {\n      "@context": "https://schema.org",\n      "@type": "Service",\n      "name": "Independent Schedule Assurance Review",\n      "serviceType": "Schedule assurance and DCMA 14 point assessment",\n      "description": "Independent, evidence based assessment of whether a project schedule can be relied on to manage a project, forecast completion and support a claim: DCMA 14 point checks, logic and critical path integrity, and a ranked list of what to fix.",\n      "provider": {\n        "@type": "Organization",\n        "name": "Planned Limited",\n        "url": "https://plannedltd.co.uk"\n      },\n      "areaServed": [\n        "GB",\n        "EMEA"\n      ],\n      "availableLanguage": "en",\n      "url": "https://plannedltd.co.uk/reviews/independent-schedule-assurance-review"\n    }\n    </script>\n    <script type="application/ld+json">\n    {\n      "@context": "https://schema.org",\n      "@type": "BreadcrumbList",\n      "itemListElement": [\n        {\n          "@type": "ListItem",\n          "position": 1,\n          "name": "Home",\n          "item": "https://plannedltd.co.uk/"\n        },\n        {\n          "@type": "ListItem",\n          "position": 2,\n          "name": "Reviews",\n          "item": "https://plannedltd.co.uk/reviews/"\n        },\n        {\n          "@type": "ListItem",\n          "position": 3,\n          "name": "Independent Schedule Assurance Review",\n          "item": "https://plannedltd.co.uk/reviews/independent-schedule-assurance-review"\n        }\n      ]\n    }\n    </script>\n'
)

# ---------------------------------------------------------------- 3
page(
    "reviews/delay-and-eot-position-review.html",
    "Delay and Extension of Time Position Review | Planned Ltd",
    "Independent assessment of your delay position before you spend on a claim or a defence: what the records support, which method fits, whether it is worth it.",
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
    "Request a position review",
    extra_ld='    <script type="application/ld+json">\n    {\n      "@context": "https://schema.org",\n      "@type": "Service",\n      "name": "Delay and Extension of Time Position Review",\n      "serviceType": "Delay analysis and extension of time position review",\n      "description": "Independent assessment of a delay and extension of time position before money is spent on a claim or a defence: what the records support, which analysis method fits, and whether the case is worth running.",\n      "provider": {\n        "@type": "Organization",\n        "name": "Planned Limited",\n        "url": "https://plannedltd.co.uk"\n      },\n      "areaServed": [\n        "GB",\n        "EMEA"\n      ],\n      "availableLanguage": "en",\n      "url": "https://plannedltd.co.uk/reviews/delay-and-eot-position-review"\n    }\n    </script>\n    <script type="application/ld+json">\n    {\n      "@context": "https://schema.org",\n      "@type": "BreadcrumbList",\n      "itemListElement": [\n        {\n          "@type": "ListItem",\n          "position": 1,\n          "name": "Home",\n          "item": "https://plannedltd.co.uk/"\n        },\n        {\n          "@type": "ListItem",\n          "position": 2,\n          "name": "Reviews",\n          "item": "https://plannedltd.co.uk/reviews/"\n        },\n        {\n          "@type": "ListItem",\n          "position": 3,\n          "name": "Delay and Extension of Time Position Review",\n          "item": "https://plannedltd.co.uk/reviews/delay-and-eot-position-review"\n        }\n      ]\n    }\n    </script>\n'
)

# ---------------------------------------------------------------- 4
FAQ_LD = """    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "Service",
      "name": "Primavera Migration Readiness Assessment",
      "serviceType": "Planning software migration assessment: Microsoft Project, Excel or other planning tools to Primavera P6 or Oracle Primavera Cloud",
      "description": "An independent, fixed scope assessment for organisations moving from Microsoft Project, Excel or another planning tool to Primavera P6 or Oracle Primavera Cloud: which platform fits, what converts, what should be rebuilt, the standards to set before day one, and the training the team will need.",
      "provider": {"@type": "Organization", "name": "Planned Limited", "url": "https://plannedltd.co.uk"},
      "areaServed": ["GB", "EMEA"],
      "availableLanguage": "en",
      "url": "https://plannedltd.co.uk/reviews/primavera-cloud-migration-readiness-assessment"
    }
    </script>
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "BreadcrumbList",
      "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://plannedltd.co.uk/"},
        {"@type": "ListItem", "position": 2, "name": "Reviews", "item": "https://plannedltd.co.uk/reviews/"},
        {"@type": "ListItem", "position": 3, "name": "Primavera Migration Readiness Assessment", "item": "https://plannedltd.co.uk/reviews/primavera-cloud-migration-readiness-assessment"}
      ]
    }
    </script>
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Can you convert a Microsoft Project schedule to Primavera P6?",
          "acceptedAnswer": {"@type": "Answer", "text": "Yes. Primavera P6 imports Microsoft Project files through the MSP XML format, and Oracle Primavera Cloud can import from P6 or from XML. What survives the import is the question. Task names, durations, links and dates usually carry across; task types, constraints, calendars, resource units, custom fields, baselines and summary structure often behave differently after import and need to be checked and reworked. In many cases it is faster and cleaner to rebuild the schedule in P6 against a set of standards than to convert it and repair it, and the assessment tells you which applies to yours."}
        },
        {
          "@type": "Question",
          "name": "Can an Excel schedule be moved into Primavera P6 or Primavera Cloud?",
          "acceptedAnswer": {"@type": "Answer", "text": "Activity lists, dates and durations can be imported from a spreadsheet, but an Excel schedule has no logic network, so there is nothing for the software to calculate a critical path from. Moving from Excel is a rebuild rather than a conversion: the activities come across, and the relationships, calendars, resources and coding are built in the new tool. The assessment establishes what the spreadsheets actually contain, how much of it is worth carrying, and what the rebuilt programme has to show."}
        },
        {
          "@type": "Question",
          "name": "Should we move to Primavera P6 or to Oracle Primavera Cloud?",
          "acceptedAnswer": {"@type": "Answer", "text": "It depends on who has to open the file, how many projects and users you have, and how you report. Many clients and contracts still require XER files, which points to P6. Organisations that want portfolio and resource views, browser access and no on premise administration lean towards Oracle Primavera Cloud. The two are different products with different data models, and the choice should be made on your projects and your contracts rather than on the newer name. The assessment gives a written recommendation and the reasons for it, and we take no commission on either."}
        },
        {
          "@type": "Question",
          "name": "How long does a move from Microsoft Project or Excel to Primavera take?",
          "acceptedAnswer": {"@type": "Answer", "text": "It depends on how many live schedules there are, whether they convert or need rebuilding, how much standard setup (enterprise structure, calendars, codes, layouts) has to be created, and how quickly the team can be trained. The assessment breaks the work down so that a duration and a cost can be built from it rather than guessed at."}
        },
        {
          "@type": "Question",
          "name": "Do we need Primavera P6 training as part of a migration?",
          "acceptedAnswer": {"@type": "Answer", "text": "Almost always. Planners who are fluent in Microsoft Project or spreadsheets can build schedules in P6 quickly, but they need to learn how P6 handles calendars, constraints, relationships, resources, baselines and enterprise data, because habits carried over from the previous tool are the most common cause of poor P6 schedules. The assessment states who needs training, on what, and when in the sequence, and Planned delivers that training if you want it delivered."}
        }
      ]
    }
    </script>
"""

page(
    "reviews/primavera-cloud-migration-readiness-assessment.html",
    "MS Project or Excel to Primavera P6 or Cloud | Planned Ltd",
    "Moving from Microsoft Project, Excel or another planning tool to Primavera P6 or Oracle Primavera Cloud? Independent assessment: which platform, what converts.",
    "Microsoft Project to Primavera P6, MS Project to P6 migration, Excel to Primavera P6, move to Oracle Primavera Cloud, Asta Powerproject to P6, Primavera migration assessment, P6 implementation UK",
    "reviews/primavera-cloud-migration-readiness-assessment", 1,
    crumb("Primavera Migration Readiness Assessment"),
    "Moving from Microsoft Project or Excel to Primavera P6 or Oracle Primavera Cloud",
    "An independent readiness assessment before you commit: which platform, what converts, what to rebuild, and how to set the team up so the new tool is used properly from day one",
    intro([
        "Most organisations do not arrive at Primavera by choice. A client asks for an XER file, a framework requires an integrated programme, a project outgrows what Microsoft Project or a spreadsheet can hold, or a parent company standardises. The decision to move is usually made quickly, and the mistakes are made in the first month: schedules converted rather than rebuilt, no enterprise structure or coding agreed before people start, and planners applying Microsoft Project habits inside a tool that does not work the same way.",
        "The Primavera Migration Readiness Assessment is a fixed scope, independent review for organisations moving from Microsoft Project, Excel, Asta Powerproject or another planning tool to Primavera P6 or Oracle Primavera Cloud. It tells you which platform fits your projects and contracts, what will carry across and what will not, what should be built fresh, and what the team needs before the first live programme goes into the new system.",
    ]) +
    sec("Who it is for", [
        "<strong>Contractors and consultancies</strong> whose clients now require Primavera P6 files, or an integrated programme that a spreadsheet cannot produce, and who need to be running the tool credibly by a contract start date.",
        "<strong>Owners, developers and asset operators</strong> running a growing portfolio in Microsoft Project or Excel who need multi project reporting, a shared resource pool and a defensible baseline, and are weighing Primavera P6 against Oracle Primavera Cloud.",
        "<strong>Planning teams</strong> who have been told to move and asked to price and plan the migration, and have no basis for the number or the sequence.",
        "<strong>Organisations already part way through</strong> a move that has stalled, where the schedules imported but nobody trusts what came out.",
    ]) +
    sec("Primavera P6 or Oracle Primavera Cloud: which one?", [
        "The two are different products, not old and new versions of the same thing. Primavera P6 remains the file format most clients and contracts ask for, and XER exchange is often the deciding factor. Oracle Primavera Cloud offers portfolio, resource and risk views in a browser with no on premise administration, but its data model, coding, baselines and reporting behave differently, and it is not the right answer simply because it is newer.",
        "The assessment answers the question on your projects, your contracts and the people who have to open the files, and gives the recommendation in writing with the reasons. If you want the background first, our comparison of <a href=\"/blog/oracle-primavera-cloud-vs-p6\">Oracle Primavera Cloud and Primavera P6</a> and our guide to <a href=\"/blog/primavera-p6-vs-microsoft-project\">Primavera P6 against Microsoft Project</a> set out the differences.",
    ]) +
    sec("What the assessment covers", [], [
        "<strong>What you actually have.</strong> The live schedules, templates, spreadsheets and reporting packs, who builds them, how they are updated, and which of them matter. Estates always contain more than anyone expects and less of it than anyone expects is worth carrying.",
        "<strong>Convert or rebuild.</strong> For each live schedule, whether an import from Microsoft Project XML or a spreadsheet will produce something usable, or whether it is faster and safer to rebuild against standards. Excel schedules have no logic and are always a rebuild; Microsoft Project schedules convert, but task types, constraints, calendars, resource units, custom fields, baselines and summary structure rarely survive untouched.",
        "<strong>The standards to set before day one.</strong> Enterprise project structure, organisational breakdown, calendars, activity codes, WBS conventions, naming, layouts and filters, baseline rules and the update cycle. This is the work that is skipped in most migrations and regretted in every one of them.",
        "<strong>Contract and client requirements.</strong> What your contracts require the programme to show, whether under NEC4, JCT or a bespoke form, which file formats clients demand, and how the new tool will meet them from the first submission.",
        "<strong>Reporting and integration.</strong> What currently feeds cost, progress and dashboard reporting from the schedule, what breaks when the source changes, and what replaces it.",
        "<strong>Administration and licensing.</strong> Who will own the environment, what governance is needed, and the hosting and licensing routes that suit your size, described plainly and without commission.",
        "<strong>The people, which is usually the real constraint.</strong> Who needs to be trained, on what, in which order, and what habits from the previous tool have to be unlearned. A planner fluent in Microsoft Project can produce a poor P6 schedule very quickly.",
    ]) +
    sec("What you receive", [
        "A written readiness assessment stating plainly whether you are ready, partly ready or not ready, and what would have to change, with a platform recommendation and the reasons for it.",
        "A migration scope with the work broken down by schedule and by task, so that a credible cost and duration can be built from it rather than guessed at.",
        "A convert, rebuild and retire list for the schedules and data you hold. The retire list is frequently the most valuable output: nobody should pay to migrate a spreadsheet that has not been opened since the project closed.",
        "A standards pack outline: the enterprise structure, calendars, codes, layouts and update rules the new environment should start with, ready to be built or handed to whoever builds it.",
        "A training and capability plan naming who needs what, and a risk list of the things that stall migrations part way through.",
    ]) +
    sec("How Microsoft Project and Excel schedules move to Primavera", [
        "Microsoft Project files go into Primavera P6 through the MSP XML format, and into Oracle Primavera Cloud from P6 or from XML. Names, durations, links and dates usually arrive intact. Fixed duration and fixed unit task types, deadline and constraint types, calendar exceptions, per cent complete methods, resource units and rates, custom fields and baselines all have P6 equivalents that behave differently, and summary tasks become WBS nodes rather than activities. Every converted schedule needs its logic, calendars and constraints checked before it is trusted, and many are cleaner rebuilt.",
        "Spreadsheets hold activity lists and dates but no relationships, so there is no network to calculate from. Moving from Excel is a rebuild: the activities can be imported, and the logic, calendars, resources and coding are built in the new tool against the standards agreed first. That is not a disadvantage. It is the point at which the schedule becomes something that can be relied on.",
        "Whichever tool you come from, the first live programme built in the new environment is the one that matters. We recommend it is built with support, checked against the contract's programme requirements, and used as the template for the rest.",
    ]) +
    sec("Common mistakes this assessment prevents", [], [
        "Importing everything, then discovering that half the schedules were dead and the live ones need rebuilding anyway",
        "Starting to build before the enterprise structure, calendars and codes exist, so every planner invents their own",
        "Choosing Oracle Primavera Cloud when clients require XER files, or choosing P6 when nobody will administer it",
        "Carrying Microsoft Project constraint and task type habits into P6, and producing schedules that fail the client's programme review",
        "Treating training as a day at the end rather than the thing that decides whether the migration works",
        "Pricing the migration before anyone has counted what is being migrated",
    ]) +
    sec("Questions we are asked", [
        "<strong>Can you convert a Microsoft Project schedule to Primavera P6?</strong> Yes. P6 imports Microsoft Project files through the MSP XML format, and Oracle Primavera Cloud can import from P6 or from XML. What survives is the question: names, durations, links and dates usually carry across; task types, constraints, calendars, resource units, custom fields, baselines and summary structure often behave differently and need to be checked and reworked. In many cases it is faster and cleaner to rebuild against standards than to convert and repair, and the assessment tells you which applies to yours.",
        "<strong>Can an Excel schedule be moved into Primavera P6 or Primavera Cloud?</strong> Activity lists, dates and durations can be imported, but a spreadsheet has no logic network, so there is nothing to calculate a critical path from. Moving from Excel is a rebuild rather than a conversion: the activities come across, and the relationships, calendars, resources and coding are built in the new tool.",
        "<strong>Should we move to Primavera P6 or to Oracle Primavera Cloud?</strong> It depends on who has to open the file, how many projects and users you have, and how you report. Many clients and contracts still require XER files, which points to P6. Organisations that want portfolio and resource views in a browser with no on premise administration lean towards Oracle Primavera Cloud. The choice should be made on your projects and contracts rather than on the newer name, and the assessment gives the recommendation in writing with reasons.",
        "<strong>How long does a move from Microsoft Project or Excel to Primavera take?</strong> It depends on how many live schedules there are, whether they convert or need rebuilding, how much standard setup has to be created, and how quickly the team can be trained. The assessment breaks the work down so that a duration and a cost can be built from it rather than guessed at.",
        "<strong>Do we need Primavera P6 training as part of a migration?</strong> Almost always. Planners fluent in Microsoft Project or spreadsheets build in P6 quickly, but habits carried over from the previous tool are the most common cause of poor P6 schedules. The assessment states who needs training, on what, and when in the sequence, and we deliver that training if you want it delivered.",
    ]) +
    sec("Independence", [
        "We do not resell Oracle licences and we take no commission on software, hosting or training products. If the assessment concludes that Microsoft Project still serves you and the pressure to move is not real, that is what it will say. If it concludes that you should move, we can build the environment, rebuild the schedules and train the team, through our <a href=\"/services/primavera-p6-consultant\">Primavera P6 consultancy</a>, <a href=\"/services/oracle-primavera-cloud-consultant\">Oracle Primavera Cloud consultancy</a> and <a href=\"/services/training\">training</a>, or hand the scope to whoever you choose.",
    ]),
    sidebar("Been told to move to Primavera?",
            "Tell us what you run today, roughly how many live schedules you have and what your clients are asking for, and we will confirm what the assessment would cover.",
            "Request this assessment", "At a glance", [
                "From Microsoft Project, Excel, Asta Powerproject or another planning tool",
                "To Primavera P6 or Oracle Primavera Cloud",
                "Independent, no software commission",
                "Convert, rebuild and retire list",
                "Standards pack and training plan",
                "Costable migration scope",
                "Remote UK wide",
            ]),
    "Set the new tool up properly, or inherit someone else's shortcuts",
    "A short assessment before you start is cheaper than a stalled migration and a set of schedules nobody trusts.",
    "Request the assessment",
    cta_text="Request this assessment",
    extra_ld=FAQ_LD
)

print("4 review pages built")
