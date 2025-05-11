import faiss
import os
from pathlib import Path
import json

class EmbRag:
    def __init__(self,docs_path,faiss_path):
        pth=os.path.join(faiss_path,"cache.json")
        self.pth_checker(pth)
        with open(pth,'r') as f:
            self.cache=json.load(f)
    
    def pth_checker(self,arge):
        file_path=Path(arge)
        
        if(not file_path.exists()):
            file_path.parent.mkdir(parents=True, exist_ok=True)
            with open(file_path,'w') as f:
                json.dump({},f)

DOC=r"C:\EAG\RAG\RAG_template\template\DOCS"
faiss_pth=r"C:\EAG\RAG\RAG_template\template\faiss_index"
obj=EmbRag(DOC,faiss_pth)