def circleAreaCoverage(radiusOfCircle1, radiusOfCircle2):
    # Validate input: must be positive integers
    if type(radiusOfCircle1) != int or type(radiusOfCircle2) != int:
        return "Error: Both radii must be integers."

    if radiusOfCircle1 <= 0 or radiusOfCircle2 <= 0:
        return "Error: Both radii must be positive integers."

    pi = 3.1415926  # Manual value of pi

    # Compute areas
    area1 = pi * radiusOfCircle1 ** 2
    area2 = pi * radiusOfCircle2 ** 2

    # Determine smaller and larger area
    smaller_area = area1 if area1 < area2 else area2
    larger_area = area2 if area1 < area2 else area1

    # Calculate percentage coverage
    percentage_coverage = (smaller_area / larger_area) * 100

    return percentage_coverage
