import os
import shutil
from nano_graphrag import GraphRAG

FAKE_TEXT = " ".join([str(i) for i in range(10000)])
WORKING_DIR = "./nano_graphrag_cache_TEST"

if os.path.exists(WORKING_DIR):
    shutil.rmtree(WORKING_DIR)


def test_init():
    rag = GraphRAG(working_dir=WORKING_DIR)
    rag.insert(FAKE_TEXT)
    # os.rmtree(rag.working_dir)

    rag = GraphRAG(working_dir=WORKING_DIR)
    rag.insert(FAKE_TEXT)
    assert len(rag.full_docs._data) == 2
