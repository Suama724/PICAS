from src.structures import PaperFTP, Author, Library, Paper
from src.utils.timer import timer


def test_01_structures():
    print("* Test 01 Data Structure Test\n")
    
    paper = Paper(
        paper_id=1,
        title="Test Paper",
        authors=["TA1","TA2"],
        year=114514,
        source="arxiv",
        month=13,
    )
    print(f"Test Paper: {paper}")

    author = Author(
        author_id=1,
        name="Akarin",
        paper_cnt=42062
    )
    
    print(f"Test Author: {author}")

    lib = Library(
        lib_id=1,
        name="Zotero",
        save_path="NULL"
    )
    print(f"Test Lib {lib}")

    paper_ftp = PaperFTP(
        paper_id=2,
        title=paper.title,
        authors=paper.authors,
        year=paper.year,
        source=paper.source
    )
    print(f"Test PaperFTP: {paper_ftp}")

    with timer("Test Timer"):
        print(sum(range(100000000)))

