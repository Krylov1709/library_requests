import requests

res = requests.get('https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json')
hero_list = ['Hulk', 'Captain America', 'Thanos']
top_intelligence = 0
for hero in res.json():
    for hero_name in hero_list:
        if hero['name'] == hero_name:
            print(f"Интелект героя {hero['name']} равен: {hero['powerstats']['intelligence']}")
            if hero['powerstats']['intelligence'] > top_intelligence:
                top_intelligence = hero['powerstats']['intelligence']
                best_hero = hero['name']
print(f"Больше всего интелекта у героя {best_hero}. Он равен {top_intelligence}")
