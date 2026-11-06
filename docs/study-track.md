# Study track

## Before testing

Write an authorization record with asset ownership, exact target inventory, allowed techniques, start/end time, data handling and a contact who can stop the work. The fixture in this repository is a fictional exercise, not permission to test a real system.

## Exercise 1: Query boundaries

Run Query Boundary Lab. Predict whether a valid account, wrong password, apostrophe and injected predicate will pass each implementation. Compare predictions with the eight tests. Write the root cause in your own words. Explain why a passing SQL test alone does not establish secure authentication.

## Exercise 2: Detection quality

Run Auth Signal Watch. Change the time window and threshold. Construct a benign failure sequence and a failure burst followed by success. Record which rule fires. Discuss shared IPs, missing logs, time skew and distributed attempts.

## Exercise 3: Evidence handling

Run Baseline Harbor. Save the first manifest outside the target folder. Change, remove and add one file. Explain why changes need review and how an attacker could tamper with an unprotected baseline.

## Exercise 4: Network evidence

Parse the synthetic Nmap XML in Pentest Tool Atlas. Distinguish an open port from a vulnerable service. Explain what packet capture would add and why a service name in an export is not independent verification.

## Final deliverable

Copy fixtures/report.json, replace fictional details with your authorized lab details, and run the report checker. Include commands, observed output, root cause, impact, remediation and retest. Have a human verify authorization, evidence accuracy and disclosure scope. The checker verifies documentation completeness only.

## Review prompts

1. Why is a target list insufficient without permission and stop conditions?
2. What false positives arise from a shared source IP?
3. What does SHA-256 detect, and what does it fail to authenticate?
4. Why is a closed port not proof that a host is secure?
5. How can you preserve useful evidence without retaining credentials?
