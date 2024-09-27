def sphere_volume(r):
    """
    This function takes the radius of a sphere as an input and returns the
    volume of the sphere.

    V = 4/3 * pi * (r ** 3)

    Args:
        r (scalar or array_like > 0): radius of sphere

    Returns:
        volume (scalar or array_like > 0): volume of sphere
    """
    pi = 3.14159
    volume = 4/3 * pi * (r ** 3)
    return volume


if __name__ == "__main__":
    print("Set the value of radius to r = 3.7.")
    r = 3.7
    volume = sphere_volume(r)
    print(f"The volume of a sphere with radius {r} is {volume}.")
