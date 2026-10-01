import math
import sqlite3
import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
import run
lift=budget=reporting=run

class ExperimentTests(unittest.TestCase):
    def test_known_effect(self):
        result=lift.estimate(10000,600,10000,400,10000)
        self.assertAlmostEqual(result['absolute_lift'],.02)
        self.assertAlmostEqual(result['relative_lift'],.5)
        self.assertAlmostEqual(result['incremental_members'],200)
        self.assertAlmostEqual(result['incremental_cac_usd'],50)
        self.assertGreater(result['ci95_lower'],0)
        self.assertLess(result['p_value'],.001)

    def test_no_effect_and_unbounded_cost(self):
        result=lift.estimate(10000,400,10000,400,10000)
        self.assertEqual(result['p_value'],1)
        self.assertIsNone(result['incremental_cac_usd'])
        self.assertIsNone(result['icac_ci_upper_usd'])

    def test_negative_effect(self):
        result=lift.estimate(10000,300,10000,500,10000)
        self.assertLess(result['ci95_upper'],0)
        self.assertIsNone(result['incremental_cac_usd'])

    def test_sample_ratio_mismatch(self):
        self.assertLess(lift.estimate(15000,600,10000,400,10000)['srm_p_value'],.01)

    def test_invalid_counts(self):
        with self.assertRaises(ValueError):lift.estimate(0,0,10,1,100)
        with self.assertRaises(ValueError):lift.estimate(10,11,10,1,100)

if __name__=='__main__':unittest.main()
