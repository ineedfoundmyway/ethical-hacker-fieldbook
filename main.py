import argparse
import json
from pathlib import Path

REQUIREMENTS = {'scope': ['authorization', 'targets', 'window', 'stop_conditions'], 'finding': ['title', 'evidence', 'impact', 'remediation', 'retest']}

def assess(report):
    problems = []
    if not isinstance(report, dict):
        return {'passed': False, 'issues': ['report must be an object']}
    for section, fields in REQUIREMENTS.items():
        value = report.get(section)
        if not isinstance(value, dict):
            problems.append(f'{section}: object required')
            continue
        for field in fields:
            if not isinstance(value.get(field), str) or not value[field].strip():
                problems.append(f'{section}.{field}: nonempty text required')
    return {'passed': not problems, 'issues': problems, 'meaning': 'Documentation completeness only; authorization and technical truth require human verification'}

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('report', type=Path)
    args = parser.parse_args()
    try:
        result = assess(json.loads(args.report.read_text()))
        print(json.dumps(result, indent=2))
        raise SystemExit(0 if result['passed'] else 1)
    except (OSError, ValueError) as error:
        parser.exit(2, f'Invalid input: {error}\n')
