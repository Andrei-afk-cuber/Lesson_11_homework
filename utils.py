import json

# функция, которая возвращает список кандидатов
def load_candidates_from_json(path):
    with open(path, 'r', encoding="utf-8") as file:
        return json.load(file)

def get_candidate(candidate_id, candidates):
    for candidate in candidates:
        if candidate['id'] == candidate_id:
            return candidate

def get_candidates_by_name(candidate_name, candidates):
    result = []

    for candidate in candidates:
        if candidate_name in candidate['name']:
            result.append(candidate)

    return result

def get_candidates_by_skill(skill_name, candidates):
    result = []

    for candidate in candidates:
        if skill_name in candidate['skills']:
            result.append(candidate)

    return result