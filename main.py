from turtle import Screen, Turtle
import turtle
import pandas

screen = Screen()
screen.title("Guess The District")
screen.setup(width=500, height=650)
image = "Blank_MapOfBD.gif"
screen.addshape(image)
turtle.shape(image)
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
game_is_on = True
data = pandas.read_csv("64_Districts.csv")
all_districts = data["District"].to_list()
guessed_districts = []

while len(guessed_districts) <= 64:
    answer_district = screen.textinput(title=f"{len(guessed_districts)}/64 Districts Correct",
                                       prompt="What's another district's name?").title()
    if answer_district == "Exit":
        # missing_districts = []
        # for district in all_districts:
        #     if district not in guessed_districts:
        #         missing_districts.append(district)
        missing_districts = [district for district in all_districts if district not in guessed_districts]
        new_data = pandas.DataFrame(missing_districts)
        new_data.to_csv("Districts_to_learn")
        break

    elif answer_district == "Crack":
        for district in all_districts:
            t = Turtle()
            t.hideturtle()
            t.penup()
            district_data = data[data["District"] == district]
            t.goto(district_data.x.item(), district_data.y.item())
            t.write(district)

    elif answer_district in all_districts:
        t = Turtle()
        t.hideturtle()
        t.penup()

        district_data = data[data["District"] == answer_district]
        t.goto(district_data.x.item(), district_data.y.item())
        t.write(answer_district)
        guessed_districts.append(answer_district)
