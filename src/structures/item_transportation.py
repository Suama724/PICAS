from dataclasses import dataclass

# Paper for transportation
@dataclass
class PaperFTP:
    paper_id: int
    title: str
    authors: list[str]
    year: int | None = None
    source: str | None = None
    
    def __repr__(self):
        return (
            f"PaperFTP(paper_id={self.paper_id}),\n"
            f"-title='{self.title}',"
            f"-authors='{self.authors}',\n"
            f"-year={self.year},\n"
            f"-source='{self.source}'\n"
        )
