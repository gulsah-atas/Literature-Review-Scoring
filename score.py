import bibtexparser
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from collections import Counter

SCORES = {
    'aircraft evacuation': -3,
    'animal': -3,
    'avalanche': -3,
    'cultural studies': -3,
    'cyclone': -1,
    'earthquake': -3,
    'environmental': -1,
    'evacuation': 2,
    'fire': 3,
    'fire dynamics': -1,
    'firefighter': -1,
    'flood': -1,
    'human factors': 2,
    'hurricane': -1,
    'indoor': -3,
    'infrastructure': -2,
    'landslide': -3,
    'medical': -3,
    'modeling': -2,
    'non-evacuation': -3,
    'nuclear': -3,
    'pedestrian': -3,
    'policy': -1,
    'post-disaster': -2,
    'pre-evacuation': -1,
    'psychological effects': -1,
    'shelter': -2,
    'ship evacuation': -3,
    'storm': -1,
    'subway': -1,
    'terrorism': -3,
    'tornado': -1,
    'traffic': 3,
    'training': -2,
    'tsunami': -1,
    'typhoon': -1,
    'volcano': -2,
    'vr': 3
}

def score_entry(entry):
    score = 0
    keywords = entry.get('keywords', '').split(', ')
    for keyword in keywords:
        score += SCORES.get(keyword.strip(), 0)  
    return score

def load_bibtex(file_path):
    with open(file_path, 'r', encoding='utf-8') as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)
    return bib_database

def process_entries(bib_database):
    for entry in bib_database.entries:
        entry['score'] = score_entry(entry)

def plot_scores(scores):
    scores_df = pd.DataFrame(scores, columns=['Score'])
    plt.figure(figsize=(10, 6))
    sns.kdeplot(data=scores_df, x='Score', fill=True, color='skyblue', bw_adjust=0.5)
    plt.title('Density Plot of BibTeX Entry Scores')
    plt.xlabel('Score')
    plt.ylabel('Density')
    plt.grid()
    plt.show()

    
def print_score_distribution(scores):
    score_counter = Counter(scores)
    
    positive_count = sum(1 for score in scores if score > 0)
    negative_count = sum(1 for score in scores if score < 0)
    zero_count = sum(1 for score in scores if score == 0)
    
    print("\nScore Distribution:")
    for score, count in sorted(score_counter.items()):
        print(f"Score {score}: {count} entries")
    
    print(f"\n# pos: {positive_count}")
    print(f"#neg: {negative_count}")
    print(f"#0: {zero_count}")


bib_database = load_bibtex('input.bib')

process_entries(bib_database)
    
scores = [entry['score'] for entry in bib_database.entries]
print_score_distribution(scores)
plot_scores(scores)
    

