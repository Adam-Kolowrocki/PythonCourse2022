graph = {
    "dom" : ["bar", "szkoła", "kościół"],
    "szkoła" : ["szpital", "dom"],
    "kościół" : ["dom", "bar", "kino"],
    "bar" : ["kościół", "szpital", "dom"],
    "szpital" : ["szkoła", "bar", "teatr", "kino"],
    "kino" : ["kościół", "szpital", "teatr"],
    "teatr" : ["szpital", "kino"]
}
for i in graph:
    for j in graph[i]:
        print(str(i)+" ----> " + str(j))
