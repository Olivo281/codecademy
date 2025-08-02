# Step 1: Convert damages strings to floats or keep "Damages not recorded"
# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

# test function by updating damages
def new_damages(damages):
  updated_damages = []
  for damage in damages:
    if damage == 'Damages not recorded':
      updated_damages.append(damage)
    else:
      if damage.endswith('B'):
        updated_damages.append(float(damage[:-1]) * 1000000000)
      elif damage.endswith('M'):
        updated_damages.append(float(damage[:-1]) * 1000000)
  return updated_damages
  
  

# 2 
def organize(names, months, years, max_sustained_winds, areas_affected, deaths, damages):
    updated_damages = new_damages(damages)  # Use updated damages
    hurricane_dict = {}
    for i in range(len(names)):
        hurricane_data = {
            'Name': names[i],
            'Month': months[i],
            'Year': years[i],
            'Max Sustained Wind': max_sustained_winds[i],
            'Areas Affected': areas_affected[i],
            'Damage': updated_damages[i],  # Use updated damages
            'Deaths': deaths[i]
        }
        hurricane_dict[names[i]] = hurricane_data
    return hurricane_dict  # Return the dictionary

# Test the function
hurricane_data = organize(names, months, years, max_sustained_winds, areas_affected, deaths, damages)

# Print the result
print(hurricane_data)
def convert_damages(damages):
    updated_damages = []
    for damage in damages:
        if damage == "Damages not recorded":
            updated_damages.append(damage)
        else:
            damage_str = damage.replace("$", "")
            if damage_str[-1] == "B":
                value = float(damage_str[:-1]) * 1_000_000_000
            elif damage_str[-1] == "M":
                value = float(damage_str[:-1]) * 1_000_000
            else:
                value = float(damage_str)
            updated_damages.append(value)
    return updated_damages

# Step 2: Create hurricane dictionary from lists
def create_hurricane_dict(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
    updated_damages = convert_damages(damages)
    hurricanes = {}
    for i in range(len(names)):
        hurricanes[names[i]] = {
            "Name": names[i],
            "Month": months[i],
            "Year": years[i],
            "Max Sustained Wind": max_sustained_winds[i],
            "Areas Affected": areas_affected[i],
            "Damage": updated_damages[i],
            "Deaths": deaths[i]
        }
    return hurricanes

# Step 3: Organize hurricanes by year
def organize_by_year(hurricane_dict):
    hurricanes_by_year = {}
    for hurricane in hurricane_dict.values():
        year = hurricane["Year"]
        hurricanes_by_year.setdefault(year, []).append(hurricane)
    return hurricanes_by_year

# Step 4: Count how often each area is affected
def count_areas(hurricane_dict):
    area_counts = {}
    for hurricane in hurricane_dict.values():
        for area in hurricane["Areas Affected"]:
            area_counts[area] = area_counts.get(area, 0) + 1
    return area_counts

# Step 5: Find the area affected the most
def most_affected_area(area_counts):
    max_area = None
    max_count = 0
    for area, count in area_counts.items():
        if count > max_count:
            max_area = area
            max_count = count
    return max_area, max_count

# Step 6: Find the hurricane with greatest deaths
def deadliest_hurricane(hurricane_dict):
    deadliest = None
    max_deaths = -1
    for hurricane in hurricane_dict.values():
        if hurricane["Deaths"] > max_deaths:
            deadliest = hurricane["Name"]
            max_deaths = hurricane["Deaths"]
    return deadliest, max_deaths

# Step 7: Rate hurricanes by mortality scale
def rate_by_mortality(hurricane_dict, mortality_scale):
    ratings = {key: [] for key in mortality_scale.keys()}
    ratings[max(mortality_scale.keys()) + 1] = []  # catch all bigger
    
    for hurricane in hurricane_dict.values():
        deaths = hurricane["Deaths"]
        rated = False
        for rating, upper_bound in mortality_scale.items():
            if deaths <= upper_bound:
                ratings[rating].append(hurricane)
                rated = True
                break
        if not rated:
            ratings[max(mortality_scale.keys()) + 1].append(hurricane)
    return ratings

# Step 8: Find hurricane causing greatest damage
def costliest_hurricane(hurricane_dict):
    costliest = None
    max_damage = -1
    for hurricane in hurricane_dict.values():
        damage = hurricane["Damage"]
        if isinstance(damage, float) and damage > max_damage:
            costliest = hurricane["Name"]
            max_damage = damage
    return costliest, max_damage

# Step 9: Rate hurricanes by damage scale
def rate_by_damage(hurricane_dict, damage_scale):
    ratings = {key: [] for key in damage_scale.keys()}
    ratings[max(damage_scale.keys()) + 1] = []  # catch all bigger
    
    for hurricane in hurricane_dict.values():
        damage = hurricane["Damage"]
        if not isinstance(damage, float):
            # Skip if damage not recorded
            continue
        rated = False
        for rating, upper_bound in damage_scale.items():
            if damage <= upper_bound:
                ratings[rating].append(hurricane)
                rated = True
                break
        if not rated:
            ratings[max(damage_scale.keys()) + 1].append(hurricane)
    return ratings


# -------------------------
# Example data for testing:
names = [
    "Cuba I", "San Felipe II Okeechobee", "Bahamas", "Cuba II",
    # ... (add all 34 names here)
]

months = [
    "October", "September", "September", "November",
    # ... (corresponding months)
]

years = [
    1924, 1928, 1932, 1932,
    # ... (corresponding years)
]

max_sustained_winds = [
    165, 160, 160, 175,
    # ... (corresponding max wind speeds)
]

areas_affected = [
    ["Central America", "Mexico", "Cuba", "Florida", "The Bahamas"],
    ["The Bahamas", "Florida", "Georgia", "The Carolinas", "Virginia"],
    ["The Bahamas", "Northeastern United States"],
    ["Lesser Antilles", "Jamaica", "Cayman Islands", "Cuba", "The Bahamas", "Bermuda"],
    # ... (corresponding areas)
]

damages = [
    "Damages not recorded", "$100M", "Damages not recorded", "$40M",
    # ... (corresponding damages)
]

deaths = [
    90, 4000, 16, 3103,
    # ... (corresponding deaths)
]

# Mortality and damage scales
mortality_scale = {0: 0, 1: 100, 2: 500, 3: 1000, 4: 10000}
damage_scale = {0: 0, 1: 100_000_000, 2: 1_000_000_000, 3: 10_000_000_000, 4: 50_000_000_000}

# -------------------------
# Using the functions:

# Create hurricane dictionary
hurricanes = create_hurricane_dict(names, months, years, max_sustained_winds, areas_affected, damages, deaths)

# Organize hurricanes by year
hurricanes_by_year = organize_by_year(hurricanes)

# Count affected areas
area_counts = count_areas(hurricanes)

# Find most affected area
top_area, top_hits = most_affected_area(area_counts)
print(f"The most affected area is {top_area} with {top_hits} hits.")

# Find deadliest hurricane
deadliest, death_count = deadliest_hurricane(hurricanes)
print(f"The deadliest hurricane is {deadliest} with {death_count} deaths.")

# Rate hurricanes by mortality
mortality_ratings = rate_by_mortality(hurricanes, mortality_scale)
print("Mortality ratings keys:", mortality_ratings.keys())

# Find costliest hurricane
costliest, cost = costliest_hurricane(hurricanes)
print(f"The costliest hurricane is {costliest} with ${cost} in damages.")

# Rate hurricanes by damage
damage_ratings = rate_by_damage(hurricanes, damage_scale)
print("Damage ratings keys:", damage_ratings.keys())
