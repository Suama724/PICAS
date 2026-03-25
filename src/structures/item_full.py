from dataclasses import dataclass, field

@dataclass
class Paper:
    paper_id: int
    title: str
    # 需要加field每次返回不同list对象否则不同paper底层共用了
    authors: list[str] = field(default_factory=list)
    year: int | None = None
    # 写来源，可能来自journal可能来自其它
    source: str | None = None
    month: str | None = None
    doi: str | None = None
    ee: str | None = None
    # xml 文件里的key
    key: str | None = None 

    def __repr__(self) -> str:
        author_str = ','.join(self.authors[:3])
        if len(self.authors) > 3:
            author_str += 'et al.'

        return (
            f"Paper(id={self.paper_id}),\n"
            f"-title='{self.title[:50]}{"..." if len(self.title) > 50 else ""}',\n"
            f"-authors=[{author_str}],\n"          
        )

@dataclass
class Author:
    author_id: int
    name: str
    paper_cnt: int = 0

    def __repr__(self):
        return (
            f"Author(id={self.author_id}),\n"
            f"-name='{self.name}'\n"
            f"-Paper Released Num={self.paper_cnt}\n"
        )
    
@dataclass 
class Library:
    lib_id: str
    name: str
    save_path: str

    def __repr__(self) -> str:
        return (
            f"Library(id={self.lib_id}),\n"
            f"-name='{self.name}',\n"
            f"-save_path='{self.save_path}'\n"
        )
