#!/usr/bin/env python3
"""Tests for the snapshot pipeline. Run: python3 -m unittest scripts/test_snapshots.py"""
import gzip, json, pathlib, sys, tempfile, unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import fetch, metrics

POOLS = {"status": "success", "data": [{"project": "maple", "symbol": "USDC",
                                        "chain": "Ethereum", "tvlUsd": 1.0}] * 1000}
PROTOCOLS = [{"name": "x"}] * 1000

class CheckTest(unittest.TestCase):
    def test_accepts_real_shapes(self):
        fetch.check("pools", POOLS)
        fetch.check("protocols", PROTOCOLS)

    def test_rejects_error_status(self):
        with self.assertRaises(ValueError):
            fetch.check("pools", {"status": "error", "data": POOLS["data"]})

    def test_rejects_short_pull(self):
        with self.assertRaises(ValueError):
            fetch.check("protocols", PROTOCOLS[:10])
        with self.assertRaises(ValueError):
            fetch.check("pools", {"status": "success", "data": []})

class SaveLoadTest(unittest.TestCase):
    def setUp(self):
        self.dir = pathlib.Path(tempfile.mkdtemp())

    def test_save_is_gzipped_and_deterministic(self):
        a = fetch.save("pools", POOLS, self.dir, "2026-10-12").read_bytes()
        b = fetch.save("pools", POOLS, self.dir, "2026-10-12").read_bytes()
        self.assertEqual(a, b)
        self.assertEqual(json.loads(gzip.decompress(a)), POOLS)

    def test_load_orders_plain_and_gzipped_by_date(self):
        old = {"status": "success", "data": [{"tag": "old"}]}
        (self.dir / "2026-07-05-pools.json").write_text(json.dumps(old))
        fetch.save("pools", {"status": "success", "data": [{"tag": "new"}]},
                   self.dir, "2026-10-12")
        newest, stamp = metrics.load("pools", snap=self.dir)
        prior, prior_stamp = metrics.load("pools", offset=1, snap=self.dir)
        self.assertEqual((newest[0]["tag"], stamp), ("new", "2026-10-12"))
        self.assertEqual((prior[0]["tag"], prior_stamp), ("old", "2026-07-05"))

if __name__ == "__main__":
    unittest.main()
