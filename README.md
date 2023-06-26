Fun with Selenium

This is the implementation of task suggested to AQA candidates as the pre-screening challenge, in my recent company.
Later, candidate code was used in technical interview to discuss involved tools and approaches.


The goal of the task was to chose arbitrary web service (default is https://www.latlong.net/), and provide pack of UI test cases with python, pytest, Selenium and POM approach.


Criteria for evaluation are:
- PEP8, style and naming consistency
- Usage of advanced pytest features (fixtures, parametrization, marks, plugins for reporting /parallelize / multiple-checks / whatever)
- Care of final results deliverability and re-usability (pinning of the dependencies, packaging, thoughtful fixtures design etc)
- All kind of documentations (README, docstrings, comments, meaningful naming)
- Output clarity (log and error messages, logging approach - in-only, out-only, in-out-both, etc)
- Testcases design (atomic, multi-check, positive/negative, splitting testing area to sub-domains, cases classification, coverage nuances like prioritization and understanding what was intentially skipped due limited task scope, etc)
- Configurability (hardcoded values, separating of code and configs)
- Any optimization attempts would be plus

