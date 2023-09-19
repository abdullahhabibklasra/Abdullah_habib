spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]




#1
list1=[]
def get_names(spicy_foods):
    for a in spicy_foods:
        list1.append(a["name"])
get_names(spicy_foods)
print(list1)


#2
list2=[]
def get_spiciest_foods(spicy_foods):
    for b in spicy_foods:
        if b["heat_level"] > 5:
            list2.append(b)


#3
get_spiciest_foods(spicy_foods)
print(list2)


#4
def print_spicy_foods(spicy_foods):
    for c in spicy_foods:
        print(c["name"],"(",c["cuisine"],")","| Heat Level:",c["heat_level"]* "🌶")


#5
print_spicy_foods(spicy_foods)


#6
def get_spicy_food_by_cuisine(spicy_foods,d):
    for e in spicy_foods:
        if e["cuisine"]==d:
            print(e)
            break
get_spicy_food_by_cuisine(spicy_foods,"American")


#7
get_spicy_food_by_cuisine(spicy_foods,"Thai")


#8
def print_spiciest_foods(spicy_foods):
    for f in spicy_foods:
        if f["heat_level"] > 5:
            print(f["name"],"(",f["cuisine"],")","| Heat Level:",f["heat_level"]* "🌶")

            
#9
print_spiciest_foods(spicy_foods)


#10
def get_average_heat_level(spicy_foods):
    a=0
    b=0
    for c in spicy_foods:
        a= c["heat_level"]+a
        b=b+1
    print("average_heat_level is",a/b)
get_average_heat_level(spicy_foods)


#11
new_list=[{'name':'Huo Guo','cuisine':'China','heat_level':7 }]
def create_spicy_food(spicy_foods,new_list):
    print(spicy_foods,new_list)
create_spicy_food(spicy_foods,new_list)

