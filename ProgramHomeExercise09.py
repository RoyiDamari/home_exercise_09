import random
import statistics

# Exercise 1
rand_list: list[int] = [random.randint(1, 100) for _ in range(50)];
print(rand_list);
print(list(filter(lambda x: x > 50, rand_list)));
print(list(filter(lambda x: x % 7 == 0, rand_list)));
print(list(filter(lambda x: 10 <= x <= 99, rand_list)));
print(list(filter(lambda x: x % 10 == x // 10, rand_list)));
print(list(filter(lambda x: x % 10 + x // 10 == 9, rand_list)));
print(statistics.mean(rand_list));
print(list(filter(lambda x: x > statistics.mean(rand_list), rand_list)));
print(max(rand_list) / 2);
print(list(filter(lambda x: x > max(rand_list) / 2, rand_list)));
print(sorted(rand_list));
print(sorted(rand_list)[(len(rand_list) - 1)// 2]);
print(list(filter(lambda x: x > sorted(rand_list)[(len(rand_list) - 1)// 2],  rand_list)));
user_list: list[int] = [int(input("Pleas enter a number: ")) for _ in range(5)];
print(list(filter(lambda x: x not in user_list,  rand_list)));
print(rand_list);
print(list(filter(lambda num: num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)),rand_list)));

# Exercise 2
game_list: list[str] = ["The Elder Scrolls V: Skyrim", "Dark Souls",
                        "Overwatch", "Fortnite", "Grand Theft Auto V"];
print(list(filter(lambda word: len(word) > 10, game_list)));
print(list(filter(lambda word: word.upper().startswith('F'), game_list)));
print(list(filter(lambda word: len(word.split()) == 2, game_list)));
print(list(filter(lambda word: 'V' in word, game_list)));
print(list(filter(lambda word: any(char in ":!^&*" for char in word), game_list)));

game_list_year: list[list] = [["The Elder Scrolls V: Skyrim", 2011], ["Dark Souls", 2011],
                              ["Overwatch", 2016], ["Fortnite", 2017], ["Grand Theft Auto V", 2013]];
print(list(filter(lambda year: year[1] > 2014, game_list_year)));

# Exercise 3
random_list: list[int] = [random.randint(-50, 50) for _ in range(20)];
print(random_list);
print(list(map(lambda x: x ** 3, random_list)));
print(list(map(lambda x: abs(x) % 10, random_list)));
print(list(map(lambda x: x * 9 / 5 + 32, random_list)));
print(list(map(lambda x: "positive" if x > 0 else "negative", random_list)));
print(list(map(lambda x: "max" if x == max(random_list) else "min" if x == min(random_list) else x, random_list)));

print(list(map(lambda x: (-1 if x < 0 else 1) * (abs(x) % 10 *
                                      (10 if len(str(abs(x))) > 1 else 1) + abs(x) // 10), random_list)));
print(list(map(lambda x: abs(x), random_list)));

income_expenses: list[list] = [[7000, 10000], [5000, 300], [8000, 2000]];
print(list(map(lambda x: x[0] - x[1], income_expenses)));

# Exercise 4
fruits_list: list[str] = ["Apple", "Banana", "Orange", "Mango", "Strawberry",
                          "Pineapple", "Grapes", "Watermelon"];
print(list(map(lambda fruit: fruit[::-1], fruits_list)));
print(list(map(lambda fruit: fruit[0], fruits_list)));
print(list(map(lambda fruit: fruit.capitalize(), fruits_list)));
print(list(map(lambda fruit: len(fruit), fruits_list)));
print(list(map(lambda fruit: fruit + "!" if fruit.endswith('s') else fruit, fruits_list)));

fruits_list_calories: list[list] = [["Apple", 52], ["Banana", 89], ["Orange", 47], ["Mango", 60],
                                    ["Strawberry", 32], ["Pineapple", 50], ["Grapes", 69], ["Watermelon", 30]];
print(list(map(lambda fruit: fruit[1], fruits_list_calories)));
print(list(map(lambda fruit: str(fruit[0]) + str(fruit[1]), fruits_list_calories)));
print(list(map(lambda fruit: str(fruit[0]) + str(fruit[1])
                                           + ("!" if fruit[1] > 50 else ""), fruits_list_calories)));

# Exercise 5
city_list: list[str] = ["Tokyo", "New York", "Paris", "London", "Sydney", "Shanghai", "Dubai"];
print(sorted(city_list, key=lambda city: len(city)));
print(sorted(city_list, key=lambda city: city[len(city) - 1]));
print(sorted(city_list, key=lambda city: city[::-1]));
city_continent_distance_list: list[list] = [["Tokyo", 5760, "Asia"], ["New York", 5690, "North America"],
                                            ["Paris", 2050, "Europe"], ["London", 2240, "Europe"],
                                            ["Sydney", 8780, "Australia"], ["Dubai", 1300, "Asia"],
                                            ["Shanghai", 4920, "Asia"]];
print(sorted(city_continent_distance_list, key=lambda city: city[1]));
print(sorted(city_continent_distance_list, key=lambda city: -1 * city[1]));
print(sorted(city_continent_distance_list, key=lambda city: city[2]));
print(sorted(city_continent_distance_list, key=lambda city: (city[2], city[1])));

#Exercise 6

'''By declaring a variable as global, that's tell Python to use the global variable with that name. 
Any assignments to this variable will modify the global variable.'''

'''Using the global keyword in functions can lead to side effects that are not immediately apparent,
and make it harder to track the flow of data and understand the state of the program.
Also it can introduce subtle bugs that are difficult to trace,
for example if multiple functions modify the same global variable.
this will require at the future to refactor code to reduce the reliance on global variables.
This can be a time-consuming and error-prone process.
Also refactoring might involve redesigning functions to accept parameters,
and return values instead of relying on global state.
'''

'''x: int = 1
def foo():
print(x)
x = 4
foo()

The error is because it Python detects that x is being assigned a value within the function,
which makes x a local variable.
However, the local variable x is used before it is assigned a value, which leads to the error.
'''