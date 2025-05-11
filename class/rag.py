import faiss
import os
from pathlib import Path
import json
from trafilatura import fetch_url, extract
import pymupdf4llm 

""" things remaining : chunker,faiss """
class EmbRag:
    # cache=""
    # urls=[]
    # files=[]
    def __init__(self,docs_path,faiss_path):

        self.docs=docs_path
        self.faiss_path=faiss_path

        pth=os.path.join(faiss_path,"cache.json")
        pth2=os.path.join(faiss_path,"meta_data.json")
        self.pth_checker(pth2)
        self.pth_checker(pth)
        with open(pth,'r') as f:
            self.cache=json.load(f)
        self.files=os.listdir(docs_path)

        for i in self.files:
            if i not in self.cache:
                if(i.endswith('.txt') and not i.startswith('url')):
                    with open(os.path.join(self.docs,i),'r') as f:
                        text=f.read()
                    print(text)
                elif(i.endswith('.pdf')):
                    md_text = pymupdf4llm.to_markdown(os.path.join(self.docs,i))
                    print(md_text)
                elif(i.endswith('.txt') and i.startswith('url')):
                    with open(os.path.join(self.docs,i),'r') as f:
                        links=f.read()
                        self.urls=links.split(',')
                    for j in self.urls:
                        downloaded = fetch_url(j)
                        result = extract(downloaded)
                        if(result == None):
                            print(f"could not access the url {j} because of authentication ")
                        else:
                            #chunker(result)
                            print(result)
                else:
                    print(f"{i} is not a part of [pdf,txt,website] markitdown feature coming soon")
                        

                self.cache[i]="True"


        with open(pth,'w') as f:
            json.dump(self.cache,f,indent=4)
    
    def pth_checker(self,arge):
        file_path=Path(arge)
        if(not file_path.exists()):
            file_path.parent.mkdir(parents=True, exist_ok=True)
            with open(file_path,'w') as f:
                json.dump({},f)

DOC=r"C:\EAG\RAG\RAG_template\template\DOCS"
faiss_pth=r"C:\EAG\RAG\RAG_template\template\faiss_index"
obj=EmbRag(DOC,faiss_pth)