graf = {
    'Arad': {'Zerind': 75, 'Timisoara': 118, 'Sibiu': 140},
    'Bucharest': {'Urziceni': 85, 'Giurgiu': 90, 'Pitesti': 101, 'Fagaras': 211},
    'Craiova': {'Drobeta': 120, 'Pitesti': 138, 'Rimnicu': 146},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Eforie': {'Hirsova': 86},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Giurgiu': {'Bucharest': 90},
    'Hirsova': {'Eforie': 86, 'Urziceni': 98},
    'Iasi': {'Neamt': 87, 'Vaslui': 92},
    'Lugoj': {'Mehadia': 70, 'Timisoara': 111},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Neamt': {'Iasi': 87},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Pitesti': {'Rimnicu': 97, 'Bucharest': 101, 'Craiova': 138},
    'Rimnicu': {'Sibiu': 80, 'Pitesti': 97, 'Craiova': 146},
    'Sibiu': {'Rimnicu': 80, 'Fagaras': 99, 'Arad': 140, 'Oradea': 151},
    'Timisoara': {'Lugoj': 111, 'Arad': 118},
    'Urziceni': {'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142},
    'Vaslui': {'Iasi': 92, 'Urziceni': 142},
    'Zerind': {'Oradea': 71, 'Arad': 75}
}

mulai = 'Arad'
tujuan = 'Bucharest'

visited = set()
dls = [(mulai, [], 0, 0)]
maksimal_kedalaman = 9

while dls:
    saat_ini, jalur, total_biaya, kedalaman = dls.pop()

    if kedalaman > maksimal_kedalaman:
        continue

    if saat_ini == tujuan:
        jalur.append(saat_ini)
        print(f"Jalur dari {mulai} sampai ke {tujuan} : {jalur}")
        print(f"Total biaya dari {mulai} sampai ke {tujuan} : {total_biaya}")
        break

    if saat_ini not in visited:
        visited.add(saat_ini)
        jalur.append(saat_ini)

    for neighbor, biaya in graf[saat_ini].items():
        if neighbor not in visited:
            total_biaya = total_biaya + biaya
            kedalaman = kedalaman + 1
            dls.append((neighbor, list(jalur), total_biaya, kedalaman))