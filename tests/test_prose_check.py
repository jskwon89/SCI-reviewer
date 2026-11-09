"""Synthetic cases only; no manuscript text is committed."""
import importlib.util
from pathlib import Path
import tempfile
import unittest
import zipfile

spec = importlib.util.spec_from_file_location('prose', Path(__file__).parents[1]/'tools/prose_check.py')
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

class ProseScanTests(unittest.TestCase):
    def test_internal_candidate_and_normal_research(self):
        self.assertTrue(mod.scan([('p1','교수님 확인 대기: 분석은 최종 잠금되었다.')]))
        self.assertFalse(mod.scan([('p2','The baseline measurement preceded the final analytic sample selection.')]))

    def test_one_necessary_boundary_is_not_density(self):
        self.assertFalse(mod.scan([('p1','이 결과는 모든 집단이 같음을 의미하지 않는다.')]))
        self.assertTrue(mod.scan([('p1','이는 차이가 없음을 의미하지 않으며 효과를 입증하지 않는다.')]))

    def test_placeholder_but_not_table_callout(self):
        self.assertTrue(mod.scan([('p1','[초록: 이 위치에 삽입]')]))
        self.assertFalse(mod.scan([('p1','[표 1 삽입]')]))

    def test_repeated_sentence(self):
        sentence = 'Participants reported the same behavior during the observation period.'
        self.assertIn('REPEATED_SENTENCE', [c['kind'] for c in mod.scan([('p1',sentence),('p2',sentence)])])

    def test_run_fragmented_docx_and_table(self):
        with tempfile.TemporaryDirectory() as t:
            p = Path(t)/'test.docx'
            with zipfile.ZipFile(p,'w') as z:
                z.writestr('word/document.xml', '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:body><w:tbl><w:tr><w:tc><w:p><w:r><w:t>교수님 확인</w:t></w:r><w:r><w:t> 대기</w:t></w:r></w:p></w:tc></w:tr></w:tbl></w:body></w:document>')
            self.assertIn('INTERNAL', [c['kind'] for c in mod.scan(list(mod.paragraphs(p)))])

    def test_author_option(self):
        rows=[('p1','We examined the relationship.')]
        self.assertFalse(mod.scan(rows))
        self.assertTrue(mod.scan(rows, single_author=True))

if __name__=='__main__':
    unittest.main()
