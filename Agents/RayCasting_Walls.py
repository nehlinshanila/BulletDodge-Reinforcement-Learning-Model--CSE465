import math


# (x, y) is the position of the ray.
# (dx, dy) is the direction vector of the ray.
# (left, top) is the top-left corner of the wall.
# (right, bottom) is the bottom-right corner of the wall.
def calculate_wall_intersection(x, y, dx, dy, left, top, right, bottom):
    if dx == 0:
        # Vertical ray, use absolute y distance
        return abs(top - y) if dy < 0 else abs(bottom - y)
    elif dy == 0:
        # Horizontal ray, use absolute x distance
        return abs(left - x) if dx < 0 else abs(right - x)
    # calculate the entry time for the ray to reach the boundaries
    t_entry_x = (left - x) / dx
    t_entry_y = (top - y) / dy
    t_exit_x = (right - x) / dx
    t_exit_y = (bottom - y) / dy
    # calculate the exit time for the ray to leave the boundaries
    t_entry = max(min(t_entry_x, t_exit_x), min(t_entry_y, t_exit_y))
    t_exit = min(max(t_entry_x, t_exit_x), max(t_entry_y, t_exit_y))
    # check if there is a valid intersection (0 <= t_entry < t_exit)
    if 0 <= t_entry < t_exit:
        # calculate the intersection point and return remaining distance
        intersection_x = x + dx * t_entry
        intersection_y = y + dy * t_entry
        # calculate and return the remaining distance to the intersection point
        return math.hypot(intersection_x - x, intersection_y - y)
    else:
        # If there's no intersection, return positive infinity
        return float('inf')
    # inf== positive infinity
