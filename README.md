# Ethical Hacker Fieldbook

A practical study track with a machine-checked assessment report, explicit engagement scope and reproducible exercises.

Python 3.11+ · Standard library only · MIT · Maintained by [ineedfoundmyway](https://github.com/ineedfoundmyway)

## Run the proof

```sh
python -m unittest -v
python main.py fixtures/report.json
python scripts/prove.py
```

The checked-in [execution evidence](proof/report.json), [test transcript](proof/tests.txt), and [source hashes](proof/sha256.json) record a real local execution. Run the same commands to verify the result independently. CI regenerates evidence as an artifact on every push. Local results are not a claim that GitHub Actions has run.

## What you learn

| Module | Exercise | Evidence to produce |
| --- | --- | --- |
| 1. Scope | Define a fictional local engagement | Target list, time window, stop conditions |
| 2. Protocols | Read TCP handshake and scan examples | Packet interpretation notes |
| 3. Web testing | Run Query Boundary Lab | Bypass and fix output |
| 4. Detection | Run Auth Signal Watch | Alert timeline and false-positive analysis |
| 5. Integrity | Run Baseline Harbor | Change report and triage decision |
| 6. Reporting | Complete the sample assessment | Evidence, impact, remediation and retest |

Start with [the study track](docs/study-track.md). Use only assets you own or have written permission to assess. The included authorization statement is fictional. Passing the checker means fields are complete; it does not grant authorization or verify findings.

## Design and limits

This is original educational code inspired by the reading below. Article text, screenshots and third-party tool code are not bundled. Examples use synthetic data and temporary directories. No Internet targets are contacted. Results describe the supplied fixtures and do not certify a production system.

## Reading

- https://www.hackingarticles.in/web-penetration-testing/
- https://www.hackingarticles.in/understanding-nmap-scan-wireshark/

## License

MIT. Third-party tools and articles retain their own licenses.
