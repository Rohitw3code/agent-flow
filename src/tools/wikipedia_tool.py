import wikipedia

class WikipediaTool:
    """
    A simple tool that searches Wikipedia and returns a short summary.
    """
    def run(self, query: str) -> str:
        try:
            results = wikipedia.search(query)
            if not results:
                return f"No Wikipedia results for '{query}'."
            page_title = results[0]
            summary = wikipedia.summary(page_title, sentences=3)
            return f"Wikipedia summary for {page_title}:\n{summary}"
        except Exception as e:
            return f"Error fetching Wikipedia data: {e}"
