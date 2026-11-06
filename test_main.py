import copy
import json
from pathlib import Path
import unittest
from main import assess

class AssessmentTests(unittest.TestCase):
    def setUp(self):
        self.report=json.loads(Path('fixtures/report.json').read_text())
    def test_complete_report(self):
        self.assertTrue(assess(self.report)['passed'])
    def test_missing_evidence(self):
        del self.report['finding']['evidence']
        self.assertIn('finding.evidence: nonempty text required',assess(self.report)['issues'])
    def test_whitespace(self):
        self.report['scope']['authorization']='  '
        self.assertFalse(assess(self.report)['passed'])
    def test_wrong_section(self):
        self.report['scope']=[]
        self.assertFalse(assess(self.report)['passed'])
    def test_nonobject(self):
        self.assertFalse(assess([])['passed'])
    def test_does_not_mutate(self):
        original=copy.deepcopy(self.report)
        assess(self.report)
        self.assertEqual(original,self.report)
    def test_multiple_issues(self):
        self.assertEqual(len(assess({'scope':{},'finding':{}})['issues']),9)
