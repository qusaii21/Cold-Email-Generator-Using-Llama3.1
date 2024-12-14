import os
import pandas as pd
import chromadb
import uuid

class Portfolio:
    def __init__(self, file_path=None):
        # Dynamically determine the absolute path to portfolio.csv
        if file_path is None:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(base_dir, "resources", "portfolio.csv")
        
        self.file_path = file_path
        self.data = pd.read_csv(file_path)
        self.chroma_client = chromadb.PersistentClient('vectorstore')
        self.collection = self.chroma_client.get_or_create_collection(name="portfolio")

    def load_portfolio(self):
        if not self.collection.count():
            for _, row in self.data.iterrows():
                self.collection.add(
                    documents=row["Techstack"],
                    metadatas={"links": row["Links"]},
                    ids=[str(uuid.uuid4())]
                )

    def query_links(self, skills):
        result = self.collection.query(query_texts=skills, n_results=2)
        return result.get('metadatas', [])

    def add_techstack(self, techstack, link):
        # Append to CSV
        new_row = pd.DataFrame({"Techstack": [techstack], "Links": [link]})
        self.data = pd.concat([self.data, new_row], ignore_index=True)
        self.data.to_csv(self.file_path, index=False)

        # Add to ChromaDB
        self.collection.add(
            documents=techstack,
            metadatas={"links": link},
            ids=[str(uuid.uuid4())]
        )
        return f"Added {techstack} to portfolio."

