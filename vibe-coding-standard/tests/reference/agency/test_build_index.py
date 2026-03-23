import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
MODULE_PATH = ROOT / "reference" / "agency" / "build_index.py"


def load_module():
    spec = importlib.util.spec_from_file_location("build_index", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class BuildIndexTest(unittest.TestCase):
    def test_build_index_includes_markdown_metadata_and_skips_other_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            base_dir = Path(tmp)
            upstream_dir = base_dir / "upstream"
            engineering_dir = upstream_dir / "engineering"
            engineering_dir.mkdir(parents=True)

            agent_file = engineering_dir / "engineering-frontend-developer.md"
            agent_file.write_text(
                "# Frontend Developer\n\n"
                "Builds polished web interfaces.\n\n"
                "## When to Use\n\n"
                "- building React pages\n"
                "- improving UI performance\n",
                encoding="utf-8",
            )

            ignored_file = engineering_dir / "notes.txt"
            ignored_file.write_text("ignore me", encoding="utf-8")

            module = load_module()
            index = module.build_index(upstream_dir)

            self.assertEqual(index["activation_policy"]["priority"], 2)
            self.assertEqual(index["activation_policy"]["mode"], "fallback_only")

            self.assertEqual(len(index["documents"]), 1)

            document = index["documents"][0]
            self.assertEqual(document["id"], "engineering-engineering-frontend-developer")
            self.assertEqual(document["title"], "Frontend Developer")
            self.assertEqual(document["category"], "engineering")
            self.assertEqual(document["path"], "engineering/engineering-frontend-developer.md")
            self.assertIn("react", document["keywords"])
            self.assertIn("ui", document["keywords"])
            self.assertIn("building React pages", document["when_to_use"])

            json.dumps(index)

    def test_search_documents_ranks_keyword_matches(self):
        with tempfile.TemporaryDirectory() as tmp:
            base_dir = Path(tmp)
            upstream_dir = base_dir / "upstream"
            engineering_dir = upstream_dir / "engineering"
            product_dir = upstream_dir / "product"
            engineering_dir.mkdir(parents=True)
            product_dir.mkdir(parents=True)

            (engineering_dir / "engineering-frontend-developer.md").write_text(
                "# Frontend Developer\n\n"
                "## When to Use\n\n"
                "- build React dashboards\n",
                encoding="utf-8",
            )
            (product_dir / "product-manager.md").write_text(
                "# Product Manager\n\n"
                "## When to Use\n\n"
                "- define roadmap and product priorities\n",
                encoding="utf-8",
            )

            module = load_module()
            index = module.build_index(upstream_dir)
            matches = module.search_documents(index, "react dashboard ui", limit=2)

            self.assertEqual(matches[0]["id"], "engineering-engineering-frontend-developer")
            self.assertLessEqual(len(matches), 2)


if __name__ == "__main__":
    unittest.main()
