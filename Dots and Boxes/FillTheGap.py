

from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk

root= Tk()
root.title('Fill the Gap')
root.geometry('800x600')

image = Image.open('Imagens/test1.jpg')
photo_image = ImageTk.PhotoImage(image)
fundo = Label(root, image = photo_image)
fundo.pack(fill=BOTH, expand=True)

my_notebook = ttk.Notebook(fundo)
my_notebook.pack()

#janela 2
players_text_1 = "null"
players_text_2 = "null"
grid_size = 64
offset_x = 10
offset_y = 10
tamanho_x = 9 #Alterar tamanho tabuleiro
tamanho_y = 9 #Alterar tamanho tabuleiro
arr = []

turn = True
player_1 = 0
player_2 = 0
sec = [
"p", "lh", "p", "lh", "p", "lh", "p", "lh", "p",
"lv", "n", "lv", "n", "lv", "n", "lv", "n", "lv",
]
def janela2():
    #novajnl = Toplevel(root)
    #novajnl.title('Fill The Gap')
    #novajnl.geometry('800x600')








    def criar_2d_array():
        rows, cols = (tamanho_x, tamanho_y)
        global arr
        arr=[]
        for i in range(rows):
            col = []
            for j in range(cols):
                col.append({"top":False,"right":False,"down":False,"left":False,})
            arr.append(col)

    def adicionar_secquencia():
        loop = 0
        for x in range(0, tamanho_x):
            for y in range(0, tamanho_y):
                if loop > len(sec)-1:
                    loop = 0

                arr[x][y] = sec[loop]
                loop += 1



    novajnl = Tk()
    # canvas=Canvas(root, width=800, height=600)
    canvas=Canvas(novajnl, width=(grid_size * tamanho_x) + offset_x + 250, height=(grid_size * tamanho_y) + offset_y)
    canvas.pack()

    def kinta():
        # for col in range(0, 9):
        #     canvas.create_line((grid_size * col) + offset_x, offset_y, (grid_size * col) + offset_x, (grid_size + offset_y) * 7, fill="green", width=1)
        #
        # for row in range(0, 9):
        #     canvas.create_line(offset_x, (grid_size * row) + offset_y, (grid_size + offset_x) * 7, (grid_size*row) + offset_y, fill="green", width=1)


        for x in range(0, tamanho_x):
            for y in range(0, tamanho_y):
                create_circle((grid_size*x) + offset_x, (grid_size*y) + offset_x, 5, canvas, "green", "black")

        add_text()
        canvas.bind("<Button 1>", get_mouse_pos)


        def motion(event):
            x, y = event.x, event.y
            x = int((x - offset_x) / grid_size)
            y = int((y - offset_y) / grid_size)
            #print('{}, {}'.format(x, y))

        novajnl.bind('<Motion>', motion)

        novajnl.mainloop()

    def create_circle(x, y, r, canvasName, fill:str, outline:str): #center coordinates, radius
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        return canvasName.create_oval(x0, y0, x1, y1, fill=fill, outline=outline)

    def get_mouse_pos(eventorigin):
        #print("Click:", (eventorigin.x -  offset_x) / grid_size, (eventorigin.y -  offset_y) / grid_size)
        get_side((eventorigin.x -  offset_x) / grid_size, (eventorigin.y -  offset_y) / grid_size)

    def get_side(mouse_pos_x, mouse_pos_y):
        global turn
        if mouse_pos_x > tamanho_x - 1 or mouse_pos_x < 0 or mouse_pos_y > tamanho_y - 1 or mouse_pos_y < 0:
            #print("Mouse out of grid")
            return

        if mouse_pos_x % 1 < 0.2 and mouse_pos_y % 1 > 0.2 and mouse_pos_y % 1 < 0.9:
            # print("left")
            if check_if_can_add_line(int(mouse_pos_x), int(mouse_pos_y), "left"):
                add_line(mouse_pos_x, mouse_pos_y, "left")
                if not check_for_box(int(mouse_pos_x), int(mouse_pos_y), "left"):
                    turn = not turn

        elif mouse_pos_x % 1 > 0.2 and mouse_pos_x % 1 < 0.9 and mouse_pos_y % 1 < 0.2:
            # print("top")
            if check_if_can_add_line(int(mouse_pos_x), int(mouse_pos_y), "top"):
                add_line(mouse_pos_x, mouse_pos_y, "top")
                if not check_for_box(int(mouse_pos_x), int(mouse_pos_y), "top"):
                    turn = not turn

        elif mouse_pos_x % 1 > 0.8 and mouse_pos_y % 1 > 0.2 and mouse_pos_y % 1 < 0.9:
            # print("right")
            if check_if_can_add_line(int(mouse_pos_x), int(mouse_pos_y), "right"):
                add_line(mouse_pos_x, mouse_pos_y, "right")
                if not check_for_box(int(mouse_pos_x), int(mouse_pos_y), "right"):
                    turn = not turn

        elif mouse_pos_x % 1 > 0.2 and mouse_pos_x % 1 < 0.9 and mouse_pos_y % 1 > 0.8:
            # print("down")
            if check_if_can_add_line(int(mouse_pos_x), int(mouse_pos_y), "down"):
                add_line(mouse_pos_x, mouse_pos_y, "down")
                if not check_for_box(int(mouse_pos_x), int(mouse_pos_y), "down"):
                    turn = not turn
        add_text()
        get_winner()

    def add_line(grid_x, grid_y, dir):
        real_grid_x = int(grid_x) * grid_size + offset_x
        real_grid_y = int(grid_y) * grid_size + offset_y

        topLeft = [real_grid_x, real_grid_y]
        topRight = [real_grid_x + grid_size, real_grid_y]
        downLeft = [real_grid_x, real_grid_y + grid_size]
        downRight = [real_grid_x + grid_size, real_grid_y + grid_size]

        if dir == "right":
            add_to_layer(2, canvas.create_oval, (topRight[0] - 5, topRight[1] - 5, topRight[0] + 5, topRight[1] + 5), fill="red", outline="blue")
            add_to_layer(2, canvas.create_oval, (downRight[0] - 5, downRight[1] - 5, downRight[0] + 5, downRight[1] + 5), fill="red", outline="blue")
            add_to_layer(4, canvas.create_line, (topRight[0], topRight[1], downRight[0], downRight[1]), fill="green", width=3)

        elif dir == "top":
            add_to_layer(2, canvas.create_oval, (topLeft[0] - 5, topLeft[1] - 5, topLeft[0] + 5, topLeft[1] + 5), fill="red", outline="blue")
            add_to_layer(2, canvas.create_oval, (topRight[0] - 5, topRight[1] - 5, topRight[0] + 5, topRight[1] + 5), fill="red", outline="blue")
            add_to_layer(4, canvas.create_line, (topLeft[0], topLeft[1], topRight[0], topRight[1]), fill="green", width=3)
        #
        elif dir == "down":
            add_to_layer(2, canvas.create_oval, (downLeft[0] - 5, downLeft[1] - 5, downLeft[0] + 5, downLeft[1] + 5), fill="red", outline="blue")
            add_to_layer(2, canvas.create_oval, (downRight[0] - 5, downRight[1] - 5, downRight[0] + 5, downRight[1] + 5), fill="red", outline="blue")
            add_to_layer(4, canvas.create_line, (downLeft[0], downLeft[1], downRight[0], downRight[1]), fill="green", width=3)
        #
        elif dir == "left":
            add_to_layer(2, canvas.create_oval, (topLeft[0] - 5, topLeft[1] - 5, topLeft[0] + 5, topLeft[1] + 5), fill="red", outline="blue")
            add_to_layer(2, canvas.create_oval, (downLeft[0] - 5, downLeft[1] - 5, downLeft[0] + 5, downLeft[1] + 5), fill="red", outline="blue")
            add_to_layer(4, canvas.create_line, (topLeft[0], topLeft[1], downLeft[0], downLeft[1]), fill="green", width=3)
        pass

    def check_if_can_add_line(grid_x, grid_y, side:str):
        if side == "right":
            if grid_x + 1 > tamanho_x - 1:
                if arr[grid_x][grid_y]["right"] == False:
                    arr[grid_x][grid_y]["right"] = "player"
                    # print("out of range right")
                    return True
            elif arr[grid_x][grid_y]["right"] == False and arr[grid_x + 1][grid_y]["left"] == False:
                arr[grid_x][grid_y]["right"] = "player"
                arr[grid_x + 1][grid_y]["left"] = "player"
                return True

        elif side == "left":
            if grid_x - 1 < 0:
                if arr[grid_x][grid_y]["left"] == False:
                    arr[grid_x][grid_y]["left"] = "player"
                    # print("out of range left")
                    return True

            elif arr[grid_x][grid_y]["left"] == False and arr[grid_x - 1][grid_y]["right"] == False:
                arr[grid_x][grid_y]["left"] = "player"
                arr[grid_x - 1][grid_y]["right"] = "player"
                return True

        elif side == "top":
            if grid_y - 1 < 0:
                if arr[grid_x][grid_y]["top"] == False:
                    arr[grid_x][grid_y]["top"] = "player"
                    # print("out of range top")
                    return True

            elif arr[grid_x][grid_y]["top"] == False or arr[grid_x][grid_y - 1]["down"] == False:
                arr[grid_x][grid_y]["top"] = "player"
                arr[grid_x][grid_y - 1]["down"] = "player"
                return True

        elif side == "down":
            if grid_y + 1 > tamanho_y:
                if arr[grid_x][grid_y]["down"] == False:
                    arr[grid_x][grid_y]["down"] = "player"
                    # print("out of range down")
                    return True

            elif arr[grid_x][grid_y]["down"] == False or arr[grid_x][grid_y + 1]["top"] == False:
                arr[grid_x][grid_y]["down"] = "player"
                arr[grid_x][grid_y + 1]["top"] = "player"
                return True

        print("can't add:")

    def check_for_box(grid_x, grid_y, side:str):
        box_1 = False
        box_2 = False
        BRUH = {"top": [0,-1], "right": [1,0], "down": [0,1], "left": [-1,0]}
        #print("box_1", arr[grid_x][grid_y])
        for i in arr[grid_x][grid_y]:
            if arr[grid_x][grid_y][i] == False:
                box_1 = False
                break
            else:
                box_1 = True
        # print("box_2", arr[grid_x + BRUH[side][0]][grid_y + BRUH[side][1]])
        for i in arr[grid_x + BRUH[side][0]] [grid_y + BRUH[side][1]]:
            if arr[grid_x + BRUH[side][0]] [grid_y + BRUH[side][1]][i] == False:
                box_2 = False
                break
            else:
                box_2 = True

        if box_1 == True:
            creat_box(grid_x, grid_y)
            #print("add BOX 1")
        if box_2 == True:
            creat_box(grid_x + BRUH[side][0], grid_y + BRUH[side][1])
            #print("add BOX 2")
        if box_1 == True or box_2 == True:
            return True
        pass

    def creat_box(grid_x, grid_y):
        global player_1
        global player_2
        real_grid_x = int(grid_x) * grid_size + offset_x
        real_grid_y = int(grid_y) * grid_size + offset_y

        if turn == True:
            add_to_layer(3, canvas.create_rectangle, (real_grid_x, real_grid_y, real_grid_x + grid_size, real_grid_y + grid_size), fill="blue")
            player_1 += 1
        else:
            add_to_layer(3, canvas.create_rectangle, (real_grid_x, real_grid_y, real_grid_x + grid_size, real_grid_y + grid_size), fill="yellow")
            player_2 += 1

        # rect = canvas.create_rectangle(real_grid_x, real_grid_y, real_grid_x + grid_size, real_grid_y + grid_size, outline="#fb0", fill="#fb0")
        pass

    _layers = []

    def add_to_layer(layer, command, coords, **kwargs):
        layer_tag = "layer %s" % layer
        if layer_tag not in _layers: _layers.append(layer_tag)
        tags = kwargs.setdefault("tags", [])
        tags.append(layer_tag)
        item_id = command(coords, **kwargs)
        _adjust_layers()
        return item_id

    def _adjust_layers():
        for layer in sorted(_layers):
            canvas.lift(layer)

    def add_text():
        global players_text_1
        global players_text_2
        position_x = (grid_size * tamanho_x) + 30
        position_y = 20
        text = ["Jogador 1 tem {0} pontos".format(player_1), "Jogador 2 tem {0} pontos".format(player_2)]

        if players_text_1 == "null":
            players_text_1 = canvas.create_text(position_x, position_y, text="", fill="black", font=('Helvetica 15 bold'), anchor="w")
        if players_text_2 == "null":
            players_text_2 = canvas.create_text(position_x, position_y+20, text="", fill="black", font=('Helvetica 15 bold'), anchor="w")

        if turn == True:
            canvas.itemconfigure(players_text_1, fill="green")
            canvas.itemconfigure(players_text_2, fill="black")
        else:
            canvas.itemconfigure(players_text_1, fill="black")
            canvas.itemconfigure(players_text_2, fill="green")

        canvas.itemconfigure(players_text_1, text=text[0])
        canvas.itemconfigure(players_text_2, text=text[1])

    def get_winner():
        global tamanho_x
        global tamanho_y

        #print(player_1 + player_2, (tamanho_x - 1) *  (tamanho_y - 1))
        if player_1 + player_2 >= (tamanho_x - 1) *  (tamanho_y - 1):
            if player_1 > player_2:
                print("jogador 1 ganhou")
                canvas.create_text(((grid_size*tamanho_x)+offset_x+250)/2, ((grid_size*tamanho_y)+offset_y)/2, text="Jogador 1 ganhou", fill="red", font=('Helvetica 30 bold'), anchor="center")
            else:
                print("jogador 2 ganhou")
                canvas.create_text(((grid_size*tamanho_x)+offset_x+250)/2, ((grid_size*tamanho_y)+offset_y)/2, text="Jogador 2 ganhou", fill="red", font=('Helvetica 30 bold'), anchor="center")

    def ready():
        criar_2d_array()
        kinta()


    ready()




    novajnl.mainloop()

#Funções de importe das outras páginas
def janela1():

    def newg():

        def limpar_menu():
            seqtest.destroy()
            my_button.destroy()
            my_button1.destroy()
            my_button2.destroy()

        def back1():
            label_newg1.destroy()
            button_newg1.destroy()
            button_newg2.destroy()
            button_newg3.destroy()
            janela1()

        def dois_jogadores():
            def limpar_menu():
                button_newg2.destroy()
                button_newg3.destroy()
                label_newg1.destroy()
                button_newg1.destroy()

            def back1():
                label_newg1.destroy()
                button_newg1.destroy()
                button_newg2.destroy()
                button_newg3.destroy()
                janela1()

            limpar_menu()
            janela2()

        limpar_menu()

        label_newg1 = Label(text='Novo Jogo', font=("Verdana","15",'bold'), bg='#CFE0E8', fg='#BB3E45')
        label_newg1.place (relx=0.4, rely=0.25)

        button_newg1 = Button(fundo, text="1 Jogador",bg='#CFE0E8', fg='#BB3E45', font=('Verdana','11', 'bold'))
        button_newg1.place (relx=0.45, rely=0.4)

        button_newg2 = Button(fundo, text="2 Jogadores",bg='#CFE0E8', fg='#BB3E45', font=('Verdana','11', 'bold'), command=dois_jogadores)
        button_newg2.place (relx=0.45, rely=0.5)

        button_newg3 = Button(fundo, text="Voltar",bg='#CFE0E8', fg='#BB3E45', font=('Verdana','11', 'bold'), command=back1)
        button_newg3.place (relx=0.45, rely=0.6)




    def definicoes():

        def limpar_menu():
            seqtest.destroy()
            my_button.destroy()
            my_button1.destroy()
            my_button2.destroy()

        def back2():
            label_def1.destroy()
            button_def1.destroy()
            button_def2.destroy()
            janela1()

        limpar_menu()

        label_def1 = Label(text='Definições', font=("Verdana","15",'bold'), bg='#CFE0E8', fg='#BB3E45')
        label_def1.place (relx=0.4, rely=0.25)

        button_def1 = Button(fundo, text="2 Jogadores",bg='#CFE0E8', fg='#BB3E45', font=('Verdana','11', 'bold'))
        button_def1.place (relx=0.45, rely=0.4)

        button_def2 = Button(fundo, text="Voltar",bg='#CFE0E8', fg='#BB3E45', font=('Verdana','11', 'bold'), command=back2)
        button_def2.place (relx=0.45, rely=0.5)


    def creditos():

        def limpar_menu():
            seqtest.destroy()
            my_button.destroy()
            my_button1.destroy()
            my_button2.destroy()

        def back3():
            label_cred1.destroy()
            button_cred1.destroy()
            janela1()

        limpar_menu()

        label_cred1 = Label(text='Créditos', font=("Verdana","15",'bold'), bg='#CFE0E8', fg='#BB3E45')
        label_cred1.place (relx=0.4, rely=0.25)

        button_cred1 = Button(fundo, text="Voltar",bg='#CFE0E8', fg='#BB3E45', font=('Verdana','11', 'bold'), command=back3)
        button_cred1.place (relx=0.4, rely=0.4)


    seqtest = Label(fundo, width=10)
    seqtest.place (relx=0.4, rely=0.25)
    seqtest.config(text='\nMenu',font=("Verdana","15",'bold'), bg='#CFE0E8', fg='#BB3E45')

    #Inserção dos botões

    my_button = Button(fundo, text="Novo Jogo", bg='#CFE0E8', fg='#BB3E45', font=('Verdana','11', 'bold'), command=newg)
    my_button.place (relx=0.45, rely=0.4)

    my_button1 = Button(fundo, text="Definições",bg='#CFE0E8', fg='#BB3E45', font=('Verdana','11', 'bold'), command=definicoes)
    my_button1.place (relx=0.45, rely=0.5)

    my_button2 = Button(fundo, text="Créditos",bg='#CFE0E8', fg='#BB3E45', font=('Verdana','11', 'bold'), command=creditos)
    my_button2.place (relx=0.45, rely=0.6)

janela1()

#Codigo Jogo







root.mainloop()
