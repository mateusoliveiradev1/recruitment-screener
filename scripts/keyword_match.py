import sys

def match_score(jd_path, cv_path):
    try:
        with open(jd_path, 'r', encoding='utf-8') as f1, open(cv_path, 'r', encoding='utf-8') as f2:
            jd_words = set(f1.read().lower().split())
            cv_words = set(f2.read().lower().split())
        match = jd_words.intersection(cv_words)
        print(f"Deterministic Keyword Match: {len(match)} exact overlap words.")
        print(f"Keywords: {', '.join(list(match)[:15])}...")
    except Exception as e:
        print(f"Match failed: {e}")

if __name__ == "__main__":
    match_score(sys.argv[1], sys.argv[2])
