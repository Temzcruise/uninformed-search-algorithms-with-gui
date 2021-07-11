
import tkinter.messagebox
import collections
import tkinter as tk
from tkinter import *
from functools import partial


class TreeNode:
    def __init__(self, val="", left=None, right=None):
        # self.window = window
        self.val = val
        self.left = left
        self.right = right


class UninformedAgorithms:
    def __init__(self, window, root, canvas_width, canvas_height):
        self.window = window
        self.root = root
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.canvas = tk.Canvas(window, width=canvas_width, height=canvas_height)
        # self.searchNode = "I"
        self.searchNode = tk.StringVar()
        # self.searchNode = tk.Entry(window, height=2, width=25, textvariable=stri)
        # self.searchNode.place(x=20, y=50, height=70)

        # self.searchNode.pack()
        # x0,y0,x1,y1
        self.circleA = self.canvas.create_oval(360, 50, 430, 115, fill="white", outline='white')
        self.textA = self.canvas.create_text(395, 85, fill='black', font='Helvetica 20 bold', text='A')

        self.circleB = self.canvas.create_oval(230, 180, 300, 250, fill="white", outline='white')
        self.textB = self.canvas.create_text(265, 215, fill='black', font='Helvetica 20 bold', text='B')

        self.circleC = self.canvas.create_oval(480, 180, 550, 250, fill="white", outline='white')
        self.textC = self.canvas.create_text(515, 215, fill='black', font='arial 20 bold', text='C')

        self.circleD = self.canvas.create_oval(130, 310, 200, 380, fill="white", outline='white')
        self.textD = self.canvas.create_text(165, 345, fill='black', font='Times 20 bold', text='D')

        self.circleE = self.canvas.create_oval(305, 310, 375, 380, fill="white", outline='white')
        self.textE = self.canvas.create_text(340, 345, fill='black', font='Times 20 bold', text='E')

        self.circleF = self.canvas.create_oval(420, 310, 490, 380, fill="white", outline='white')
        self.textF = self.canvas.create_text(455, 345, fill='black', font='Times 20 bold', text='F')

        self.circleG = self.canvas.create_oval(560, 310, 630, 380, fill="white", outline='white')
        self.textG = self.canvas.create_text(595, 345, fill='black', font='Times 20 bold', text='G')

        self.circleH = self.canvas.create_oval(30, 450, 100, 520, fill="white", outline='white')
        self.textH = self.canvas.create_text(65, 485, fill='black', font='Times 20 bold', text='H')

        self.circleI = self.canvas.create_oval(200, 450, 270, 520, fill="white", outline='white')
        self.textI = self.canvas.create_text(235, 485, fill='black', font='Times 20 bold', text='I')

        self.circleJ = self.canvas.create_oval(350, 450, 425, 520, fill="white", outline='white')
        self.textJ = self.canvas.create_text(385, 485, fill='black', font='Times 20 bold', text='J')

        self.canvas.create_line(395, 115, 290, 190, arrow=tk.LAST, fill="black")  # A-B
        self.canvas.create_line(395, 115, 500, 180, arrow=tk.LAST, fill="black")  # A-C

        self.canvas.create_line(260, 250, 335, 310, arrow=tk.LAST, fill="black")  # B-E
        self.canvas.create_line(260, 250, 185, 320, arrow=tk.LAST, fill="black")  # B-D

        self.canvas.create_line(510, 250, 580, 315, arrow=tk.LAST, fill="black")  # C-G
        self.canvas.create_line(510, 250, 455, 310, arrow=tk.LAST, fill="black")  # C-F

        self.canvas.create_line(160, 380, 230, 450, arrow=tk.LAST, fill="black")  # D-I
        self.canvas.create_line(160, 380, 90, 450, arrow=tk.LAST, fill="black")  # D-H

        self.canvas.create_line(450, 380, 395, 450, arrow=tk.LAST, fill="black")  # F-J
        # canvas.create_line(480, 380, 550, 450, arrow=tk.LAST, fill="black") #I-K
        self.usa = tk.Label(window, text="Uninformed Search Algorithms", font = "Helvetica 17 bold italic")
        self.usa.place(x=700, y=70)

        self.searchNodeLabel = tk.Label(window, text='Input node to be found', font=('calibre', 13, 'bold'))
        self.searchNodeLabel.place(x=800, y=125)

        self.searchEntry = tk.Entry(window, textvariable=self.searchNode, width=4, font=('calibre', 10, 'normal'))
        self.searchEntry.place(x=755, y=125)

        self.searchNode.set(self.searchNode.get().upper())  #convert all search entries to Uppercase

        self.searchBTN = tk.Button(self.window, height = 2, width = 15, text="Search", font='arial 10 bold', command= lambda : self.breadthFirstSearch(root, self.searchNode))
        self.searchBTN.place(x=800, y=470)


        self.searchAlgo = tk.StringVar()
        self.searchAlgo.set("Breadth First Search")  # initializing the choice, i.e. Breadth first

        self.algorithms = [("Breadth First Search", "..."),
                     ("Depth First Search", "..."),
                     ("Iterative Deepning Search", "..."),
                     ("Uniform Cost Search", "..."),
                     ("C", "...")]

        for alg, val in self.algorithms:
            tk.Radiobutton(window, text=alg, padx = 20,
                           variable=self.searchAlgo,
                           command = self.runAlgo, value=val).place(x=900, y = 500)
            #make distance dynamic
            # self.Radiobutton.place(x=800, y=470)
        self.canvas.pack()

    def runAlgo(self):
        print("yea")


    def breadthFirstSearch(self, root, searchNode):
        queue_ = collections.deque()
        visited = []
        queue_.append(root)

        while queue_:
            queue_length = len(queue_)

            for i in range(queue_length):
                node = queue_.popleft()
                print(node)
                if node and (node.val == searchNode):
                    # print(searchNode)
                    visited.append(node.val)
                    break
                elif node:
                    visited.append(node.val)
                    queue_.append(node.left)
                    queue_.append(node.right)

            if visited[-1] == searchNode:
                break

        print(visited)
        self.breadthFirstSearchVisualizer(visited)


    def breadthFirstSearchVisualizer(self, list_of_nodes):
        node_mapper = {'A': self.circleA, 'B': self.circleB, 'C': self.circleC,
                       'D': self.circleD, 'E': self.circleE, 'F': self.circleF, 'G': self.circleG,
                       'H': self.circleH, 'I': self.circleI,
                       'J': self.circleJ}

        for i in list_of_nodes:
            self.window.after(500, self.canvas.itemconfig(node_mapper[i], fill="green"))
            self.canvas.update()

        self.window.after(100, self.canvas.itemconfig(node_mapper[list_of_nodes[-1]], fill="#FFD700"))
        self.canvas.update()
        return


window = tk.Tk()
window.title("Uninformed search algorithms")
root = TreeNode("A", TreeNode("B", TreeNode("D", TreeNode("H", None, None), TreeNode("I", None, None)), TreeNode("E", None, None)), TreeNode("C", TreeNode("F", TreeNode("J", None, None), None), TreeNode("G", None, None)))
UIA = UninformedAgorithms(window, root, canvas_width=1100, canvas_height=650)
window.mainloop()
