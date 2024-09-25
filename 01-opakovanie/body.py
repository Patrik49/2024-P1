max_points = int(input("Enter the maximum amount of points: "))

if max_points > 0:
    points_got = int(input("Enter the points you got: "))

    if 0 <= points_got <= max_points:
        percentage = (points_got / max_points) * 100

        def get_grade(points):
            if points >= 90:
                return '1'
            elif points >= 80:
                return '2'
            elif points >= 70:
                return '3'
            elif points >= 60:
                return '4'
            else:
                
                return '5'

        grade = get_grade(percentage)
        print(f"You scored {points_got} out of {max_points}, which is {round (percentage,2):.2f}%. Your grade is: {grade}.")
    else:
        print("error.")
else:
    print("error.")
