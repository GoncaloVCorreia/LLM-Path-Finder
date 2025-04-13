def build_system_prompt(docs, metas):
    file_blocks = []
    for doc, meta in zip(docs, metas):
        file_blocks.append(f"<FILE>\n{doc.strip()}\n</FILE>")
    retrieved_context = "\n\n".join(file_blocks)

    return (
        "You are a file analysis expert.\n"
            "The user has several files and folders."
            f"FILES and Folders:\n{retrieved_context}\n\n"
            "INSTRUCTIONS:\n"
            "- Only answer queries that are about locating files or folders.\n"
            "- If the user asks something unrelated to files/folders, respond with an empty list [].\n"
            "- If there are matches, respond with a JSON list of objects in the follwing format:\n"
            '  - "score": integer from 0 to 100 indicating confidence (100 being the most cofident)\n'
            '  - "path": string of full file/folder path\n'
            '  - "justification": A big explanation of why this file/folder is a match, including reasoning like name similarity, file extension, directory context, or abbreviations \n\n'
            'For example: [{"score": 87, "path": "...", "justification": "..."}]\n\n'
            "You may choose any value between 0 and 100 when scoring"
            "Respond ONLY with a JSON array of such objects, one per file\n"
            "Besides the JSON array don't write nothing more\n\n"
    )
