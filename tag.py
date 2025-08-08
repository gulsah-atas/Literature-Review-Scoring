import bibtexparser
import re

EVACUATION_TERMS = ['evacuate', 'evacuee', 'evacuation', 'evacuating', 'evacuations', 'evacuees', 'evacuates']
FLOOD_TERMS = ['flood', 'flooding', 'floods']
EARTHQUAKE_TERMS = ['earthquake', 'seismic', 'earthquakes']
FIRE_TERMS = ['fire', 'wildfire', 'bushfire', 'fires', 'bushfires', 'wildfires']
HURRICANE_TERMS = ['hurricane', 'hurricanes']
TSUNAMI_TERMS = ['tsunami', 'tsunamis']
AVALANCHE_TERMS = ['avalanche', 'avalanche']
LANDSLIDE_TERMS = ['landslide', 'landslide']
INDOOR_TERMS = ['building', 'indoor', 'indoors', 'mall', 'airport', 'airports', 'hospital', 'hospitals', 'buildings', 'office', 'apartment', 'house', 'homes', 'home', 'houses', 'apartments']
TERRORISM_TERMS = ['warzone', 'terrorist', 'terrorists', 'terrorism', 'bomb', 'bombs', 'hostage', 'hostages', 'militancy', 'armed assault', 'armed conflicts']
TRAFFIC_TERMS = ['transport', 'vehicle', 'vehicles', 'traffic', 'driving', 'routing', 'routes', 'rerouting', 'trip chaining', 'congestion', 'car', 'cars', 'road safety', 'commuting', 'route choice', 'mode choice']
SHELTER_TERMS = ['shelter', 'shelters', 'refuge', 'sanctuary', 'safe space']
FIRE_DYNAMICS_TERMS = ['smoke propagation', 'fire damage', 'heat transfer', 'flame spread', 'combustion', 'fire spread', 'fire growth', 'fire behavior', 'fire behaviour']
INFRASTRUCTURE_TERMS = ['building durability', 'infrastructure', 'structural integrity', 'urban planning', 'bridge durability']
TRAINING_TERMS = ['firefighter training', 'evacuation training', 'emergency response training', 'disaster preparedness training', 'fire safety training', 'first responder training', 'rescue training', 'fire safety training', 'evacuee training', 'drill', 'education', 'educational']
MATHEMATICAL_MODEL_TERMS = ['modelling', 'neural network', 'neural networks', 'multi agent', 'bayesian network', 'bayesian networks', 'multi-agent', 'mathematical model', 'optimisation algorithm', 'optimization algorithm', 'mathematical models', 'optimisation algorithms', 'optimization algorithms', 'monte carlo simulation', 'monte carlo simulations', 'simulation models', 'computational models', 'predictive models', 'stochastic models', 'probabilistic models', 'deterministic models', 'statistical models', 'analytical models', 'numerical models', 'optimisation models', 'optimization models', 'algorithmic models', 'simulation model', 'computational model', 'predictive model', 'stochastic model', 'probabilistic model', 'deterministic model', 'statistical model', 'analytical model', 'numerical model', 'optimisation model', 'optimization model', 'algorithmic model', 'agent based', 'agent-based']
POLICY_TERMS = ['policy', 'regulation', 'guideline', 'legislation', 'regulatory', 'policies', 'legislations', 'guidelines', 'regulations']
ENVIRONMENTAL_TERMS = ['pollution', 'climatology', 'carbon monoxide', 'carbon dioxide', 'carbon emission', 'air quality', 'air pollution', 'environmental', 'ecological', 'sustainability', 'climate', 'ecosystem', 'ecosystems', 'habitat loss', 'biodiversity', 'pollution', 'emission']
MEDICAL_TERMS = ['nursing', 'stroke', 'epidural', 'hemorrhage', 'diseases', 'disease', 'blood pressure', 'blunt trauma', 'medical emergency', 'healthcare', 'first aid', 'artery', 'medical', 'paramedic', 'illnesses', 'sicknesses', 'epidemics', 'pandemics', 'injuries', 'surgeries', 'ambulance', 'medicine', 'health', 'illness', 'sickness', 'epidemic', 'pandemic', 'injury', 'surgery']
PEDESTRIAN_TERMS = ['pedestrian evacuation', 'pedestrian evacuations', 'foot traffic', 'crowd control', 'pedestrian', 'pedestrians', 'footpath', 'footpaths', 'urban mobility']
SUBWAY_TERMS = ['subway', 'metro', 'light rail']
PRE_EVACUATION_TERMS = ['pre-evacuation', 'pre-emptive', 'advance warning', 'before evacuation', 'preparation', 'awareness', 'preparedness', 'threat assessment', 'prevention']
POST_DISASTER_TERMS = ['post-disaster', 'recovery', 'aftermath', 'reconstruction', 'restoration', 'emergency rescue']
FIREFIGHTING_TERMS = ['firefighting', 'firefighter', 'firefighters']
CULTURAL_STUDIES_TERMS = ['cultural heritage', 'cultural characteristics', 'gender', 'ethnicity', 'indigenous', 'feminism', 'queer']
PSYCHOLOGICAL_EFFECTS_TERMS = ['anxiety', 'psychological effects', 'mental health', 'emotional response', 'emotional responses', 'PTSD', 'traumatic stress disorder', 'traumatic stress disorders']
HUMAN_FACTORS_TERMS = [
    'risk awareness', 'risk perception', 'decision-making', 'judgment', 'cognition', 'decision making',
    'panic', 'compliance', 'help-seeking behavior', 'risk-taking', 'panics',
    'group behavior', 'community response', 'social networks', 'interpersonal communication',
    'threat perception', 'vulnerability', 'hazard awareness', 'anxiety', 'stress', 'trauma', 'resilience'
]
VR_TERMS = ['virtual reality', 'vr', 'augmented reality', 'extended reality', 'xr', 'ar', 'mixed reality', 'mr', 'immersive simulation', 'immersive technology', 'immersive technologies', 'immersive simulations']
VOLCANO_TERMS = ['volcano', 'volcanic', 'volcanoes']
TORNADO_TERMS = ['tornado', 'tornadoes']
STORM_TERMS = ['storm', 'storms']
SHIP_TERMS = ['ship evacuation', 'boat evacuation', 'ship evacuations', 'boat evacuations']
NUCLEAR_TERMS = ['nuclear']
LANDS_TERMS = ['landslide', 'landslides']
CYCLONE_TERMS = ['cyclone', 'cyclones']
AVAL_TERMS = ['avalanche', 'avalanches']
ANIMAL_TERMS = ['animal', 'animals']
AIRCRAFT_TERMS = ['aircraft', 'aircraft evacuation', 'aircraft evacuations', 'airplane evacuation', 'airplane evacuations']


def add_keywords(entry, keywords):
    existing_keywords = entry.get('keywords', '')
    existing_keywords_set = set(existing_keywords.split(', '))
    new_keywords_set = set(keywords)
    combined_keywords_set = existing_keywords_set | new_keywords_set
    entry['keywords'] = ', '.join(combined_keywords_set)

def remove_keywords(entry, keywords):
    existing_keywords = entry.get('keywords', '')
    existing_keywords_set = set(existing_keywords.split(', '))
    keywords_to_remove_set = set(keywords)
    remaining_keywords_set = existing_keywords_set - keywords_to_remove_set
    entry['keywords'] = ', '.join(remaining_keywords_set)

def check_terms(text, terms):
    return any(re.search(r'\b' + term + r'\b', text, re.IGNORECASE) for term in terms)

def process_entries(bib_database):
    for entry in bib_database.entries:
        title = entry.get('title', '')
        abstract = entry.get('abstract', '')
        keywords = entry.get('keywords', '')
        
        combined_text = f"{title} {abstract} {keywords}".lower()

        if check_terms(combined_text, EVACUATION_TERMS):
            add_keywords(entry, ['evacuation'])
            remove_keywords(entry, ['non-evacuation'])
        else:
            add_keywords(entry, ['non-evacuation'])
            remove_keywords(entry, ['evacuation'])

        if check_terms(combined_text, FLOOD_TERMS):
            add_keywords(entry, ['flood'])
        if check_terms(combined_text, EARTHQUAKE_TERMS):
            add_keywords(entry, ['earthquake'])
        if check_terms(combined_text, FIRE_TERMS):
            add_keywords(entry, ['fire'])
        if check_terms(combined_text, HURRICANE_TERMS):
            add_keywords(entry, ['hurricane'])
        if check_terms(combined_text, TSUNAMI_TERMS):
            add_keywords(entry, ['tsunami'])
        if check_terms(combined_text, AVALANCHE_TERMS):
            add_keywords(entry, ['avalanche'])
        if check_terms(combined_text, LANDSLIDE_TERMS):
            add_keywords(entry, ['landslide'])
        if check_terms(combined_text, INDOOR_TERMS):
            add_keywords(entry, ['indoor'])
        if check_terms(combined_text, TERRORISM_TERMS):
            add_keywords(entry, ['terrorism'])
        if check_terms(combined_text, TRAFFIC_TERMS):
            add_keywords(entry, ['traffic'])
        if check_terms(combined_text, SHELTER_TERMS):
            add_keywords(entry, ['shelter'])
        if check_terms(combined_text, FIRE_DYNAMICS_TERMS):
            add_keywords(entry, ['fire dynamics'])
        if check_terms(combined_text, INFRASTRUCTURE_TERMS):
            add_keywords(entry, ['infrastructure'])
        if check_terms(combined_text, TRAINING_TERMS):
            add_keywords(entry, ['training'])
        if check_terms(combined_text, MATHEMATICAL_MODEL_TERMS):
            add_keywords(entry, ['modeling'])
        if check_terms(combined_text, POLICY_TERMS):
            add_keywords(entry, ['policy'])
        if check_terms(combined_text, ENVIRONMENTAL_TERMS):
            add_keywords(entry, ['environmental'])
        if check_terms(combined_text, MEDICAL_TERMS):
            add_keywords(entry, ['medical'])
        if check_terms(combined_text, PEDESTRIAN_TERMS):
            add_keywords(entry, ['pedestrian'])
        if check_terms(combined_text, SUBWAY_TERMS):
            add_keywords(entry, ['subway'])
        if check_terms(combined_text, PRE_EVACUATION_TERMS):
            add_keywords(entry, ['pre-evacuation'])
        if check_terms(combined_text, POST_DISASTER_TERMS):
            add_keywords(entry, ['post-disaster'])
        if check_terms(combined_text, FIREFIGHTING_TERMS):
            add_keywords(entry, ['firefighter'])
        if check_terms(combined_text, CULTURAL_STUDIES_TERMS):
            add_keywords(entry, ['cultural studies'])
        if check_terms(combined_text, PSYCHOLOGICAL_EFFECTS_TERMS):
            add_keywords(entry, ['psychological effects'])
        if check_terms(combined_text, HUMAN_FACTORS_TERMS):
            add_keywords(entry, ['human factors'])
        if check_terms(combined_text, VR_TERMS):
            add_keywords(entry, ['vr'])
        if check_terms(combined_text, VOLCANO_TERMS):
            add_keywords(entry, ['volcano'])
        if check_terms(combined_text, TORNADO_TERMS):
            add_keywords(entry, ['tornado'])
        if check_terms(combined_text, STORM_TERMS):
            add_keywords(entry, ['storm'])
        if check_terms(combined_text, SHIP_TERMS):
            add_keywords(entry, ['ship evacuation'])
        if check_terms(combined_text, NUCLEAR_TERMS):
            add_keywords(entry, ['nuclear'])
        if check_terms(combined_text, LANDS_TERMS):
            add_keywords(entry, ['landslide'])
        if check_terms(combined_text, CYCLONE_TERMS):
            add_keywords(entry, ['cyclone'])
        if check_terms(combined_text, AVAL_TERMS):
            add_keywords(entry, ['avalanche'])
        if check_terms(combined_text, ANIMAL_TERMS):
            add_keywords(entry, ['animal'])
        if check_terms(combined_text, AIRCRAFT_TERMS):
            add_keywords(entry, ['aircraft evacuation'])
        if check_terms(combined_text, SHIP_TERMS):
            add_keywords(entry, ['ship evacuation'])
        

def load_bibtex(file_path):
    with open(file_path, 'r', encoding='utf-8') as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)
    return bib_database

def save_bibtex(bib_database, output_file):
    with open(output_file, 'w', encoding='utf-8') as bibtex_file:
        bibtexparser.dump(bib_database, bibtex_file)

def main(input_file, output_file):
    bib_database = load_bibtex(input_file)
    process_entries(bib_database)
    save_bibtex(bib_database, output_file)
    print(f"Updated BibTeX file saved to {output_file}")

if __name__ == "__main__":
    input_file = 'input.bib' 
    output_file = 'output.bib' 
    main(input_file, output_file)
