from classe.rag import EmbRag

Docs=r"C:\EAG\RAG\RAG_template\test\docs"
faiss=r"C:\EAG\RAG\RAG_template\test\FAISS"

obj=EmbRag(Docs,faiss)

ans=obj.queryDB("hi,how are you?")
print(ans)