with open('D5.txt') as file:
    input_data = file.read().split("\n\n")

# part 1

seed, *mappings = input_data[0], *input_data[1:]


locations = [*map(int, seed.split()[1:])]

for conversion_map in mappings:
    paths = *map(lambda path: [*map(int, path.split())], conversion_map.split('\n')[1:]),
    for seed_no, seed_loc in enumerate(locations):
        for destination, source, length in paths:
            if source <= seed_loc < source + length:
                locations[seed_no] = destination + seed_loc - source
                break

print(min(locations))

# part 2

seeds, *almanac = input_data
seed_ranges = map(int, seeds.split()[1:])
ranges = [[start, start + length] for start, length in zip(seed_ranges, seed_ranges)]

for conversion_map in almanac:
    mapper = []
    for path in conversion_map.split('\n')[1:]:
        destination, source, length = map(int, path.split())
        mapper.append([source, source + length, destination])
    mapper.sort(), ranges.sort()
    map_index = range_index = 0

    while (map_index < len(mapper)) and (range_index < len(ranges)):
        map_start, map_end, new_loc = mapper[map_index]
        range_start, range_end = ranges[range_index]
        unchanged = not (map_start <= range_start and map_end >= range_end)
        if range_start < map_start < range_end:
            unchanged = ranges.insert(0, [range_start, map_start])
            range_index += 1
        if range_start < map_end < range_end:
            unchanged = ranges.insert(range_index + 1, [map_end, range_end])
        if not unchanged:
            mapped_start = max(map_start, range_start) + new_loc - map_start
            mapped_end = min(map_end, range_end) + new_loc - map_start
            ranges[range_index] = [mapped_start, mapped_end]
            range_index += 1
        elif range_end <= map_end:
            range_index += 1
        elif range_end >= map_end:
            map_index += 1

print(sorted(ranges)[0][0])