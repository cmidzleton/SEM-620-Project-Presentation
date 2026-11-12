# Other cities on 311 misroutes ("bounces") and wasted referrals

Research for SEM 620 Team 2, Edmonton 311 final presentation. Compiled 2026-11-11.

## Bottom line

- **No city found has published a before-and-after result showing it cut misrouted or re-referred 311 tickets.** Plenty of audits name the problem, and several cities have built fixes, but none of the public documents found report a measured drop. Say this plainly in the deck. It supports the team's diagnosis that nobody publishes a routing measure, and it means Edmonton would be early, not late.
- **Amsterdam is the closest match to the Route Check design**, and it is in production. It runs an ML classifier (TF-IDF + logistic regression) on resident reports. Reports scoring under 40% confidence go to a human service desk, staff fix misroutes by hand, and those corrections retrain the model. Its published accuracy is macro F1 0.88. Several other Dutch municipalities reuse the same open-source system. It does **not** publish a misroute rate.
- **Measured bounce rates elsewhere:** Dallas about 5% of requests transferred (2026). San Antonio's reclassify/reassign queue held 9,512 requests in 10 months (2026). NYC agencies closed 0.8% as "Wrong Agency" (2018). Those are the benchmarks a deck can use.
- **The wasted field visit is large and documented:** in NYC in 2018, 24.8% of 311 complaints closed as "Did Not Observe" and 18.7% as "No Action Taken". San Diego auditors (2022) recommended a program that screens low-priority code complaints before an inspector goes out.

## City by city

Legend: **Verified** = the figure was read verbatim in the source. **Summary-only** = it came from the part of a long PDF our reader only summarised, so check the page before putting it on a slide. **Not read** = the source could not be fetched.

### 1. Amsterdam and other Dutch municipalities: ML classifier with a human fallback (deployed)
- What they did: "Signalen" (SIA) classifies free-text public-space reports into a category, which sets the receiving department. TF-IDF + logistic regression. Below 40% confidence the report goes to "overig" (other) and a human service desk categorises it. Misrouted reports are fixed by hand and the corrections feed regular retraining. Trained first on 300,000 past reports. Other methods tried (Word2Vec, CNN+LSTM, BERT) did worse, per the register (no figures given). In use since July 2022. Verified.
- Result: macro-weighted F1 of 0.88. Verified. **No misroute rate or before/after published.**
- Same system, same 40% rule, in use at Enschede (since 2023-12), Woensdrecht (2023-01), Leeuwarden (06-2023) and Aa en Hunze. None publishes figures. Verified.
- Sources: [Amsterdam register entry](https://algoritmes.overheid.nl/nl/algoritme/gm0363/21579514/meldingen-openbare-ruimte-signalen-sia) · [Enschede](https://algoritmes.overheid.nl/nl/algoritme/gm0153/27683734/meldingen-openbare-ruimte) · [Woensdrecht](https://algoritmes.overheid.nl/nl/algoritme/gm0873/91295620/meldingen-openbare-ruimte) · [Leeuwarden](https://algoritmes.overheid.nl/en/algoritme/75142979) · [Aa en Hunze](https://algoritmes.overheid.nl/nl/algoritme/gm1680/83454194/signalen) · [Code](https://github.com/Amsterdam/meldingen)
- Related: Amsterdam's AI Lab (Feb 2025) says 25-30% of reports need no further action and explored GPT-4o drafted replies for them. Research only, not deployed. [Source](https://openresearch.amsterdam/en/page/117892/ai-driven-support-for-citizens-making-a-signal-melding). A 2023 UvA thesis with the City tested text + photo + location classifiers. Research only; numbers in the PDF not read. [Source](https://openresearch.amsterdam/en/id/98630)
- Why it matters for Edmonton: it is public, working proof of the exact pattern the team proposes: suggest a code, send low-confidence cases to a person, learn from corrections. Note the difference: Amsterdam classifies resident free text; Edmonton agents pick the code and open data has no free text.

### 2. Dallas: audit measured transfers, no fix results yet (April 2026)
- Finding: "About five percent of the service requests submitted during the 18-month period under review were transferred." Each transfer closes the old request and opens a new one with a new SLA clock, and the resident gets two emails with no reason. 45% of transferred requests reviewed had no explanation in the file. One case had four transfers over 25 business days. Sanitation reported 5.3% of its 135,078 requests involved a transfer, and 95.6% of those came from eight request types. 67 of 162 request types are used less than daily. Verified.
- What they're doing: management agreed to all 6 recommendations: documented transfer process with a reason recorded for each, review of seldom-used request types, quarterly escalation review. Target dates 9/30/2026 to 6/30/2027. No results yet.
- Source: [Dallas City Auditor, 311 SLA audit](https://dallascityhall.com/departments/auditor/DCH%20Documents/Audit%20of%20Communications%20Customer%20Experience%20311%20Service%20Level%20Agreements.pdf)
- Why it matters: the closest public parallel to Edmonton's "Redirecting to Other Business Area" bounce. The finding that transfers cluster in a few types matches the team's per-code risk score.

### 3. San Antonio: reclassify/reassign queue (January 2026)
- Finding: requests "require reclassification or reassignment by 311 if they are assigned to the incorrect department or service type." 9,512 went to the reclass/reassign queue Oct 2024 to Jul 2025 (10 months). 149 (1.6%) were sitting closed but pending reassignment for 7 to 79 days. 6% of 208 request types had wrong SLAs in the CRM. Verified (p. 7-9).
- Response: weekly workload review and new SOPs. Action plan, no outcome results.
- Source: [San Antonio Office of the City Auditor, AU25-001](https://www.sa.gov/files/assets/main/v/1/oca/documents/audit-reports/au25-01.pdf)
- Unknown: total request volume to turn 9,512 into a rate was not extracted.

### 4. New York City: how complaints actually close (2018 data)
- Finding: NYC Council data team classified agency responses to 311 complaints in 2018: Did Not Observe 24.8%, Fixed 21.5%, No Action Taken 18.7%, Ambiguous 17.3%, Ongoing 6.2%, Duplicate 5.5%, Violation Issued 4.8%, Wrong Agency 0.8%. Verified. Page has no publication date.
- Source: [NYC Council, 311 agency analysis](https://council.nyc.gov/data/311-agency/)
- Why it matters: supports the widened "Referral Check" framing. Wrong-agency misroutes are small; field visits that find nothing are large.

### 5. Los Angeles: 40%+ of calls transferred (March 2021)
- Finding: 311 must "transfer over 40% of calls answered", while peers "only transfer between 5% and 20%". Over 70% of zoning, building code and permit calls are transferred. Verified. Note: these are call transfers, not misrouted tickets, so not directly comparable to Edmonton.
- Recommended: move frequently transferred request types to the departments, call protocols and training, and "AI-powered recommendations to select the right service request." No implementation results found.
- Source: [LA Controller, "The 411 on 311"](https://controller.lacity.gov/audits/311)

### 6. Toronto: intake redesign aimed at misrouting (planned, April 2026)
- Plan: "Simplifying the 311 Intake Experience" says the redesign "will reduce errors, misrouting, and rework for service areas." 600+ service request codes. Q1 2026 analysis of service data and error logs complete (no findings published). Intake simplification Q3 2026 to Q1 2027, starting with Urban Forestry and Transportation. Verified. **No baselines, targets or results.**
- Source: [City of Toronto report, April 30 2026](https://www.toronto.ca/legdocs/mmis/2026/ex/bgrd/backgroundfile-287175.pdf)
- A councillor's blog claims AI tools cut connection times from about three minutes to forty seconds. Unsourced; do not cite as a City metric. [Source](https://www.shelleycarroll.ca/post/making-311-work-better-for-residents)
- Why it matters: Canadian peer, same code-count problem (600+ vs Edmonton's 1,917 phone codes), working on it now. A good Q&A answer to "has anyone else done this?"

### 7. Chicago: duplicates and unexplained closures (Inspector General, ~Feb 2026)
- Finding: Salesforce auto-assigns by request type and is meant to merge duplicates, but "Salesforce frequently fails to couple duplicate complaints." Departments close duplicates without explanation, sometimes as "no cause". No counts published. Verified (p. 10, 17); some later pages summary-only.
- Response: the 311 agency (OEMC) agreed to create a "duplicate" outcome category. Depends on funding and vendor work.
- Source: [Chicago OIG, Audit of 311 Service Request Process](https://igchicago.org/wp-content/uploads/2026/02/OIG-Audit-of-311-Service-Request-Process.pdf)
- Why it matters: you cannot measure wasted referrals if closure codes don't distinguish "duplicate", "nothing found" and "fixed". Same data-construction point the team makes.

### 8. Denver: misrouting from missing information (audit Aug/Sep 2025)
- Finding (from the auditor's public statement): agents "are relying on some resources and tools that are inaccurate or inconsistent"; once transferred, 311 does not close the request or tell the resident the outcome; 311 has no authority over partner agencies. Denver 311 agreed with all five recommendations. Verified from the statement. Colorado Politics reports the audit found "some cases being misrouted to the wrong agency due to missing information" (no figures).
- Sources: [Auditor statement, reprinted by El Comercio de Colorado](https://elcomerciodecolorado.com/audit-finds-ongoing-issues-in-denver-311-operations/) · [Colorado Politics, Oct 2025](https://www.coloradopolitics.com/2025/10/06/denver-311-service-hours-reduced-sunny-chatbot-takes-on-more/) · [Audit landing page](https://www.denvergov.org/Government/Agencies-Departments-Offices/Agencies-Departments-Offices-Directory/Auditors-Office/Audit-Services/Audit-Reports/Denver-311-and-Select-Agency-Case-Management)
- **Not read:** the full audit PDF (site blocks automated retrieval). Any figures inside it are unknown.
- Why it matters: same authority vs accountability split as Edmonton (311 routes, departments are accountable).

### 9. San Diego: closures and screening code complaints before a visit (2022)
- Get It Done audit (Oct 2022): 19% of closures reviewed gave residents "inaccurate or misleading closure details". Requests referred outside the City are shown as "Closed". Management agreed to 5 of 6 recommendations. Verified. [Source](https://www.sandiego.gov/sites/default/files/23-004_get_it_done_application_and_service_requests_management.pdf)
- Code enforcement audit (June 2022): only 56-64% of cases got a first inspection on time. Auditors recommended re-starting a Voluntary Compliance Program to cut low-priority cases sent to inspectors; management agreed, target July 1 2023. Verified. Summary-only: 29% of eligible Priority 3 cases had no violation, and the audit quotes a Portland audit that "about one-third of complaints are determined to be without merit." [Source](https://www.sandiego.gov/sites/default/files/22-009_dsd_code_enforcement.pdf)
- Unknown: whether the program was launched and what it achieved.

### 10. Older Canadian and US audits (context only)
- **Winnipeg (Dec 2014):** 5,738 "flow-backs" (requests a department sent back to 311) Jan-Sep 2013, about 0.5%, called "reasonable"; flow-back trend analysis recommended and marked complete. Summary-only. [Source](https://legacy.winnipeg.ca/audit/pdfs/reports/2015/311ContactCentreFinalReport.pdf)
- **Ottawa (June 2018 follow-up):** 60% of sampled knowledge-base items were "inaccurate, not up to date or no longer needed". Verified. [Source](https://www.oagottawa.ca/media/2oahihh0/2018.pdf)
- **San Francisco (Aug 2018):** most app/web requests routed automatically; 1,852 request categories; audit sample found routing correct but closures inaccurate (summary-only). [Source](https://sfcontroller.org/sites/default/files/Documents/Auditing/SF311%20Performance%20Audit%20Report%20-%20Final.pdf)
- **Toronto (Oct 2011):** called for an SLA with divisions and faster updates to agent information. [Source](https://www.toronto.ca/legdocs/mmis/2011/au/bgrd/backgroundfile-42365.pdf)

## Vendor claims (do not cite as evidence)
- SeeClickFix (CivicPlus) AI category suggestion: suggests, does not assign. Claims it helps route "correctly the first time". No accuracy or results published. [Source](https://www.civicplus.help/seeclickfix/docs/ai-improved-category-search-and-photo-analysis)
- OpenGov blog: says requests get misrouted, with no figures or sources. [Source](https://opengov.com/resources/blog/311-request-management-system-costs/)
- Boston moved 311 to an AI-enabled platform (Creatio) in 2025; no routing or classification results reported. [GovTech, Nov 2025](https://www.govtech.com/artificial-intelligence/boston-311-services-shaped-by-adaptable-ai-powered-platform)

## Could not verify
- Calgary 311 Response Audit (June 2021): [link](https://pub-calgary.escribemeetings.com/filestream.ashx?DocumentId=169102) blocked from this environment. Worth a manual read: it is the nearest Canadian peer.
- Denver full audit PDF (see above).
- "Automatic Type Detection of 311 Service Requests Based on Customer Provided Descriptions" (Applied Artificial Intelligence, 2022): [link](https://www.tandfonline.com/doi/full/10.1080/08839514.2022.2073717) blocked. City, accuracy and whether it was deployed are unknown.
