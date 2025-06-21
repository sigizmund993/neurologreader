import matplotlib.pyplot as plt
import matplotlib.patches as patches
from enum import Enum
class Color(Enum):
    """Класс с цветами"""

    ALL = 0
    BLUE = 1
    YELLOW = 2

    def reverse(self) -> "Color":
        """Returns another color"""
        if self == Color.BLUE:
            return Color.YELLOW
        if self == Color.YELLOW:
            return Color.BLUE
        return Color.ALL

class Robot:
    def __init__(self,color:Color,id:int,pos_x:float,pos_y:float,ang:float):
        self.color = color
        self.id = id
        self.x = pos_x
        self.y = pos_y
        self.ang = ang
    def __str__(self):
        return f"{self.color}, id: {self.id}, x = {self.x:.2f}, y = {self.y:.2f},ang: {self.ang:.2f}"
class Log:
    def __init__(self,content:str):
        self.content = content
        self.i = 0
        self.length = len(self.content)-1
    def get_iteration(self)-> tuple[list[Robot],float,float]:
        bots:list[Robot] = []
        ball_pos_x_str = ""
        char = ""
        while self.i<self.length and char != " ":
            char = self.content[self.i]
            ball_pos_x_str+=char
            self.i +=1
        ball_pos_x = float(ball_pos_x_str)
        ball_pos_y_str = ""
        char = ""
        while self.i<self.length and char != "\n":
            char = self.content[self.i]
            ball_pos_y_str+=char
            self.i +=1
        ball_pos_y = float(ball_pos_y_str)
        rob_id = 0
        col_str = "y "
        while self.i<self.length and(col_str == "y " or col_str == "b "):
            col_str = ""
            char = ""
            while self.i<self.length and char != " ":
                char = self.content[self.i]
                col_str+=char
                self.i +=1
            if(col_str == "y "):
                col = Color.YELLOW
            elif(col_str == "b "):
                col = Color.BLUE
            if(col_str != "y " and col_str != "b "):
                break
            rob_id_str = ""
            char = ""
            while self.i<self.length and char != " ":
                char = self.content[self.i]
                rob_id_str+=char
                self.i +=1
            rob_id = int(rob_id_str)

            rob_pos_x_str = ""
            char = ""
            while self.i<self.length and char != " ":
                char = self.content[self.i]
                rob_pos_x_str+=char
                self.i +=1
            rob_pos_x = float(rob_pos_x_str)

            rob_pos_y_str = ""
            char = ""
            while self.i<self.length and char != " ":
                char = self.content[self.i]
                rob_pos_y_str+=char
                self.i +=1
            rob_pos_y = float(rob_pos_y_str)

            rob_ang_str = ""
            char = ""
            while self.i<self.length and char != "\n":
                char = self.content[self.i]
                rob_ang_str+=char
                self.i +=1
            rob_ang = float(rob_ang_str)
            bots.append(Robot(col,rob_id,rob_pos_x,rob_pos_y,rob_ang))

        for bot in bots:
            print(bot)
        self.i-=5
        return bots,ball_pos_x,ball_pos_y

fig, ax = plt.subplots()
file_name = "log.txt"
with open(file_name, 'r') as file:
    content = file.read()
log = Log(content)
bots,ball_pos_x,ball_pos_y = log.get_iteration()


ax.clear()
rect = patches.Rectangle((-4500, -3000), 4500*2, 3000*2, linewidth=2, edgecolor='blue', facecolor='green')
ax.add_patch(rect)
for bot in bots:
    if(bot.color == Color.BLUE):
        color = (0,0,1)
    else:
        color = (1,1,0)
    ax.plot(bot.x,bot.y,marker = 'o',color = color)
ax.plot(ball_pos_x,ball_pos_y,marker = 'o',color = 'orange')
print(ball_pos_x,ball_pos_y)
ax.set_aspect('equal', adjustable='box')
ax.set_xlim(-5000, 5000)
ax.set_ylim(-3500, 3500)
# ax.grid(True)
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.show()
print("end of log")