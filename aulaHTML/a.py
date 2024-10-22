from tkinter import *
import configure
import new


root = Tk()
root.configure(bg = "black") #deixa o fundo preto
root.geometry(f'{configure.WIDTH}x{configure.HEIGHT}') #muda o tamanho da janela
root.title("Campo Minado")  #titulo da janela
root.resizable(False, False) #proibe redimensionar a janela

top_frame = Frame(root, bg="#5D6D7E",
                  width = configure.WIDTH,
                  height = new.height_prct(25)) #quadro superior pro numero de celulas?

top_frame.place(x=0, y=0) #abrir o quadro Score


game_title = Label(top_frame, bg = "#5D6D7E", fg= "white", 
                    text = "Campo Minado", 
                    font = ('', 48)) #titulo do jogo muda o fundo, texto e a fonte das letras

game_title.place(x= new.width_prct(30), y=0) #define a altura e largura do nome do jogo

center_frame = Frame(root, bg="white", width = new.width_prct(75),
                    height = new.height_prct(75)
                    ).place(
                        x=new.width_prct(30),
                        y=new.height_prct(30)
                    ) #quadro para as celulas








root.mainloop()